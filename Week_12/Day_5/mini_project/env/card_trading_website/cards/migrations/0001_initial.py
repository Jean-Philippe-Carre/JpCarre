# Generated by Django 5.0.7 on 2024-08-01 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('amount_of_money', models.IntegerField(default=1000)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_character', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
                ('date_of_birth', models.DateTimeField(null=True)),
                ('patronus', models.CharField(max_length=100)),
                ('price', models.IntegerField(verbose_name=252)),
                ('xp_points', models.IntegerField(verbose_name=5)),
                ('current_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_cards', to='cards.user')),
                ('previous_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_cards', to='cards.user')),
            ],
        ),
    ]
