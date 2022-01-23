from django.shortcuts import render

def index(request):
    return render(request, 'polls/index.html',{ })

def detail(request):
    print("REQUEST",request.GET.get('fname',''))
    context = {
        "url": request.GET.get('url','')
    }
    return render(request,'polls/detail.html',context)
