from django.contrib import admin
from django import forms
from .models import Post, Response

from ckeditor_uploader.widgets import CKEditorUploadingWidget


# class PostAdminForm(forms.ModelForm):
#     text = forms.CharField(widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = Post
#         fields = '__all__'
#
#
# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm

admin.site.register(Post)
admin.site.register(Response)
# admin.site.register(PostAdminForm)
