# Generated by Django 3.2.5 on 2021-08-15 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('2000s', '2000s'), ('1990s', '1990s'), ('2010s', '2010s'), ('1980s', '1980s')], max_length=30)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
            ],
        ),
    ]
