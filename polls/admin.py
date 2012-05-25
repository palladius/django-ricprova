from polls.models import Poll, Choice
#from polls.models import Choice
from django.contrib import admin

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                              {'fields': ['question']} ),
        ('Date info (if u really want it)', {'fields': ['pub_date'], 'classes': ['collapse']} ),
    ]
    inlines = [ChoiceInline]
    #list_display = ('question', 'pub_date')
    list_display = ('question', 'pub_date', 'was_published_recently')
    search_fields = ['question']


class ChoiceAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,   {'fields': ['poll']} ),
    (None,   {'fields': ['choice']} ),
    ('Votes..', {'fields': ['votes'], 'classes': ['collapse']} ),
  ]

#admin.site.register(Poll)           # base
admin.site.register(Poll, PollAdmin) # custom
#admin.site.register(Choice)          # base
admin.site.register(Choice, ChoiceAdmin)    # custom