# Phase 0: Legal and ethics

Phase ID: `legal-ethics` · Planned time: week 1 (about 6–8 hours)

Read this page before any hands-on work. It is a practical introduction written by learners for
learners. **It is not legal advice.** Laws differ by country, and sometimes by state or region. If you
are unsure whether an activity is legal where you live, stop and ask a qualified lawyer or your
employer's legal team.

## Goal

Understand the rules that separate security learning and authorized testing from crime, so that
every later phase is done safely, legally, and with permission.

## Prerequisites

None. This is the first thing to read.

## The core rule: explicit, written authorization

Security testing is legal only when the owner of a system has given you permission to test it, and
only within the limits of that permission.

- **Get permission in writing**, from someone who actually has the authority to grant it. A friend
  who works somewhere cannot authorize you to test their employer's systems.
- **Stay inside the written scope.** Scope names which systems, addresses, applications, and
  techniques are allowed, and when. Anything not listed is out of scope.
- **Permission does not transfer.** Permission to use one training platform, one lab, or one bug-bounty
  program applies only there. It says nothing about any other system, including systems that look
  related, share a domain, or belong to the same company.
- **Your own equipment is the safe default.** A local virtual machine running an intentionally
  vulnerable application (such as DVWA or OWASP Juice Shop) on an isolated network is where most
  experimentation in this roadmap should happen.

## Computer-misuse law, in general terms

Most countries have laws that make it a crime to access a computer system without authorization, to
exceed the access you were given, or to impair, damage, or interfere with a system or its data. Many
also cover making or supplying tools with intent to commit those offences. Penalties can include
fines and imprisonment, and civil claims can follow even when no one is prosecuted.

Two official sources show what such laws look like:

- [src:uk-computer-misuse-act](../SOURCES.md#uk-computer-misuse-act): the UK Computer Misuse Act 1990.
- [src:us-doj-cfaa-manual](../SOURCES.md#us-doj-cfaa-manual): the US Department of Justice manual
  section on the Computer Fraud and Abuse Act.

These are examples only. **Check the law in your own country**, and the rules of any organization,
school, employer, or platform you work with. Good intentions are not, by themselves, a legal defence.

## Rules of engagement

Professional testers agree on rules of engagement before starting. As a learner, adopt the same habits
now:

1. Know exactly what is in scope and what is out of scope.
2. Know the allowed time window, testing techniques, and any rate limits.
3. Know who to contact if something goes wrong, and how.
4. Avoid actions that could harm availability or data, such as denial of service, mass automated
   scanning, or modifying or deleting other people's data, unless explicitly allowed.
5. Handle any personal data you encounter minimally: do not copy, keep, or share it.
6. **When scope or authorization is unclear, stop.** Ask, in writing, and wait for an answer before
   continuing. "I assumed it was fine" is not authorization.

## Responsible disclosure

If you find a vulnerability in a system you were authorized to test, report it privately to the owner
and give them reasonable time to fix it before discussing it publicly.

- Look for an official channel first: a vulnerability disclosure policy, a bug-bounty program, or a
  `security.txt` file ([src:rfc9116-security-txt](../SOURCES.md#rfc9116-security-txt)).
- Describe the issue clearly and minimally: what is affected, how to reproduce it at a high level,
  and its impact. Do not include more sensitive data than needed to prove the issue.
- Communicate politely and keep records. Do not make demands or threats, and never ask for payment as
  a condition of disclosure.
- Read [src:owasp-vuln-disclosure-cheatsheet](../SOURCES.md#owasp-vuln-disclosure-cheatsheet) and
  [src:disclose-io](../SOURCES.md#disclose-io) for practical guidance and safe-harbour language.

If you stumble on something by accident on a system you were **not** authorized to test, do not
investigate further. Stop, and consider whether reporting through an official channel is appropriate.

## Bug-bounty programs: scope, exclusions, and program rules

A bug-bounty program is a specific, limited permission. Each program publishes its own rules, and
they differ.

- **Read the whole policy before testing**, every time, because programs change their rules.
- **In-scope assets** are listed explicitly. Assume everything else is out of scope.
- **Exclusions** list vulnerability types and techniques the program does not accept or forbids, such
  as social engineering, physical testing, or denial of service.
- **Rate limits and automation rules** say how fast and how much you may send. Respect them exactly.
- **Program-specific rules** cover things like test accounts, data handling, disclosure timing, and
  confidentiality.
- Platforms document how programs and reports work. See
  [src:hackerone-docs](../SOURCES.md#hackerone-docs) and, for how severity is classified on one
  platform, [src:bugcrowd-vrt](../SOURCES.md#bugcrowd-vrt).

Joining a platform does not authorize you to test every company on it. Each program's scope is
separate.

## Never test real systems without permission

Do not test websites, networks, devices, or accounts that you do not own or have explicit written
permission to test. This includes your school, your employer, your internet provider, public Wi-Fi,
and "just checking" a website you use. All hands-on work in this roadmap uses only:

- intentionally vulnerable training platforms, used under their own terms (OverTheWire, TryHackMe,
  PortSwigger Web Security Academy, Hack The Box, picoCTF, Hacker101, Cryptopals), and
- local virtual machines or containers you control, running intentionally vulnerable applications
  (DVWA, OWASP Juice Shop).

Each platform's terms apply only to that platform's own targets.

## Week-by-week plan

| Week | Focus |
| --- | --- |
| 1 | Read this page and the linked laws and disclosure guidance. Look up the computer-misuse law that applies where you live. Read the terms of service of the first platform you plan to use. |

## Resources

- [src:uk-computer-misuse-act](../SOURCES.md#uk-computer-misuse-act)
- [src:us-doj-cfaa-manual](../SOURCES.md#us-doj-cfaa-manual)
- [src:disclose-io](../SOURCES.md#disclose-io)
- [src:owasp-vuln-disclosure-cheatsheet](../SOURCES.md#owasp-vuln-disclosure-cheatsheet)
- [src:rfc9116-security-txt](../SOURCES.md#rfc9116-security-txt)
- [src:hackerone-docs](../SOURCES.md#hackerone-docs)
- [src:bugcrowd-vrt](../SOURCES.md#bugcrowd-vrt)

## Hands-on labs

This phase has no hacking labs. The exercise is to read and summarize:

| Lab | Learning goal | Where |
| --- | --- | --- |
| Find your local law | Identify the computer-misuse law that applies to you and summarize it in your own words | Your government's official legislation website |
| Read a platform's terms | Know what a training platform allows before using it | The terms page of the first platform you will use, such as OverTheWire or TryHackMe |
| Read a disclosure policy | Practise identifying scope, exclusions, and safe-harbour language | Any public disclosure policy or bug-bounty program page |

## Checkpoint

Answer these without looking anything up:

1. What does "authorization" mean in security testing, and who can give it?
2. Why is written permission better than verbal permission?
3. What should you do if you are unsure whether a target is in scope?
4. Does permission to use one training platform let you test a company's live website? Why not?
5. Name three kinds of activity that computer-misuse laws commonly prohibit.
6. What is responsible disclosure, and why does timing matter?
7. What is a `security.txt` file for?
8. What do "exclusions" and "rate limits" mean in a bug-bounty policy?
9. What should you do if you accidentally find a weakness in a system you were not testing?
10. Which law applies to computer misuse where you live, and where did you confirm that?

**Portfolio artifact:** a short personal "rules of engagement" document (one page) that states the
platforms you will use, the local lab setup you will build, and what you will never do. Publish it in
your learning repository or blog.

## Common mistakes

- Treating "it is publicly reachable" as permission to test.
- Assuming that a bug-bounty program covers every asset a company owns.
- Running automated scanners against targets that do not allow them.
- Keeping or sharing data found during testing.
- Skipping this page because it is not technical. It is the page most likely to keep you out of
  trouble.
