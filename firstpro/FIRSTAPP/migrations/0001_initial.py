# Generated by Django 5.0 on 2024-01-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('gmail', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('confrmpassword', models.CharField(max_length=100)),
            ],
        ),
    ]
