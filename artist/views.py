from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# views function
from django.utils import timezone


def hello(request):
    # return HttpResponse(f'<h1 style="color: red;">Hello world</h1>')
    context = dict()
    context['fulname'] = 'Olimjon Mamadjanov'
    context['about'] = 'Men Olimjon Mamadjanov 1992 yilda Tug`ilganman.'
    context['time'] = timezone.now()

    return render(request, 'base.html', context=context)
