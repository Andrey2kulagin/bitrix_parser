# Generated by Django 4.2 on 2023-04-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0003_alter_user_end_of_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата активации подписки'),
        ),
    ]
