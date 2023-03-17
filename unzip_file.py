from zipfile import ZipFile

z = ZipFile('newfile.zip', 'r')
z.extractall()
z.close()