from django.db import models
from django.urls import reverse
# Create your models here.

class Bookmark(models.Model): #models.Model 상속
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL') #인자는 레이블 네임
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컴럼 종류
    # 2. 제약 사항
    # 3. Form의 종류
    # 4. Form의 제약사항

    def __str__(self): #문법 함 보기
        return "이름 : "+self.site_name+", 주소 : "+self.url
# 모델을 만들었다 => DB에 어떤 데이터들을 넣을지 결정함
# makemigrations -> 모델의 변경사항을 추적해서 기록
# 마이그레어션(migrate) => 데이터베이스에 모델의 내용을 반영(테이블 생성)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)]) #detail 뷰의 매개변수로 str(self.id)