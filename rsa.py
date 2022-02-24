# RSA

from math import gcd


def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = []
    for i in message:
        c = (ord(i) ** e) % n
        encrypted_message.append(c)
    return encrypted_message


def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''
    a = 0
    for i in range(0, len(encrypted_message)):
        a = ((encrypted_message[i] ** d) % n)
        decrypted_message += chr(a)
    return decrypted_message


def key_gen():
    p = 17
    q = 11
    n = p * q
    e = 2
    f_n = (p - 1) * (q - 1)

    while e < f_n:
        if gcd(e, f_n) == 1:
            break
        else:
            e = e + 1

    k = 2
    d = (1 + (k * f_n)) // e
    private_key = (d, n)
    public_key = (e, n)

    return private_key, public_key

