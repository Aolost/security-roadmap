# v0.1.0 release checklist

No release or tag has been created yet. Work through this list before tagging `v0.1.0`.

## Repository setup

- [x] Choose and add a licence (`LICENSE`), then update the Licence section of the README.
- [ ] Create the GitHub repository and push the default branch `main`.
- [ ] Enable issues so that readers can report corrections and the weekly link check can open its
      tracking issue.
- [ ] In repository settings, set the default `GITHUB_TOKEN` permission to read-only, and require
      approval before running workflows from first-time fork contributors.
- [ ] Protect `main`: require the CI checks to pass before merging.

## Checks

- [ ] `make check` passes locally.
- [ ] CI passes on a pull request: Markdown lint, offline checks, and link check.
- [ ] Run the scheduled link check once by hand (`workflow_dispatch`) and confirm that it creates or
      updates a single tracking issue only when problems exist.
- [ ] `make stale` reports no stale sources.

## Content review

- [ ] Every phase document has a goal, prerequisites, week-by-week plan, resources, labs, a
      10-question checkpoint with a portfolio artifact, and common mistakes.
- [ ] Phase weeks in the README table add up to 52 and match `roadmap/phases.py`.
- [ ] No document contains attack instructions for real systems or working exploit code.
- [ ] Certification details are either confirmed on the official site with a date, or say "check the
      official site". Recheck the OffSec price recorded in `data/sources.yaml` close to release.
- [ ] The README states that sequencing, estimates, and career guidance are opinions, and invites
      issues.

## Release

- [ ] Update the version in `pyproject.toml` and `roadmap/__init__.py` if it changed.
- [ ] Tag `v0.1.0` and create the GitHub release with a short summary of the phases and checks.
