from django.shortcuts import render
from django.utils import  timezone
from .models import post
# Create your views here.

def post_list(request):
    posts = post.objects.filter(publioshed_date=timezone.now()).order_by('publioshed_date')
    return  render(request, 'sample/post_list.html', {'posts': posts})

