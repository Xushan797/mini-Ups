# Generated by Django 4.0.4 on 2022-04-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upswebsite', '0035_alter_package_status_alter_truck_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('pick_up', 'pick_up'), ('loading', 'loading'), ('delivering', 'delivering'), ('delivered', 'delivered')], default='pick_up', max_length=32),
        ),
        migrations.AlterField(
            model_name='truck',
            name='status',
            field=models.CharField(choices=[('idle', 'idle'), ('arrive warehouse', 'arrive warehouse'), ('traveling', 'traveling'), ('loading', 'loading'), ('delivering', 'delivering')], default='idle', max_length=32),
        ),
    ]
