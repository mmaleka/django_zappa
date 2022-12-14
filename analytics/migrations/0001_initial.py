# Generated by Django 2.1.9 on 2022-08-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('page_visited', models.CharField(blank=True, default='', max_length=200)),
                ('user_action', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
