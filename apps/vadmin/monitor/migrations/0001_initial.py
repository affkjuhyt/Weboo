# Generated by Django 3.0.8 on 2021-12-11 09:02

import apps.vadmin.op_drf.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='Description', null=True, verbose_name='Description')),
                ('modifier', apps.vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='The record was last modified by', max_length=255, null=True, verbose_name='editor')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='Data attribution department')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('cpu_num', models.CharField(max_length=8, verbose_name='CPU核数')),
                ('cpu_sys', models.CharField(max_length=8, verbose_name='CPU已使用率')),
                ('mem_num', models.CharField(max_length=32, verbose_name='内存总数(KB)')),
                ('mem_sys', models.CharField(max_length=32, verbose_name='内存已使用大小(KB)')),
                ('seconds', models.CharField(max_length=32, verbose_name='系统已运行时间')),
            ],
            options={
                'verbose_name': '服务器监控信息',
                'verbose_name_plural': '服务器监控信息',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Tên máy chủ')),
                ('ip', models.CharField(max_length=32, verbose_name='Địa chỉ ip')),
                ('os', models.CharField(max_length=32, verbose_name='Hệ điều hành')),
                ('remark', models.CharField(blank=True, max_length=256, null=True, verbose_name='Nhận xét')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': 'Thông tin máy chủ',
                'verbose_name_plural': 'Thông tin máy chủ',
            },
        ),
        migrations.CreateModel(
            name='SysFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='Description', null=True, verbose_name='Description')),
                ('modifier', apps.vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='The record was last modified by', max_length=255, null=True, verbose_name='editor')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='Data attribution department')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('dir_name', models.CharField(max_length=32, verbose_name='磁盘路径')),
                ('sys_type_name', models.CharField(max_length=400, verbose_name='系统文件类型')),
                ('type_name', models.CharField(max_length=32, verbose_name='盘符类型')),
                ('total', models.CharField(max_length=32, verbose_name='磁盘总大小(KB)')),
                ('disk_sys', models.CharField(max_length=32, verbose_name='已使用大小(KB)')),
            ],
            options={
                'verbose_name': '系统磁盘',
                'verbose_name_plural': '系统磁盘',
            },
        ),
    ]
