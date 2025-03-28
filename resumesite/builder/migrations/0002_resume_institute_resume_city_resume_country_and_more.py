# Generated by Django 5.0.6 on 2025-02-23 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='Institute',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='degree',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='eduCity',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='eduField',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='pin_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interestDesc', models.CharField(max_length=50, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interests', to='builder.resume')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100, null=True)),
                ('company', models.CharField(max_length=50, null=True)),
                ('timePeriod', models.CharField(max_length=50, null=True)),
                ('workDesc', models.CharField(max_length=500, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to='builder.resume')),
            ],
        ),
    ]
