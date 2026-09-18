// Node 22+. Start headless Chrome with --remote-debugging-port=9444 first.
// Usage: node scripts/check-font-loading.mjs http://127.0.0.1:8777/ 1200 light
// Disable cache and delay fonts; fail if visible homepage typography swaps later.
import assert from 'node:assert/strict';
const [url = 'http://127.0.0.1:8777/', delay = '1200', theme = 'dark', width = '390'] = process.argv.slice(2);
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
const tab = await (await fetch('http://localhost:9444/json/new?about:blank', { method: 'PUT' })).json();
const ws = new WebSocket(tab.webSocketDebuggerUrl);
await new Promise(resolve => ws.addEventListener('open', resolve, { once: true }));
let id = 0;
const pending = new Map(), requests = [];
function call(method, params = {}) {
  return new Promise((resolve, reject) => {
    pending.set(++id, { resolve, reject });
    ws.send(JSON.stringify({ id, method, params }));
  });
}
ws.addEventListener('message', async event => {
  const message = JSON.parse(event.data);
  if (message.id) {
    const promise = pending.get(message.id);
    pending.delete(message.id);
    message.error ? promise.reject(message.error) : promise.resolve(message.result);
  } else if (message.method === 'Fetch.requestPaused') {
    await sleep(Number(delay));
    await call('Fetch.continueRequest', { requestId: message.params.requestId });
  } else if (message.method === 'Network.requestWillBeSent') {
    requests.push(message.params.request.url);
  }
});
const evaluate = async expression => (await call('Runtime.evaluate', {
  expression, returnByValue: true, awaitPromise: true,
})).result.value;
const deadline = setTimeout(() => { console.error('Font check timed out'); process.exit(1); }, 15000);
try {
  for (const domain of ['Page', 'Network', 'DOM', 'CSS']) await call(`${domain}.enable`);
  await call('Network.clearBrowserCache');
  await call('Network.setCacheDisabled', { cacheDisabled: true });
  await call('Emulation.setDeviceMetricsOverride', { width: Number(width), height: 844, deviceScaleFactor: 1, mobile: Number(width) < 600 });
  // Exclude existing entrance animations from font/layout comparisons.
  await call('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
  await call('Fetch.enable', { patterns: ['*fonts.googleapis.com*', '*fonts.gstatic.com*', '*.woff2'].map(urlPattern => ({ urlPattern })) });
  await call('Page.addScriptToEvaluateOnNewDocument', { source: `
    localStorage.setItem('theme', ${JSON.stringify(theme)});
    window.fontCLS = 0;
    new PerformanceObserver(list => { for (const e of list.getEntries()) if (!e.hadRecentInput) window.fontCLS += e.value; }).observe({type:'layout-shift', buffered:true});
  ` });
  await call('Page.navigate', { url });
  while (!await evaluate(`!!document.querySelector('.home-bio p') && getComputedStyle(document.body).fontSize === '14px'`)) await sleep(25);
  await sleep(200);
  async function sample() {
    const { root } = await call('DOM.getDocument');
    const items = [];
    for (const selector of ['.home-name', '.home-bio p', '.site-title']) {
      const { nodeId } = await call('DOM.querySelector', { nodeId: root.nodeId, selector });
      const { fonts } = await call('CSS.getPlatformFontsForNode', { nodeId });
      const box = await evaluate(`(()=>{const r=document.querySelector('${selector}').getBoundingClientRect();return [r.width,r.height,r.y]})()`);
      items.push({ selector, box, fonts: fonts.map(f => [f.familyName, f.isCustomFont]) });
    }
    return items;
  }
  const initial = await sample();
  await sleep(Number(delay) * 2 + 2000);
  await evaluate('document.fonts.ready.then(() => true)');
  const final = await sample();
  const cls = await evaluate('window.fontCLS');
  console.log(JSON.stringify({ delay, theme, width, initial, final, cls, fontRequests: requests.filter(u => /fonts\.(googleapis|gstatic)|\.woff2/.test(u)) }, null, 2));
  assert.deepEqual(final, initial, 'Visible fonts or layout changed after initial render');
  assert.equal(await evaluate('document.documentElement.scrollWidth > innerWidth'), false, 'Horizontal overflow');
  assert.equal(requests.some(u => /https:\/\/fonts\.(googleapis|gstatic)\.com/.test(u)), false, 'External font request');
  // Check all declared weights and real italic faces, even when absent on the homepage.
  const loaded = await evaluate(`Promise.all(['Space Grotesk','Lora','JetBrains Mono'].flatMap(f => [400,500,600,700].map(w => document.fonts.load(w+' 16px "'+f+'"'))).concat(['Lora','JetBrains Mono'].map(f => document.fonts.load('italic 400 16px "'+f+'"')))).then(results => results.every(faces => faces.length > 0))`);
  assert.equal(loaded, true, 'Missing normal weight or italic face');
} finally {
  clearTimeout(deadline);
  await call('Page.close');
  ws.close();
}
