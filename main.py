import string
import secrets


def secure_password(length=16, include_uppercase=True, include_numbers= True, include_symbols=True ):
    
    chars = string.ascii_lowercase

    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    password = "".join(secrets.choice(chars) for _ in range (length))

    while True:
        conditions = []
        conditions.append(any(c.lower() for c in password ))

        if include_uppercase:
            conditions.append(any(c.isupper() for c in password ))
        if include_numbers:
            conditions.append(any(c.isdigit() for c in password ))
        if include_symbols:
            conditions.append(any(c in string.punctuation for c in password ))

        if all(conditions):
            break
        password = "".join(secrets.choice(chars) for _ in range (length))
    
    return password

if __name__ == "_main_":
    print(f'Password Examples: ')
    print(f'Default Password (16): {secure_password()}')
    print(f'Easy Password (12, non-numbers): {secure_password(length=8, include_numbers=False)}')
    print(f'Symbols and Letters: {secure_password(length=24, include_numbers=False)}')