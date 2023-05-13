def xorCipher(text: str, key: int) -> str:
    """Encrypts/decrypts with the XOR cipher"""
    if key > 2**8 - 1:
        raise ValueError("Key can not be greater than 255.")

    return "".join(chr(ord(c) ^ key) for c in text)