# Generated by Django 4.0 on 2021-12-17 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Gry', '0005_alter_kategoriagry_nazwa'),
    ]

    operations = [
        migrations.AddField(
            model_name='gry',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gry', to='auth.user'),
            preserve_default=False,
        ),
    ]
