from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
# Create your views here.
#def login(request):
        #導入login頁面
 #       return render_to_response('login/index.html')
def login(request):
    if request.user.is_authenticated():
        return render_to_response('login/index.html')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('login/index.html')
    else:
        return render_to_response('login/loginfail.html', RequestContext(request, locals()))

def logout(request):
    auth.logout(request)
    return  HttpResponseRedirect('login/login.html')
