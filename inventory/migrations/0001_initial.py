# Generated by Django 3.0.2 on 2020-01-09 14:47

from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id_barang', models.CharField(default=inventory.models.incerement_id_barang, max_length=8, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=35)),
                ('jenis', models.CharField(choices=[('Inventaris', 'Inventaris'), ('Modal', 'Modal'), ('Persediaan', 'Persediaan')], max_length=35)),
                ('jumlah', models.PositiveIntegerField()),
                ('satuan', models.CharField(choices=[('Persediaan', 'Pak'), ('Buah', 'Buah'), ('Kotak', 'Kotak')], max_length=10)),
                ('nilai_barang', models.DecimalField(decimal_places=2, max_digits=8)),
                ('satker', models.CharField(max_length=35)),
                ('tgl_pengadaan', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('keterangan', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tempat',
            fields=[
                ('id_tempat', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=35)),
            ],
        ),
    ]
