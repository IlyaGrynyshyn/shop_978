# Generated by Django 5.0 on 2023-12-24 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_customer_phone_number"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="phone_number",
            new_name="phone",
        ),
    ]
