# Generated by Django 4.1.7 on 2023-05-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]