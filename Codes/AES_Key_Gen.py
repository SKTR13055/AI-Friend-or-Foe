import os

def generate_aes_key_iv(key_size=256):
    if key_size not in (128, 192, 256):
        raise ValueError("Key size must be 128, 192, or 256")

    key_bytes = key_size // 8
    key = os.urandom(key_bytes)
    iv = os.urandom(16)

    return key, iv


if __name__ == "__main__":
    key, iv = generate_aes_key_iv(256)

    print("AES-256 Key (Hex):")
    print(key.hex())

    print("\nIV (Hex):")
    print(iv.hex())