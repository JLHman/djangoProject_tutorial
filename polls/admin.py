# INF601 - Advanced Programming in Python
# Jesse Heckman
# Mini Project # 4


from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):


 '''class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)'''