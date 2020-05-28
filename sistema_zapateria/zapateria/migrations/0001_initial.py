# Generated by Django 3.0.6 on 2020-05-27 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=100)),
                ('Telefono', models.IntegerField()),
                ('Nit', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zapato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estilo', models.CharField(max_length=100)),
                ('Color', models.CharField(max_length=100)),
                ('Talla', models.CharField(max_length=100)),
                ('Marca', models.CharField(max_length=100)),
                ('Proveedor', models.CharField(max_length=100)),
                ('Genero', models.CharField(max_length=100)),
                ('Tipo', models.CharField(max_length=100)),
                ('Precio', models.FloatField()),
                ('Stock', models.IntegerField()),
                ('Fecha_entrada', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField()),
                ('Total', models.FloatField()),
                ('id_Factura', models.IntegerField()),
                ('id_Zapato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zapateria.Zapato')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('total', models.FloatField()),
                ('id_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zapateria.Clientes')),
            ],
        ),
    ]