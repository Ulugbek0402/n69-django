from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Sarlavha')
    content = models.TextField(blank=True, null=True, verbose_name='Text')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    bool = models.BooleanField(default=False, verbose_name='Bool')
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category')

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = 'News'
    #     verbose_name_plural = 'News'
    #     ordering = ['-created']



