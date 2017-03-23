from . import db
from time import time
from datetime import date
from flask import json, jsonify
class UserProfile(db.Model):
	__tablename__ = 'UserProfileInfo'
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
	
	@staticmethod
	def get_new_id():
		new_id = long(time())
		return new_id
	
	@staticmethod
	def timeinfo():
		"""Forats the date and time"""
		d = date.today();
		return "{0:%A}, {0:%B} {0:%d}, {0:%y}".format(d)
	
	def __repr__(self):
		return '<User %r>' % (self.username)

	def get_image_url(self):
		return '/uploads/{0}'.format(self.image)
	
	def all_json(self):
		return jsonify(username = self.username, userid = self.id)