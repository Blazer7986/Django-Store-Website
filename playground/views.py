from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg
from store.models import Products, OrderItems, Orders, Customers


# Create your views here.
# request --> response
# request handler
# action

def say_hello(request):
  # Pull data from a database
  # Transform data
  # Send emails
  
  ### Try ####
  # try:
  #   query_set = Products.objects.all()
  #   product = Products.objects.get(pk=0)
  # except ObjectDoesNotExist:
  #   pass
  
  # query_set.filter().filter().order_by()
  # for product in query_set:
  #   print(product)
  
  ### FILTER ###
  # exists = Products.objects.filter(pk=0).exists()
  
  ### Keyword=value ###
  # query_set = Products.objects.filter(unit_price__range=(20, 30))
  # query_set = Products.objects.filter(collection__id__range=(1, 2, 3))
  # query_set = Products.objects.filter(title__icontains='coffee')
  # query_set = Products.objects.filter(last_update_year=2021)
  # query_set = Products.objects.filter(description__isnull=True)
  
  ### Q AND Symbols (lt, gt, ...) ###
  # Products: inventory < 10 AND unit_price < 20
  # query_set = Products.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
  # Products: inventory < 10 OR unit_price < 20
  # query_set = Products.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))
  
  ### F: Reference an object ###
  # Products: inventory = price 
  # query_set = Products.objects.filter(inventory=F('unit_price'))
  
  ### Other Methods: earliest, latest, order_by ###
  # query_set = Products.objects.order_by('unit_price','-title').reverse()
  # product = Products.objects.order_by('unit_price')[0]
  # product = Products.objects.earliest('unit_price')
  # return render(request, 'hello.html', {'name': 'Sam', 'product': product})
  
  ### Other Methods: all, values, values_list, distinct ###
  # 0, 1, 2, 3, 4
  # 5, 6, 7, 8, 9
  # query_set = Products.objects.all()[5:10]
  
  # query_set = Products.objects.values_list('id', 'title', 'collection__title')
  
  # query_set = Products.objects.filter(id__in=OrderItems.objects.values('product_id').distinct()).order_by('title')
  
  ### Other Methods: only ###
  # Works similarly to values however this will slow down the server and you have
  # wait for seconds/mins for the webpage to load. The reasoning for this is that
  # it loads multiple queries to the server and with added loop in hello.html
  # there will be a longer load and wait time. So please be warned.
  # query_set = Products.objects.only('id', 'title)

  ### Other Methods: defer ###
  # Will leave the description until later on 
  # query_set = Products.objects.defer('description')
  
  ### Other Methods: select_related, prefetch_related ###
  # select_related (1)
  # prefetch_related (n = many)
  # query_set = Products.objects.select_related('collection').all()
  # query_set = Products.objects.prefetch_related('promotions').select_related('collection').all()
  # query_set = Orders.objects.select_related('customers').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
  # return render(request, 'hello.html', {'name': 'Sam', 'products': list(query_set)})
  
  ### AAGGREGATE ###
  # result = Products.objects.filter(collection__id=1).aaggregate(count=Count('id'), min_price=Min('unit_price'))
  
  ### Other Methods: annotate ###
  # Annotate - add addional attritutes to queries
  # query_set = Customers.objects.annotate(is_new=Value(True))
  # query_set = Customers.objects.annotate(new_id=F(id) + 1)
  # query_set = Customers.objects.annotate(
  #   # CONCAT
  #   full_name=Func(F('first_name', Value(' '), 'last_name'), function='CONCAT')
  # )
  # Short-hand Style
  # query_set = Customers.objects.annotate(
  #   # CONCAT
  #   full_name=Concat('first_name', Value(' '), 'last_name')
  # )
  # query_set = Customers.objects.annotate(
  #   # CONCAT
  #   orders_count=Count('orders')
  # )
  
  ### Working with Expression Wrappers ###
  # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField() )
  # query_set = Products.objects.annotate(
  #   discount_price = discounted_price
  # ) 
  
  return render(request, 'hello.html', {'name': 'Sam'})