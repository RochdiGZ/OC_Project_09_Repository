# Generated by Django 4.1.5 on 2023-02-28 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0002_alter_userfollows_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userfollows",
            options={"verbose_name": "Suivi"},
        ),
    ]