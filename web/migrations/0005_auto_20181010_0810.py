# Generated by Django 2.0.6 on 2018-10-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_userprofile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, to='web.UserGroup'),
        ),
    ]
