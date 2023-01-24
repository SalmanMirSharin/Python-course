import glob
import shutil
import os

source_path = '../source/*'
destination_path = '../destination'
postfix = [1,2,3]

while True:
    source_object = glob.glob(source_path)
    if len(source_object)>0:
        object_path = source_object[0]
        # print(object_path)
        shutil.copy(object_path,'.')

        object_name = object_path.split('\\')[-1].split('.')
        prifix = object_name[0]
        postfix2 = object_name[1]
        # print(object_name)

        for item in range(len(postfix)):
            file_name = prifix+'_'+ str(item+1)+'.' +postfix2

            # print(file_name)
            shutil.copy(object_path,f'{destination_path}/{file_name}')

        os.remove(object_path)
        os.remove(object_path.split('\\')[-1])