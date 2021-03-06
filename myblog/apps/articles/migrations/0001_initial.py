# Generated by Django 2.0.1 on 2018-07-14 13:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('click_nums', models.IntegerField(default=0, verbose_name='查看数量')),
                ('image', models.ImageField(default='/static/image/4.ipg', upload_to='static/image/%Y/%m', verbose_name='文章图片')),
                ('mean', models.CharField(choices=[('生活百态', '生活'), ('零一世界', '编程')], default='零一的世界', max_length=10, verbose_name='文章类别')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='文章作者')),
            ],
            options={
                'verbose_name': '文章内容',
                'verbose_name_plural': '文章内容',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='分类名称')),
                ('categroy_num', models.IntegerField(default=0, verbose_name='分类数量')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Category', to_field='name', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='articles',
            name='tags',
            field=models.ManyToManyField(blank=True, to='articles.Tag', verbose_name='文章标签'),
        ),
    ]
