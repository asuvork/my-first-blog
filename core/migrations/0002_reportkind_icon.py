# Generated by Django 2.2.5 on 2019-10-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportkind',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
