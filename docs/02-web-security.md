# Phase 2: Web security

Phase ID: `web-security` · Planned time: weeks 13–22 (10 weeks at about 8–10 hours a week)

## Goal

Understand how web applications work and fail, recognize the most common vulnerability classes, and
explain both how each is found in a lab and how it is fixed.

## Prerequisites

- Phase 1 complete, especially HTTP, Python, and the command line.
- A local VM or container runtime for running intentionally vulnerable applications.

## Week-by-week plan

| Week | Focus | Outcome |
| --- | --- | --- |
| 13 | How the web works: requests, cookies, sessions, same-origin policy. Set up Burp Suite Community or ZAP | You can intercept and replay your own lab traffic |
| 14 | OWASP Top 10 overview; set up DVWA and Juice Shop locally on an isolated network | Both apps running on your machine |
| 15 | Injection: SQL injection concepts in Web Security Academy labs | Notes on root cause and fix |
| 16 | Cross-site scripting (reflected, stored, DOM) | You can explain output encoding and CSP |
| 17 | Authentication and session management flaws | Notes on secure session design |
| 18 | Access control and IDOR | You can explain why server-side checks matter |
| 19 | Server-side request forgery, path traversal, file upload risks | Notes and lab completions |
| 20 | CSRF, CORS, and clickjacking | You can explain the browser rules involved |
| 21 | Juice Shop and Natas practice; methodology with the OWASP testing guide | A repeatable testing checklist |
| 22 | Checkpoint and portfolio artifact | Checkpoint answered; artifact published |

## Resources

Learning:

- [src:portswigger-web-security-academy](../SOURCES.md#portswigger-web-security-academy): main
  course and labs for this phase.
- [src:hacker101](../SOURCES.md#hacker101): video lessons and practice CTF.
- [src:mdn-http](../SOURCES.md#mdn-http): refresh HTTP details as needed.

Frameworks and methodology:

- [src:owasp-top-ten](../SOURCES.md#owasp-top-ten)
- [src:owasp-wstg](../SOURCES.md#owasp-wstg)
- [src:owasp-cheat-sheets](../SOURCES.md#owasp-cheat-sheets): how to fix what you find.

Local practice applications:

- [src:dvwa](../SOURCES.md#dvwa)
- [src:owasp-juice-shop](../SOURCES.md#owasp-juice-shop) and its companion guide
  [src:pwning-juice-shop](../SOURCES.md#pwning-juice-shop)
- [src:otw-natas](../SOURCES.md#otw-natas)

Tools (use only against lab targets):

- [src:burp-community](../SOURCES.md#burp-community)
- [src:owasp-zap](../SOURCES.md#owasp-zap)

## Hands-on labs

| Lab | Learning goal | Where to find it |
| --- | --- | --- |
| Web Security Academy topic labs | Recognize each vulnerability class and its root cause in a safe, hosted lab | PortSwigger Web Security Academy, one learning path per topic |
| DVWA at different security levels | See how the same feature behaves with weak and stronger defences | DVWA running in a local VM or container |
| OWASP Juice Shop challenges | Practise discovery across a modern single-page application | Juice Shop running locally; its score board lists challenges |
| OverTheWire Natas | Server-side web basics through short levels | OverTheWire, Natas wargame |
| Hacker101 CTF | Apply lessons in a beginner-friendly CTF | Hacker101 CTF |

Keep DVWA and Juice Shop off the public internet. They are deliberately insecure.

## Checkpoint

1. What is the difference between authentication and authorization?
2. Why does parameterizing a database query prevent SQL injection?
3. Compare reflected, stored, and DOM-based XSS.
4. What does the same-origin policy restrict, and what does CORS relax?
5. Why must access-control checks happen on the server?
6. How does a CSRF token protect a state-changing request?
7. What makes server-side request forgery dangerous inside a cloud environment?
8. Which cookie attributes help protect session cookies, and what does each do?
9. How would you describe a finding's impact to a developer who must fix it?
10. Name one OWASP Top 10 category and a defensive control for it.

**Portfolio artifact:** a learning write-up of one lab vulnerability class, published on your blog or
repository. Explain the root cause, how you recognized it in the lab, and how to fix it, with code
showing the secure pattern. Do not publish working exploit payloads or full lab solutions.

## Common mistakes

- Memorizing payloads instead of understanding root causes.
- Pointing tools at real websites "just to see". Only use lab targets.
- Running automated scanners before understanding the application manually.
- Exposing DVWA or Juice Shop on a network others can reach.
- Writing up only the attack and not the fix. Employers and programs value both.
