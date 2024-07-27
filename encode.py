def encode(password):
    new_password = ''
    for i in password:
        new_password += str((int(i) + 3) % 10)
    return new_password
