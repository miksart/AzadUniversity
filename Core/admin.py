from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from Core.models import Article, ContactMessage, Slider


class ArticleAdmin(TranslationAdmin):
    fieldsets = [
        (u'Article', {'fields': ('title', 'text', 'photo')})
    ]

    list_display = ('title', 'text','publish')


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email','message')

    
class SliderAdmin(TranslationAdmin):
    fieldsets = [
        (u'Slider', {'fields': ('title', 'photo')})
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Slider, SliderAdmin)
