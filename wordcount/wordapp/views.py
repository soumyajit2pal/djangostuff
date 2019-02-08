from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.

def home(request):
    return render(request,'wordcount/index.html')

def count(request):
    data=request.GET['fulltext']
    word_list=data.split(" ")
    list_len=len(word_list)
    word_dic={}

    for word in word_list:
        if word in word_dic:
            word_dic[word]+=1
        else:
            word_dic[word]=1
    sort_wordlist=sorted(word_dic.items(),key=operator.itemgetter(1))
    return render(request, "wordcount/count.html",{'data':data,'count':list_len,'sort':sort_wordlist})