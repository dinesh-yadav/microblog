from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Dinesh'}
	#1 return render_template('index.html',title='Home',user=user)
	#2 return render_template('index.html',user=user)
	posts = [
	    {
		'author':{'username': 'Tom'},
		'body': 'Beautiful day in Portland!'
	    },
	    {
		'author':{'username': 'Mike'},
		'body': 'Avengers movie is cool!!'
	    }
	]
	return render_template('index.html',title='Home',user=user,posts=posts)
