# Generated by Django 2.2.1 on 2019-09-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0021_remove_waituser_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='board_station',
            field=models.CharField(default='', max_length=70, verbose_name='いつも乗る駅'),
        ),
        migrations.AddField(
            model_name='profile',
            name='exit_station',
            field=models.CharField(default='', max_length=70, verbose_name='いつも降りる駅'),
        ),
    ]