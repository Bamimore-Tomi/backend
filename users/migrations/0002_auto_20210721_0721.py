# Generated by Django 3.1.7 on 2021-07-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerprofile',
            name='accepted_vendor_policy',
            field=models.BooleanField(default=False, verbose_name='accepted_vendor_policy'),
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='bank_account_is_verified',
            field=models.BooleanField(default=False, verbose_name='bank_account_is_verified'),
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='bank_sort_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
