# Generated by Django 2.2.2 on 2019-09-23 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0014_auto_20190923_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valoration',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Score'),
        ),
    ]