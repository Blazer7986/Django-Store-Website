from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Products


# Create your views here.
# request --> response
# request handler
# action

def say_hello(request):
  # Pull data from a database
  # Transform data
  # Send emails
  
  # try:
  #   query_set = Products.objects.all()
  #   product = Products.objects.get(pk=0)
  # except ObjectDoesNotExist:
  #   pass
  
  # query_set.filter().filter().order_by()
  # for product in query_set:
  #   print(product)
  
  # None
  # exists = Products.objects.filter(pk=0).exists()
  
  # Keyword=value
  # query_set = Products.objects.filter(unit_price__range=(20, 30))
  # query_set = Products.objects.filter(collection__id__range=(1, 2, 3))
  # query_set = Products.objects.filter(title__icontains='coffee')
  # query_set = Products.objects.filter(last_update_year=2021)
  query_set = Products.objects.filter(description__isnull=True)
  
  return render(request, 'hello.html', {'name': 'Sam', 'products': list(query_set)})