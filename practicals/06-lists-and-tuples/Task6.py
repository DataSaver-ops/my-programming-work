

import random
import string


def random_interval_encrypt(message):
    interval = random.randint(2, 20)
    encrypted_message = []
    message_index = 0

    while message_index < len(message):
        for _ in range(interval):
            if message_index < len(message):
                encrypted_message.append(random.choice(string.ascii_lowercase))
            else:
                encrypted_message.append(random.choice(string.ascii_lowercase))
        if message_index < len(message):
            encrypted_message[-1] = message[message_index]
            message_index += 1

    return ''.join(encrypted_message), interval


def decrypt_message(encrypted_message, interval):
    return ''.join([encrypted_message[i] for i in range(interval - 1, len(encrypted_message), interval)])



message = "send cheese"
encrypted_message, interval = random_interval_encrypt(message)
print("Encrypted message:", encrypted_message)
print("Interval used:", interval)


decrypted_message = decrypt_message(encrypted_message, interval)
print("Decrypted message:", decrypted_message)
