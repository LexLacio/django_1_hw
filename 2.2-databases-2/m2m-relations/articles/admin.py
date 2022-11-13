from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_mains = []
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main')
            if is_main is True:
                is_mains.append(is_main)
        if len(is_mains) > 1:
            raise ValidationError('Основной тег может быть только 1')
        elif len(is_mains) == 0:
            raise ValidationError('Укажите основной тег')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['id', 'title', 'published_at']


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ['name']