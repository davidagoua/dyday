# Generated by Django 2.2.1 on 2019-07-14 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0006_auto_20190705_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-time']},
        ),
    ]