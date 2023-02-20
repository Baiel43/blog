# Generated by Django 4.1.6 on 2023-02-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_posts_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='hashtags',
            field=models.ManyToManyField(to='posts.hashtag'),
        ),
    ]
