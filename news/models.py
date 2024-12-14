from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField('Категория', max_length=50)

    def __str__(self):
        return self.title


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField('Название', max_length=50)
    content = models.TextField('Контент', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    update_at = models.DateTimeField('Дата изменение', auto_now=True)
    photo = models.ImageField('Фото', upload_to='media/')
    is_publish = models.BooleanField('Публиковать')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', null=True)

    def __str__(self):
        return self.title
    

