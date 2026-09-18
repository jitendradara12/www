+++
date = '2026-09-12T18:09:57+05:30'
title = 'the agents gaslit me into reverse engineering an unsupported fingerprint sensor for Linux'
description = "successfully reverse engineered an unsupported fingerprint sensor (goodix 27c6:5e0a) for linux using AI agents to write fprintd compatable drivers"
rss_exclude = true 
+++

Ever since I've moved to Linux, there was this one little nitpick I had that my fingerprint scanner wouldn't work. because, well, tHe DrIvERs aNd aLL ArE PrOpRiEtArY. me being 18-year-old me, dug through the whole internet looking for _workarounds_ and finally gave up.

looking back, it was a correct decision because I, a freshmen in college,
wasn't nearly qualified enough to debug the assembly and then, write the drivers from scratch.
and now... spoiler alert: I still can't. but in 2026, _"coding is solved"_ they say.
ofcourse, just prompting _"make no mistake"_ wouldn't work. or will it?

### the dump

good thing I had W*ndows laying around in one partition of the disk. so I just had to mount it and point the agents towards
`/run/media/user/Windows`. they figured out the core architecture and stuff and got the first
image capture rather very quickly.

![milestone](/goodix/milestone.png)

It was just an image capture. and I had no intention to see how my fingerprints look in a 64×80 pixel image.
I need it to correctly identify and do the PAM verification. which was quite far but achievable now.

"go ahead mr llm. run in loops and make it work somehow" and it did! or that's what it told me. everytime
asking me to go rebuild my NixOS and check for myself. naive me kept circling in a loop of these three failures
and burning tokens in between.

```
1. Stuck at `Enrolling right-index-finger finger.` (touching/removing/waiting produces no stage advance; journal logs `Failed to detect minutiae: No minutiae found`).
2. Fingerprint enroll fails (false-completing on empty air background noise or failing during activation).
3. Stuck in verify or verify fails (`verify-unknown-error (done)`, hanging on verify requiring `^C`, or only the first verify matching after restart while all subsequent verify calls fail with `verify-unknown-error` and `Command timed out: 0xa2`).
```

I know how to solve this. just burn more tokens. use subagents and make subagents use subagnets. make it a full corporate.
and see all 6 tickets get solved in one hour. 6 tickets? we have 10 now. 10
superseded by 11 and 11 superseded by 12 and it's 4am already I need to sleep; matching the agents' speed is tiring.

### We're half there

the first `verify-match` was achieved by ticket 18. but random bugs like
