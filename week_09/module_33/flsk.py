#  week 7:

from flask import Flask,request

app = Flask(__name__)
database ={'Mehedi':'100','kona':'141'}
@app.route('/', methods=['GET'])
def home():
    return 'Welcome to my cute web api!'

@app.route('/something', methods=['GET'])
def somthing():
    return 'Somthings page!'

# data read:
@app.route('/getdata',methods=['GET'])
def get_data():
    return database

# data write/create:
@app.route('/adddata',methods=['POST'])
def add_data():
    key,val = list(request.args.items())[0]
    # print(key,val)

    database[key] = val
    return(f'{key} added!')

@app.route('/deletedata',methods=['DELETE'])
def delete_data():
    key,val = list(request.args.items())[0]
    database.pop(val)
    return f'{val} delete'

# if __name__=='__main__':
app.run()

# End:


# week 9:
# from flask import Flask,jsonify,request

# app = Flask(__name__)

# students = [{'id':1,'name':'rahim'},{'id':2,'name':'karim'}]

# @app.route('/')
# def home():
#     return jsonify(students)

# @app.route('/add', methods=['GET','POST'])
# def add():
#     students.append(request.args)
#     return 'student added successfully!'


# @app.route('/update', methods=['GET','PUT'])
# def updated():
#     for student in students:
#         if str(student.get('id')) == request.args.get('id'):
#             student.update(request.args)
#     return 'student update successfully!'

# @app.route('/delete', methods=['GET','DELETE'])
# def delete():
#     for i in range(len(students)):
#         if str(students[i].get('id')==request.args.get('id')):
#             del students[i]
#             break
#     return 'Student deleted successfully!'

# app.run(debug=True)

# a,b = [1,2,3]
# print(a,b)

