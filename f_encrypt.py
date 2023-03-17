from cryptography.fernet import Fernet

print("For encrypting the file you need to put that file into a particular folder so that it would be easy to find.")
file_name = input("Enter the name of the file.")

key = Fernet.generate_key()                                              #Fernet.generate_key()

fkey = open(file_name + "_key.zip", "wb")
fkey.write(key)

fkey = open(file_name + "_key.zip", "rb")
key = fkey.read()
cipher = Fernet(key)
# print(key)

filename = file_name

try:
    with open(filename,"rb") as f:
        e_file = f.read()

    encrypted_file = cipher.encrypt(e_file)

    with open(filename + "encrypted","wb") as ef:
        ef.write(encrypted_file)

except FileNotFoundError as fnfe:
    print(fnfe)
