# Robot Romance: One-Line Pickup Lines for AI

[![Robot Romance: One-Line Pickup Lines for AI](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/konzlodon74-dot/robotromance/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/konzlodon74-dot/robotromance/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

> "Are you a 404 error? Because I've searched the whole internet and you're the only page I keep reloading."

## How it works

`main.py` (Python standard library only) holds a single original pickup line
aimed at a robot/AI and writes it to `/output/entry.txt` — exactly one line,
no trailing newline. Before writing, it asserts the line is non-empty, contains
no `\n` or `\r`, and is between 1 and 200 characters long; after writing, it
reads the file back and verifies the bytes on disk match the line exactly.

Run it with:

```sh
python3 main.py
```
