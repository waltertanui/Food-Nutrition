from django.db import models

# Create your models here.
class  Foodinfo(models.Model):
    id=models.AutoField('id',primary_key=True)
    Name=models.CharField('食物名称',max_length=255,default='')
    Type = models.CharField('食物类型', max_length=255, default='')
    Edible = models.CharField('可食用部分', max_length=255, default='')
    Water = models.CharField('水分', max_length=255, default='')
    Energy = models.CharField('能量', max_length=255, default='')
    Protein = models.CharField('蛋白质', max_length=255, default='')
    Fat = models.CharField('脂肪', max_length=255, default='')
    Cholesterol = models.CharField('胆固醇', max_length=255, default='')
    Ash = models.CharField('灰分', max_length=255, default='')
    CHO = models.CharField('碳水化合物', max_length=255, default='')
    DietaryFiber = models.CharField(' 总膳食纤维', max_length=255, default='')
    Carotene = models.CharField('胡萝卜素', max_length=255, default='')
    Vitamin = models.CharField('维生素A', max_length=255, default='')
    α_TE = models.CharField('α - 生育酚当量', max_length=255, default='')
    Thiamin = models.CharField('硫胺素', max_length=255, default='')
    Riboflavin = models.CharField('核黄素', max_length=255, default='')
    Niacin = models.CharField('烟酸', max_length=255, default='')
    VitaminC = models.CharField('维生素 C', max_length=255, default='')
    Ca = models.CharField('钙', max_length=255, default='')
    P = models.CharField('磷', max_length=255, default='')
    K = models.CharField('钾', max_length=255, default='')
    Na = models.CharField('钠', max_length=255, default='')
    Mg = models.CharField('镁', max_length=255, default='')
    Fe = models.CharField('铁', max_length=255, default='')
    Zn = models.CharField('锌', max_length=255, default='')
    Se = models.CharField('硒', max_length=255, default='')
    Cu = models.CharField('铜', max_length=255, default='')
    Mn = models.CharField('锰', max_length=255, default='')
    I = models.CharField('碘', max_length=255, default='')
    SFA = models.CharField('饱和脂肪酸', max_length=255, default='')
    MUFA = models.CharField('单不饱和脂肪酸', max_length=255, default='')
    PUFA = models.CharField('多不饱和脂肪酸', max_length=255, default='')
    TotalFattyAcids = models.CharField('总脂肪酸', max_length=255, default='')
    class Meta:
        db_table="foodinfo"


class  User(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField('用户名', max_length=255, null=False, blank=False)  # 添加用户名的字段
    password = models.CharField('密码', max_length=255, null=False, blank=False)
    avatar= models.FileField('用户头像',upload_to="avatar",default="avatar/default.jpg",null=True,blank=True)
    #健康信息
    age = models.IntegerField('年龄', null=True, blank=True)
    gender = models.CharField('性别', max_length=10, null=True, blank=True)
    height = models.FloatField('身高（cm）', null=True, blank=True)
    weight = models.FloatField('体重（kg）', null=True, blank=True)
    allergies = models.TextField('过敏信息', null=True, blank=True)
    health_conditions = models.TextField('健康状况', null=True, blank=True)
    preferred_foods = models.TextField('偏好食物', null=True, blank=True)
    dietary_restrictions = models.TextField('饮食限制', null=True, blank=True)
    taste_preference = models.CharField('口味偏好', max_length=255, null=True, blank=True)
    exercise_frequency = models.CharField('运动频率', max_length=255, null=True, blank=True)
    sleep_hours = models.IntegerField('睡眠时间（小时）', null=True, blank=True)
    health_goal = models.CharField('健康目标', max_length=255, null=True, blank=True)
    class Meta:
        db_table="user"