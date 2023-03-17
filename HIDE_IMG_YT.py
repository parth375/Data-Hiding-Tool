# This program is for hiding image inside image

# import PIL.Image
# import io

# img = PIL.Image.open('ARM.jpg')
# byte_arr_ = io.BytesIO()
# img.save(byte_arr_,format = 'PNG')
#
# with open('arm1.jpg','ab') as f:
#     f.write(byte_arr_.getvalue())

# with open('arm1.jpg','rb') as f:
#     content = f.read()
#     offset = content.index(bytes.fromhex('FFD9'))
#
#     f.seek(offset + 2)
#
#     new_img = PIL.Image.open(io.BytesIO(f.read()))
#     new_img.save("new_image.png")


# This is for embedding file inside image
# with open('image1.jpeg','ab') as f, open('againsecret.wmv','rb') as e:
#     f.write(e.read())


# This is for extracting file from the image
# with open('secrethaibhai.jpg','rb') as f:
#     content = f.read()
#     offset = content.index(bytes.fromhex('FFD9'))
#
#     f.seek(offset + 2)
#
#     with open('newfile2.zip','wb') as e:
#         e.write(f.read());


cover_img = input("Enter the image name where file is hidden:-  ")
with open(cover_img,'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)

    with open('newfile.zip','wb') as e:
        e.write(f.read())



