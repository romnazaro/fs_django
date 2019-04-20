from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField('Название', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField('Тег', max_length=50)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE)

    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True)

    title = models.CharField(
        'Заголовок',
        max_length=120)

    text_min = models.TextField(
        'Превью',
        max_length=350)

    text = models.TextField('Текст')
    tag = models.ManyToManyField(Tag, verbose_name='Теги')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    description = models.CharField('Описание', max_length=100)
    keywords = models.CharField('Ключевые слова', max_length=50)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE)

    post = models.ForeignKey(
        Post,
        verbose_name='Пост',
        on_delete=models.CASCADE)

    text = models.TextField('Комментарий')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        null=True)
    moderation = models.BooleanField('Модерация', default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return '{}'.format(self.user)
