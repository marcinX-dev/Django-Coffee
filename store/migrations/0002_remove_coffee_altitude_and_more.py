# Generated by Django 5.0.6 on 2025-05-20 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='altitude',
        ),
        migrations.RemoveField(
            model_name='coffee',
            name='country_of_origin',
        ),
        migrations.RemoveField(
            model_name='coffee',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='coffee',
            name='roaster',
        ),
        migrations.RemoveField(
            model_name='coffee',
            name='variety',
        ),
    ]
