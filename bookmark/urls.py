from django.urls import path
#from .views import BookmarkListView, BookmarkCreateView, BookmartDetailView
from .views import *
urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),  #클래스형 뷰는 as_view 붙여야함 함수형으로 변환
    path('add/', BookmarkCreateView.as_view(), name='add'), #name은 url의 패턴
    path('detail/<int:pk>/', BookmartDetailView.as_view(), name='detail'), #뷰 뒤에 글번호를 인자로 받는다.
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]