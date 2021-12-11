# Generated by Django 3.0.8 on 2021-12-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=16)),
                ('book_id', models.CharField(max_length=16)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('rating_timestamp', models.DateTimeField()),
                ('type', models.CharField(default='explicit', max_length=8)),
            ],
        ),
    ]
