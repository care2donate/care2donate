# Generated by Django 3.2.2 on 2021-05-14 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('covid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coviduserdetail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='app_user', to='user.user'),
        ),
    ]
