# Generated by Django 4.0.3 on 2022-04-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='creator',
        ),
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]