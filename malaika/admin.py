from django.contrib import admin
from .models import Book, Child, Parent
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
	list_display=('name',)


class ChildAdmin(admin.ModelAdmin):
	list_display=('child_name',)

class ParentAdmin(admin.ModelAdmin):
	list_display=['parent_name', 'number_kids']

	filter_horizontal=('kid',)

	def number_kids(self, obj):
		return obj.kid.count()
		
	number_kids.short_description='Children'

admin.site.register(Book, BookAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Parent, ParentAdmin)
