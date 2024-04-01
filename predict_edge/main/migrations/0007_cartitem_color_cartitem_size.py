# Generated by Django 5.0.2 on 2024-03-31 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_clothes_colors_options_alter_clothing_gender_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="color",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main.clothes_colors",
            ),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="size",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main.clothes_sizes",
            ),
        ),
    ]