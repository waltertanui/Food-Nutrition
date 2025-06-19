from django.urls import path,re_path
from myApp import views


urlpatterns=[
    path('login/',views.login,name='login'),
    path('signup/', views.signup, name='signup'),
    path('index/',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('account/',views.account,name='account'),
    path('changePassword/',views.changePassword,name='changePassword'),
    path('foodCategory/',views.foodCategory,name='foodCategory'),
    path('foodData/',views.foodData,name='foodData'),
    path('charts/',views.charts,name='charts'),
    path('recommend/',views.recommend,name='recommend'),
    path('help/',views.help,name='help'),
    path('weekly-recipes/', views.weekly_recipes, name='weekly_recipes'),
]


