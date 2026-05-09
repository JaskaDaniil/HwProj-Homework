"""
Unit tests for 02.Base85
"""



import base85ed
import os
import base64


def test_shorts_encode():
    """
    Test trivial short encodes
    """
    assert base85ed.encode(b"1") == b"F#"
    assert base85ed.encode(b"12") == b"F){"
    assert base85ed.encode(b"123") == b"F)}j"
    assert base85ed.encode(b"1234") == b"F)}kW"


def test_shorts_decode():
    """
    Test trivial short decodes
    """
    assert base85ed.decode(b"F#") == b"1"
    assert base85ed.decode(b"F){") == b"12"
    assert base85ed.decode(b"F)}j") == b"123"
    assert base85ed.decode(b"F)}kW") == b"1234"


def test_long_strings():
    """
    Test longer strings of different lengths
    """
    tests = [
        b"Hello world!",
        b"aaaaaaaaaaaaaaaaaaaa",
        b"Hi, my name is, what? My name is, who? My name is, chka-chka, Slim Shady.",
        b"1234567890" * 15,
        bytes(range(256)),
    ]

    for test in tests:
        encoded = base85ed.encode(test)
        decoded = base85ed.decode(encoded)

        assert encoded == base64.b85encode(test)
        assert base85ed.decode(base64.b85encode(test)) == test


def test_all_lengths():
    """
    Test all short lengths for padding correctness
    """
    for n in range(100):
        test = b"a" * n

        assert base85ed.decode(base85ed.encode(test)) == test
        assert base85ed.encode(test) == base64.b85encode(test)


def test_random_bytes():
    """
    Test random byte strings
    """
    for n in range(1, 200):
        test = os.urandom(n)

        assert base85ed.encode(test) == base64.b85encode(test)
        assert base85ed.decode(base64.b85encode(test)) == test
