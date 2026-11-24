# Contributing

Thank you for helping keep this roadmap accurate. Corrections, broken-link reports, and resource
suggestions are all welcome.

## Start with an issue

Open an issue for anything beyond a typo fix. Useful issues include:

- **Broken or redirected link:** the resource ID and what you saw when you opened it.
- **Factual correction:** what is wrong, and an official source that shows the correct detail.
- **Suggested resource:** the URL, the phase it fits, and one sentence on why it helps learners.
- **Disagreement with an opinion:** sequencing, time estimates, and career guidance are editorial
  opinions. Explain what you would change and why.

## Ground rules

- **No attacks on real systems.** Do not add instructions for attacking systems you are not authorized
  to test, and do not add working exploit code. Hands-on work must use only these legal platforms or
  local VMs: OverTheWire, TryHackMe, PortSwigger Web Security Academy, Hack The Box, picoCTF,
  Hacker101, Cryptopals, DVWA, and OWASP Juice Shop.
- **Never imply that permission transfers.** Permission for one platform or program does not apply to
  any other.
- **Fewer, verified resources beat many guessed ones.** Do not add a resource just to fill a phase.

## Adding or updating a resource

`data/sources.yaml` is the single source of truth. **Never edit `SOURCES.md` by hand.**

1. **Open the URL yourself** before adding it. Record what you actually observe:
   - `url`: the URL you requested.
   - `final_url`: where you ended up after any redirects.
   - `http_status`: the status of the first response to `url`. A redirect is a 3xx value, never 200.
   - `final_http_status`: the status of the final response.
   - `page_title`: the page's title exactly as shown.
   - `verified_on`: the date you checked (`YYYY-MM-DD`).
   - `verified_with`: how you checked (for example, a browser, or `curl -L`).

   Example of observing these with curl:

   ```bash
   curl -sSL -o /dev/null -D - -w '%{url_effective} %{http_code}\n' https://example.org/
   ```

2. **Use `unknown`** for anything you could not verify. Never fill in a status, title, author, or
   price from memory. If you cannot confirm what the resource is or where it leads, do not add it.
3. **Books:** add `book.authors` and `book.edition` only when confirmed on a publisher, author, or
   library page you opened, and record that page in `book.details_source`. Do not add ISBNs or prices
   from memory.
4. **Certifications:** add prerequisites, price, and exam format only when confirmed on the official
   site, with `certification.checked_on`. Otherwise write "check the official site".
5. **Write `why_included`** as at least one full sentence about why the resource helps learners.
6. **Choose a stable ID** in lowercase kebab-case. Do not rename existing IDs.
7. **Reference it** from at least one phase document as `[src:your-id](../SOURCES.md#your-id)`.
   The validator fails on unreferenced (orphaned) sources and on references to unknown IDs.
8. Regenerate and check:

   ```bash
   make sources
   ```

   ```bash
   make check
   ```

## Rechecking stale resources

`make stale` lists resources whose `verified_on` is more than 12 months old. **Do not update
`verified_on` without actually reopening the resource**, and update the other observed fields to
match what you see. If a resource is gone or has changed into something else, remove it or replace it
and update the phase documents.

The weekly scheduled workflow opens or updates one tracking issue for dead, moved, redirected, or
stale sources. It never edits the data itself.

## Pull requests

- Keep each pull request small and focused.
- Run `make check` before opening it. CI runs Markdown lint, the offline validator, the tests, and a
  link check.
- Explain what you verified and when.
