from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
    return render(request,"testapp/home.html")

def movies_news_view(request):
    news1='What gave Kangana the right to tamper with what I did?'
    news2="Like Salman's patriotic act in Bharat teaser?"
    news3="Shreyas Talpade brings comedy to your home"
    news4="Karan Johar: 'I have had so many sleepless nights'"

    head_dic={'news1':news1,'news2':news2,'news3':news3,'news4':news4}
    return render(request,'testapp/movie.html',context=head_dic)