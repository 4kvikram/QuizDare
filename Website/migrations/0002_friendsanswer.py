# Generated by Django 3.0.5 on 2020-04-02 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendsAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('Register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Website.Register')),
            ],
        ),
    ]
