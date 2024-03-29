# Generated by Django 2.0.3 on 2019-10-01 04:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birth_date', models.DateField(db_index=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_at', models.DateTimeField()),
                ('sent_at', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=6)),
                ('discount', models.FloatField(default=0)),
                ('quantity', models.FloatField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, default=1, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=6)),
                ('stock', models.IntegerField(default=1)),
                ('reorder', models.IntegerField(default=1)),
                ('commited', models.IntegerField(default=1)),
                ('active', models.BooleanField(default=True)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='sales.OrderDetail', to='sales.Product'),
        ),
        migrations.AddField(
            model_name='area',
            name='clients',
            field=models.ManyToManyField(to='sales.Client'),
        ),
    ]
