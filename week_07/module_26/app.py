from flask import Flask

apps = Flask(__name__)

@apps.route('/',methods=['GET'])
def home():
        return('This is home page!')

@apps.route('/something',methods=['GET'])
def somthing():
    return 'we are in somthing page!'


if __name__=='__main__':
    apps.run()

