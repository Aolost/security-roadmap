# security-roadmap tasks. Everything except `links` and `lint-md` (first run downloads the
# linter) works offline.
PYTHON ?= python3
MARKDOWNLINT ?= npx --yes markdownlint-cli2@0.24.0

.PHONY: help check validate sources sources-check test stale lint-md links

help:
	@echo "make check          run every pre-merge check (validate, sources-check, test, lint-md)"
	@echo "make validate       validate data/sources.yaml and phase references (offline)"
	@echo "make sources        regenerate SOURCES.md from data/sources.yaml (offline)"
	@echo "make sources-check  fail if SOURCES.md is out of date (offline)"
	@echo "make test           run the unit tests (offline)"
	@echo "make stale          list sources not verified in the last 12 months (offline)"
	@echo "make lint-md        lint Markdown with markdownlint-cli2 (needs Node.js)"
	@echo "make links          check every source URL over the network (writes link-report.md)"

check: validate sources-check test lint-md

validate:
	$(PYTHON) scripts/validate_sources.py

sources:
	$(PYTHON) scripts/generate_sources.py

sources-check:
	$(PYTHON) scripts/generate_sources.py --check

test:
	$(PYTHON) -m unittest discover -s tests -t . -v

stale:
	$(PYTHON) scripts/report_stale_sources.py

lint-md:
	$(MARKDOWNLINT)

links:
	$(PYTHON) scripts/check_links.py --output link-report.md
