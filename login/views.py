from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def login(request):
        #導入login頁面
        return render_to_response('login/index.html')
