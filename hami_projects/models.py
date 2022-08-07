from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q

status = [
    ('enable', 'فعال'),
    ('disable', 'غیر فعال'),
]

project_status = [
    ('enable', 'در حال اجرا'),
    ('disable', 'پایان یافته'),
    ('notshow', 'غیر فعال')
]


class ProjectManager(models.Manager):
    def get_by_category_id(self, category_id):
        return self.get_queryset().filter(project_category__id=category_id)

    def search(self, query):
        lookup = (Q(name_show__icontains=query) | Q(description_show__icontains=query))
        lookup_status = (Q(status='enable') | Q(status='disable'))

        return self.get_queryset().filter(lookup, lookup_status).distinct()


class ProjectCategory(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='عنوان')
    slug = models.CharField(max_length=120, verbose_name='عنوان مدیریتی', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=None, blank=True, null=True, verbose_name='عکس ')

    def __str__(self):
        return self.title or " "

    def project_count(self):
        return (self.project_set.count())

    def completed_project_count(self):
        return (self.project_set.filter(status='disable').count())

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Project(models.Model):
    name = models.CharField(max_length=25, verbose_name='عنوان مدیریتی', blank=True, null=True)
    name_show = models.CharField(max_length=25, verbose_name='عنوان قابل نمایش')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='صاحب پروژه', blank=True, null=True)
    project_category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, verbose_name='دسته بندی')
    description = models.TextField(max_length=250, verbose_name='شرح مدیریتی', blank=True, default=0)
    description_show = models.TextField(max_length=250, verbose_name='شرح قابل نمایش')
    budget = models.PositiveIntegerField(verbose_name='مبلغ مورد نیاز')
    current_budget = models.PositiveIntegerField(verbose_name='مبلغ جمع شده', blank=True, null=True, default=0)
    needed_time = models.DateField(verbose_name='مدت زمان مورد نیاز')
    site = models.CharField(max_length=35, verbose_name='سایت')
    email = models.CharField(max_length=35, verbose_name='ایمیل')
    logo = models.ImageField(upload_to=None, blank=True, null=True, verbose_name='عکس کاور')
    status = models.CharField(max_length=35, choices=project_status, verbose_name='وضعیت', default='disable')
    
    objects = ProjectManager()

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'

    def __str__(self):
        return self.name_show or " "

    def supports(self):
        return str(self.support_set.count())

    def support_fullname(self):
        return self.creator.get_full_name()

    def percent(self):
        convert_to_percent = (int((self.current_budget * 100)/self.budget))
        if convert_to_percent > 100:
            return 100
        else:
            return convert_to_percent

    def get_absolute_url(self):
        return f"/projects/{self.id}"


class Comment(models.Model):
    name = models.CharField(max_length=25, verbose_name='نام و نام خانوادگی', blank=True, null=True)
    subject = models.CharField(max_length=25, verbose_name='عنوان', blank=True, null=True)
    message = models.CharField(max_length=250, verbose_name='متن پیام')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='پروژه مرتبط', blank=True, null=True)
    date = models.DateField(verbose_name='تاریخ')
    status = models.CharField(max_length=35, choices=status, verbose_name='وضعیت', default='disable')

    class Meta:
        verbose_name = 'دیدگاه'
        verbose_name_plural = 'دیدگاه ها'

    def __str__(self):
        return self.name or " "




