from django.contrib.auth.views import redirect_to_login

class RequireLoginMixin:
    login_url = '/poll/login/'

    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(),self.login_url)
        return super(RequireLoginMixin,self).dispatch(request,*args,**kwargs)