"""
Base85 encoder and decoder
"""

from __future__ import annotations
from beartype import beartype

ALPHABET = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
alphabet_map = {c: i for i, c in enumerate(ALPHABET)}


@beartype
def encode(b: bytes):
    """
    Base85 encoder
    """

    res = b""
    blocks = [b[i:i + 4] for i in range(0, len(b), 4)]

    for block in blocks:
        original_len = len(block)
        block = block.ljust(4, b"\0")

        n = int.from_bytes(block, "big")

        chars = []

        for _ in range(5):
            chars.append(ALPHABET[n % 85])
            n //= 85

        chars.reverse()
        res += bytes(chars[:original_len + 1])

    return res


@beartype
def decode(b: bytes):
    """
    Base85 decoder
    """

    res = b""
    blocks = [b[i:i + 5] for i in range(0, len(b), 5)]

    for block in blocks:
        original_len = len(block)
        block = block.ljust(5, ALPHABET[-1:])

        n = 0

        for c in block:
            n = n * 85 + alphabet_map[c]

        decoded = n.to_bytes(4, "big")
        res += decoded[:original_len - 1]

    return res
