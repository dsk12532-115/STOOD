# Generated by Django 2.2.1 on 2019-09-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0017_auto_20190912_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacant_seats',
            name='seat_id',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='vacant_seats',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
