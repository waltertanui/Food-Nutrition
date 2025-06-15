from myApp.models import  *


def getAllUsers():
    return User.objects.all()

def getAllfoods():
    return  Foodinfo.objects.all()

def getAppleData():
    """获取苹果相关的食物数据"""
    return Foodinfo.objects.filter(Name__icontains='苹果')

