# Generated by Django 4.1.3 on 2022-12-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_downloaded_file_details_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bureau',
            name='DPD_month_new',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
