# Generated by Django 3.0.8 on 2021-12-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookDescriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=16)),
                ('title', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=1024)),
                ('tags', models.CharField(default='', max_length=512)),
                ('lda_vector', models.CharField(max_length=56, null=True)),
                ('sim_list', models.CharField(default='', max_length=512)),
            ],
            options={
                'db_table': 'book_description',
            },
        ),
        migrations.CreateModel(
            name='LdaSimilarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('source', models.CharField(db_index=True, max_length=16)),
                ('target', models.CharField(max_length=16)),
                ('similarity', models.DecimalField(decimal_places=7, max_digits=8)),
            ],
            options={
                'db_table': 'lda_similarity',
            },
        ),
        migrations.CreateModel(
            name='Recs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=16)),
                ('item', models.CharField(max_length=16)),
                ('rating', models.FloatField()),
                ('type', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'recs',
            },
        ),
        migrations.CreateModel(
            name='SeededRecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('source', models.CharField(max_length=16)),
                ('target', models.CharField(max_length=16)),
                ('support', models.DecimalField(decimal_places=8, max_digits=10)),
                ('confidence', models.DecimalField(decimal_places=8, max_digits=10)),
                ('type', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'seeded_recs',
            },
        ),
        migrations.CreateModel(
            name='Similarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('source', models.CharField(db_index=True, max_length=16)),
                ('target', models.CharField(max_length=16)),
                ('similarity', models.DecimalField(decimal_places=7, max_digits=8)),
            ],
            options={
                'db_table': 'similarity',
            },
        ),
    ]
