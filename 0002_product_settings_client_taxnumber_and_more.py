# Generated by Django 5.0 on 2024-01-02 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(choices=[('R', 'ZAR'), ('$', 'USD')], default='R', max_length=100)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(blank=True, max_length=200, null=True)),
                ('addressLine1', models.CharField(blank=True, max_length=200, null=True)),
                ('province', models.CharField(blank=True, choices=[('Maharashtra', 'Maharashtra'), ('Delhi', 'Delhi'), ('Kerala', 'Kerala')], max_length=100)),
                ('postalCode', models.CharField(blank=True, max_length=10, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('emailAddress', models.CharField(blank=True, max_length=100, null=True)),
                ('taxNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='taxNumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='province',
            field=models.CharField(blank=True, choices=[('Maharashtra', 'Maharashtra'), ('Delhi', 'Delhi'), ('Kerala', 'Kerala')], max_length=100),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.CharField(blank=True, max_length=100, null=True)),
                ('dueDate', models.DateField(blank=True, null=True)),
                ('paymentTerms', models.CharField(choices=[('14 days', '14 days'), ('30 days', '30 days'), ('60 days', '60 days')], default='14 days', max_length=100)),
                ('status', models.CharField(choices=[('CURRENT', 'CURRENT'), ('OVERDUE', 'OVERDUE'), ('PAID', 'PAID')], default='CURRENT', max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.client')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.product')),
            ],
        ),
    ]
