import os.path

from django.shortcuts import HttpResponse
from shop.models import Product, Tag
from shop import ProductSerializer as ps
import simplejson
from django.views.decorators.csrf import csrf_exempt

UPLOAD_DIR = os.path.dirname(__file__) + '/static/images/'

def list(request):
    items=Product.objects.order_by("-product_name")
    serializer = ps.ProductSerializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

@csrf_exempt
def insert(request):
    if "img" in request.FILES:
        file = request.FILES["img"]
        file_name = file._name
        fp = open("%s%s" % (UPLOAD_DIR, file_name), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    else:
        file_name = "-"

    row = Product(product_name=request.POST["product_name"], description=request.POST["description"],
                  price=request.POST["price"], filename=file_name)

    row.save()

def detail(request, product_code):
    row = Product.objects.get(product_code=product_code)
    serializer = ps.ProductSerializer(row)
    return HttpResponse(simplejson.dumps(serializer.data))

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set
    #items = Product.objects.order_by("-product_name")
    serializer = ps.ProductSerializer(tag, post_list, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))