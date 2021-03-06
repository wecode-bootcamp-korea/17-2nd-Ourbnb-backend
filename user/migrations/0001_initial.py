# Generated by Django 3.1.6 on 2021-03-05 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialPlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'social_platforms',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('profile_image', models.URLField(max_length=2000)),
                ('date_of_birth', models.DateField(null=True)),
                ('social_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.socialplatform')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
