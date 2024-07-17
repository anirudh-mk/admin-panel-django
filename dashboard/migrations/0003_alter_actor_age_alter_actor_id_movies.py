# Generated by Django 5.0.7 on 2024-07-17 16:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_actor_age_alter_actor_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="age",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="actor",
            name="id",
            field=models.CharField(
                default=uuid.UUID("0c13803d-fcc8-469b-a5d5-3cc349070536"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.CreateModel(
            name="Movies",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.UUID("fd5b9905-a2cc-4d0c-84ce-1c75aad0b185"),
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "actor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.actor",
                    ),
                ),
            ],
        ),
    ]