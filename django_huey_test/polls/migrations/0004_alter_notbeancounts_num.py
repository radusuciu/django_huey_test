# Generated by Django 3.2.7 on 2021-09-10 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_notbeancounts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notbeancounts',
            name='num',
            field=models.TextField(),
        ),
    ]
