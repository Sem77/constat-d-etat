# Generated by Django 3.2 on 2021-08-12 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constat_d_etat', '0017_auto_20210812_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photosignificativesupportartgraphique',
            old_name='supportArtGraphique',
            new_name='support',
        ),
        migrations.AlterField(
            model_name='photosignificativesupportartgraphique',
            name='nature_alteration',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='photosignificativesupportartgraphique',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='photosignificativesupportartgraphique',
            name='photo_avec_emplacement',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
