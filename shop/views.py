import os.path

from django.shortcuts import HttpResponse
from shop.models import Post, Tag, Post2, Post3,Post4, Post5,Post6, Post7,Post8, Post9,Post10,Post11, Post12
from shop import PostSerializer as ps
import simplejson
from django.views.decorators.csrf import csrf_exempt
from shop.PostSerializer import PostSerializer
from rest_framework import viewsets
from geopy.geocoders import Nominatim

UPLOAD_DIR = os.path.dirname(__file__) + '/static/images/'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

####### 도로명주소 위도 경도 값으로 바꿔주기 ########
geo_local = Nominatim(user_agent='South Korea')

'''
# 위도, 경도 반환하는 함수
def geocoding(address):
    try:
        geo = geo_local.geocode(address)
        x_y = [geo.latitude, geo.longitude]
        x= geo.latitude
        y= geo.longitude
        return x_y

    except:
        return [0,0]
'''

def geocoding(address):
    try:
        geo = geo_local.geocode(address)
        return geo.latitude

    except:
        return 0

def geocoding2(address):
    try:
        geo = geo_local.geocode(address)
        return geo.longitude

    except:
        return 0

def list(request):
    items=Post.objects.order_by("-date")
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

    row = Post(letter=request.POST["letter"], date=request.POST["date"], address=request.POST["address"],
               latitude=78.5, longitude=121.2,
               name=request.POST["name"], image=file_name)

    row.save()

def detail(request, post_code):
    row = Post.objects.get(post_code=post_code)
    serializer = ps.PostSerializer(row)
    return HttpResponse(simplejson.dumps(serializer.data))


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set
    #items = Product.objects.order_by("-product_name")
    serializer = ps.PostSerializer(tag, post_list, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

def delete(request):
    Post.objects.get(post_code=request.GET["post_code"]).delete()