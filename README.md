## info3180-Project1
INFO3180-Project1 provides simple user profile management. It handles the common of creating a profile,
viewing profiles and api call to return JSON data.

INFO3180-Project1 bound to any particular database system or permissions
model. However for the application to work, the user must create a database called ```Project1Database```

## Start up
You may run the following to get the table in the database
```sh
## Creating the Table 
$ python flaskmigrate.py db init
$ python ##To open the python console (if using the command line)
$ from app import db
$ db.create_all()
## At the end of these commands, you will be able to store and grab data from the database
```

## Basic Setup
```python 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:PostgreSQL@localhost/Project1Database'
app.debug = True ##for debugging purposes. This is optional
app.secret_key = os.urandom(24) ##best way to create a secret key is to generate a random one
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True ##also optional when deploying

```

## Usage

Once that is completed, the application is easy to use. Lets walk through how the 
table in the database is strucured

```python
from . import db
from time import time
from datetime import date
from flask import json, jsonify
class UserProfile(db.Model):
	__tablename__ = "UserProfileInfo"
	id = db.Column(db.Integer, primary_key=True)
	first_name 		= db.Column(db.String(80))
	last_name 		= db.Column(db.String(80))
	username 		= db.Column(db.String(80), unique=True)
	password		= db.Column(db.String(80))
	gender			= db.Column(db.String(10))
	age				= db.Column(db.Integer)
	profile_photo 	= db.Column(db.String(80))
	date_created 	= db.Column(db.String(30))
	bio 			= db.Column(db.String(250))

	def __init__(self, first_name, last_name, username, password, age, gender, profile_photo, bio):
		self.id		 		= UserProfile.get_new_id()
		self.first_name 	= first_name
		self.last_name 		= last_name
		self.username 		= username
		self.password 		= password
		self.age			= age
		self.gender 		= gender
		self.profile_photo  = profile_photo
		self.date_created 	= UserProfile.timeinfo()
		self.bio 			= bio

```
Above shows how the UserProfileInfo table is structured in the database and also the
constructor for a user. A few static methods were created in the class to help with
creating the user.



## Credits
The `HTML` rendering was taken from my lecturer with a little modification of my own. 


## Contributing

Contributions to this project is not welcome because it is for a school assignment. Users may however

1. Fork this repository
2. Make your changes
3. Install the requirements in `requirements.txt`
4. Have fun
