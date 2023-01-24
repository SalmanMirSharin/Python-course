import zipfile


targer = '../destination/All_file.zip'

handle = zipfile.ZipFile(targer,'r')

handle.extractall('.')

handle.close()