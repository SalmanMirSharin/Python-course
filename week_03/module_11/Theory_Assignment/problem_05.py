
import uuid
id = str(uuid.uuid4())[0:7]

name = input('Enter name: ')
mark = input('Enter Mark: ')

with open('student_list.txt','a') as file:
    file.write(f'Student_id: {id} - Name: {name} - Mark: {mark} \n')


