import rsa


def main():

    private_key, public_key = rsa.key_gen()
    print("private key ", private_key)
    print("public key", public_key)

    message = input("Enter the message: ")
    encrypted_message = rsa.encrypt(message, public_key)
    print('Encoded message: ', encrypted_message)

    decrypted_message = rsa.decrypt(encrypted_message, private_key)
    print('Decoded message: ', decrypted_message)


if __name__ == "__main__":
    main()

