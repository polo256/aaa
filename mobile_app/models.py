from django.db import models
import datetime
from django.contrib.auth.models import User
from secretariat.models import Member, SectorDesk

class Blog(models.Model):
	member = models.ForeignKey(Member)
	title = models.CharField(max_length=400)
	img = models.CharField(max_length=200, null=True, blank=True)
	blog = models.TextField()
	created_at=models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.title


class Feedback(models.Model):
	member = models.ForeignKey(Member)
	feedback = models.TextField()
	created_at=models.DateTimeField(default=datetime.datetime.now)

	class Meta:
		verbose_name_plural='Feedback'

	def __str__(self):
		return self.feedback


class Notice(models.Model):
	member = models.ForeignKey(Member)
	title = models.CharField(max_length=100)
	notice = models.TextField()
	attachment = models.CharField(max_length=200, null=True, blank=True)
	attachment_type = models.CharField(max_length=10, null=True, blank=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	status = models.IntegerField(default=1)
	created_at = models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.title

class NoticeComment(models.Model):
	notice = models.ForeignKey('Notice', on_delete=models.CASCADE)
	member = models.ForeignKey(Member)
	comment = models.TextField()
	attachment = models.CharField(max_length=100, null=True, blank=True)
	attachment_type = models.CharField(max_length=10, null=True, blank=True, editable=False)
	name = models.CharField(max_length=100, null=True, blank=True, editable=False)
	status = models.IntegerField(default=1, editable=False)
	created_at = models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.comment


class SectorDeskPost(models.Model):
	sector_desk = models.ForeignKey(SectorDesk)
	member = models.ForeignKey(Member, default=729, editable=False)
	title = models.CharField(max_length=200)
	post = models.TextField()
	attachment = models.CharField(max_length=100, null=True, blank=True)
	attachment_type = models.CharField(max_length=10, null=True, blank=True, editable=False)
	name = models.CharField(max_length=100, null=True, blank=True, editable=False)
	status = models.IntegerField(default=1, editable=False)
	created_at = models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.title

class SectorDeskPostComment(models.Model):
	sector_desk_post = models.ForeignKey('SectorDeskPost', on_delete=models.CASCADE)
	member = models.ForeignKey(Member)
	comment = models.CharField(max_length=200)
	attachment = models.CharField(max_length=100, null=True, blank=True)
	attachment_type = models.CharField(max_length=10, null=True, blank=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	status = models.IntegerField()
	created_at = models.DateTimeField()

	def __str__(self):
		return self.comment

class Device(models.Model):
	member = models.ForeignKey(Member)
	email = models.CharField(max_length=200)
	token = models.TextField()
	notification_status = models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)

class Resource(models.Model):
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	description = models.TextField()
	created_at=models.DateTimeField()

	def __str__(self):
		return self.title


class Message(models.Model):
	message = models.CharField(max_length=1000)
	sender = models.ForeignKey(Member, related_name='sender')
	receiver = models.ForeignKey(Member, related_name='receiver')
	created_at = models.DateTimeField(datetime.datetime.now)


