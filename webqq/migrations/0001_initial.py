# Generated by Django 2.0.6 on 2018-09-21 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0004_userprofile_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='QQGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('brief', models.TextField(max_length=1024)),
                ('member_limit', models.IntegerField(default=200)),
                ('admin', models.ManyToManyField(related_name='group_admin', to='web.UserProfile')),
                ('founder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserProfile')),
                ('members', models.ManyToManyField(related_name='group_member', to='web.UserProfile')),
            ],
        ),
    ]
