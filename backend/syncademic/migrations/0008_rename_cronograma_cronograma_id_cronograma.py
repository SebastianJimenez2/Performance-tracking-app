# Generated by Django 5.0.7 on 2024-08-05 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syncademic', '0007_alter_cronograma_asignatura'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cronograma',
            old_name='cronograma',
            new_name='id_cronograma',
        ),
    ]
