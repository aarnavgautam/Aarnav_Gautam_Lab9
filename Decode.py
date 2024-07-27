def decode(password):
    original_password = ''
    for i in password:
        original_password += str((int(i) - 3) % 10)
    return original_password