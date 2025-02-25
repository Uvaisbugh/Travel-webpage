# Generated by Django 5.0.6 on 2024-10-16 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Individual",
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
                ("Pname", models.CharField(max_length=250)),
                ("Pimg", models.ImageField(upload_to="per")),
                ("Pdesc", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Place",
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
                ("name", models.CharField(max_length=250)),
                ("img", models.ImageField(upload_to="pics")),
                ("desc", models.TextField()),
            ],
        ),
    ]
