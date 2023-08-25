# Generated by Django 4.2.4 on 2023-08-24 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("MainApp", "0003_snippet_parameter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="snippet",
            name="parameter",
            field=models.CharField(
                choices=[("pr", "Private"), ("je", "General")],
                default="Empty",
                max_length=30,
            ),
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("text", models.CharField(max_length=100)),
                ("creation_date", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "snippet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="MainApp.snippet",
                    ),
                ),
            ],
        ),
    ]