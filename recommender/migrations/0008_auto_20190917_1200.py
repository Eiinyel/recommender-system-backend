# Generated by Django 2.2.2 on 2019-09-17 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0007_auto_20190624_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='recommender.City', verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recommendation',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End date'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start date'),
        ),
    ]