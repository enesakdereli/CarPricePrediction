# Generated by Django 2.0.4 on 2018-05-10 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpp', '0003_remove_userpreference_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('power', models.IntegerField()),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cpp.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='CaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GearType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gear', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='userpreference',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='userpreference',
            name='model',
        ),
        migrations.RemoveField(
            model_name='userpreference',
            name='series',
        ),
        migrations.DeleteModel(
            name='UserPreference',
        ),
        migrations.AddField(
            model_name='carproperties',
            name='case_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cpp.CaseType'),
        ),
        migrations.AddField(
            model_name='carproperties',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cpp.Color'),
        ),
        migrations.AddField(
            model_name='carproperties',
            name='exchange_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cpp.ExchangeStatus'),
        ),
        migrations.AddField(
            model_name='carproperties',
            name='fuel_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cpp.FuelType'),
        ),
        migrations.AddField(
            model_name='carproperties',
            name='gear_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cpp.GearType'),
        ),
        migrations.AddField(
            model_name='carproperties',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cpp.Model'),
        ),
        migrations.AddField(
            model_name='carproperties',
            name='owner_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cpp.OwnerType'),
        ),
        migrations.AddField(
            model_name='carproperties',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cpp.Series'),
        ),
    ]