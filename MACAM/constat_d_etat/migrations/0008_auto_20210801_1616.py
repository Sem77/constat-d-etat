# Generated by Django 3.2 on 2021-08-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constat_d_etat', '0007_auto_20210801_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emballageoeuvre',
            name='autres_ouvres_dans_la_meme_caisse',
        ),
        migrations.RemoveField(
            model_name='emballageoeuvre',
            name='nom_convoyeur',
        ),
        migrations.RemoveField(
            model_name='emballageoeuvre',
            name='nom_transporteur',
        ),
        migrations.RemoveField(
            model_name='emballageoeuvre',
            name='num_caisse',
        ),
        migrations.RemoveField(
            model_name='emballageoeuvre',
            name='signature_convoyeur',
        ),
        migrations.AddField(
            model_name='constatartgraphique',
            name='autres_ouvres_dans_la_meme_caisse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='constatartgraphique',
            name='nom_convoyeur',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='constatartgraphique',
            name='nom_transporteur',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='constatartgraphique',
            name='num_caisse',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='constatartgraphique',
            name='photos_numeriques_realisees_au_depart',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='constatartgraphique',
            name='signature_convoyeur',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='constatpeinturesurbois',
            name='autres_ouvres_dans_la_meme_caisse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='constatpeinturesurbois',
            name='nom_convoyeur',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='constatpeinturesurbois',
            name='nom_transporteur',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='constatpeinturesurbois',
            name='num_caisse',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='constatpeinturesurbois',
            name='photos_numeriques_realisees_au_depart',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='constatpeinturesurbois',
            name='signature_convoyeur',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='constatpeinturesurtoile',
            name='autres_ouvres_dans_la_meme_caisse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='constatpeinturesurtoile',
            name='nom_convoyeur',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='constatpeinturesurtoile',
            name='nom_transporteur',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='constatpeinturesurtoile',
            name='num_caisse',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='constatpeinturesurtoile',
            name='photos_numeriques_realisees_au_depart',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='constatpeinturesurtoile',
            name='signature_convoyeur',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
