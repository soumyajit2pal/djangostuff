from django.shortcuts import render

# Create your views here.
def  addZero(hr):
    if(int(hr)<10):
        return "0"+hr
    else:
        return hr
def index(request):
    context_dic={"hr":range(24),"min":range(60),"sec":range(60)}
    if request.method=="POST":
        hr=request.POST['hour']
        min=request.POST['minutes']
        sec=request.POST['seconds']
        # print(addZero(hr))
        # print(addZero(min))
        # print(addZero(sec))
    return render(request,'testapp/index.html',context=context_dic)