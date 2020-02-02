encrypted_key = input()
decrypted_key = input()
encrypted = input()
decrypted = input()

cipher_direct = dict()
cipher_reversed = dict()

for i in range(len(encrypted_key)):
    cipher_direct[encrypted_key[i]] = decrypted_key[i]
    cipher_reversed[decrypted_key[i]] = encrypted_key[i]

for i in encrypted:
    print(cipher_direct[i], end='')
print()

for i in decrypted:
    print(cipher_reversed[i], end='')
print()
