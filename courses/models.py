from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string
from django.db import models

from .fields import OrderField


class Subject(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', verbose_name='Создатель курса',
                              on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', verbose_name='Предмет',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Заголовок курса')
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField(verbose_name='Обзор курса')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    students = models.ManyToManyField(User, related_name='courses_joined',
                                      blank=True, verbose_name='Привязанные студенты')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', verbose_name='Курс',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание(необязательно)')
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)


class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', verbose_name='Модуль', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ('text',
                                                                                                            'video',
                                                                                                            'image',
                                                                                                            'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', verbose_name='Владелец', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        self.title

    def render(self):
        return render_to_string('courses/content/{}.html'.format(
            self._meta.model_name), {'item': self})


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()
