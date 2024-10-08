# Generated by Django 5.1.1 on 2024-09-26 03:33

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255, null=True)),
                ('job_type', models.CharField(choices=[('fulltime', 'Full-time'), ('parttime', 'Part-time')], max_length=10, null=True)),
                ('company_logo', models.ImageField(null=True, upload_to='company_logos/')),
                ('company_name', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('requirements', models.TextField(null=True)),
                ('salary', models.CharField(max_length=255, null=True)),
                ('posted_on', models.DateField(default=django.utils.timezone.now, null=True)),
                ('updated_on', models.DateField(auto_now=True, null=True)),
                ('application_deadline', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobAppliModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.TextField()),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.jobmodel')),
            ],
        ),
    ]
