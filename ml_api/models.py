from django.db import models

# Create your models here.
TRUE=1
FALSE=0
GENDER = [
	(FALSE,'male'),
	(TRUE,'female'),
]

WEEKEND = [
	(FALSE,'weekday'),
	(TRUE,'weekend'),
]

EDUCATION = [
	('High School or Below','High School or Below'),
	('college','college'),
	('Bechalor','Bechalor'),
	('Master or Above','Master or Above'),
]


class Applicant(models.Model):
	Principal = models.IntegerField()
	terms = models.IntegerField()
	age = models.IntegerField()
	Gender = models.IntegerField(choices=GENDER)
	weekend = models.IntegerField(choices=WEEKEND)
	education = models.CharField(choices=EDUCATION,max_length=100)
