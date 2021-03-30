# Generated by Django 3.0.5 on 2021-03-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_whyus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footerTitle', models.CharField(max_length=100)),
                ('footerBody', models.CharField(max_length=100)),
                ('twitterLink', models.TextField()),
                ('facebookLink', models.TextField()),
                ('instagramLink', models.TextField()),
                ('linkedinLink', models.TextField()),
            ],
        ),
    ]