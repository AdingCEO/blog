# Generated by Django 2.2.4 on 2022-01-13 11:23

import blog.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20220113_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(2, '2글자 이상 적어줘잉'), blog.validators.validate_symbols]),
        ),
    ]
