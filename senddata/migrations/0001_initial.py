# Generated by Django 2.2.5 on 2019-09-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.TextField()),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
