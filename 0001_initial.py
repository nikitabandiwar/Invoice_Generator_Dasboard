# Generated by Django 5.0 on 2024-01-02 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(blank=True, max_length=200, null=True)),
                ('addressLine1', models.CharField(blank=True, max_length=200, null=True)),
                ('province', models.CharField(blank=True, choices=[('Delhi', 'Delhi'), ('Maharashtra', 'Maharashtra'), ('Kerala', 'Kerala')], max_length=100)),
                ('postalCode', models.CharField(blank=True, max_length=10, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('emailAddress', models.CharField(blank=True, max_length=100, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
