# Generated by Django 4.2.2 on 2023-07-01 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m_tienda', '0008_tipo_producto_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plataforma',
            name='marca',
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
    ]
