# Generated by Django 3.2 on 2021-08-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constat_d_etat', '0012_auto_20210804_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='constatartgraphique',
            name='ville',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='constatpeinturesurbois',
            name='ville',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='constatpeinturesurtoile',
            name='ville',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
