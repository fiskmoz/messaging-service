# Generated by Django 2.1.3 on 2019-03-20 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Date',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
        ),
    ]
