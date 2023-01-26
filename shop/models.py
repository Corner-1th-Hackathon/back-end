from django.db import models
from django.contrib.auth.models import AbstractUser

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
    date = models.DateField(null=True)  #post 날짜
    name = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter = models.TextField(null=False)  #메세지
    image = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags = models.ManyToManyField(Tag, blank=True)
    tag = models.CharField(null=True, max_length=100)
    address=models.TextField(null=True)


class Post2(models.Model):
    post_code2 = models.AutoField(primary_key=True)  #post 고유 번호
    date2 = models.DateField()  #post 날짜
    name2 = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter2 = models.TextField(null=False)  #메세지
    image2 = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags2 = models.ManyToManyField(Tag, blank=True)

class Post3(models.Model):
    post_code3 = models.AutoField(primary_key=True)  #post 고유 번호
    date3 = models.DateField()  #post 날짜
    name3 = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter3 = models.TextField(null=False)  #메세지
    image3 = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags3 = models.ManyToManyField(Tag, blank=True)

class Post4(models.Model):
    post_code4 = models.AutoField(primary_key=True)  #post 고유 번호
    date4 = models.DateField()  #post 날짜
    name4 = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter4 = models.TextField(null=False)  #메세지
    image4 = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags4 = models.ManyToManyField(Tag, blank=True)

class Post5(models.Model):
    post_code5 = models.AutoField(primary_key=True)  #post 고유 번호
    date5 = models.DateField()  #post 날짜
    name5 = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter5 = models.TextField(null=False)  #메세지
    image5 = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags5 = models.ManyToManyField(Tag, blank=True)

class Post6(models.Model):
    post_code6 = models.AutoField(primary_key=True)  #post 고유 번호
    date6 = models.DateField()  #post 날짜
    name6 = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter6 = models.TextField(null=False)  #메세지
    image6 = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags6 = models.ManyToManyField(Tag, blank=True)

class Post7(models.Model):
    post_code7 = models.AutoField(primary_key=True)  #post 고유 번호
    date7 = models.DateField()  #post 날짜
    name7 = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter7 = models.TextField(null=False)  #메세지
    image7 = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags7 = models.ManyToManyField(Tag, blank=True)

class Post8(models.Model):
    post_code8 = models.AutoField(primary_key=True)  #post 고유 번호
    date8 = models.DateField()  #post 날짜
    name8 = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter8 = models.TextField(null=False)  #메세지
    image8 = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags8 = models.ManyToManyField(Tag, blank=True)

class Post9(models.Model):
    post_code9 = models.AutoField(primary_key=True)  #post 고유 번호
    date9 = models.DateField()  #post 날짜
    name9 = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter9 = models.TextField(null=False)  #메세지
    image9 = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags9 = models.ManyToManyField(Tag, blank=True)

class Post10(models.Model):
    post_code10 = models.AutoField(primary_key=True)  #post 고유 번호
    date10 = models.DateField()  #post 날짜
    name10 = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter10 = models.TextField(null=False)  #메세지
    image10 = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags10 = models.ManyToManyField(Tag, blank=True)

class Post11(models.Model):
    post_code11 = models.AutoField(primary_key=True)  #post 고유 번호
    date11 = models.DateField()  #post 날짜
    name11 = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter11 = models.TextField(null=False)  #메세지
    image11 = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags11 = models.ManyToManyField(Tag, blank=True)

class Post12(models.Model):
    post_code12 = models.AutoField(primary_key=True)  #post 고유 번호
    date12 = models.DateField()  #post 날짜
    name12 = models.CharField(null=False, max_length=100)  #작성자 닉네임
    letter12 = models.TextField(null=False)  #메세지
    image12 = models.CharField(null=True, blank=True, default="", max_length=500)  #이미지 파일명
    tags12 = models.ManyToManyField(Tag, blank=True)

class CustomUser(AbstractUser):
    # Any extra fields would go here

    def __str__(self):
        return self.username