"""The roadmap's phases: one stable definition shared by the CLI and the validator.

Phase IDs are stable. Renaming one would orphan learners' saved progress, so add a
new phase instead of renaming an existing one.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Phase:
    id: str
    number: int
    title: str
    doc: str
    weeks: int


PHASES: tuple[Phase, ...] = (
    Phase("legal-ethics", 0, "Legal and ethics", "docs/00-legal-and-ethics.md", 1),
    Phase("foundations", 1, "Foundations: Linux, networking, Python, Bash", "docs/01-foundations.md", 11),
    Phase("web-security", 2, "Web security", "docs/02-web-security.md", 10),
    Phase("cryptography", 3, "Cryptography basics", "docs/03-cryptography-basics.md", 6),
    Phase("offensive-practice", 4, "Offensive practice and CTFs", "docs/04-offensive-practice-and-ctf.md", 10),
    Phase("defence-malware", 5, "Defence and malware analysis", "docs/05-defence-and-malware-analysis.md", 8),
    Phase("certs-bug-bounty", 6, "Certifications and bug bounty", "docs/06-certs-and-bug-bounty.md", 6),
)

PHASE_IDS: tuple[str, ...] = tuple(p.id for p in PHASES)


def get_phase(phase_id: str) -> Phase | None:
    for phase in PHASES:
        if phase.id == phase_id:
            return phase
    return None
