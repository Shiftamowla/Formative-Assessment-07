# Generated by Django 5.1.1 on 2024-10-01 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_custom_user_gender_custom_user_city_custom_user_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='Gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=100, null=True),
        ),
    ]
