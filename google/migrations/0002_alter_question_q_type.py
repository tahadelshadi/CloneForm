# Generated by Django 4.0.2 on 2022-02-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.IntegerField(choices=[(2, 'نتخابی'), (1, 'پاسخ تشریحی'), (0, 'چهارگزینه ای')], default=0, verbose_name='نوع سوال'),
        ),
    ]