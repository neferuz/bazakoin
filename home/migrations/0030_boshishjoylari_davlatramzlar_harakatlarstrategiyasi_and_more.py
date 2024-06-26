# Generated by Django 4.2.7 on 2024-06-16 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0029_alter_tenderlar_options_tenderlar_status_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoshIshJoylari",
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
                    "text_en",
                    models.TextField(
                        default="Default Text", verbose_name="Text (English)"
                    ),
                ),
                (
                    "text_ru",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Russian)"
                    ),
                ),
                (
                    "text_uz",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Uzbek)"
                    ),
                ),
            ],
            options={
                "verbose_name": "Bosh Ish Joylari",
                "verbose_name_plural": "Bosh Ish Joylari",
            },
        ),
        migrations.CreateModel(
            name="DavlatRamzlar",
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
                    "text_en",
                    models.TextField(
                        default="Default Text", verbose_name="Text (English)"
                    ),
                ),
                (
                    "text_ru",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Russian)"
                    ),
                ),
                (
                    "text_uz",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Uzbek)"
                    ),
                ),
            ],
            options={
                "verbose_name": "Davlat Ramzlar",
                "verbose_name_plural": "Davlat Ramzlar",
            },
        ),
        migrations.CreateModel(
            name="HarakatlarStrategiyasi",
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
                    "text_en",
                    models.TextField(
                        default="Default Text", verbose_name="Text (English)"
                    ),
                ),
                (
                    "text_ru",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Russian)"
                    ),
                ),
                (
                    "text_uz",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Uzbek)"
                    ),
                ),
            ],
            options={
                "verbose_name": "Harakatlar Strategiyasi",
                "verbose_name_plural": "Harakatlar Strategiyasi",
            },
        ),
        migrations.CreateModel(
            name="KopKelganSavollargaJavoblar",
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
                    "text_en",
                    models.TextField(
                        default="Default Text", verbose_name="Text (English)"
                    ),
                ),
                (
                    "text_ru",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Russian)"
                    ),
                ),
                (
                    "text_uz",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Uzbek)"
                    ),
                ),
            ],
            options={
                "verbose_name": "Kop Kelgan Savollarga Javoblar",
                "verbose_name_plural": "Kop Kelgan Savollarga Javoblar",
            },
        ),
        migrations.CreateModel(
            name="OchiqMalumotlar",
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
                    "text_en",
                    models.TextField(
                        default="Default Text", verbose_name="Text (English)"
                    ),
                ),
                (
                    "text_ru",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Russian)"
                    ),
                ),
                (
                    "text_uz",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Uzbek)"
                    ),
                ),
            ],
            options={
                "verbose_name": "Ochiq Malumotlar",
                "verbose_name_plural": "Ochiq Malumotlar",
            },
        ),
        migrations.CreateModel(
            name="QonunchilikBazasi",
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
                    "text_en",
                    models.TextField(
                        default="Default Text", verbose_name="Text (English)"
                    ),
                ),
                (
                    "text_ru",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Russian)"
                    ),
                ),
                (
                    "text_uz",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Uzbek)"
                    ),
                ),
            ],
            options={
                "verbose_name": "Qonunchilik Bazasi",
                "verbose_name_plural": "Qonunchilik Bazasi",
            },
        ),
        migrations.CreateModel(
            name="SaytHaritasi",
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
                    "text_en",
                    models.TextField(
                        default="Default Text", verbose_name="Text (English)"
                    ),
                ),
                (
                    "text_ru",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Russian)"
                    ),
                ),
                (
                    "text_uz",
                    models.TextField(
                        default="Default Text", verbose_name="Text (Uzbek)"
                    ),
                ),
            ],
            options={
                "verbose_name": "Sayt Haritasi",
                "verbose_name_plural": "Sayt Haritasi",
            },
        ),
        migrations.AlterModelOptions(
            name="davlattashkilotlari",
            options={
                "verbose_name": "Davlat Tashkilotlari",
                "verbose_name_plural": "Davlat Tashkilotlari",
            },
        ),
    ]
