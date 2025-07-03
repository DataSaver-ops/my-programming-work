def simple_encrypt(message):
    return message.replace(" ", "")[::-1]


print(simple_encrypt("Hi ANAS"))
