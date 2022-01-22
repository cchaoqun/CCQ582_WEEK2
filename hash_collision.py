import hashlib
import os


def hash_collision(k):
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')

    # Collision finding code goes here
    # Generate 2 random bytes of 32 bits
    INT_BYTE_LEN = 4

    while(True):
        x = get_random_bytes(INT_BYTE_LEN)
        y = get_random_bytes(INT_BYTE_LEN)
        if get_last_k_bits(INT_BYTE_LEN, x) == get_last_k_bits(INT_BYTE_LEN, y):
            return (x, y)
    return (b'\x00', b'\x00')


def get_random_bytes(byte):
    return os.urandom(byte)

def get_last_k_bits(k, bytes):
    kMask = 2 ** k - 1
    bytes = hashlib.sha256(bytes)
    bits = int(bytes.hexdigest(), 16)
    return (bits & kMask)

