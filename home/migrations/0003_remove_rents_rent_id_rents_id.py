# Generated by Django 4.2.7 on 2023-11-21 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_remove_rents_title_rents_total_guests_limit"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rents",
            name="rent_id",
        ),
        migrations.AddField(
            model_name="rents",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
    ]
