import gnupg

gpg = gnupg.GPG()

encrypted_data = gpg.encrypt("Nishith", "Nishithgupta@gmail.com")
# print(encrypted_data)

decrypted_data = gpg.decrypt(encrypted_data.data, passphrase='your_passphrase')
print(decrypted_data)
