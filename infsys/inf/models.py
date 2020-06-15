from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

def image_folder(instance, filename):
    filename = instance.slug + '.' + filename#.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)

#def image_folder(instance, filename):
#    filename = instance.slug + '.' + filename#.split('.')[1]
#    return "{0}/{1}".format(instance.slug, filename)
# Create your models here.
#class Weapon_image(models.Model):
#    weapon_image_name = models.CharField(max_length=150, verbose_name="Название изображения", blank=True)
##    weapon_image_description = models.CharField(max_length=300, verbose_name="Описание изображения", blank=True)    
##    image = models.ImageField(upload_to=image_folder, verbose_name="Загрузите изображение")
#    slug = models.SlugField(max_length=150, unique=True, blank=True)
#    class Meta:
#        verbose_name = 'Общее изображение оружия'
#        verbose_name_plural = 'Общее изображение оружия'
#
#    def __str__(self):
#        return '{}'.format(self.weapon_image_name)
#
#    def save(self, *args, **kwargs):
#        if not self.id:
#            self.slug = gen_slug(self.weapon_image_name)
#        super().save(*args, **kwargs)

#class Weapon_special_image(models.Model):
#    name = models.CharField(max_length=150, verbose_name="Название изображения", blank=True)
#    image = models.ImageField(upload_to=image_folder, verbose_name="Загрузите изображение")
#    class Meta:
#        verbose_name = 'Специальное изображение оружия'
#        verbose_name_plural = 'Специальное изображение оружия'
#
#    def __str__(self):
#        return '{}'.format(self.name)
#
#class Trace_pattern_sleev_image(models.Model):
#    name = models.CharField(max_length=150, verbose_name="Название изображения", blank=True)
#    image = models.ImageField(upload_to=image_folder, verbose_name="Загрузите изображение")
#    class Meta:
#        verbose_name = 'Изображение следообразующих деталей оружия'
#        verbose_name_plural = 'Изображение следообразующих деталей оружия'
#
#    def __str__(self):
#        return '{}'.format(self.name)

class Weapon(models.Model):
    #основные характеристики
    name = models.CharField(max_length=150, db_index=True, verbose_name="Название оружия", blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, verbose_name="Введите название на английском")
    producer = models.CharField(max_length=100, verbose_name="Производитель", blank=True)
    image = models.ImageField(upload_to='', blank=True, verbose_name="Изображение оружия")
    length = models.DecimalField(verbose_name="Длина, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    height = models.DecimalField(verbose_name="Высота, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    width = models.DecimalField(verbose_name="Ширина, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    barrel_length = models.DecimalField(verbose_name="Длина ствола, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    mass = models.DecimalField(verbose_name="Масса, г", blank=True, default=0, max_digits=15, decimal_places=10)
    description = models.TextField(blank=True, verbose_name="Описание")
    caliber = models.CharField(blank=True, max_length=150, db_index=True, verbose_name="Калибр")

    #характеристики следообразующих деталей
    method_manufacture_barrel = models.TextField(verbose_name="Способ изготовления ствола", blank=True)
    number_rifling = models.DecimalField(verbose_name="Количество нарезов", default=0, blank=True, max_digits=15, decimal_places=10)
    direction_rifling = models.CharField(max_length=100, verbose_name="Направление нарезов", blank=True)
    width_fields_rifling = models.DecimalField(verbose_name="Ширина полей нарезов, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    angle_rifling = models.DecimalField(verbose_name="Угол наклона нарезов", blank=True, default=0, max_digits=15, decimal_places=10)
    gas_outlet = models.TextField(verbose_name="Наличае газоотводного отверстия в канале ствола", blank=True) 
    strikers_diameter = models.DecimalField(verbose_name="Диаметр бойка, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    width_hook_extractor = models.DecimalField(verbose_name="Ширина зацепа выбрасывателя, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    angle_between_hook_reflector = models.DecimalField(verbose_name="Угол между зацепом выбрасывателя и отражателем", default=0, blank=True, max_digits=15, decimal_places=10)
    chamber_shape = models.CharField(max_length=200, verbose_name="Форма патронника", blank=True)
    chamber_length = models.DecimalField(verbose_name="Длина патронника, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    tfp_im1 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Изображение следообразующих деталей №1\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    tfp_im2 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Изображение следообразующих деталей №2\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    tfp_im3 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Изображение следообразующих деталей №3\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    tfp_im4 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Изображение следообразующих деталей №4\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")


    # технические характеристики
    sleeves_reflection = models.TextField(verbose_name="Отражение гильзы", blank=True)
    automation_principle = models.TextField(verbose_name="Принцип отражателя", blank=True)
    locking_mech = models.TextField(verbose_name="Механизм запирания ствола", blank=True)
    trigger_mech = models.TextField(verbose_name="Ударно-спусковой механизм", blank=True)
    safety_catch = models.TextField(verbose_name="Предохранитель", blank=True)
    liner_removal_mech = models.TextField(verbose_name="Механиз удаления гильзы", blank=True)
    ammos = models.ManyToManyField('Ammo', blank=True, related_name='weapons', verbose_name='Используемые боеприпасы')
    magazine = models.TextField(verbose_name="Магазин", blank=True)
    magazines_capacity = models.DecimalField(verbose_name="Ёмкость магазина, патронов", blank=True, default=0, max_digits=15, decimal_places=10)

    #маркировочные обозначенния 
    marking_designation_description = models.TextField(verbose_name="Маркировочные обозначения (описание)", blank=True)
    location_details = models.TextField(verbose_name="Расположение на деталях оружия", blank=True)
    marking_image = models.ImageField(upload_to=image_folder, null=True, blank=True, verbose_name="Изображение маркировочных значений")

    #иные сведения
    disassembly_procedure = models.TextField(verbose_name="Порядок неполной сборки и разборки", blank=True)
    features = models.TextField(verbose_name="Технические и иные особенности, характерные для этой модели", blank=True)
    add_images1 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Дополнительное изображение №1\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    add_images2 = models.ImageField(upload_to=image_folder, 
    verbose_name="Дополнительное изображение №2\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    add_images3 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Дополнительное изображение №3\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    add_images4 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Дополнительное изображение №5\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    add_images5 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Дополнительное изображение №5\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    add_images6 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Дополнительное изображение №6\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    
    def get_absolute_url(self):
        return reverse('weapon_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse('weapon_update_url', kwargs={'slug': self.slug})
    
    def get_del_url(self):
        return reverse('weapon_del_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.name) #можно исправить на return self.name

    class Meta:
        ordering = ['-caliber']
        verbose_name = 'Оружие'
        verbose_name_plural = 'Оружие'

#class Ammo_image(models.Model):
#    ammo_image_name = models.CharField(max_length=150, verbose_name="Название изображения", blank=True)
#    ammo_image_description = models.CharField(max_length=300, verbose_name="Описание изображения")
#    ammo_image = models.ImageField(upload_to=image_folder, verbose_name="Загрузите изображение")
#
#    class Meta:
#        verbose_name = 'Общее изображение патрона'
#        verbose_name_plural = 'Общее изображение патрона'
#
#    def __str__(self):
#        return '{}'.format(self.ammo_image_name)

#class Ammo_special_image(models.Model):
#    name = models.CharField(max_length=150, verbose_name="Название изображения", blank=True)
#    image = models.ImageField(upload_to=image_folder, verbose_name="Загрузите изображение")
#    class Meta:
#        verbose_name = 'Специальное изображение патрона'
#        verbose_name_plural = 'Специальное изображение патрона'
#
#    def __str__(self):
#        return '{}'.format(self.name)
#
#class Markings_image(models.Model):
#    name = models.CharField(max_length=150, verbose_name="Название изображения", blank=True)
#    image = models.ImageField(upload_to=image_folder, verbose_name="Загрузите изображение")
#    class Meta:
#        verbose_name = 'Специальное изображение патрона'
#        verbose_name_plural = 'Специальное изображение патрона'
#
#    def __str__(self):
#        return '{}'.format(self.name)

class Ammo(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название", blank=True)
    caliber = models.CharField(max_length=50, blank=True, db_index=True, verbose_name="Калибр")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="Введите название на английском")
    image = models.ImageField(upload_to=image_folder, blank=True, verbose_name="Изображение боеприпаса")
    producer = models.CharField(max_length=100, verbose_name="Производитель", blank=True)
    length = models.DecimalField(verbose_name="Длина, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    mass = models.DecimalField(blank=True, verbose_name="Масса патрона, г", default=0, max_digits=15, decimal_places=10)
    powder_mass = models.DecimalField(verbose_name="Масса порохового (иного) заряда, г", blank=True, default=0, max_digits=15, decimal_places=10)
    ignition_type = models.CharField(max_length=160, verbose_name="Тип воспламенитиля", blank=True)
    mounting_method = models.CharField(max_length=160, verbose_name="Способ крепления пули с гильзой", blank=True)

#, default=0
    #характеристики гильзы
    shell_length = models.DecimalField(verbose_name="Длина гильзы, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    diameter_dults = models.DecimalField(verbose_name="Диаметр дульца, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    diameter_case_slope = models.DecimalField(verbose_name="Диаметр корпуса у ската, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    case_diameter_bottom = models.DecimalField(verbose_name="Диаметр корпуса у донного упора, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    bottom_diameter = models.DecimalField(verbose_name="Диаметр донного упора, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    flange_diameter = models.DecimalField(verbose_name="Диаметр фланца, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    form = models.TextField(verbose_name="Форма", blank=True)
    material_color = models.CharField(max_length=150, verbose_name="Цвет материала", blank=True)
    
    #характеристики капсуля
    capsule_type = models.CharField(max_length=150, verbose_name="Тип капсуля", blank=True)
    capsule_material_color = models.CharField(max_length=80, verbose_name="Цвет материала капсюля", blank=True)
    diameter = models.DecimalField(verbose_name="Диаметр капсуля, мм", blank=True, default=0, max_digits=15, decimal_places=10)

    #характеристики пули
    head_part_form = models.DecimalField(verbose_name="Длина головной части, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    bullet_length = models.DecimalField(verbose_name="Длина пули, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    diameter_head_part = models.DecimalField(verbose_name="Диаметр ведущей части, мм", blank=True, default=0, max_digits=15, decimal_places=10)
    bullet_mass = models.DecimalField(verbose_name="Масса пули, г", blank=True, default=0, max_digits=15, decimal_places=10)
    bullet_type = models.CharField(max_length=150, verbose_name="Тип пули", blank=True)

    #маркировочные обозначения
    markings = models.TextField(verbose_name="Маркировочное обозначение (описание)", blank=True)
    markings_image1 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Изображение маркировочных обозначений №1\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    markings_image2 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Изображение маркировочных обозначений №2\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    markings_image3 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Изображение маркировочных обозначений №3\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    
    
    #иные сведения
    common_view_ammo = models.ImageField(upload_to=image_folder, blank=True, verbose_name="Изображение общего вида патрона")
    common_view_bullet = models.ImageField(upload_to=image_folder, blank=True, verbose_name="Общее изображение пули")
    pack_common_view = models.ImageField(upload_to=image_folder, blank=True, verbose_name="Изображение упаковки")
    add_images1 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Дополнительное изображение №1\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    add_images2 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Дополнительное изображение №2\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    add_images3 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Дополнительное изображение №3\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    add_images4 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Дополнительное изображение №5\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    add_images5 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Дополнительное изображение №5\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    add_images6 = models.ImageField(upload_to=image_folder, blank=True,
    verbose_name="Дополнительное изображение №6\nЕсди нет подходящего изображения, то\nобязательно поставте любое изображение на ваш выбор")
    #weapons = models.ManyToManyField('Weapon', blank=True, related_name='ammos', verbose_name='Оружие под этот боеприпас')

    class Meta:
        ordering = ['-caliber']
        verbose_name = 'Патроны'
        verbose_name_plural = 'Патроны'

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ammo_detail_url', kwargs={'slug': self.slug})
    
    def get_update_url(self):
        return reverse('ammo_update_url', kwargs={'slug': self.slug})

    def get_del_url(self):
        return reverse('ammo_del_url', kwargs={'slug': self.slug})

