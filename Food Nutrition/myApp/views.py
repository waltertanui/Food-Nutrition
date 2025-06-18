from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import logging
from myApp.models import User, Foodinfo
from .utils.error import *
from .utils import getHomeData
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
        'apple_data_list_json': json.dumps(apple_data_list, ensure_ascii=False),
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
        # Basic Information
        age = int(request.POST.get('age', 25))
        gender = request.POST.get('gender', 'male')
        height = float(request.POST.get('height', 170))
        weight = float(request.POST.get('weight', 65))
        
        # Health Information
        exercise_frequency = request.POST.get('exercise_frequency', 'never')
        sleep_hours = request.POST.get('sleep_hours', '7_8')
        allergies = request.POST.getlist('allergies')
        allergy_other = request.POST.get('allergy_other_text', '').strip()
        if allergy_other:
            allergies.append(allergy_other)
        health_conditions = request.POST.getlist('health_conditions')
        health_other = request.POST.get('health_other_text', '').strip()
        if health_other:
            health_conditions.append(health_other)
        
        # Dietary Preferences
        favorite_foods = request.POST.getlist('favorite_foods')
        favorite_other_food = request.POST.get('favorite_other_food_text', '').strip()
        if favorite_other_food:
            favorite_foods.append(favorite_other_food)
        diet_restrictions = request.POST.getlist('diet_restrictions')
        diet_other_restriction = request.POST.get('diet_other_restriction_text', '').strip()
        if diet_other_restriction:
            diet_restrictions.append(diet_other_restriction)
        taste_preferences = request.POST.getlist('taste_preferences')
        taste_other_taste = request.POST.get('taste_other_taste_text', '').strip()
        if taste_other_taste:
            taste_preferences.append(taste_other_taste)
        
        # Lifestyle
        health_goals = request.POST.getlist('health_goals')
        health_goal_other = request.POST.get('health_goal_other_text', '').strip()
        if health_goal_other:
            health_goals.append(health_goal_other)
        
        # Fetch all foods
        foods = list(Foodinfo.objects.all().values())

        # Calculate BMR and daily energy needs
        def calculate_bmr(age, gender, height, weight):
            if gender == 'male':
                return 10 * weight + 6.25 * height - 5 * age + 5
            elif gender == 'female':
                return 10 * weight + 6.25 * height - 5 * age - 161
            else:
                return 10 * weight + 6.25 * height - 5 * age - 78  # Average for 'other'

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

        # Adjust energy based on health goals
        if 'weight_loss' in health_goals:
            daily_energy *= 0.85  # Reduce by 15% for weight loss
        elif 'weight_gain' in health_goals:
            daily_energy *= 1.15  # Increase by 15% for weight gain

        # Macronutrient targets
        target_protein = daily_energy * 0.15 / 4  # 15% of energy from protein
        target_fat = daily_energy * 0.3 / 9       # 30% from fat
        target_cho = daily_energy * 0.55 / 4      # 55% from carbs

        # Adjust sleep impact (simplified)
        sleep_adjustment = 1.0
        if sleep_hours in ['under_6']:
            sleep_adjustment = 0.95  # Slightly reduce recommendations due to poor sleep
        elif sleep_hours in ['over_9']:
            sleep_adjustment = 1.05  # Slightly increase for high sleep

        recommended = []
        for food in foods:
            # Exclude allergens
            if any(allergy.lower() in food['Name'].lower() or allergy.lower() in (food.get('Type', '')).lower() for allergy in allergies):
                continue

            # Filter based on health conditions
            try:
                if 'diabetes' in health_conditions or '糖尿病' in health_conditions:
                    if float(food.get('CHO', 0)) >= 10:
                        continue
                if 'hypertension' in health_conditions or '高血压' in health_conditions:
                    if float(food.get('Na', 0)) >= 100:
                        continue
                if 'heart_disease' in health_conditions:
                    if float(food.get('Fat', 0)) >= 5 or float(food.get('Cholesterol', 0)) >= 50:
                        continue
            except (ValueError, TypeError):
                continue

            # Filter based on dietary restrictions
            try:
                if 'vegetarian' in diet_restrictions:
                    if 'meat' in food['Name'].lower() or 'fish' in food['Name'].lower() or food.get('Type', '').lower() in ['meat', 'fish']:
                        continue
                if 'vegan' in diet_restrictions:
                    if any(term in food['Name'].lower() or term in food.get('Type', '').lower() for term in ['meat', 'fish', 'dairy', 'egg']):
                        continue
                if 'low_salt' in diet_restrictions:
                    if float(food.get('Na', 0)) >= 50:
                        continue
                if 'low_fat' in diet_restrictions:
                    if float(food.get('Fat', 0)) >= 3:
                        continue
            except (ValueError, TypeError):
                continue

            # Prioritize favorite foods and taste preferences
            score = 0
            food_type = food.get('Type', '').lower()
            food_name = food['Name'].lower()
            
            # Boost score for favorite foods
            if favorite_foods:
                for fav in favorite_foods:
                    if fav.lower() in food_type or fav.lower() in food_name:
                        score += 10
                    elif fav.lower() == 'fruits' and 'fruit' in food_type:
                        score += 10
                    elif fav.lower() == 'vegetables' and 'vegetable' in food_type:
                        score += 10
                    elif fav.lower() == 'grains' and 'grain' in food_type:
                        score += 10
                    elif fav.lower() == 'snacks' and 'snack' in food_type:
                        score += 10

            # Boost score for taste preferences (simplified mapping)
            if taste_preferences:
                for taste in taste_preferences:
                    if taste.lower() == 'sweet' and any(term in food_name for term in ['sugar', 'honey', 'sweet']):
                        score += 5
                    elif taste.lower() == 'salty' and float(food.get('Na', 0)) > 50:
                        score += 5
                    elif taste.lower() == 'sour' and float(food.get('VitaminC', 0)) > 10:  # Proxy for sourness
                        score += 5
                    elif taste.lower() == 'spicy' and any(term in food_name for term in ['chili', 'pepper']):
                        score += 5
                    elif taste.lower() == 'bitter' and any(term in food_name for term in ['bitter', 'kale']):
                        score += 5

            # Adjust based on nutritional needs
            try:
                protein = float(food.get('Protein', 0))
                fat = float(food.get('Fat', 0))
                cho = float(food.get('CHO', 0))
                if (protein <= target_protein * 0.2 and fat <= target_fat * 0.2 and cho <= target_cho * 0.2):
                    score += 5  # Favor foods that align with macro targets
            except (ValueError, TypeError):
                pass

            # Apply sleep adjustment
            score *= sleep_adjustment

            # Add food with score
            if score > 0 or not (favorite_foods or taste_preferences):  # Include all foods if no preferences
                food['score'] = score
                recommended.append(food)

        # Sort by score (highest first) and limit to top 10
        recommended = sorted(recommended, key=lambda x: x['score'], reverse=True)[:10]

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