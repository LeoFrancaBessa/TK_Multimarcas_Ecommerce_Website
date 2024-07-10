# Generated by Django 5.0.2 on 2024-07-05 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_alter_cart_options_alter_cartitem_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attribute",
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
                ("name", models.CharField(max_length=100, verbose_name="Atributo")),
            ],
            options={
                "verbose_name": "Atributo",
                "verbose_name_plural": "Atributos",
            },
        ),
        migrations.RemoveField(
            model_name="clothing",
            name="subtype",
        ),
        migrations.RemoveField(
            model_name="clothing",
            name="type",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="country",
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cartItems",
                to="main.cart",
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="phone",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name="AttributeValue",
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
                ("value", models.CharField(max_length=100, verbose_name="Valor")),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="values",
                        to="main.attribute",
                        verbose_name="Atributo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Valor do Atributo",
                "verbose_name_plural": "Valores do Atributo",
            },
        ),
        migrations.AddField(
            model_name="clothing",
            name="attributes",
            field=models.ManyToManyField(
                blank=True, to="main.attributevalue", verbose_name="Atributos"
            ),
        ),
        migrations.DeleteModel(
            name="SubType",
        ),
        migrations.DeleteModel(
            name="Type",
        ),
    ]