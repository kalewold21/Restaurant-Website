# Generated by Django 3.0.5 on 2021-03-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='facebookLink',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='footer',
            name='footerBody',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='footer',
            name='instagramLink',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='footer',
            name='linkedinLink',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='footer',
            name='twitterLink',
            field=models.TextField(max_length=100),
        ),
    ]
