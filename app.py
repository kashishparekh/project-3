from flask import Flask,request

app = Flask(__name__)

a=10
b=20

@app.route('/',methods=['GET'])#end point(path,http method)
def welcome():
    return "hello world"

@app.route('/login',methods=['GET'])
def login():
    return 'you are in login page'

@app.route('/register',methods=['GET'])
def register():
    return "you are in register page"

@app.route('/home_page',methods=['get'])
def home_page():
    return 'you are in home page'

@app.route('/last_page',methods=['get'])
def last_page():
    return 'you are in last page'


@app.route('/add',methods=['get'])#when we declare the values before execution
def addition():
    return f"addition of {a} and {b} is {a+b}"

@app.route('/sub',methods=['get'])
def substraction():
    return f"substraction of {a} and {b} is {b-a}"

@app.route('/mul',methods=['get'])
def multiplication():
    return f"multiplication of {a} and {b} is {a*b}"

@app.route('/div',methods=['get'])
def division():
    return f"division of {a} and {b} is {a/b}"


#declaring during execution

@app.route('/add/<a>/<b>',methods=['get'])#path parameters
def additions(a,b):
    a=int(a)
    b=int(b)
    return f"addition of {a} and {b} is {a+b}"

@app.route('/sub/<a>/<b>',methods=['get'])#path parameters
def sub(a,b):
    a=int(a)
    b=int(b)
    return f"addition of {a} and {b} is {a-b}"

@app.route('/mul/<a>/<b>',methods=['get'])#path parameters
def mul(a,b):
    a=int(a)
    b=int(b)
    return f"addition of {a} and {b} is {a*b}"

@app.route('/div/<a>/<b>',methods=['get'])#path parameters
def div(a,b):
    a=int(a)
    b=int(b)
    return f"addition of {a} and {b} is {a/b}"


app.run()