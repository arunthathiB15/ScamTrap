# ScamTrap

Checks a suspicious message (SMS, WhatsApp, email, call transcript) and returns a risk verdict, the warning signs it found, the known scam it matches, what to do next, and a complaint draft for cybercrime.gov.in / helpline 1930.

Built for ForgeHacks 2026, track: AI + Cybersecurity.

## How it works
1. Signal detection: regex rules find urgency, requests for OTP/PIN/money, authority threats, suspicious links, secrecy and remote-access demands.
2. Retrieval: a TF-IDF index over `backend/kb.json` (8 scam patterns) finds the closest known scam.
3. Optional LLM review (`LLM_API_KEY`): explains the verdict in plain language. The message is treated as untrusted input in the prompt. Without a key the app runs on rules only.

## What works / what doesn't (update before submitting)
- Works: verdict, red flags, pattern match, complaint draft, 8 India-focused scam patterns; decoy agent that plays a fictional victim and extracts links, UPI IDs, phone numbers, bank accounts, IFSC codes and wallets into an evidence pack.
- Limits: the decoy talks only to a built-in simulated scammer (a fixed 3-turn script that reveals fake details); it never contacts real people. The simulated scammer is KYC-themed whatever the input scam type. Detection is rule-based plus TF-IDF, so new wording can slip past it.
- Accuracy (rules only, no LLM): `python backend/eval.py` scores 24/24, but those messages were written alongside the rules. A second set, `python backend/eval_holdout.py` (30 messages, different wording, Hinglish, tricky legitimate bank and payment alerts), scored 28/30 (93%) on the first run with no rule changes: all 15 scams caught, 2 false alarms (a friend saying "I transferred Rs 2000", and a legitimate "police verification form" notice). Both sets are small and hand-written by the authors, so treat them as sanity checks, not a benchmark.
- Not built: email inbox intake (Agentboxd). LLM mode (explanations and decoy replies) is optional and needs your own API key; the tested path is rules-only.

## Decoy safety
Victim replies (LLM or scripted) are filtered so they cannot contain digits runs, handles or links; the LLM prompt treats scammer text as untrusted; the loop is capped at 3 turns.

## Run locally
```bash
cd backend && pip install -r requirements.txt && uvicorn main:app --reload
# open docs/index.html in a browser (it calls http://localhost:8000)
```

## Deploy (free)
1. Push this repo to GitHub.
2. Backend: on render.com, New > Blueprint, pick the repo (uses `render.yaml`). Add `LLM_API_KEY` if you have one. Copy the service URL.
3. Frontend: put that URL in `API` in `docs/index.html`, commit, then in GitHub go to Settings > Pages > Source: GitHub Actions. The workflow publishes `docs/`.
