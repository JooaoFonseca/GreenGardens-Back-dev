# Generated by Django 5.0.7 on 2024-07-13 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carausel',
            name='titulo',
        ),
        migrations.AlterField(
            model_name='carausel',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='img/slider', verbose_name='Foto'),
        ),
    ]
