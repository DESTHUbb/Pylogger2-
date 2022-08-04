from cryptography.fernet import Fernet
nes(5 sloc)  137 Bytes


key = Fernet.generate_key()
file = open("encryption_key.txt", 'wb')
file.write(key)
file.close()
