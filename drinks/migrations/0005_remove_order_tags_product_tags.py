# Generated by Django 4.2.7 on 2023-11-30 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0004_tag_order_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='drinks.tag'),
        ),
    ]
