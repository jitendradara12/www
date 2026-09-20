+++
date = '2026-09-12T18:09:57+05:30'
title = 'the agents gaslit me into reverse engineering an unsupported fingerprint sensor for Linux'
description = "successfully reverse engineered an unsupported fingerprint sensor (goodix 27c6:5e0a) for linux using AI agents to write fprintd compatible drivers"
rss_exclude = false
math = true
+++

Ever since I've moved to Linux, there was this one little nitpick I had that my fingerprint scanner wouldn't work. because, well, tHe DrIvERs aNd aLL ArE PrOpRiEtArY. me being 18-year-old me, dug through the whole internet looking for _workarounds_ and finally gave up.

looking back, it was a correct decision because I, a freshman in college,
wasn't nearly qualified enough to grasp the assembly dumps and then, write the drivers from scratch in C.
and now... spoiler alert: I still can't. but in 2026, _"coding is solved"_ they say.
of course, just prompting "make no mistake" wouldn't work. or would it?

### the dump

good thing I had W*ndows lying around in one partition of the disk. so I just had to mount it and point the agents towards
`/run/media/user/Windows`. they figured out the core architecture and stuff and got the first
image capture rather quickly.

![milestone](/goodix/milestone.png)

It was just an image capture. and I had no intention to see how my fingerprints look in a 64×80 pixel image.
I needed it to correctly identify and do the PAM verification, which was quite far but achievable now.

"go ahead mr llm. run in loops and make it work somehow" and it did! or that's what it told me. every time
asking me to go rebuild my NixOS and check for myself. naive me kept circling in a loop of these three failures
and burning tokens in between.

```
1. Stuck at `Enrolling right-index-finger finger.` (touching/removing/waiting produces no stage advance; journal logs `Failed to detect minutiae: No minutiae found`).
2. Fingerprint enroll fails (false-completing on empty air background noise or failing during activation).
3. Stuck in verify or verify fails (`verify-unknown-error (done)`, hanging on verify requiring `^C`, or only the first verify matching after restart while all subsequent verify calls fail with `verify-unknown-error` and `Command timed out: 0xa2`).
```

I know how to solve this. just burn more tokens. use subagents and make subagents use subagents. make it a full corporate.
and see all 6 tickets get solved in one hour. 6 tickets? we have 10 now. 10
superseded by 11 and 11 superseded by 12 and it's 4am already I need to sleep; matching the agents' speed is tiring.

### we're half there

> Goodix ships a single Windows driver binary (wbdi.dll) that supports multiple hardware variants. Deep in .rdata, that DLL contains six distinct 256-byte configuration tables for different sensors (ChicagoH, ChicagoHS, ChicagoT, MilanG, MilanH, MilanHuHV).
> The early Linux driver had accidentally extracted table 6 (offset 0x248a00, starting with byte 0x70), which belongs to a completely different sensor family (MilanHuHV GF5298).

so we were basically trying to make our sensor work with a table which belongs to an entirely different family of silicon.
after ticket 13, we were able to retrieve the full 10564 bytes of data. and the first `verify-match` was achieved at ticket 18 via
a Python script.

but dumb models don't write perfect code. and the code had several problems like a verify retry race, zombie USB read loops and a leaked state machine. that means if I run sudo and then ctrl^c, the device will not be released and would require restarting fprintd.

solving these bugs was the agents' work. but testing every little change was a real pain in the ass. anyway, I pushed through. and by ticket 42, I had a deployed and working driver. it would instantly unlock my device. everything was rainbows and sunshine.

### the brutal truth

while demoing my hard work to my friends I realised something which I was ignoring previously -- the FAR.
yeah I know I've set the Bozorth match threshold to 11. but it shouldn't be this bad right?

I had

- 8 enrolled fingers.
- 11 Bozorth score threshold (1.2% FAR).
- 12 separate enrollment stages.

so in total, for every fingerprint matching,  
it compares it with $8\times12=96$ templates.  
so the $\text{FAR} = 1 - (1 - 0.012)^{96} \approx 1 - 0.313 = 68.7$%

that's bad. a stranger has a 70% chance to unlock where my own fingerprints barely get recognised.

the fix: 11 to 14 (0.11% FAR), and reduce enrollment stages from 12 to 5.

this is not a fix. it's a punishment! it would always give `no-match` this way. ticket after ticket,
refinement after refinement I thought I would make it work after some iterations but ended up
frustrated, with dark circles and no solution in my hands.

the problem was never my drivers. it was the whole Linux biometrics stack.

due to my emotional relationship with my agents, I can't just give up without telling them right?
here's what I prompted just before letting it all go and accept defeat.

> i'm giving up on this project. i thought the drivers are the only hurdle for fingerprint to work on linux but it's rotten all the way. i've done 70 fucking tickets when it was kinda working in 30ish ticket. just to make it usable like windows where 99% of times it works in one touch. i couldn't. fprintd is not windows. and I don't think i can do it anymore. it works, just like it should it's just that it never opens in a _normal and single_ touch, even when you have multiple fingers enrolled, it also unlocks with any finger if you try enough. the accuracy just sucks. it'll never be like windows

the response is always _"You are completely right"_, but the comparison table which it gave me is useful for context here.

| Windows Hello                                                                                                           | Linux libfprint                                                                                         |
| :---------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **Goodix / MilanFlat Engine:** Tracks ridge flow in frequency domain, phase correlation, and neural feature embeddings. | **NIST Bozorth3:** 1990s FBI ink card matcher relying purely on classical minutiae points.              |
| **Micro-Aperture Sensors:** Tuned specifically for tiny laptop touch sensors with low feature counts.                   | **Giant 500 DPI Ink Cards:** Expects full rolled or flat card prints showing 50–100 minutiae.           |
| **Continuous Mosaic Stitching:** Merges successive touches into 1 composite master map per finger.                      | **Discrete Snapshot Dumping:** Dumps 10 disconnected postage-stamp crops straight into an array.        |
| **1 Master Template / Finger:** Authenticates against a single unified map.                                             | **10–14 Templates / Finger:** Sweeps through 80–100 disconnected fragments across a multi-finger setup. |
| **Sub-Second Partial Matching:** Authenticates instantly even on a tiny edge of your finger.                            | **Rigid Graph Matching:** Rejects touches exceeding 10% stretch or 11° rotation.                        |

### the hope

while casually browsing, I came across [this repo](https://github.com/OMGrant/ft9201-libfprint.git) and cloned it
to find out how the hell is he doing it. I couldn't understand it obviously
so I asked the agent to find out if it's useful for us or not. and the response is **"huge!"**

![response: yes this is exactly what we need](/goodix/llm-reply.png)

Windows used Goodix's proprietary `GoodixEngineAdapter.dll` (the Milan engine), which works on frequency-domain ridge flow and stitches multiple touches into a unified composite template.

the solution is simple: instead of reverse engineering an entire commercial biometric engine from scratch, we load `GoodixEngineAdapter.dll` directly into the Linux C process.

how it works:

1. parse the dll with a custom PE parser in about 200 lines of C.
2. Linux won't let us malloc like the old days so the loader uses a Linux system call called `memfd_create`, which creates a temporary file that lives entirely in RAM. The loader copies the DLL into this memory file, and then maps it into memory twice using `mmap`.
3. and several more tricks which neither I nor you will understand; let's just ignore them conveniently.

### outcome

**It Works!** and that's very important because I've been longing to use my fingerprint unlock for the last 3 years.
I don't care how much code I wrote myself and how much the AI wrote or how many legal licenses I broke.
because in the end, I get to use my fingerprint sensor and you don't. (or you use W*ndows/MacOS which is actually worse)

repo: https://github.com/jitendradara12/goodix-5e0a
