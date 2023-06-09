# Generated by Django 4.1.7 on 2023-03-19 20:01

import api.models.submission
import api.models.user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.TextField(default=api.models.user.UserType['BROKER'], verbose_name=api.models.user.UserType)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sayata_userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('submission_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('physical_address', models.CharField(max_length=255)),
                ('annual_revenue', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.TextField(default=api.models.submission.StatusChoices['NEW'], verbose_name=api.models.submission.StatusChoices)),
                ('application_file', models.FileField(blank=True, null=True, upload_to='applications/')),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='api.userprofile')),
            ],
        ),
    ]
