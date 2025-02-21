# Generated by Django 5.1.6 on 2025-02-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinique',
            fields=[
                ('clinique_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.TextField()),
                ('ville', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
