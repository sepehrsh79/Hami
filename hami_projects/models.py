from django.db import models

objects = [
    ('game', 'بازی'),
    ('book', 'کتاب'),
    ('cosial', 'اجتماعی')
]

city = [
    ('esf', 'اصفهان'),
    ('teh', 'تهران'),
    ('shz', 'شیراز')
]

status = [
    ('enable', 'فعال'),
    ('disable', 'غیر فعال'),
    ('success', 'موفق'),
    ('failed', 'شکست خورده'),
]

class Project (models.Model):
    name = models.CharField(max_length=25,verbose_name='عنوان')
    Groups = models.CharField(max_length=35, choices=objects, verbose_name='دسته بندی')
    discribtion = models.CharField(max_length=250, verbose_name='شرح کامل')
    #creat class for project team
    budget = models.PositiveIntegerField(verbose_name='بودجه مورد نیاز')
    needed_time =  models.PositiveIntegerField(verbose_name='مدت زمان مورد نیاز (روز)')
    #needed time by date
    site = models.CharField(max_length=35, verbose_name='سایت')
    email = models.CharField(max_length=35, verbose_name='ایمیل')
    place = models.CharField(max_length=35, choices=city, verbose_name='محل اجرا') 
    logo = models.ImageField(upload_to=None, blank=True, null=True, verbose_name='عکس کاور')
    status = models.CharField(max_length=35, choices=status, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'

    def __str__(self):
        return self.name


class Reward (models.Model):
    name = models.CharField(max_length=25,verbose_name='عنوان')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='پروژه مرتبط')
    discribtion = models.CharField(max_length=250, verbose_name='شرح پاداش')
    price = models.PositiveIntegerField(verbose_name='هزینه پاداش')
    supports = models.PositiveIntegerField(verbose_name='حمایت ها')

    class Meta:
        verbose_name = 'پاداش'
        verbose_name_plural = 'پاداش ها'

    def __str__(self):
        return self.name

class Comment (models.Model):
    name = models.CharField(max_length=25,verbose_name='نام و نام خانوادگی', blank=True, null=True)
    subject = models.CharField(max_length=25,verbose_name='عنوان', blank=True, null=True)
    message = models.CharField(max_length=250, verbose_name='متن پیام')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='پروژه مرتبط', blank=True, null=True)
    date = models.DateField(verbose_name='تاریخ')

    class Meta:
        verbose_name = 'دیدگاه'
        verbose_name_plural = 'دیدگاه ها'

    def __str__(self):
        return self.name