from django.shortcuts import render

# Create your views here.
# CRUD : create read update delete
# List

# 클래스형 뷰, 함수형 뷰 두종류가 있음
# 웹페이지에 접속하는것 - > 페이지를 본다.


from django.views.generic.list import  ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Bookmark

class BookmarkListView(ListView): #istview는 generic view중 하나임
    model = Bookmark              #북마크 불러와야함

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url'] #어떤걸 수정할지 지정하는거
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmartDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url'] #어떤걸 수정할지 지정하는거
    template_name_suffix = '_update' #기본적으로 불러오는 form을 안가져올려고

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')