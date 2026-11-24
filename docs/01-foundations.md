# Phase 1: Foundations (Linux, networking, Python, Bash)

Phase ID: `foundations` · Planned time: weeks 2–12 (11 weeks at about 8–10 hours a week)

## Goal

Become comfortable on the Linux command line, understand how data moves across a network, and write
small Python and Bash scripts. Every later phase assumes these skills.

## Prerequisites

- [Phase 0: Legal and ethics](00-legal-and-ethics.md) read and understood.
- A computer that can run a Linux virtual machine (or a Linux install), plus basic typing and
  file-management skills.

## Week-by-week plan

| Week | Focus | Outcome |
| --- | --- | --- |
| 2 | Set up a Linux VM. Shell basics: navigation, files, permissions, help pages | You can move around and read `man` pages |
| 3 | Pipes, redirection, text tools (`grep`, `sort`, `cut`), processes | You can answer questions about a log file with a pipeline |
| 4 | OverTheWire Bandit, first levels; SSH; users and groups | Bandit progress logged in your notes |
| 5 | Networking model: IP addresses, ports, TCP vs UDP, DNS, routing | You can explain what happens when you open a web page |
| 6 | HTTP in detail; capture your own traffic in Wireshark on your own machine | You can read a captured HTTP exchange |
| 7 | Python: variables, control flow, functions, files | Small scripts run without help |
| 8 | Python: data structures, modules, error handling, working with text and JSON | A log-parsing script |
| 9 | Python: sockets and simple clients against your own local server | A local client/server pair |
| 10 | Bash scripting: variables, conditions, loops, quoting; lint with ShellCheck | A clean, ShellCheck-quiet script |
| 11 | Finish more Bandit levels; review weak areas | Bandit notes and a list of gaps |
| 12 | Checkpoint and portfolio artifact | Checkpoint answered; artifact published |

## Resources

Linux and Bash:

- [src:tlcl-book](../SOURCES.md#tlcl-book): main text for the shell.
- [src:gnu-bash-manual](../SOURCES.md#gnu-bash-manual): reference when Bash behaves unexpectedly.
- [src:explainshell](../SOURCES.md#explainshell): break down commands you do not recognize.
- [src:shellcheck](../SOURCES.md#shellcheck): lint every script you write.

Networking:

- [src:mdn-http](../SOURCES.md#mdn-http): HTTP methods, headers, status codes, cookies.
- [src:wireshark](../SOURCES.md#wireshark) and
  [src:wireshark-users-guide](../SOURCES.md#wireshark-users-guide): capture and read traffic.
- [src:beej-network-programming](../SOURCES.md#beej-network-programming): sockets, optional but
  recommended if you want to see networking from a programmer's side.

Python:

- [src:python-tutorial](../SOURCES.md#python-tutorial): the official tutorial.
- [src:automate-boring-stuff](../SOURCES.md#automate-boring-stuff): practical scripting.

Practice platforms:

- [src:otw-bandit](../SOURCES.md#otw-bandit)
- [src:tryhackme](../SOURCES.md#tryhackme)

## Hands-on labs

| Lab | Learning goal | Where to find it |
| --- | --- | --- |
| OverTheWire Bandit | Linux commands, file permissions, SSH, and reading documentation under light pressure | OverTheWire, Bandit wargame |
| Capture your own traffic | Recognize DNS, TCP handshakes, and HTTP requests in a real capture | Wireshark on your own computer, capturing only your own traffic |
| Local client and server | Understand ports and sockets by building both ends | Two Python scripts on your own machine or VM |
| Beginner rooms on Linux and networking | Reinforce fundamentals with guided exercises | TryHackMe, beginner learning paths (pick rooms on Linux and networking basics) |

Capture only traffic on networks and devices you own or are explicitly allowed to monitor.

## Checkpoint

1. What do the read, write, and execute permission bits mean on a file and on a directory?
2. What is the difference between `>` and `>>`, and what does `2>&1` do?
3. How would you find every line containing "error" in all `.log` files under a directory?
4. Describe the TCP three-way handshake.
5. What does DNS do, and what record type maps a name to an IPv4 address?
6. What is the difference between an HTTP `GET` and `POST` request?
7. What does a 302 status code mean, and how does a browser respond to it?
8. In Python, how do you read a file line by line and handle a missing file gracefully?
9. Why should you quote variables in Bash, and what can go wrong if you do not?
10. What is a port, and why can two programs not normally listen on the same port and address?

**Portfolio artifact:** a small, well-documented defensive utility, such as a Python script that
summarizes failed SSH logins from a sample log file you created, with a README and tests. Publish it
in a public repository. Use only sample data you made yourself.

## Common mistakes

- Copying commands without understanding them. Use `man`, `--help`, and explainshell first.
- Running as root by default. Use `sudo` only when you need it.
- Skipping networking because it feels abstract. Web security and defence depend on it.
- Writing long scripts without testing small pieces first.
- Posting Bandit passwords or full solutions publicly. Share what you learned, not the answers.
