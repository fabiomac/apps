#--* coding: utf-8 *--#
from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_pymongo import PyMongo
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'dblogin' 
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dblogin'

mongo = PyMongo(app)

@app.route('/')
def index():
	if 'username' in session:
		return 'You are logged as ' + session['username']
		
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password_candidate = request.form['password']

		# Fazer a conexao com o MongoDB e um find do username/password
		result = 0

		# Logica do sistema de login
		if result > 0:
			flash('User logged!!!', 'success')
		else:
			error = 'Invalid login!!!'
			return render_template('login.html', error=error)

	return render_template('login.html')


class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=50)])
	username = StringField('Username', [validators.Length(min=4, max=30)])
	password = PasswordField('Password',[
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords do not match')
	])
	confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data 
		username = form.username.data
		password = sha256_crypt.encrypt(str(form.password.data))
		flash('You are now registered an can login!!!', 'success')
		return redirect(url_for('login'))

	return render_template('register.html', form=form)


if __name__ == '__main__':
	app.secret_key = 'loginsecret'
	app.run(debug=True)