# Generated by Django 4.2.6 on 2023-12-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_tg_id_user_tg_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tg_id',
            field=models.IntegerField(default=None, null=True, unique=True, verbose_name='ID телеграме'),
        ),
    ]