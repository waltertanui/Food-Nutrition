from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import logging
from myApp.models import User, Foodinfo
from .utils.error import *
from .utils import  getHomeData
from .utils.getPublicData import getAppleData
import json


# Create your views here.

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        try:
            user=User.objects.get(name=uname,password=pwd)
            request.session['name']=user.name
            return  redirect('/myApp/index')
        except:
            messages.error(request, '用户名或密码出错！')
            return redirect('/myApp/login')

def signup(request):
    if request.method == 'GET':

        return render(request, 'signup.html')
    else:
        uname = request.POST.get('signup-name')
        pwd = request.POST.get('signup-password')
        checkPwd = request.POST.get('signup-checkpassword')
        print(f"接收到的用户名：{uname}")
        # 检查两次密码是否一致
        if pwd != checkPwd:
            messages.error(request, '两次输入的密码不一致，请重新输入！')
            return redirect('/myApp/signup')

        try:
            # 创建用户
            User.objects.create(name=uname, password=pwd)
            messages.success(request, '注册成功！请登录。')
            return redirect('/myApp/login?success=1')
        except Exception as e:
         messages.error(request, f'注册失败：{str(e)}')
         return redirect('/myApp/signup')

def logout(request):
    request.session.clear()
    return  redirect('login')

def index(request):
    uname = request.session.get('name')
    userinfo = User.objects.get(name=uname)
    
    # Fetch apple data
    try:
        apples = Foodinfo.objects.filter(Name__contains='苹果')
        apple_data_list = []

        for apple in apples:
            apple_data = {
                'name': apple.Name,
                '可食用部分': apple.Edible,
                '水分': apple.Water,
                '能量': apple.Energy,
                '蛋白质': apple.Protein,
                '脂肪': apple.Fat,
                '碳水化合物': apple.CHO,
                '总膳食纤维': getattr(apple, 'DietaryFiber', 'N/A'),
                '维生素C': getattr(apple, 'VitaminC', 'N/A'),
                '钙': apple.Ca,
                '铁': apple.Fe,
                '锌': apple.Zn
            }
            apple_data_list.append(apple_data)
            
        # For backward compatibility, keep the first apple data separately
        apple_data = apple_data_list[0] if apple_data_list else {}
    except Exception as e:
        print("Error fetching apple data:", str(e))
        apple_data_list = []
        apple_data = {}

    # Fetch coconut data (unchanged)
    try:
        coconut = Foodinfo.objects.get(Name='椰子')
        coconut_data = {
            '可食用部分': coconut.Edible,
            '水分': coconut.Water,
            '能量': coconut.Energy,
            '蛋白质': coconut.Protein,
            '脂肪': coconut.Fat,
            '碳水化合物': coconut.CHO,
            '总膳食纤维': coconut.DietaryFiber,
            '维生素C': coconut.VitaminC,
            '钙': coconut.Ca,
            '铁': coconut.Fe,
            '锌': coconut.Zn
        }
        has_coconut_data = True
    except Foodinfo.DoesNotExist:
        coconut_data = {}
        has_coconut_data = False

    return render(request, 'index.html', {
        'userinfo': userinfo,
        'apple_data_json': json.dumps(apple_data, ensure_ascii=False),
        'apple_data_list_json': json.dumps(apple_data_list, ensure_ascii=False),  # Add the list of all apple data
        'coconut_data_json': json.dumps(coconut_data, ensure_ascii=False),
        'has_coconut_data': has_coconut_data
    })

def account(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    return render(request, 'account.html', {
        'userinfo': userinfo
    })

def changePassword(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    return render(request, 'resetPassword.html', {
        'userinfo': userinfo
    })

def foodCategory(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    return render(request, 'foodCategory.html', {
        'userinfo': userinfo
    })

def foodData(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    foods = Foodinfo.objects.all()
    # Convert QuerySet to list of dictionaries
    foods_list = list(foods.values())
    return render(request, 'foodData.html', {
        'userinfo': userinfo,
        'foods': foods_list
    })

def charts(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    
    # Get all food data
    foods = Foodinfo.objects.all()
    foods_list = list(foods.values())
    
    # Get specific foods for detailed charts
    spring_roll = Foodinfo.objects.filter(Name='春卷').first()
    wheat_flour = Foodinfo.objects.filter(Name='小麦粉（标准粉）').first()
    
    # Prepare spring roll data
    spring_roll_data = {
        '可食用部分': spring_roll.Edible if spring_roll else '0',
        '水分': spring_roll.Water if spring_roll else '0',
        '能量': spring_roll.Energy if spring_roll else '0',
        '蛋白质': spring_roll.Protein if spring_roll else '0',
        '脂肪': spring_roll.Fat if spring_roll else '0',
        '胆固醇': spring_roll.Cholesterol if spring_roll else '0',
        '灰分': spring_roll.Ash if spring_roll else '0',
        '碳水化合物': spring_roll.CHO if spring_roll else '0',
        '总膳食纤维': spring_roll.DietaryFiber if spring_roll else '0',
        '胡萝卜素': spring_roll.Carotene if spring_roll else '0',
        '维生素A': spring_roll.Vitamin if spring_roll else '0',
        'α-生育酚': spring_roll.α_TE if spring_roll else '0',
        '硫胺素': spring_roll.Thiamin if spring_roll else '0',
        '核黄素': spring_roll.Riboflavin if spring_roll else '0',
        '烟酸': spring_roll.Niacin if spring_roll else '0',
        '维生素C': spring_roll.VitaminC if spring_roll else '0'
    }
    
    # Prepare wheat flour data
    wheat_data = {
        '可食用部分': wheat_flour.Edible if wheat_flour else '0',
        '水分': wheat_flour.Water if wheat_flour else '0',
        '能量': wheat_flour.Energy if wheat_flour else '0',
        '蛋白质': wheat_flour.Protein if wheat_flour else '0',
        '脂肪': wheat_flour.Fat if wheat_flour else '0',
        '碳水化合物': wheat_flour.CHO if wheat_flour else '0',
        '膳食纤维': wheat_flour.DietaryFiber if wheat_flour else '0',
        '维生素B1': wheat_flour.Thiamin if wheat_flour else '0',
        '维生素B2': wheat_flour.Riboflavin if wheat_flour else '0',
        '烟酸': wheat_flour.Niacin if wheat_flour else '0',
        '钙': wheat_flour.Ca if wheat_flour else '0',
        '磷': wheat_flour.P if wheat_flour else '0',
        '钾': wheat_flour.K if wheat_flour else '0',
        '钠': wheat_flour.Na if wheat_flour else '0',
        '镁': wheat_flour.Mg if wheat_flour else '0',
        '铁': wheat_flour.Fe if wheat_flour else '0',
        '锌': wheat_flour.Zn if wheat_flour else '0'
    }
    
    # Get food type distribution
    food_types = {}
    for food in foods:
        if food.Type in food_types:
            food_types[food.Type] += 1
        else:
            food_types[food.Type] = 1
    
    # Convert to list for pie chart
    type_distribution = [{'name': k, 'value': v} for k, v in food_types.items()]
    
    return render(request, 'charts.html', {
        'userinfo': userinfo,
        'foods': foods_list,
        'spring_roll_data': spring_roll_data,
        'wheat_data': wheat_data,
        'type_distribution': type_distribution
    })

def recommend(request):
    uname = request.session.get('name')
    userinfo = User.objects.get(name=uname)
    if request.method == 'POST':
        age = int(request.POST.get('age', 25))
        gender = request.POST.get('gender', 'male')
        height = float(request.POST.get('height', 170))
        weight = float(request.POST.get('weight', 65))
        exercise_frequency = request.POST.get('exercise_frequency', 'never')
        allergies = request.POST.getlist('allergies')
        allergy_other = request.POST.get('allergy_other_text', '').strip()
        if allergy_other:
            allergies.append(allergy_other)
        health_conditions = request.POST.getlist('health_conditions')
        health_other = request.POST.get('health_other_text', '').strip()
        if health_other:
            health_conditions.append(health_other)
        # You can parse more fields as needed
        foods = list(Foodinfo.objects.all().values())
        # Simple recommend_foods logic inline (replace with import if you have a util)
        def calculate_bmr(age, gender, height, weight):
            if gender == 'male':
                return 10 * weight + 6.25 * height - 5 * age + 5
            else:
                return 10 * weight + 6.25 * height - 5 * age - 161
        def calculate_daily_energy(bmr, exercise_frequency):
            activity_factors = {
                "never": 1.2,
                "rarely": 1.375,
                "sometimes": 1.55,
                "often": 1.725,
                "always": 1.9
            }
            return bmr * activity_factors.get(exercise_frequency, 1.2)
        bmr = calculate_bmr(age, gender, height, weight)
        daily_energy = calculate_daily_energy(bmr, exercise_frequency)
        # Example macronutrient targets
        target_protein = daily_energy * 0.15 / 4
        target_fat = daily_energy * 0.3 / 9
        target_cho = daily_energy * 0.55 / 4
        recommended = []
        for food in foods:
            # Exclude allergens
            if any(allergy and allergy in food['Name'] for allergy in allergies):
                continue
            # Example: filter for diabetes/hypertension
            if any('糖尿病' in cond for cond in health_conditions):
                try:
                    if float(food.get('CHO', 0)) >= 10:
                        continue
                except:
                    continue
            if any('高血压' in cond for cond in health_conditions):
                try:
                    if float(food.get('Na', 0)) >= 100:
                        continue
                except:
                    continue
            recommended.append(food)
        return render(request, 'recommend.html', {
            'userinfo': userinfo,
            'recommended_foods': recommended
        })
    return render(request, 'recommend.html', {'userinfo': userinfo})

def help(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    return render(request, 'help.html', {
        'userinfo': userinfo
    })

def apple_data_view(request):
    apple_data = getAppleData()
    return render(request, 'index.html', {'apple_data': apple_data})











