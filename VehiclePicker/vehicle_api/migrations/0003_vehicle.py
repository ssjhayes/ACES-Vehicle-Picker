# Generated by Django 4.0 on 2021-12-22 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_api', '0002_remove_make_models_remove_model_submodels_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_api.make')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_api.model')),
                ('submodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_api.submodel')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_api.year')),
            ],
        ),
    ]
