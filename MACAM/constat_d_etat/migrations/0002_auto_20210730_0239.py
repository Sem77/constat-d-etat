# Generated by Django 3.2 on 2021-07-30 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constat_d_etat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constatartgraphique',
            name='revers_inaccessible',
        ),
        migrations.AddField(
            model_name='artgraphique',
            name='revers_inaccessible',
            field=models.BooleanField(default=True),
        ),
    ]
