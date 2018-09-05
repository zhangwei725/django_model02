# Generated by Django 2.1.1 on 2018-09-05 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('real_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=100)),
                ('telno', models.CharField(max_length=11)),
                ('mobile', models.CharField(max_length=11)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=64)),
                ('state', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]