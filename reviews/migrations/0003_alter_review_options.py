# Generated by Django 4.1.5 on 2023-03-01 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_alter_review_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="review",
            options={"verbose_name": "Critique"},
        ),
    ]
