# Generated by Django 3.0 on 2021-10-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('gitlink', models.URLField(max_length=500)),
                ('hostedlink', models.URLField(blank=True, max_length=500)),
            ],
        ),
    ]
