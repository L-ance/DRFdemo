from django.db import models

# Create your models here.


class Tag(models.Model):
    tag_type_choices = ((0, "用户注册标签"), (1, "文章标签"), )
    tag_type = models.SmallIntegerField(choices=tag_type_choices, default=0, verbose_name="标签类型")
    name = models.CharField(verbose_name="名称", max_length=18)
    order = models.SmallIntegerField(verbose_name="用于排序字段", default=0)
    date = models.DateTimeField(auto_now_add=True)


class Article(models.Model):

    title = models.CharField(max_length=128, )
    img = models.CharField(max_length=255, )
    tags = models.ManyToManyField("Tag", limit_choices_to={"tag_type": 1})


class Comment(models.Model):

    parent = models.ForeignKey("self", null=True, blank=True)
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)
