from django.db import models


class Tag(models.Model):
    name=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/tag/{self.slug}/'

#게시물 모델
class Post(models.Model):
    post_code = models.AutoField(primary_key=True)  #post 고유 번호
    date = models.DateField()  #post 날짜
    name = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter = models.TextField(null=False)  #메세지
    image = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags = models.ManyToManyField(Tag, blank=True)

