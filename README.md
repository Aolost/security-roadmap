# security-roadmap

A phased, ethical learning path from beginner toward job-ready or bug-bounty-ready security skills,
planned for about 12 months of part-time study.

> **Start here:** read [Phase 0: Legal and ethics](docs/00-legal-and-ethics.md) before anything else.
> Every hands-on activity in this roadmap uses only legal, intentionally vulnerable platforms or local
> virtual machines you control.

## Who this is for

- People new to security who want a structured, honest path rather than a random list of links.
- Developers, IT staff, and students who want to move toward a security role.
- Anyone considering bug bounty who wants the fundamentals first.

**Assumed background:** comfortable using a computer, installing software, and reading technical
English. No prior programming or security experience is assumed. You will need a computer that can run
a virtual machine and roughly 8–10 hours a week.

## Editorial opinions, not guarantees

The phase order, the time estimates, the choice of resources, the estimated hours per resource, and all
career and certification guidance are **editorial opinions**. They reflect one reasonable path, not
the only one. They do not guarantee a job, a certification pass, or bug-bounty income. Job markets,
certification value, and platform terms differ by country and change over time.

Resource *facts* are treated differently: every resource URL was opened before being added, and the
observed destination, HTTP status, page title, and check date are recorded in
[`data/sources.yaml`](data/sources.yaml) and listed in [`SOURCES.md`](SOURCES.md). Details that could
not be verified are recorded as `unknown`, and certification prices and formats say "check the
official site" unless they were confirmed there.

**Found a mistake, a broken link, or a better resource?** Please
[open an issue](../../issues/new). Corrections to opinions are welcome too: say what you would change
and why.

## Phase overview

| Phase | ID | Goal | Weeks | Planned time |
| --- | --- | --- | --- | --- |
| [0. Legal and ethics](docs/00-legal-and-ethics.md) | `legal-ethics` | Know the legal and ethical limits before touching anything | 1 | 1 week |
| [1. Foundations](docs/01-foundations.md) | `foundations` | Linux, networking, Python, and Bash | 2–12 | 11 weeks |
| [2. Web security](docs/02-web-security.md) | `web-security` | Understand, find (in labs), and explain fixes for common web flaws | 13–22 | 10 weeks |
| [3. Cryptography basics](docs/03-cryptography-basics.md) | `cryptography` | Know what crypto guarantees and how it is misused | 23–28 | 6 weeks |
| [4. Offensive practice and CTFs](docs/04-offensive-practice-and-ctf.md) | `offensive-practice` | A documented methodology on invited targets | 29–38 | 10 weeks |
| [5. Defence and malware analysis](docs/05-defence-and-malware-analysis.md) | `defence-malware` | Detection, response, and safe malware triage | 39–46 | 8 weeks |
| [6. Certifications and bug bounty](docs/06-certs-and-bug-bounty.md) | `certs-bug-bounty` | Choose a direction, prepare, and build a portfolio | 47–52 | 6 weeks |
| **Total** | | | | **52 weeks** |

Each phase document has a goal, prerequisites, a week-by-week plan, resources, hands-on labs, a
10-question checkpoint with a portfolio artifact, and common mistakes.

## How to use the roadmap

1. Read Phase 0 and write your own one-page rules of engagement.
2. Work through the phases in order. Each builds on the last.
3. At the end of each phase, answer the checkpoint questions without notes and publish the portfolio
   artifact.
4. Track your progress with the `roadmap` CLI (below) or any method you like.

### If you have less time

The 12-month plan assumes about 8–10 hours a week. With less time, **stretch the calendar rather
than cutting content**:

- At about 4–5 hours a week, plan on roughly two years: double each phase's weeks.
- Never skip Phase 0 or shorten Phase 1. Later phases depend on both.
- If you must trim, drop the optional "going deeper" resources and extra lab platforms first, not the
  checkpoints.
- Move on when you can answer the checkpoint, not when the calendar says so.

## The `roadmap` CLI

A small command-line tool that tracks which phases you have completed. Progress is stored **only on
your machine**, in your user configuration directory:

| Platform | Location |
| --- | --- |
| Linux and other Unix | `$XDG_CONFIG_HOME/security-roadmap/progress.json` (default `~/.config/security-roadmap/progress.json`) |
| macOS | `~/Library/Application Support/security-roadmap/progress.json` |
| Windows | `%APPDATA%\security-roadmap\progress.json` |

Set `SECURITY_ROADMAP_PROGRESS` to use a different file. Progress is never written into this
repository and never uploaded.

### Install

The CLI needs Python 3.10 or newer and has no third-party dependencies.

```bash
python3 -m pip install --user .
```

Or run it without installing, from the repository root:

```bash
python3 -m roadmap list
```

### Usage

```text
roadmap list          list the phases and their completion state
roadmap next          show the next incomplete phase
roadmap done ID       mark a phase complete, for example: roadmap done foundations
roadmap status        show overall and per-phase progress
```

A missing progress file means a fresh start. If the file is unreadable, the CLI explains the problem,
exits with status 3, and leaves the file untouched so that you can fix or move it.

## Repository checks

The checks need Python 3.10+ and, for Markdown lint, Node.js.

```bash
python3 -m pip install -r requirements-dev.txt
```

```bash
make check
```

| Command | What it does | Network |
| --- | --- | --- |
| `make validate` | Schema, unique IDs, URL schemes, dates, phase references, orphaned sources | Offline |
| `make sources` | Regenerate `SOURCES.md` from `data/sources.yaml` | Offline |
| `make sources-check` | Fail if `SOURCES.md` is out of date | Offline |
| `make test` | Unit tests | Offline |
| `make stale` | List sources not rechecked in 12 months | Offline |
| `make lint-md` | Markdown lint with markdownlint-cli2 | Downloads the linter on first run |
| `make links` | Check every source URL and write `link-report.md` | Network |

`make check` runs `validate`, `sources-check`, `test`, and `lint-md`.

### Continuous integration

- **Pull requests** run Markdown lint, the offline checks, and a link check. These workflows have
  read-only permissions, including for forks.
- **A weekly scheduled job** checks every source URL in a read-only job, then a separate job with only
  `issues: write` permission opens or updates a single tracking issue for dead, moved, or stale
  sources.

## Repository layout

```text
README.md                 this file
SOURCES.md                generated list of resources (do not edit by hand)
CONTRIBUTING.md           how to propose and verify resources
RELEASE_CHECKLIST.md      steps for tagging v0.1.0
data/sources.yaml         single source of truth for resources
data/sources.schema.json  JSON Schema for sources.yaml
docs/                     the legal page and six phase documents
roadmap/                  the CLI
scripts/                  validator, generator, stale report, network link check
tests/                    offline tests and fixtures
.github/workflows/        CI and the weekly link check
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: open an issue first, verify any resource by opening
it, record what you observed, and run `make check`.

## Licence

No licence has been chosen yet. Until one is added, normal copyright applies. See
[RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md).
