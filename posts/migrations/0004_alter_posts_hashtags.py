# Generated by Django 4.1.6 on 2023-02-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_hashtag_posts_hashtags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='posts.hashtag'),
        ),
    ]
