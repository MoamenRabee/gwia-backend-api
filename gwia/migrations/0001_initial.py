# Generated by Django 4.0.6 on 2022-07-18 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('code', models.IntegerField()),
                ('u_id', models.CharField(blank=True, max_length=255)),
                ('token_fcm', models.CharField(blank=True, max_length=255)),
                ('avatar_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PersonMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_username', models.CharField(max_length=50)),
                ('receiver_username', models.CharField(max_length=50)),
                ('sender_code', models.CharField(max_length=50)),
                ('receiver_code', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='media/images/%y/%m/%d/')),
            ],
        ),
    ]
