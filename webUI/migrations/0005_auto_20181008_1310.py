# Generated by Django 2.0.7 on 2018-10-08 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webUI', '0004_auto_20181008_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='choice',
            new_name='choices',
        ),
    ]
