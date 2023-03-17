# Data-Hiding-Tool
Data Hiding
In this mode, you can either hide the data (file) inside an image or extract the data from the image. 
THE ALGORITHM
Encrypting and Embedding Process
a) After the user selects encrypts as an option, we ask them to provide the email so that we can 
verify the user's authenticity at the time of the extraction process.
b) Then we ask for the file that the user wants to hide. 
c) After getting the file from the user we start our encryption process. We first encrypt the 
provided file.
d) Then we ask for a cover image from the user in which we will be hiding that file.
e) After that, we hide the file behind the image and provide the final image to the user which 
they need to keep with them for further use and extraction of data from it.
f) After getting the final stego image, the user can delete all the instances of that data which are 
hidden inside our stego image.
Decryption and Extraction Process
a) Now as we are done with the encryption or embedding process, we can now look at the 
process of extracting.
b) When the user selects the decryption option, the first step that occurs is email verification
c) After validating the user through email verification, we can move to our extraction process
d) For extraction, we first send a secret key to the user's authentic email address.
e) After getting the key from the user we extract the data which is hidden behind the image.
f) Then we perform a decryption process to get the original data from the image for use

![image](https://user-images.githubusercontent.com/88189173/225986294-f975590d-a5d0-4cf2-9571-057bb2d9a535.png)

So, firstly, the user will be authenticated using their email id. After this, they must provide the 
data in zip file format to the tool they want to secure.
2. After this, it will first encrypt the data using the cryptography module of python then it will 
hide that encrypted data inside an image by using steganography (specifically image 
steganography). 
3. Now, if a user wants to get back their data, they must prove their legitimacy by entering the 
same email id they entered at the time of embedding. 
4. If it matches the tool will share a unique key to that email id and if the user enters the same 
key only then they can get back their original data.
