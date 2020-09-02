from modeltranslation.translator import translator, TranslationOptions

from .models import Article, Slider


class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
    required_languages = {'en': ('title', 'text'), 'default': ('title', 'text')}


class SliderTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = {'en': ('title',), 'default': ('title',)}


translator.register(Article, ArticleTranslationOptions)
translator.register(Slider, SliderTranslationOptions)
