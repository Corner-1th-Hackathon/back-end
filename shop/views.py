import os.path

from django.shortcuts import HttpResponse

from shop.PostSerializer import PostSerializer
from shop.models import Post, Tag, Post2, Post3,Post4, Post5,Post6, Post7,Post8, Post9,Post10,Post11, Post12
from shop import PostSerializer as ps
import simplejson
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

UPLOAD_DIR = os.path.dirname(__file__) + '/static/images/'

def list(request):
    try:
        tag=request.GET["tag"]
    except:
        tag=""
    items=Post.objects.filter(tag__contains=tag).order_by("date")
    serializer = ps.PostSerializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))


def list2(request):
    items=Post2.objects.order_by("-date2")
    serializer = ps.Post2Serializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

def list3(request):
    items=Post3.objects.order_by("-date3")
    serializer = ps.Post3Serializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

def list4(request):
    items=Post4.objects.order_by("-date4")
    serializer = ps.Post4Serializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

def list5(request):
    items=Post5.objects.order_by("-date5")
    serializer = ps.Post5Serializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

def list6(request):
    items=Post6.objects.order_by("-date6")
    serializer = ps.Post6Serializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

def list7(request):
    items=Post7.objects.order_by("-date7")
    serializer = ps.Post7Serializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

def list8(request):
    items=Post8.objects.order_by("-date8")
    serializer = ps.Post8Serializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

def list9(request):
    items=Post9.objects.order_by("-date9")
    serializer = ps.Post9Serializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

def list10(request):
    items=Post10.objects.order_by("-date10")
    serializer = ps.Post10Serializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

def list11(request):
    items=Post11.objects.order_by("-date11")
    serializer = ps.Post11Serializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

def list12(request):
    items=Post12.objects.order_by("-date12")
    serializer = ps.Post12Serializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))


@csrf_exempt
def insert(request):
    if "image" in request.FILES:
        file = request.FILES["image"]
        file_name = file._name
        fp = open("%s%s" % (UPLOAD_DIR, file_name), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    else:
        file_name = "-"

    row = Post(letter=request.POST["letter"],address=request.POST["address"],
                  name=request.POST["name"], image=file_name, date=request.POST["date"], tag=request.POST["tag"])

    row.save()

def detail(request, post_code):
    row = Post.objects.get(post_code=post_code)
    serializer = ps.PostSerializer(row)
    return HttpResponse(simplejson.dumps(serializer.data))

# def tag_page(request, slug): #함수작성 / request와 slug 변수도 받으니 slug도 작성
#     if slug=='no_tag' : #category가 미분류일때 / sidebar.html에서 no_category인자를 전달해서
#         tag ='미분류'
#         post_list = Post.objects.filter(tag=None)
#     else: #category를 가지고 있을 때
#         category=Tag.objects.get(slug=slug) #왼쪽 slug : category의 필드명
#                                                  #오른쪽 slug : 함수 선언할 때 작성해둔 인자인 slug=url을 통해 전달된 어떤 특정한 값=사용자가 찾기 원하는 값
#         post_list=Tag.objects.filter(tag=tag) #왼쪽 category : 위에서 생성한 변수인 category
#     return render(request, 'blog/post_list.html',{
#         'category':category,
#         'post_list':post_list,
#         'categories':Category.objects.all(),
#         'no_category_post_count':Post.objects.filter(category=None).count
#     })

def delete(request):
    Post.objects.get(post_code=request.GET["post_code"]).delete()