
from .models import Event, Chapter, Sector, Staff, Trainer, Staffactivity, BusinessClub, Member, BcMeeting, MemberInterest, Partner, User, SectorDesk
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
from django.contrib.admin import SimpleListFilter
from django.forms import TextInput, Textarea
from django.db import models
from django.utils import timezone
from django.http import HttpResponse

#admin.site.site_header = 'Africa Agribusiness Academy'



class SectorAdmin(admin.ModelAdmin):
	list_display=['sector_name', 'description']

class SectorDeskAdmin(admin.ModelAdmin):
	list_display=['name', 'created_at']


class EventAdmin(admin.ModelAdmin):
	list_display=['name', 'start_date', 'duration',  'number_participants', 'added_by', 'chapter']
	list_filter=['start_date', 'chapter', 'status']
	date_hierarchy = 'start_date'

	formfield_overrides = {
	models.CharField: {'widget': TextInput(attrs={'size':'80'})}
	}

	fieldsets = [
	(None, {'fields': ['chapter', 'trainer', 'sector']}),
	('Event Details', {'fields': ['status','name', 'venue', 'start_date', 'end_date', 'description', 'participants']}),

	]
	filter_horizontal = ('participants',)

	def number_participants(self, obj):
		if (obj.start_date < datetime.datetime.now().date() ):
			return obj.participants.count()
		else:
			return "Upcoming"
	number_participants.short_description='Participants'


	def duration(self, obj):
		start = datetime.datetime.strptime(str(obj.start_date), "%Y-%m-%d").date()
		end = datetime.datetime.strptime(str(obj.end_date), "%Y-%m-%d").date()
		period = (end-start).days

		if (period < 2):
			return "1 day"
		else:
			return str(period) + " days"

#	def save_model(self, request, obj, form, change):
#		if not change:
#			obj.created_by = request.user
#		obj.save()
        


class ChapterAdmin(admin.ModelAdmin):
	list_display=['name', 'cordinator','established','email', 'mm_status']

	formfield_overrides = {
	models.TextField: {'widget': TextInput(attrs={'size':'80'})}
	}

	def mm_status(self, obj):
		if (obj.mm_number):
			return True
		else:
			return False
	mm_status.boolean = True
	mm_status.short_description = 'Mobile Money'

	fieldsets = [
	(None, {'fields': ['name', 'cordinator', 'phone', 'established', 'email', 'postal_address', 'physical_address', 'avatar']}),
	('Transaction Details', {'fields':['account_name', 'bank', 'branch', 'account_no', 'forex_rate', 'mm_number']})]


class StaffAdmin(admin.ModelAdmin):
	list_display=['fullname', 'country_chapter']
	
class TrainerAdmin(admin.ModelAdmin):
	list_display=['fullname', 'speciality']
	list_filter=['speciality']

class InterestAdmin(admin.ModelAdmin):
	list_display=['interest']

	def number_members(self, members):
		return members_fullname.count()


class ActivityAdmin(admin.ModelAdmin):
	list_display=['staff', 'activity_date', 'country', 'duration', 'created_by']
	list_filter=['country', 'created_by']

	fieldsets = [
	(None, {'fields': ['staff']}),
	('Activity Details', {'fields': ['activity_date', 'activity_end', 'country', 'activity', 'location']}),

	]

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_by = request.user
		obj.save()

	def duration(self, obj):
		if obj.activity_end:
			start = datetime.datetime.strptime(str(obj.activity_date), "%Y-%m-%d").date()
			end = datetime.datetime.strptime(str(obj.activity_end), "%Y-%m-%d").date()
			period = (end-start).days

		if (period < 2):
			return str(period) + " day"
		else:
			return str(period) + " days"




class BcMeetingAdmin(admin.ModelAdmin):
	list_display=['business_club', 'meeting_date', 'cost']
	list_filter=['business_club']
	date_hierarchy='meeting_date'

class BcAdmin(admin.ModelAdmin):
	list_display=['club_name', 'leader']
	list_filter=['country']
	list_per_page = 20
	search_fields=('club_name', 'established')


class MemberInline(admin.StackedInline):
	model = Member

class MemberAdmin(admin.ModelAdmin):
	list_display=['fullname', 'company', 'join_date', 'subscription_date', 'sub_status']
	list_filter=['sub_status', 'status', 'subscription_date', 'chapter', 'sector', 'business_club',  'interest' ]
	search_fields=('fullname', 'company')
	#inlines = [MemberInline]
	#list_editable=('company')
	list_per_page = 50
	

	filter_horizontal = ('interest',)

	actions= ['download_csv']

	def download_csv(modeladmin, request, queryset):
		import csv
		from django.utils.encoding import smart_str

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition']='attachment;filename=members.csv'
		writer = csv.writer(response,csv.excel)
		response.write(u'\ufeff'.encode('utf8'))
		writer.writerow([
			smart_str(u"fullname"),
			smart_str(u"chapter"),
			smart_str(u"company"),
			smart_str(u"email"),
			smart_str(u"phone"),
			smart_str(u"business_club"),
			smart_str(u"sector"),
			smart_str(u"join_date"),
			smart_str(u"subscription_date"),
			
		])
		for obj in queryset:
			writer.writerow([
				smart_str(obj.fullname),
				smart_str(obj.chapter),
				smart_str(obj.company),
				smart_str(obj.email),
				smart_str(obj.phone),
				smart_str(obj.business_club),
				smart_str(obj.sector),
				smart_str(obj.join_date),
				smart_str(obj.subscription_date),
				
			])
		return response
	download_csv.short_description="Export selected data"

	def save_model(self, request, obj, form, change):
		if (obj.subscription_date):
			sub = datetime.datetime.strptime(str(obj.subscription_date), "%Y-%m-%d").date()
			period = (datetime.datetime.now().date()-sub).days

			if period<365:
				obj.sub_status = True
			else:
				obj.sub_status = False

			obj.save()
		else:
			obj.sub_status = False
			obj.save()


class PartnerAdmin(admin.ModelAdmin):
	list_display = ['partner_name', 'contact', 'phone']
	filter_horizontal = ('speciality',)
	list_filter = ('speciality',)

admin.site.register(Event, EventAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Staffactivity, ActivityAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(BusinessClub, BcAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(BcMeeting, BcMeetingAdmin)
admin.site.register(MemberInterest, InterestAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(SectorDesk, SectorDeskAdmin)
