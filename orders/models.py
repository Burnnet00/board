from django.db import models
from django.utils.html import mark_safe


class Product(models.Model):
    name = models.CharField('Назва', max_length=150)
    image = models.ImageField('Світлина', upload_to='image/%Y', null=True)
    description = models.TextField('Опис')
    price = models.DecimalField('Ціна', max_digits=7, decimal_places=2, null=True)
    date = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    # def image_tag(self):
    #     return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))
    #
    # image_tag.short_description = 'Image'

