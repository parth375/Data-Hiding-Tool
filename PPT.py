print("                                                                 DATA HIDING TOOL (STEGANOGRAPHY)")
print()

print("We suggest you to first see how to use the tool and what steps to follow.")
help = int(input("To go to help press 1 or to skip press 2:- "))
if(help == 1):
    print("When you select option to embed, tool will first create a zip file of you secret file inside you computer.")
    print("So for after the embedding process gets completed. It is advised that you delete both the original secret file and the zip file that is created"
          "by the tool for ensuring complete safety.")
    print("But you should always have the image in which the data is hidden. ")
    print("At the time extracting data provide that image file name with extension.")
else:
    embedd_or_extract = input("Press (e) for embed(e) and (d) for extract(d):- ")

    if (embedd_or_extract == 'e'):

        email = input("Enter your email:-  ")
        file = open("email.txt")
        with open("email.txt",'r') as fr:
            if(email in file.read()):
                print("Email already exits!!!")
            else:
                with open("email.txt", 'a') as f:
                    f.write('\n')
                    f.write(email)

        import f_encrypt as fe
        from f_encrypt import *
        import menusteg as ms           # These are the modules/files that are used for embedding the file inside an image
        from menusteg import *
    elif (embedd_or_extract == 'd'):
        import new_email_file as nef
        from new_email_file import *

        # auth = input("Enter your email for Authentication:-  ")
        # filename = open("email.txt")

        # if(auth in filename.read()):
        #     import send_email as se
        #     from send_email import *
        #
        #     # import HIDE_IMG_YT as yt  # These are the modules/files that are used for extracting file from the image
        #     # from HIDE_IMG_YT import *
        #     #
        #     # import unzip_file as uf
        #     # from unzip_file import *
        #     #
        #     # import f_decrypt as fd
        #     # from f_decrypt import *
        # else:
        #     print("Email not Found!!!")





