# Generated by Django 3.0.2 on 2020-02-01 18:02

from django.db import migrations, models
import django.db.models.deletion
import transaksi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id_transaksi', models.CharField(default=transaksi.models.auto_id, editable=False, max_length=13, primary_key=True, serialize=False)),
                ('transaksi', models.CharField(max_length=13)),
                ('tgl_pengambilan', models.DateTimeField()),
                ('tgl_kembali', models.DateTimeField(blank=True, null=True)),
                ('pengguna', models.CharField(max_length=35)),
                ('jumlah', models.PositiveIntegerField()),
                ('keterangan', models.TextField(blank=True)),
                ('user_updated', models.CharField(blank=True, max_length=35)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('id_barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Barang')),
            ],
        ),
    ]
