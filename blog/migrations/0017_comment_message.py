# Generated by Django 2.2.4 on 2022-01-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20220118_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
