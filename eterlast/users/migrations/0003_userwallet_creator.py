# Generated by Django 3.2.13 on 2022-05-28 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220528_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwallet',
            name='creator',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='users.user'),
            preserve_default=False,
        ),
    ]
