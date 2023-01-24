import zipfile
# target = 'sample.txt'

# handle = zipfile.ZipFile('doZip.zip','w')
# handle.write(target,compress_type=zipfile.ZIP_DEFLATED)

# handle.close()


extract = zipfile.ZipFile.extract('doZip.zip')


