# Generated by Django 4.0.3 on 2022-04-19 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_question_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='status',
        ),
    ]