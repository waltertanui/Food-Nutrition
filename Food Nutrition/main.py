#python manage.py runserver
# This is a sample Python script.
import mimetypes

from django.db.backends import mysql
from django.http import HttpResponse

from pydjango import settings

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from django.db import connection

def some_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM your_table")
        results = cursor.fetchall()
    # 处理结果

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_view()


# 计算用户每日所需能量的函数
def calculate_daily_energy(bmr, exercise_frequency):
    activity_factors = {
        "很少运动": 1.2,
        "每周1-3次运动": 1.375,
        "每周3-5次运动": 1.55,
        "每周6-7次运动": 1.725,
        "每天剧烈运动或体力劳动": 1.9
    }
    activity_factor = activity_factors.get(exercise_frequency, 1.2)
    return bmr * activity_factor


# 食物推荐函数
def recommend_foods(user):
    bmr = calculate_bmr(user.age, user.gender, user.height, user.weight)
    daily_energy = calculate_daily_energy(bmr, user.exercise_frequency)

    # 根据健康目标调整营养需求比例
    if user.health_goal == "减脂":
        protein_ratio = 0.4  # 蛋白质占比
        fat_ratio = 0.2  # 脂肪占比
        cho_ratio = 0.4  # 碳水化合物占比
    elif user.health_goal == "增肌":
        protein_ratio = 0.5  # 蛋白质占比
        fat_ratio = 0.25  # 脂肪占比
        cho_ratio = 0.25  # 碳水化合物占比
    else:
        protein_ratio = 0.3  # 蛋白质占比
        fat_ratio = 0.3  # 脂肪占比
        cho_ratio = 0.4  # 碳水化合物占比

    target_protein = (daily_energy * protein_ratio) / 4  # 每克蛋白质提供4kcal能量
    target_fat = (daily_energy * fat_ratio) / 9  # 每克脂肪提供9kcal能量
    target_cho = (daily_energy * cho_ratio) / 4  # 每克碳水化合物提供4kcal能量

    all_foods = Foodinfo.objects.all()
    recommended_foods = defaultdict(list)

    for food in all_foods:
        # 根据过敏信息排除食物
        if user.allergies and any(allergy.strip() in food.Name for allergy in user.allergies.split(",")):
            continue

        # 根据饮食限制排除食物
        if user.dietary_restrictions and any(restriction in food.Type for restriction in user.dietary_restrictions.split(",")):
            continue

        # 计算食物的营养贡献
        edible_weight = 100 * user.Edible  # 假设每次食用100g可食用部分
        protein_contribution = (food.Protein / 100) * edible_weight
        fat_contribution = (food.Fat / 100) * edible_weight
        cho_contribution = (food.CHO / 100) * edible_weight

        # 根据营养需求推荐食物
        if (
            protein_contribution >= (target_protein * 0.1) and  # 满足至少10%的蛋白质需求
            fat_contribution >= (target_fat * 0.1) and  # 满足至少10%的脂肪需求
            cho_contribution >= (target_cho * 0.1)
        ):
            recommended_foods["满足营养需求"].append(food)

        # 根据口味偏好推荐食物
        if user.taste_preference and user.taste_preference in food.Type:
            recommended_foods["符合口味偏好"].append(food)

        # 根据健康状况推荐食物
        if user.health_conditions:
            if "糖尿病" in user.health_conditions and food.CHO < 10:  # 假设低糖食物CHO含量低于10g/100g
                recommended_foods["适合糖尿病患者"].append(food)
            elif "高血压" in user.health_conditions and food.Na < 100:  # 假设低盐食物Na含量低于100mg/100g
                recommended_foods["适合高血压患者"].append(food)

    return recommended_foods