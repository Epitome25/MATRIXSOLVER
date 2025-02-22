# Generated by Django 5.1.6 on 2025-02-21 21:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_support_amount', models.IntegerField()),
                ('finished', models.BooleanField(default=False)),
                ('support_image', models.ImageField(blank=True, null=True, upload_to='support_posts/')),
                ('description', models.TextField(blank=True, null=True)),
                ('requesting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='support_requests', to=settings.AUTH_USER_MODEL)),
                ('sponsoring_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sponsored_support_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
