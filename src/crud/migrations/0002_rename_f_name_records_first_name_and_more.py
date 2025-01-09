# Generated by Django 5.1.4 on 2025-01-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='records',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='records',
            name='l_name',
        ),
        migrations.AddField(
            model_name='records',
            name='last_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]