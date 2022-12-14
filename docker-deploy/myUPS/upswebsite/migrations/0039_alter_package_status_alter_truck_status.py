# Generated by Django 4.0.4 on 2022-04-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upswebsite', '0038_alter_package_status_alter_truck_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('delivering', 'delivering'), ('delivered', 'delivered'), ('loading', 'loading'), ('pick_up', 'pick_up')], default='pick_up', max_length=32),
        ),
        migrations.AlterField(
            model_name='truck',
            name='status',
            field=models.CharField(choices=[('traveling', 'traveling'), ('loading', 'loading'), ('arrive warehouse', 'arrive warehouse'), ('delivering', 'delivering'), ('idle', 'idle')], default='idle', max_length=32),
        ),
    ]
