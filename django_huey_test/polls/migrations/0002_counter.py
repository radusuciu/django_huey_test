# Generated by Django 3.2.7 on 2021-09-10 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failed', models.BooleanField(default=False)),
                ('succeeded', models.BooleanField(default=False)),
            ],
        ),
    ]
