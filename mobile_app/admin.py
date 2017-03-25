from django.contrib import admin
from .models import Blog, Feedback, Notice, NoticeComment, SectorDeskPost, SectorDeskPostComment, Device, Resource, NoticeComment
from django.utils import timezone
from django.db import models

from django.forms import TextInput, Textarea


class BlogAdmin(admin.ModelAdmin):
	list_display=['title', 'member', 'created_at']
	list_filter=['created_at']

class NoticeAdmin(admin.ModelAdmin):
	list_display=['title', 'member', 'created_at']
	list_filter=['created_at']

class ResourceAdmin(admin.ModelAdmin):
	list_display=['title', 'created_at']
	list_filter=['created_at']

class FeedbackAdmin(admin.ModelAdmin):
	list_display=['member', 'feedback', 'created_at']

class SDPostAdmin(admin.ModelAdmin):
	list_display=['title', 'created_at', 'member']
	list_filter=['sector_desk', 'created_at']

class NoticeCommAdmin(admin.ModelAdmin):
	list_display=['member', 'notice', 'comment']

class SDCommentAdmin(admin.ModelAdmin):
	list_display=['member', 'comment', 'sector_desk_post', 'created_at']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(NoticeComment, NoticeCommAdmin)
admin.site.register(SectorDeskPost, SDPostAdmin)
admin.site.register(SectorDeskPostComment, SDCommentAdmin)
admin.site.register(Resource, ResourceAdmin)
