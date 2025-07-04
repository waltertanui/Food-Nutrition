# Generated by Django 3.0.1 on 2025-04-09 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foodinfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('Name', models.CharField(default='', max_length=255, verbose_name='食物名称')),
                ('Type', models.CharField(default='', max_length=255, verbose_name='食物类型')),
                ('Edible', models.CharField(default='', max_length=255, verbose_name='可食用部分')),
                ('Water', models.CharField(default='', max_length=255, verbose_name='水分')),
                ('Energy', models.CharField(default='', max_length=255, verbose_name='能量')),
                ('Protein', models.CharField(default='', max_length=255, verbose_name='蛋白质')),
                ('Fat', models.CharField(default='', max_length=255, verbose_name='脂肪')),
                ('Cholesterol', models.CharField(default='', max_length=255, verbose_name='胆固醇')),
                ('Ash', models.CharField(default='', max_length=255, verbose_name='灰分')),
                ('CHO', models.CharField(default='', max_length=255, verbose_name='碳水化合物')),
                ('DietaryFiber', models.CharField(default='', max_length=255, verbose_name=' 总膳食纤维')),
                ('Carotene', models.CharField(default='', max_length=255, verbose_name='胡萝卜素')),
                ('Vitamin', models.CharField(default='', max_length=255, verbose_name='维生素A')),
                ('α_TE', models.CharField(default='', max_length=255, verbose_name='α - 生育酚当量')),
                ('Thiamin', models.CharField(default='', max_length=255, verbose_name='硫胺素')),
                ('Riboflavin', models.CharField(default='', max_length=255, verbose_name='核黄素')),
                ('Niacin', models.CharField(default='', max_length=255, verbose_name='烟酸')),
                ('VitaminC', models.CharField(default='', max_length=255, verbose_name='维生素 C')),
                ('Ca', models.CharField(default='', max_length=255, verbose_name='钙')),
                ('P', models.CharField(default='', max_length=255, verbose_name='磷')),
                ('K', models.CharField(default='', max_length=255, verbose_name='钾')),
                ('Na', models.CharField(default='', max_length=255, verbose_name='钠')),
                ('Mg', models.CharField(default='', max_length=255, verbose_name='镁')),
                ('Fe', models.CharField(default='', max_length=255, verbose_name='铁')),
                ('Zn', models.CharField(default='', max_length=255, verbose_name='锌')),
                ('Se', models.CharField(default='', max_length=255, verbose_name='硒')),
                ('Cu', models.CharField(default='', max_length=255, verbose_name='铜')),
                ('Mn', models.CharField(default='', max_length=255, verbose_name='锰')),
                ('I', models.CharField(default='', max_length=255, verbose_name='碘')),
                ('SFA', models.CharField(default='', max_length=255, verbose_name='饱和脂肪酸')),
                ('MUFA', models.CharField(default='', max_length=255, verbose_name='单不饱和脂肪酸')),
                ('PUFA', models.CharField(default='', max_length=255, verbose_name='多不饱和脂肪酸')),
                ('TotalFattyAcids', models.CharField(default='', max_length=255, verbose_name='总脂肪酸')),
            ],
            options={
                'db_table': 'foodInfo',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=255, verbose_name='用户名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('avatar', models.FileField(default='avatar/default.jpg', upload_to='avatar', verbose_name='用户头像')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('gender', models.CharField(blank=True, max_length=10, null=True, verbose_name='性别')),
                ('height', models.FloatField(blank=True, null=True, verbose_name='身高（cm）')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='体重（kg）')),
                ('allergies', models.TextField(blank=True, null=True, verbose_name='过敏信息')),
                ('health_conditions', models.TextField(blank=True, null=True, verbose_name='健康状况')),
                ('preferred_foods', models.TextField(blank=True, null=True, verbose_name='偏好食物')),
                ('dietary_restrictions', models.TextField(blank=True, null=True, verbose_name='饮食限制')),
                ('taste_preference', models.CharField(blank=True, max_length=255, null=True, verbose_name='口味偏好')),
                ('exercise_frequency', models.CharField(blank=True, max_length=255, null=True, verbose_name='运动频率')),
                ('sleep_hours', models.IntegerField(blank=True, null=True, verbose_name='睡眠时间（小时）')),
                ('health_goal', models.CharField(blank=True, max_length=255, null=True, verbose_name='健康目标')),
                ('signup_time', models.DateTimeField(blank=True, null=True, verbose_name='注册时间')),
                ('signup_location', models.CharField(blank=True, max_length=100, null=True, verbose_name='注册地点')),
                ('last_login_time', models.DateTimeField(blank=True, null=True, verbose_name='最近登录时间')),
                ('last_login_location', models.CharField(blank=True, max_length=100, null=True, verbose_name='最近登录地点')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
