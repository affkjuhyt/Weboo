# Generated by Django 3.0.8 on 2021-10-30 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_downloadbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=20),
        ),
    ]
