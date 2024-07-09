import gnupg

gpg = gnupg.GPG()

path = '/Users/19049/Videos/Nishith'
filename = '/sample.txt'

with open(path + filename, 'rb') as f:
        status = gpg.encrypt_file(f, ['Nishithgupta@gmail.com'], output= path + filename + ".encrypted")

print(status.ok)