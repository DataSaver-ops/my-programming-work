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



encrypted_message, interval = random_interval_encrypt("send cheese")
print(encrypted_message, interval)
