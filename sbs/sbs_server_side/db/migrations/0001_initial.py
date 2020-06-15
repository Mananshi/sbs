# Generated by Django 3.0.3 on 2020-06-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=500)),
                ('room', models.CharField(max_length=3)),
                ('event', models.CharField(max_length=10)),
                ('requested_by', models.CharField(max_length=20)),
                ('from_ts', models.DateTimeField()),
                ('to_ts', models.DateTimeField()),
            ],
        ),
    ]