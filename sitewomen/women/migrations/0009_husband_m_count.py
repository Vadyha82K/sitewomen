# Generated by Django 5.1.3 on 2024-12-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("women", "0008_husband_women_husband"),
    ]

    operations = [
        migrations.AddField(
            model_name="husband",
            name="m_count",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]