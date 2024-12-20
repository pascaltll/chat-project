# Generated by Django 4.1.13 on 2024-12-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('room', models.CharField(max_length=50)),
                ('message_content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('profile_pic', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ('date_added',),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
