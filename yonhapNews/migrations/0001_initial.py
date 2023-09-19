# Generated by Django 4.2.4 on 2023-09-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CultureNews",
            fields=[
                (
                    "title",
                    models.CharField(max_length=80, primary_key=True, serialize=False),
                ),
                ("posting_date", models.CharField(max_length=30)),
                ("content", models.TextField()),
                ("order", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="EconomyNews",
            fields=[
                (
                    "title",
                    models.CharField(max_length=80, primary_key=True, serialize=False),
                ),
                ("posting_date", models.CharField(max_length=30)),
                ("content", models.TextField()),
                ("order", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="EntertainmentsNews",
            fields=[
                (
                    "title",
                    models.CharField(max_length=80, primary_key=True, serialize=False),
                ),
                ("posting_date", models.CharField(max_length=30)),
                ("content", models.TextField()),
                ("order", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="InternationalNews",
            fields=[
                (
                    "title",
                    models.CharField(max_length=80, primary_key=True, serialize=False),
                ),
                ("posting_date", models.CharField(max_length=30)),
                ("content", models.TextField()),
                ("order", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="NorthKoreaNews",
            fields=[
                (
                    "title",
                    models.CharField(max_length=80, primary_key=True, serialize=False),
                ),
                ("posting_date", models.CharField(max_length=30)),
                ("content", models.TextField()),
                ("order", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="PoliticsNews",
            fields=[
                (
                    "title",
                    models.CharField(max_length=80, primary_key=True, serialize=False),
                ),
                ("posting_date", models.CharField(max_length=30)),
                ("content", models.TextField()),
                ("order", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="SocietyNews",
            fields=[
                (
                    "title",
                    models.CharField(max_length=80, primary_key=True, serialize=False),
                ),
                ("posting_date", models.CharField(max_length=30)),
                ("content", models.TextField()),
                ("order", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="SportsNews",
            fields=[
                (
                    "title",
                    models.CharField(max_length=80, primary_key=True, serialize=False),
                ),
                ("posting_date", models.CharField(max_length=30)),
                ("content", models.TextField()),
                ("order", models.CharField(max_length=12)),
            ],
        ),
    ]
