# Generated by Django 4.0.2 on 2023-07-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackfood', '0004_alter_event_contactdetail_alter_event_contactperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contactDetail',
            field=models.CharField(default='9996234567', max_length=10),
        ),
    ]