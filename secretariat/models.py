from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.utils import timezone

STATUS_CHOICES = (
    ('t', 'Training'),
    ('v', 'Company Visit'),
    ('e', 'Exhibition'),
)

MEMBER_CHOICES = (
	('10', 'Member'),
	('1', 'Non-Member'),
)



# Create your models here.
class Event(models.Model):
	chapter = models.ForeignKey('Chapter',  on_delete=models.CASCADE)
	sector = models.ForeignKey('Sector', on_delete=models.CASCADE, null=True, blank=True)
	trainer = models.ForeignKey('Trainer', null=True, on_delete=models.CASCADE, blank=True)
	name = models.CharField(max_length = 200)
	venue = models.CharField(max_length=400)
	start_date = models.DateField('Start Date')
	end_date = models.DateField('End Date')
	description = models.TextField()
	status = models.CharField(max_length=1, null=True, choices=STATUS_CHOICES, verbose_name='Event Type', default="t")
	participants = models.ManyToManyField('Member', blank=True, related_name='participants')
	#created_by = models.ForeignKey(User, editable=False)
	added_by = models.ForeignKey('Member', default=729, related_name='added_by')

	def __str__(self):
		return self.name

	def count_events(self):
		return str(name.count())




class Chapter(models.Model):
	name = models.CharField(max_length = 200)
	postal_address = models.CharField(max_length = 600, null=True, blank=True)
	physical_address = models.TextField(max_length=600, null=True, blank=True)
	phone = models.CharField(max_length=50)
	email = models.EmailField(null=True, blank=True)
	established = models.IntegerField()
	account_name = models.CharField(max_length=200, null=True, blank=True)
	avatar = models.CharField(max_length=200, null=True, blank=True)
	bank = models.CharField(max_length=200, null=True, blank=True)
	branch = models.CharField(max_length = 400, null=True, blank=True)
	account_no = models.CharField(max_length=200, null=True, blank=True)
	forex_rate = models.IntegerField()
	mm_number = models.CharField(max_length=50, verbose_name='Mobile Money Number', null=True, blank=True)
	cordinator = models.ForeignKey('Staff',null=True, on_delete=models.CASCADE)

	def __str__(self):	
		return self.name 


class Sector(models.Model):
	sector_name = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.sector_name


class SectorDesk(models.Model):
	name = models.CharField(max_length=100)
	avatar = models.CharField(max_length=100)
	created_at = models.DateTimeField()

	def __str__(self):
		return self.name


class Staff(models.Model):
	fullname = models.CharField(max_length=200)
	mobile = models.CharField(max_length=30)
	dob=models.DateField(null=True)
	country_chapter = models.ForeignKey('Chapter', null=True, blank=True, on_delete=models.CASCADE)
	position = models.CharField(max_length=300)

	def __str__(self):
		return self.fullname

	class Meta:
		verbose_name = u'Staff'
		verbose_name_plural=u'Staff'



class Staffactivity(models.Model):
	staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
	activity_date = models.DateField()
	activity_end = models.DateField()
	activity = models.TextField()
	location = models.CharField(max_length=400)
	country = models.ForeignKey('Chapter', on_delete=models.CASCADE)
	created_by = models.ForeignKey(User, editable=False)


	class Meta:
		verbose_name = u'Staff Activities'
		verbose_name_plural=u'Staff Activities'


class Trainer(models.Model):
	fullname = models.CharField(max_length=200)
	phone = models.CharField(max_length=30)
	email = models.EmailField()
	speciality = models.CharField(max_length=400)
	chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, verbose_name='Country')


	def __str__(self):
		return self.fullname

class BusinessClub(models.Model):
	club_name = models.CharField(max_length=200)
	country = models.ForeignKey('Chapter', on_delete=models.CASCADE)
	established = models.IntegerField()
	leader = models.ForeignKey('Member', null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.club_name


class Member(models.Model):
#	NO = False
#	YES = True
#
#	YES_NO_CHOICES = ((NO, 'Inactive'), (YES, 'Active'))

	fullname = models.CharField(max_length=200, verbose_name='Full Name')
	join_date = models.DateField(default=datetime.datetime.now)
	subscription_date = models.DateField(null=True, blank=True)
	chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE)
	town = models.CharField(max_length=200, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	phone=models.CharField(max_length=30, null=True, blank=True)
	company = models.CharField(max_length=200)
	company_logo = models.CharField(max_length=200, null=True, blank=True, default='logos/logogeneric.png')
	description = models.TextField(default="This is my company description")
	website = models.URLField(null=True, blank=True)
	sector = models.ForeignKey('Sector', on_delete=models.CASCADE)
	sector_desk = models.ForeignKey('SectorDesk', default=1)
	business_club = models.ForeignKey('BusinessClub', on_delete=models.CASCADE)
	sub_status = models.BooleanField(verbose_name='Subscription')
	status = models.CharField(max_length=2, choices=MEMBER_CHOICES, default=10, verbose_name='user status')
	password = models.CharField(max_length=200, default='$2y$10$eM0VDmCiZq692kNgs4K5R.NFKFSQAkV0SkzAC7lW6Ib.iwy2LdvYu')
	interest = models.ManyToManyField('MemberInterest', null=True, blank=True)

	def __str__(self):
		return self.fullname



class BcMeeting(models.Model):
	business_club = models.ForeignKey('BusinessClub', on_delete=models.CASCADE)
	meeting_date = models.DateField(default=datetime.datetime.now)
	secretary = models.CharField(max_length=200)
	guest_speaker = models.CharField(max_length=200)
	minutes = models.TextField()
	next_date = models.DateField(verbose_name=u'Next Meeting Date')
	cost = models.IntegerField(verbose_name='Cost ($)')

	class Meta:
		verbose_name = u'Business Club Meeting'
		verbose_name_plural=u'Business Club Meetings'


class MemberInterest(models.Model):
	interest = models.CharField(max_length=100)

	def __str__(self):
		return self.interest

	class Meta:
		verbose_name = u'Member Interest'
		verbose_name_plural=u'Member Interests'

class Partner(models.Model):
	partner_name = models.CharField(max_length=100, verbose_name='partner')
	contact = models.CharField(max_length=150)
	phone = models.CharField(max_length=40)
	email = models.EmailField()
	country = models.ForeignKey('Chapter')
	speciality = models.ManyToManyField('MemberInterest')
	created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)



