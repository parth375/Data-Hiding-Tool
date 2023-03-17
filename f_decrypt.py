from cryptography.fernet import Fernet

file_name_for_decryption = input("Enter the name of the file for decryption:-  ")

fkey = open(file_name_for_decryption + "_key.zip", "rb")
key = fkey.read()
cipher = Fernet(key)

with open(file_name_for_decryption + "encrypted", "rb") as df:
    encrypted_data = df.read()

decrypted_file = cipher.decrypt(encrypted_data)

with open(file_name_for_decryption + " decrypted.zip", "wb")as df:
    df.write(decrypted_file)