# Generated by Django 4.1.2 on 2022-11-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="price",
            name="photo",
            field=models.CharField(default=None, max_length=2083),
        ),
    ]