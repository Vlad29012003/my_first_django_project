from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False,verbose_name='Заголовок')
    text = models.TextField(max_length=3000, null=False, blank=False,verbose_name='Текст')
    author = models.CharField(max_length=40, null=False, blank=False,default='Unknown', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Времясоздания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Времяизменения')
def __str__(self):
    return "{}. {}".format(self.pk, self.title)
