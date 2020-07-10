# import Flask class
from flask import Flask

#create an instance of this class
# __name__ is application's module or package name
app = Flask(__name__)

# route() decorator to tell Flask what URL 
# should trigger our function
@app.route('/')
def hello_world():
	return 'Hello World'
