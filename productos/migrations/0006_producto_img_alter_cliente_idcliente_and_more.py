# Generated by Django 4.0.4 on 2022-05-12 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_producto_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idCliente',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idpro',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='idTp',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
