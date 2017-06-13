from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'关联Django内的用户类')
    name = models.CharField(max_length=32, verbose_name=u'昵称')
    signature = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'签名')
    head_img = models.ImageField(blank=True, null=True, verbose_name=u'头像', upload_to='img')
    friends = models.ManyToManyField('self', related_name='my_friends', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'用户表'
        verbose_name_plural = u'用户表'


class WebGroup(models.Model):
    name = models.CharField(max_length=64)
    brief = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(UserProfile)
    admins = models.ManyToManyField(UserProfile, blank=True,  related_name='group_admin')
    menbers = models.ManyToManyField(UserProfile, blank=True,  related_name='group_members')
    max_members = models.IntegerField(default=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'聊天组'
        verbose_name_plural = u'聊天组'


class Column(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'分类')
    intro = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = u'分类'
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to='img', blank=True, null=True)
    columns = models.ForeignKey(Column)
    author = models.OneToOneField(UserProfile)
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    last_modify = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=255, verbose_name=u'内容')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, null=True)
    article = models.ForeignKey(Article, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content










