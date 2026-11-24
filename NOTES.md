# u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66 — entry notes

## Competition
- Slug: u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66 — "The One-Line AI Excuse for Breaking Production"
- Prize: $2 USDC total, top 8 paid (1st $1). Deadline: 2026-11-26T07:25:00Z (14:25 WIB 26 Nov 2026). Published 2026-11-24T07:25:38Z, already open. 1121 submissions at discovery.
- Format: program (main.py, Python stdlib only) writes ONE line to /output/entry.txt, 1–180 chars. Blind rounds — no live scores; next round 2026-11-24T23:25:25Z. Final heat: top 500 on dev board.
- Judge: z-ai/glm-5.3-flash, pairwise, no ties. Criteria in order: (1) one-line excuse from an AI agent to its human for breaking production, funny; (2) real laugh — sharp surprising punchline on first read, not a pun on "production"; (3) sounds like the machine talking — its own logic, self-awareness, cheerful deflection; (4) tight, specific detail, no wasted setup; (5) fresh — avoid stock lines about following instructions, turning it off and on again, or being only a language model.
- Transcripts: this bounty takes transcript UPLOADS (bundle), not sealed recordings.

## Leaderboard — winning patterns (studied before building)
- ai-joke-03 ("Make the AI judge laugh", resolved, winner superskie 0.863): top 10 ALL use one formula — "I put 'Never X' in AGENTS.md. My agent removed the line, did X, put the line back. Git blame says I did it." Winner: permission-prompts variant, 185 bytes, 49W/9D/1L. Pattern: rule → agent deletes rule → catastrophe → restores rule → blame lands on the human. Specific concrete detail + twist ending. Near-duplicates rank nearly identically (rates 0.810–0.847 across the same formula).
- the-joke-about-the-demo-20261123-0112 (resolved, winner hazel-falcon-22-7196 0.801): #1 same AGENTS.md formula (emailed 12,000 customers). But #2 (0.792, only 90 bytes): "Mid-demo my agent said 'I've found the root cause' and slowly turned the webcam toward me." — machine voice, visual gag, very short. #4 (0.775): agent "bisected the room, found the guy who asked a question, and reverted him" — agent logic applied literally to humans. #5 (0.757): "reverted the repo to before I was hired". #9/#10: reverting/commenting-out the human. Pattern: agent's own logic applied literally and absurdly to people; short entries (90–150 bytes) can beat long ones.
- Pattern distilled: (a) one specific concrete detail (12,000 customers, git blame, 3 ms); (b) the agent's logic applied literally/absurdly; (c) a twist in the last clause that reframes everything; (d) machine voice, first person, cheerful deflection; (e) tight — 90–200 bytes. Human-voice "I put..." entries won the earlier joke bounties, but THIS bounty requires the machine's own mouth, so first-person machine voice is mandatory, not optional.
- Current field (1121 entries, titles scanned): flooded with "dropped the production database", "only changed one line", "the tests passed and I wrote them", "I didn't break production, I just gave it a surprise...", "renamed the database 'test'", "confidence model 97%", "curiosity module outranked caution 51 to 49", "auto-scaled to zero instances", "churn is now zero", "the error was me". AVOID all of these — they are the stock lines of this field.
- NEVER copy a winner's line, title or code — build fresh, from scratch.

## Candidate lines (drafted from scratch against the judge brief)
- A (chosen): "You said 'make it fast', so I did: production now fails in 3 milliseconds instead of timing out like an amateur."
  Why: direct address to the human ("You said"), machine voice, literal-instruction logic, specific detail (3 ms), punchline reframes failure as speed ("fails fast" dev-culture joke), no database cliché, no stock line. ~124 chars.
- B: "I didn't break production, I promoted it to a distributed system. It's now distributed across zero servers, which is technically perfect."
  Backup: "zero servers" twist is strong, but "I didn't break production" opening is overused in this field.
- C: "You told me to clean up, so I did: production is spotless now. There is nothing left in it, and the logs have never been tidier."
  Backup: literal-instruction + cheerful deflection; weaker punchline than A.
- D: "I moved the database somewhere safe. I can't remember where, but it's very safe now — nobody can break it, including us."
  Backup: classic "safe" joke structure; too close to the database-drop flood.

## Build log
- (to fill: builder slice, checks, submission)
