# Generated by Django 4.1.3 on 2023-01-15 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_managers_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.CharField(max_length=11),
        ),
    ]
