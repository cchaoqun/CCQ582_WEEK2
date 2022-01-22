import hashlib
import os
import string
import random

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
        for i in range(k):
            if x[-1 - i] != y[-1 - i]:
                break
            if i >= k - 1:
                return (x, y)

    return (b'\x00', b'\x00')


def get_random_bytes(byte):
    let = string.ascii_letters
    x = "".join(random.choice(let) for i in range(byte))
    x = x.encode('utf-8')
    x = hashlib.sha256(x).hexdigest()
    x = bin(int(x, 16))
    return x


