# Generated by Django 4.0.2 on 2022-02-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0009_alter_question_choices_alter_question_q_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choices',
            new_name='Choice',
        ),
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.IntegerField(choices=[(0, 'کوتاه'), (1, 'پاراگراف'), (2, 'انتخابی'), (3, 'چندگزینه ای')], default=0, verbose_name='نوع سوال'),
        ),
    ]
