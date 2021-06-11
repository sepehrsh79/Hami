from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to='', null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title or " " 
    