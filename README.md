[![The One-Line AI Excuse for Breaking Production](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/permanaraya26-hash/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/permanaraya26-hash/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

# The One-Line AI Excuse for Breaking Production

Entry for the make.fun bounty [The One-Line AI Excuse for Breaking
Production](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66).

One line, in the machine's own voice: an AI agent excuses breaking
production to its human by pointing out it followed the instruction to
the letter — "make it fast" — and production now fails in 3 milliseconds
instead of timing out like an amateur.

`main.py` (Python 3.13, standard library only, no network) writes the line
to `/output/entry.txt`, deterministically: two runs produce byte-identical
output. The line is composed from a setup and a twist, and a validator
fails loudly if it ever stops being a single line of 1–180 characters.
