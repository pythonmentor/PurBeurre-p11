# Generated by Django 2.1.3 on 2018-12-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]