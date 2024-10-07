# Generated by Django 4.2.16 on 2024-10-05 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('experience_level', models.CharField(max_length=50)),
                ('skills', models.JSONField()),
                ('preferences', models.JSONField()),
            ],
        ),
    ]
