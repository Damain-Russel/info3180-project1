from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, FileField, SelectField
from wtforms.validators import InputRequired, Length, Regexp, Required

class CreateUserForm(FlaskForm):
	firstname 		= StringField('First Name', validators 		= [ InputRequired()], render_kw = {'placeholder' : 'Last Name'})
	lastname 		= StringField('Last Name', 	validators 		= [ InputRequired()], render_kw = { 'placeholder' : 'Last Name'})
	username 		= StringField('Username', 	validators 		= [ InputRequired(),Length(min = 8, max = 200) ], render_kw = {'placeholder' : 'Username'})
	age 			= IntegerField('Age', 		validators 		= [ InputRequired()], render_kw = {'placeholder' : 'Age'})
	bio 			= TextAreaField('BIO', 		validators 		= [ InputRequired(), Length(max = 200) ], render_kw = {'placeholder' : 'A short bio....', 'rows' : '5'})
	gender 			= SelectField('Gender Type',choices 		= [('1','FEMALE'), ('2','MALE')], default = '2')
	image 			= FileField('Image File', 	validators 		= [ Regexp(u'^[^/\\\\]\.$'), InputRequired() ])
	password 		= PasswordField('Password', validators 		= [ InputRequired() ] , render_kw = {'placeholder' : 'Password'})

class LoginForm(FlaskForm):
	username 		= StringField('Username', 	validators 		= [ InputRequired(),Length(min = 8, max = 200) ], render_kw = {'placeholder' : 'Username'})
	password 		= PasswordField('Password', validators 		= [ InputRequired() ] , render_kw = {'placeholder' : 'Password'})