# Generated by Django 3.0.5 on 2020-04-04 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_friendsanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]
