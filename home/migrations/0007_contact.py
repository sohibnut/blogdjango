# Generated by Django 4.2.6 on 2023-10-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]