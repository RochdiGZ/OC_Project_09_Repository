# Generated by Django 4.1.5 on 2023-03-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0003_alter_ticket_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
