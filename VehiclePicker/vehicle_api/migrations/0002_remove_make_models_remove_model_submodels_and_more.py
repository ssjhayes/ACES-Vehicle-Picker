# Generated by Django 4.0 on 2021-12-22 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='make',
            name='models',
        ),
        migrations.RemoveField(
            model_name='model',
            name='submodels',
        ),
        migrations.RemoveField(
            model_name='submodel',
            name='years',
        ),
        migrations.AddField(
            model_name='model',
            name='make',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicle_api.make'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submodel',
            name='model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicle_api.model'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='year',
            name='submodel',
            field=models.ManyToManyField(to='vehicle_api.Submodel'),
        ),
    ]