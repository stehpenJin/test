from django.contrib import admin

# Register your models here.
# 모델 migrate 이후
# 내가 만든 모델을 관리자 페이지에서 관리할 수 있도록 등록

from .models import Bookmark

admin.site.register(Bookmark) # Bookmark app을 등록Bookmark

