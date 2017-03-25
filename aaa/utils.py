from secretariat.models import Event, Member, Partner, BcMeeting
from mobile_app.models import Notice, Resource, Feedback, SectorDeskPost
from django.utils import timezone


class count_events():
	def __str__(self):
		
		return str(Event.objects.count())


class count_members():

	def __str__(self):
		return str(Member.objects.count())

class count_partners():
	def __str__(self):
		return str(Partner.objects.count())


class count_notices():
	def __str__(self):
		return str(Notice.objects.count())


class count_resources():
	def __str__(self):
		return str(Resource.objects.count())

class count_meetings():
	def __str__(self):
		return str(BcMeeting.objects.count())


class count_feedback():
	def __str__(self):
		return str(Feedback.objects.count())


def count_discussions():
	return str(SectorDeskPost.objects.count())


