# Generated by Django 2.0.4 on 2018-04-07 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_articles_cate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='first_cate',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='second_cate',
        ),
    ]
