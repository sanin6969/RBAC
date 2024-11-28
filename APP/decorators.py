from django .http import HttpResponse
from django.shortcuts import redirect,render

def unauthenticated_user(funtion_view):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return funtion_view(request,*args,**kwargs)
    return wrapper


from django.http import HttpResponseForbidden
from functools import wraps

def role_required(allowed_roles):
    def wrapper(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role not in allowed_roles:
                return render(request,'403.html')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return wrapper
