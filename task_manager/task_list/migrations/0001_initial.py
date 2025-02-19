# Generated by Django 5.1.6 on 2025-02-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=200)),
                ("descrition", models.TextField(max_length=700, null=True)),
                ("completed", models.BooleanField(default=False)),
                ("createdat", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
