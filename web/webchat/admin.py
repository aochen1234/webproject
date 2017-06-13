from django.contrib import admin
from django.db import models
from django import forms
from .models import UserProfile, Article, Column, Comment, WebGroup
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'row': 41, 'cols': 100})}, }
    list_display = ('title', 'columns', 'author', 'pub_date', 'last_modify', 'status')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'pub_date')


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(UserProfile)
admin.site.register(WebGroup)