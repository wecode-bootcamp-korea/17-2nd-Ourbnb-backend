# Generated by Django 3.1.6 on 2021-03-05 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accommodation', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clean_rate', models.DecimalField(decimal_places=1, max_digits=2)),
                ('communication_rate', models.DecimalField(decimal_places=1, max_digits=2)),
                ('checkin_rate', models.DecimalField(decimal_places=1, max_digits=2)),
                ('accuracy_rate', models.DecimalField(decimal_places=1, max_digits=2)),
                ('location_rate', models.DecimalField(decimal_places=1, max_digits=2)),
                ('value_rate', models.DecimalField(decimal_places=1, max_digits=2)),
                ('content', models.TextField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accommodation.accommodation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
    ]
