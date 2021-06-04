from django.db import models

city = [
    ('esf', 'اصفهان'),
    ('teh', 'تهران'),
    ('shz', 'شیراز')
]

status = [
    ('enable', 'فعال'),
    ('disable', 'غیر فعال'),
    
]

class ProjectManager(models.Manager):

    def get_by_id(self, project_id):
        qs = self.get_queryset().filter(id=project_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_by_groups(self, group_name):
        return self.get_queryset().filter(Groups__slug__iexact=group_name)

class Group (models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    slug = models.CharField(max_length=120, verbose_name='عنوان مدیریتی', null=True, blank=True)
    discribtion = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=None, blank=True, null=True, verbose_name='عکس ')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class Project (models.Model):
    name = models.CharField(max_length=25,verbose_name='عنوان مدیریتی', blank=True, null=True)
    name_show = models.CharField(max_length=25,verbose_name='عنوان قابل نمایش')
    Groups = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='دسته بندی')
    discribtion = models.TextField(max_length=250, verbose_name='شرح مدیریتی',  blank=True, null=True,)
    discribtion_show = models.TextField(max_length=250, verbose_name='شرح قابل نمایش')
    order = models.IntegerField(verbose_name='وزن', blank=True, null=True)
    budget = models.PositiveIntegerField(verbose_name='مبلغ مورد نیاز')
    Currentـbudget = models.PositiveIntegerField(verbose_name='مبلغ جمع شده', blank=True, null=True, default=0)
    needed_time =  models.DateField(verbose_name='مدت زمان مورد نیاز ')
    site = models.CharField(max_length=35, verbose_name='سایت')
    email = models.CharField(max_length=35, verbose_name='ایمیل')
    logo = models.ImageField(upload_to=None, blank=True, null=True, verbose_name='عکس کاور')
    status = models.CharField(max_length=35, choices=status, verbose_name='وضعیت', default='disable')
    
    objects = ProjectManager()


    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'

    def __str__(self):
        return self.name_show

    def sponsors(self):
        return str(self.sponsor_set.count())

    def percent(self):
        return ((self.Currentـbudget * 100)/self.budget)
    
    def get_absolute_url(self):
        return f"/projects/{self.id}"


#maybe we dont need
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




