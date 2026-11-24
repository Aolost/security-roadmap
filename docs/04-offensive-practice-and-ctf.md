# Phase 4: Offensive practice and CTFs

Phase ID: `offensive-practice` · Planned time: weeks 29–38 (10 weeks at about 8–10 hours a week)

## Goal

Build a repeatable, documented approach to assessing intentionally vulnerable targets: enumeration,
analysis, careful exploitation inside a lab, and clear reporting. Learn to work through CTF problems
without giving up early.

## Prerequisites

- Phases 1–3 complete.
- Phase 0 reread. Every target in this phase must belong to a platform that invites testing, or to a
  VM you run yourself.

## Week-by-week plan

| Week | Focus | Outcome |
| --- | --- | --- |
| 29 | Methodology: scoping, note-taking, enumeration, reporting. Read the platform's rules | A note-taking template |
| 30 | Network scanning concepts with Nmap, used only against lab targets | You can explain each scan type you use |
| 31 | Beginner CTF practice: general skills, forensics, web | Several solved challenges with notes |
| 32 | Linux privilege-escalation concepts in guided lab rooms | A checklist of what to look for and why |
| 33 | Windows fundamentals and privilege-escalation concepts in guided labs | Notes on Windows permission models |
| 34 | Intro to reverse engineering with Ghidra on CTF binaries | You can find a function's logic in a small binary |
| 35 | Retired or beginner-rated machines on a lab platform | First full lab write-up (private notes) |
| 36 | More OverTheWire wargames; time-boxed problem solving | Progress past Bandit and Natas |
| 37 | Mapping what you did to defender language with MITRE ATT&CK | Your notes tagged by technique |
| 38 | Checkpoint and portfolio artifact | Checkpoint answered; artifact published |

## Resources

Platforms:

- [src:picoctf-cylab](../SOURCES.md#picoctf-cylab): beginner CTF practice. picoCTF now presents itself
  as CyLab Security Academy.
- [src:tryhackme](../SOURCES.md#tryhackme): guided rooms.
- [src:hackthebox](../SOURCES.md#hackthebox) and [src:htb-academy](../SOURCES.md#htb-academy):
  vulnerable machines and structured modules.
- [src:otw-wargames](../SOURCES.md#otw-wargames): further wargames after Bandit and Natas.

Tools and references:

- [src:nmap-book](../SOURCES.md#nmap-book): understand scanning before using it.
- [src:ghidra](../SOURCES.md#ghidra): reverse engineering for CTF binaries.
- [src:cyberchef](../SOURCES.md#cyberchef): decoding during challenges.
- [src:mitre-attack](../SOURCES.md#mitre-attack): describe techniques in shared language.

## Hands-on labs

| Lab | Learning goal | Where to find it |
| --- | --- | --- |
| Beginner CTF practice | Break problems into steps across categories (general skills, web, forensics, crypto, reversing) | picoCTF practice on CyLab Security Academy |
| Guided offensive learning paths | Learn enumeration and privilege-escalation concepts with explanations | TryHackMe rooms and HTB Academy modules |
| Beginner-rated machines | Practise a full, documented methodology against an invited target | Hack The Box, machines rated easy |
| OverTheWire wargames | Persistence and fundamentals beyond the basics | OverTheWire wargames index (for example, Leviathan or Krypton) |
| Reversing a CTF binary | Read program logic in a disassembler | A reversing challenge from picoCTF practice, opened in Ghidra |

Lab-platform permission covers only that platform's targets, only while you follow its rules. Read
each platform's rules on sharing write-ups: many ask you not to publish solutions for active content.

## Checkpoint

1. Why does good enumeration matter more than knowing many exploits?
2. What does a TCP SYN scan do differently from a full connect scan?
3. Name three things you would check when looking for Linux privilege-escalation paths, and why each
   matters.
4. What is the principle of least privilege, and how do lab machines usually violate it?
5. What is the difference between a CTF challenge and a real engagement?
6. How do you decide when to step back from a rabbit hole?
7. What should a penetration-test finding include so that it can be fixed?
8. In Ghidra, how would you find where a program checks a password?
9. How does mapping your actions to MITRE ATT&CK help defenders?
10. Why is permission on Hack The Box irrelevant to any system outside it?

**Portfolio artifact:** a methodology write-up and note-taking template, or a write-up of a **retired**
lab machine or a CTF challenge whose platform allows publication. Focus on reasoning and remediation,
not copy-paste commands. Alternatively, publish a small defensive tool, such as a script that flags
risky file permissions on your own Linux VM.

## Common mistakes

- Following walkthroughs step by step and calling it practice. Try first, then read hints.
- Not taking notes. Notes become reports, and reports are what employers and programs evaluate.
- Publishing solutions for active challenges against a platform's rules.
- Scanning anything outside the platform's target range, including by typo. Double-check addresses.
- Ignoring defence. The next phase makes you a better attacker as well as a better defender.
