# Generated by Django 2.1.7 on 2019-04-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='star',
            field=models.CharField(max_length=20),
        ),
    ]
