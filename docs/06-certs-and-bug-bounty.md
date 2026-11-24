# Phase 6: Certifications and bug bounty

Phase ID: `certs-bug-bounty` · Planned time: weeks 47–52 (6 weeks at about 8–10 hours a week)

## Goal

Choose a direction, toward a security job or toward bug-bounty work, and prepare for it: pick a
certification if it helps your goal, understand how bug-bounty programs work, and assemble a portfolio.

This phase contains the most opinion. Certification value varies by country, employer, and role.
Treat the guidance below as one reasonable path, not a guarantee of a job or of bounty income.

## Prerequisites

- Phases 0–5 complete.
- Phase 0 reread, especially the sections on bug-bounty scope and disclosure.

## Week-by-week plan

| Week | Focus | Outcome |
| --- | --- | --- |
| 47 | Choose a direction. Read job descriptions in your region and list the skills and certifications they ask for | A short written plan |
| 48 | If pursuing a certification: read the official exam objectives and map them to your gaps | A study plan with dates |
| 49 | Bug-bounty basics: how programs, scopes, and reports work; severity scoring | You can read a program policy and summarize scope |
| 50 | Report writing: practise on lab findings from Phases 2 and 4 | Two polished practice reports |
| 51 | Portfolio: collect artifacts from every phase; tidy repositories and write-ups | A portfolio page |
| 52 | Checkpoint, retrospective, and next-year plan | Checkpoint answered; plan published |

## Direction A: security job

Entry-level certifications can help some applicants pass résumé filters. Prices, prerequisites, and
exam formats change, so confirm everything on the official site before paying.

- [src:comptia-security-plus](../SOURCES.md#comptia-security-plus): widely listed for junior roles.
  Price and exam format: check the official site.
- [src:isc2-cc](../SOURCES.md#isc2-cc): entry-level; the official page said no experience is needed.
  Price and exam format: check the official site.
- [src:offsec-pen-200](../SOURCES.md#offsec-pen-200): advanced, hands-on, for offensive roles. The
  official page described a 24-hour proctored exam. See `SOURCES.md` for the price observed on the
  check date, and confirm on the official site.
- [src:htb-academy](../SOURCES.md#htb-academy): offers its own certifications alongside training.

Many employers value demonstrated skill (write-ups, tools, detections) as much as certificates. Your
portfolio from earlier phases is evidence of that.

## Direction B: bug bounty

Bug bounty is competitive and income is unpredictable. Start with programs that welcome newcomers,
read every policy fully, and expect duplicates and rejections while you learn.

- [src:hacker101](../SOURCES.md#hacker101): free lessons aimed at bug hunters.
- [src:hackerone-docs](../SOURCES.md#hackerone-docs): how programs and reports work on one platform.
- [src:bugcrowd-vrt](../SOURCES.md#bugcrowd-vrt): how one platform rates severity.
- [src:first-cvss](../SOURCES.md#first-cvss): the common scoring standard.
- [src:disclose-io](../SOURCES.md#disclose-io): what safe-harbour language looks like.

Before testing any program, confirm:

1. the asset is listed as in scope,
2. the vulnerability type and technique are not excluded,
3. you can follow the rate limits and automation rules,
4. you understand the program's rules on test accounts, data, and disclosure.

If any of these is unclear, ask the program and wait. Permission from one program never covers another.

## Hands-on labs

| Lab | Learning goal | Where to find it |
| --- | --- | --- |
| Policy reading drill | Identify scope, exclusions, rate limits, and safe harbour in real program policies (reading only, no testing) | Public program pages on bug-bounty platforms |
| Practice reports | Write clear, reproducible, remediation-focused reports | Your own findings from Web Security Academy, DVWA, or Juice Shop labs |
| Severity scoring | Score your practice findings consistently | CVSS calculator and documentation from FIRST |
| Bug-hunter CTF | Practise in a hunter-oriented environment | Hacker101 CTF |
| Certification-aligned labs | Close gaps found in the exam objectives | TryHackMe, HTB Academy, or Hack The Box content mapped to your chosen certification |

## Checkpoint

1. Which direction did you choose, and what evidence from job listings or programs supports it?
2. What does an in-scope asset list mean, and what should you assume about unlisted assets?
3. What are common bug-bounty exclusions, and why do programs exclude them?
4. What should a good vulnerability report contain?
5. How does CVSS represent severity, and what are its limits?
6. What is a duplicate report, and how should you react to one?
7. Why should you confirm certification prices and formats on the official site?
8. What is safe-harbour language, and why does it matter?
9. What would you do if testing unexpectedly exposed personal data?
10. Which three portfolio pieces best show your skills, and why?

**Portfolio artifact:** a portfolio page linking your artifacts from every phase, plus one polished
sample vulnerability report based on a lab finding (not a real program), including severity reasoning
and remediation advice.

## Common mistakes

- Buying a certification before checking whether employers in your area ask for it.
- Testing bug-bounty assets before reading the full policy.
- Using automated tools against programs that limit or forbid them.
- Writing reports that show an attack but give developers nothing to act on.
- Measuring progress only by bounties. Learning and a strong portfolio come first.
