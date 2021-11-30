# Generated by Django 3.0.8 on 2021-11-07 16:47

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
            name='LoginInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_belong_id', models.CharField(blank=True, max_length=100, null=True)),
                ('update_datetime', models.DateTimeField(auto_now_add=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('session_id', models.CharField(blank=True, max_length=64, null=True)),
                ('browser', models.CharField(max_length=64, null=True)),
                ('ipaddr', models.CharField(blank=True, max_length=32, null=True)),
                ('loginLocation', models.CharField(blank=True, max_length=64, null=True)),
                ('msg', models.TextField(blank=True, null=True)),
                ('os', models.CharField(blank=True, max_length=64, null=True)),
                ('status', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]