# Generated by Django 4.0.5 on 2022-07-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trs_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trs_id', models.CharField(max_length=10)),
                ('trs_pw', models.CharField(max_length=20)),
            ],
        ),
    ]
