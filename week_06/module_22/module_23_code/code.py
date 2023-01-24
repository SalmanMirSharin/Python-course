import os
import zipfile
import glob
import shutil

source_path = '../source/*'
destinatin_path = '../destination'
server_path = './All_file.zip'
add_postfix = [1,2,3]
# ser = glob.glob(server_path)
# print(ser)
while True:
    source_object = glob.glob(source_path)
    # print(source_object)
    if len(source_object)>0:
        object_path = source_object[0]
        # print(object_path)
        shutil.copy(object_path,'.')
        # print(object_path)
        object_name = object_path.split('\\')[-1].split('.')

        # print(object_name)
        prefix = object_name[0]
        postfix = object_name[1]

        # print(prefix)
        try:
            for item in range(len(add_postfix)):
                file_name = prefix+'_'+str(item+1)+'.'+postfix+' will have '+str((item+1)*10)+ ' lines'
                shutil.copy(object_path,f'./{file_name}')

            handle = zipfile.ZipFile('All_file.zip','w')
            for x in os.listdir():
                if x.endswith('lines'):
                    handle.write(x,compress_type=zipfile.ZIP_DEFLATED)

            # handle.close()

            shutil.move(server_path,destinatin_path)

            targer = '../destination/All_file.zip'

            handle = zipfile.ZipFile(targer,'r')

            handle.extractall('../destination/')

            # handle.close()


            # os.remove(object_path)
            # os.remove(object_path.split('\\')[-1])


            def run(runfile):
                with open(runfile,"r") as rnf:
                    exec(rnf.read())

            for x in os.listdir():
                try:
                    if x.endswith('.py'):
                        run(x)
                except Exception as e:
                    # print(e)
                    print('Opps!')



            os.remove(object_path)
            os.remove(object_path.split('\\')[-1])
            os.remove('./All_file.zip')
            os.remove('../destination/All_file.zip')
            # for z in os.listdir():
            #     if z.endswith('.zip'):
            #         os.remove('../destination/'f'{z}')

            for x in os.listdir():
                if x.endswith('lines'):
                    os.remove(x)

            # for i in os.listdir():
            #     if i.endswith('lines'):
            #         os.remove(i)
        except:
            print('Oh, bad!')