import os
import zipfile

# for x in os.listdir():
#     if x.endswith('.zip'):
#         print(x)

handle = zipfile.ZipFile('All_file.zip','w')

for x in os.listdir():
    if x.endswith('.txt'):
        handle.write(x,compress_type=zipfile.ZIP_DEFLATED)

handle.close()