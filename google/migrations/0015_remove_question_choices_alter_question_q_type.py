# Generated by Django 4.0.2 on 2022-02-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0014_choice_question_alter_question_q_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.IntegerField(choices=[(1, 'پاراگراف'), (0, 'کوتاه'), (3, 'چندگزینه ای'), (2, 'انتخابی')], default=0, verbose_name='نوع سوال'),
        ),
    ]
