# Generated by Django 3.1.7 on 2021-10-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20211020_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='subcategory',
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='categories',
            field=models.ManyToManyField(related_name='subcategories', to='market.Category'),
        ),
    ]
