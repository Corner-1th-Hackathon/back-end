import os.path

from django.shortcuts import HttpResponse
from shop.models import Post, Tag
from shop import PostSerializer as ps
import simplejson
from django.views.decorators.csrf import csrf_exempt

UPLOAD_DIR = os.path.dirname(__file__) + '/static/images/'

def list(request):
    items=Post.objects.order_by("-date")
    serializer = ps.PostSerializer(items, many=True)
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

    row = Post(letter=request.POST["letter"],
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