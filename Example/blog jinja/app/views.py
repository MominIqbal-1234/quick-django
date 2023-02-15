
        
from django.shortcuts import render,HttpResponse
from django.views import View



class Home(View):
    def get(self,request):
        return HttpResponse('<h1>visit : <a href="https://mefiz.com">mefiz.com</a></h1>')
        # return render(request,'index.html')
        