# Generated by Django 5.0 on 2023-12-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_rename_phone_number_customer_phone"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer",
            options={"verbose_name": "customer", "verbose_name_plural": "customers"},
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.CharField(
                blank=True,
                default="",
                max_length=30,
                null=True,
                verbose_name="phone number",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="customer",
            unique_together={("username", "email", "phone")},
        ),
    ]