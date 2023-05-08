"""Implement a simple shift cipher like Caesar and a more secure substitution cipher."""

from random import choice
from string import ascii_lowercase
from itertools import cycle

az_twice_up_idxs = {k: v for k, v in enumerate(2 * ascii_lowercase, ord("a"))}
az_twice_down_idxs = {k: v for k, v in enumerate(
    2 * ascii_lowercase, ord("a") - (ord("z") - ord("a") + 1))}


def key_len_equalizer(key: str, text: str) -> str:
    """Ajust key length in order to be equal to the text length."""
    if len(key) < len(text):
        # then we have to add cycle repeated key characters to key itself, until len(key) == len(text)
        cycle_key = cycle(key)
        ajusted_key = "".join(next(cycle_key) for _ in range(len(text)))
    elif len(key) > len(text):
        # then we just have to slice the key
        ajusted_key = key[:len(text)]
    else:
        ajusted_key = key
    return ajusted_key


class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = "".join([choice(ascii_lowercase) for n in range(100)])
        self.key = key

    def encode(self, text: str) -> str:
        """Return a cipher according to an input text"""
        encode_key = key_len_equalizer(self.key, text)
        text_idx = [ord(char) for char in text]
        key_idx = [ord(char) - ord("a") for char in encode_key]
        compared_indexes = [(t_idx + k_idx)
                            for t_idx, k_idx in zip(text_idx, key_idx)]
        return "".join(az_twice_up_idxs[idx] for idx in compared_indexes)

    def decode(self, text: str) -> str:
        """Decode a cipher to the original text"""
        decode_key = key_len_equalizer(self.key, text)
        text_idx = [ord(char) for char in text]
        key_idx = [ord(char) - ord("a") for char in decode_key]
        compared_indexes = [(t_idx - k_idx)
                            for t_idx, k_idx in zip(text_idx, key_idx)]
        return "".join(az_twice_down_idxs[idx] for idx in compared_indexes)
