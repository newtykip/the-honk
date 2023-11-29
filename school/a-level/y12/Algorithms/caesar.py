# def encode(text: str, key: int) -> str:
#     return ''.join(chr(ord(c) + (key % 26)) for c in text)

# def decode(ciphertext: str, key: int) -> str:
#     return ''.join(chr(ord(c) - (key % 26)) for c in ciphertext)

c,o,e,d=chr,ord,lambda t,k:''.join(c(o(x)+k%26)for x in t),lambda t,k:''.join(c(o(x)-k%26)for x in t)

print(e("cats", 6))
