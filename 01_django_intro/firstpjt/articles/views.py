from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def greeting(request):
    family = 'mom', 'dad', 'sister',
    context = {
        'name': 'Alice', 
        'age': 25, 
        'family': family,
    }
    # return render(request, 'greeting.html')
    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['가지덮밥', '차돌된장찌개', '오리주물럭', '열무국수']
    context = {
        'foods': foods,
    }
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request, 'throw.html') 

def catch(request):
    # raise
    print(request)
    print(type(request))
    print(request.GET.get('message'))
    print(request.GET)

    message = request.GET.get('message')
    message1 = request.GET.get('message1')
    context = {
        'message' : message,
        'message1' : message1,
    }
    print(context)

    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)

def hello1(request):
    return render(request, 'hello1.html')