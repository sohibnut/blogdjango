# Generated by Django 4.2.6 on 2023-10-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images/icons/'),
        ),
        migrations.AddField(
            model_name='contact',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]