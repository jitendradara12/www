# Font sources

Downloaded 2026-09-17 from Google Fonts. Unmodified Latin-subset variable WOFF2 files, weights 400–700. Other scripts use the existing system fallbacks.

`assets/fonts.css` declares these faces with `font-display: optional` and joins the existing Hugo CSS bundle. The three normal faces total 91,508 bytes and are preloaded; italic faces load only when used. Slow first visits retain system fallbacks for that navigation instead of swapping late. No text-hiding script is used.

Run `node scripts/check-font-loading.mjs http://127.0.0.1:8777/ 1200 light` against a Hugo build served at that URL, with headless Chrome listening on port 9444. The check disables cache, delays font requests, compares actual rendered fonts and boxes, checks for external font requests and overflow, and loads all normal weights plus both italic faces. Use delay `0` to check immediate loading, or a final `1280` argument for desktop width. Browser font-display timing and system fallback metrics vary across platforms.

Families and upstream OFL licenses:
- jetbrainsmono: https://raw.githubusercontent.com/google/fonts/main/ofl/jetbrainsmono/OFL.txt
- lora: https://raw.githubusercontent.com/google/fonts/main/ofl/lora/OFL.txt
- spacegrotesk: https://raw.githubusercontent.com/google/fonts/main/ofl/spacegrotesk/OFL.txt

## jetbrains-mono-italic-latin.woff2

- Source: https://fonts.gstatic.com/s/jetbrainsmono/v24/tDbp2o-flEEny0FZhsfKu5WU4xD-IQ-PuZJJXxfpAO-LfjGbsVNLG7DGdF6OZ1PswAMg.woff2
- SHA-256: `89d4f8e433fee8bccca552bda7cbeefd44c2406f454d17593811344088bbeabb`
- Size: 33096 bytes

## jetbrains-mono-normal-latin.woff2

- Source: https://fonts.gstatic.com/s/jetbrainsmono/v24/tDbv2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8yKwBNntkaToggR7BYRbKPxDcwg.woff2
- SHA-256: `83c005d49d8a6a50474c73a5a36ac0468076e9c4a29da7bdb14995d80560a5be`
- Size: 31432 bytes

## lora-italic-latin.woff2

- Source: https://fonts.gstatic.com/s/lora/v37/0QIhMX1D_JOuMw_LIftL.woff2
- SHA-256: `d824d807d4d832d12c87932d0b8ec1314dcfd502157a56dee6bb04cf8a3768ae`
- Size: 40772 bytes

## lora-normal-latin.woff2

- Source: https://fonts.gstatic.com/s/lora/v37/0QIvMX1D_JOuMwr7Iw.woff2
- SHA-256: `ddb8c66035104e233fc024669183aad3738b6daa16deee2ebb1241bd0f98ace1`
- Size: 37788 bytes

## space-grotesk-normal-latin.woff2

- Source: https://fonts.gstatic.com/s/spacegrotesk/v22/V8mDoQDjQSkFtoMM3T6r8E7mPbF4Cw.woff2
- SHA-256: `0640890476fc1198ab4de571fb658de443c4d85b66466ec09534a8737ab1ce9d`
- Size: 22288 bytes
