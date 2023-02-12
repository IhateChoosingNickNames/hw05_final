# Generated by Django 2.2.16 on 2022-11-09 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_auto_20221109_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='post',
            field=models.ForeignKey(help_text='Пост, которому ставят лайк/дизлайк', on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.Post', verbose_name='Лайк поста'),
        ),
    ]
