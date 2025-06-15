from django.shortcuts import render

def errorReaponse(request,errMsg):
    return render(request,"404.html"),{
        'errMsg':errMsg
    }