# Devpost submission text (edit the brackets)

**Track:** AI + Cybersecurity

**Tagline:** Paste a suspicious message. ScamTrap explains the scam, tells you what to do, and can run a decoy that gathers evidence.

**What it does:** ScamTrap checks SMS, WhatsApp, email or call transcripts for scams common in India. It returns a risk verdict, the exact warning signs it found, the known scam it matches, next steps, and a complaint draft for cybercrime.gov.in and helpline 1930. For likely scams, a decoy agent plays a fictional confused victim, keeps the scammer talking, and extracts links, UPI IDs, phone numbers and bank details into an evidence pack.

**The problem:** Scam victims lose money in minutes, and reporting is slow and confusing. People need a clear explanation and a ready report, not just a score.

**How we built it:** FastAPI backend; regex signal detection; TF-IDF retrieval over a library of 8 scam patterns; optional LLM (Featherless or any OpenAI-compatible API) for plain-language explanations and decoy replies, with scammer text treated as untrusted input; static front end on GitHub Pages; backend on Render.

**Where AI is used:** retrieval and LLM review for the verdict explanation, and an LLM-driven decoy persona with output filters (no numbers, handles or links can be sent; 3-turn cap).

**What works:** verdict, warning signs, pattern match, complaint draft, decoy against a simulated scammer, evidence extraction.

**What doesn't (yet):** the decoy only talks to a built-in simulated scammer with a fixed KYC-themed script, never real people. Detection is rule-based, so new wording can slip past it. Tested on two small hand-written sets: 24/24 on the first (written alongside the rules) and 28/30 on the second (2 false alarms). Email inbox intake is not built.

**Links:** Live demo: [GitHub Pages URL] | Code: [GitHub repo URL] | Video: [video URL]
