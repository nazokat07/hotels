# Generated by Django 4.2.6 on 2023-10-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=256)),
                ('lastname', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('phonenumber', models.CharField(max_length=256)),
            ],
        ),
    ]
