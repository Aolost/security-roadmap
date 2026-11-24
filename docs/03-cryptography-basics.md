# Phase 3: Cryptography basics

Phase ID: `cryptography` · Planned time: weeks 23–28 (6 weeks at about 8–10 hours a week)

## Goal

Understand what the main cryptographic building blocks guarantee, recognize common ways they are
misused, and know when to rely on well-reviewed libraries instead of building your own.

## Prerequisites

- Phase 1 complete, especially Python.
- Comfort with basic algebra. Some optional resources assume discrete mathematics.

## Week-by-week plan

| Week | Focus | Outcome |
| --- | --- | --- |
| 23 | Encoding vs encryption vs hashing; XOR; randomness | You can tell the three apart in real data |
| 24 | Symmetric ciphers, block cipher modes, and why ECB leaks patterns | Cryptopals set 1 progress |
| 25 | Hashes, MACs, and password storage | You can explain salts and slow hashes |
| 26 | Public-key cryptography, key exchange, and digital signatures | You can explain what TLS protects |
| 27 | Common misuse: nonce reuse, padding oracles, weak randomness (concepts, in Cryptopals) | Notes on how each is prevented |
| 28 | Checkpoint and portfolio artifact | Checkpoint answered; artifact published |

## Resources

Core:

- [src:crypto101](../SOURCES.md#crypto101): readable introduction.
- [src:cryptopals](../SOURCES.md#cryptopals): hands-on challenges on your own machine.
- [src:owasp-password-storage-cheatsheet](../SOURCES.md#owasp-password-storage-cheatsheet)
- [src:cyberchef](../SOURCES.md#cyberchef): explore encodings and transformations.

Going deeper (optional, pick one):

- [src:serious-cryptography-2e](../SOURCES.md#serious-cryptography-2e): practical book (paid).
- [src:coursera-cryptography-1](../SOURCES.md#coursera-cryptography-1): university course.
- [src:boneh-shoup-applied-crypto](../SOURCES.md#boneh-shoup-applied-crypto): rigorous textbook.

## Hands-on labs

| Lab | Learning goal | Where to find it |
| --- | --- | --- |
| Cryptopals sets 1–2 | Implement and break toy constructions to see why modes, padding, and randomness matter | Cryptopals, sets 1 and 2, solved locally in Python |
| Encoding exploration | Recognize Base64, hex, and URL encoding and see why they are not encryption | CyberChef in your browser, with sample data you create |
| Password storage review | Compare fast hashes with password-hashing functions | A local Python script using a well-known password-hashing library |
| Crypto challenges in CTF practice | Apply concepts in short puzzles | picoCTF (now CyLab Security Academy), cryptography category |

## Checkpoint

1. What is the difference between encoding, encryption, and hashing?
2. Why does ECB mode reveal patterns in the plaintext?
3. What problem does a MAC solve that encryption alone does not?
4. Why should passwords be stored with a slow, salted password-hashing function?
5. What is a nonce, and what can happen if one is reused?
6. What does a digital signature prove, and what does it not prove?
7. How does a key exchange let two parties agree on a secret over an open network?
8. Why is "roll your own crypto" discouraged?
9. What does TLS protect, and what does it not protect?
10. Why does the quality of random number generation matter for keys?

**Portfolio artifact:** a learning write-up explaining one Cryptopals concept (for example, why ECB
leaks structure) with diagrams and your own explanation, plus a small defensive helper such as a
script that flags weak password-hash formats in a sample configuration file you created. Do not
publish full Cryptopals solutions.

## Common mistakes

- Treating Base64 as encryption.
- Using a general-purpose hash such as SHA-256 alone for password storage.
- Implementing primitives yourself for real use instead of using vetted libraries.
- Getting stuck on the mathematics. Understand the guarantees first, then go deeper if you want.
- Skipping this phase. Many web and protocol bugs are really cryptography misuse.
