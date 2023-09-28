def encrypt(plain_text, key):
    cipher_text = []
    for i in range (len(read_file(plain_text))):
        cipher_text.append(key[read_file(plain_text)[i]])
    return cipher_text
def decrypt(cipher_text, key):
    plain_text = []
    for i in range (len(read_file(cipher_text))):
        plain_text.append(key.index(read_file(cipher_text)[i]))
    return plain_text
def read_file(file_name):
    file = open(file_name,"rb")
    number = list(file.read())
    return (number)
    file.close()

def write_file(file_name, content):
    file = open(file_name, "wb")
    print(content)
    file.write(bytes(content))
    file.close()
def test_encryption():
    read_file("key")
    cipher_text = encrypt("plain_text", read_file("key"))
    write_file("cipher_text", cipher_text)
    plain_text = decrypt("cipher_text",read_file("key"))
    write_file("plain_text1", plain_text)

if __name__ == '__main__':
    test_encryption()


