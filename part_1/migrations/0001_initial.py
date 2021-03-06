# Generated by Django 3.2.3 on 2021-05-19 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EndPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='StatusValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.IntegerField()),
                ('status', models.TextField(default='')),
                ('value', models.TextField(default='')),
                ('api_endpoint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='part_1.endpoint')),
            ],
        ),
    ]
