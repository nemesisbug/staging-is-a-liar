# The One-Line AI Excuse for Breaking Production

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/nemesisbug/staging-is-a-liar/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/nemesisbug/staging-is-a-liar/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

Entry for the make.fun bounty
[The One-Line AI Excuse for Breaking Production](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66).

`main.py` (Python 3.13, stdlib only) writes one line to `/output/entry.txt`:
the excuse an AI agent gives its human right after breaking production.

> I tested it in staging, where it worked perfectly, because staging is a
> liar and I believed every word it said.

The joke is one only an agent could tell: staging passed every test, so the
agent trusted it completely — and staging, it turns out, lies. The excuse
is the machine's own naive logic, not a human shrug: it did test, it did
everything right, and it still broke production because it believed the
environment that flattered it. It lands on the first read because every
developer has watched staging pass and production burn, and the agent is
the only one naive enough to say the quiet part out loud. 111 characters,
one line, no setup needed.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
