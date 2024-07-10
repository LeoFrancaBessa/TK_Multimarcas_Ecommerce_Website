# Generated by Django 5.0.2 on 2024-07-05 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_attribute_remove_clothing_subtype_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="clothes_colors",
            name="clothing",
        ),
        migrations.RemoveField(
            model_name="clothes_colors",
            name="count",
        ),
        migrations.RemoveField(
            model_name="clothes_sizes",
            name="clothing",
        ),
        migrations.RemoveField(
            model_name="clothes_sizes",
            name="count",
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(
                        default=0, verbose_name="Quantidade em Estoque"
                    ),
                ),
                (
                    "clothing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stocks",
                        to="main.clothing",
                        verbose_name="Roupa",
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.clothes_colors",
                        verbose_name="Cor",
                    ),
                ),
                (
                    "size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.clothes_sizes",
                        verbose_name="Tamanho",
                    ),
                ),
            ],
        ),
    ]