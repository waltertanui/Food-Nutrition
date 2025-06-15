from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,redirect
class UserMW(MiddlewareMixin):
   def process_request(self,request):
      path = request.path_info
      # {{ edit_1 }}
      # Allow access to login and signup pages (handle potential missing trailing slash)
      if path.startswith('/myApp/login') or path.startswith('/myApp/signup'):
        return None
      else:
        if not request.session.get('name'):
          return redirect('login')
      return None


   def process_view(self,request,callback,callback_args,callback_kwargs):
        return None

   def process_response(self,request,response):
        return response