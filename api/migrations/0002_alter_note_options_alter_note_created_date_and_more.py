# Generated by Django 4.1.7 on 2023-03-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-updated_date']},
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
