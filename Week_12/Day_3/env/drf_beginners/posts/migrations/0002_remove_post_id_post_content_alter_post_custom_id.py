# Generated by Django 5.0.7 on 2024-07-31 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='post',
            name='custom_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]