from django.shortcuts import render

from django.http import Http404

from secretariat.models import Chapter, Event, Sector

# Create your views here.

def index(request):
	events = Event.objects.all()
	return render(request, 'secretariat/index.html', {
		'events': events,
		})


def event_detail(request, id):
	try:
		event = Event.objects.get(id=id)
	except Event.DoesNotExist:
		raise Http404('This event does not exist')
	return render(request, 'secretariat/event_detail.html', {
		'event': event,
		})
