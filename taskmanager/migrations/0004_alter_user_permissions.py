# Generated by Django 3.2.9 on 2021-11-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_alter_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='permissions',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Normal')]),
        ),
    ]
