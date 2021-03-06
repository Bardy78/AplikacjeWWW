# Generated by Django 4.0 on 2021-12-16 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gry', '0002_alter_producentgry_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gry',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='kategoriagry',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='producentgry',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='gry',
            name='kategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kategoria', to='Gry.kategoriagry'),
        ),
        migrations.AlterField(
            model_name='gry',
            name='producent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='producent', to='Gry.producentgry'),
        ),
    ]
