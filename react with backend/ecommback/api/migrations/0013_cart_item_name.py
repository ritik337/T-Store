# Generated by Django 4.2.4 on 2023-11-30 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_cart_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='item_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
