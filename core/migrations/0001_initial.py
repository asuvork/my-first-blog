# Generated by Django 2.2.5 on 2019-10-03 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('url', models.CharField(blank=True, max_length=1000, null=True)),
                ('url_web', models.CharField(blank=True, max_length=1000, null=True)),
                ('crtime', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('vendor', models.CharField(blank=True, max_length=50, null=True)),
                ('kind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ReportKind')),
            ],
        ),
    ]
