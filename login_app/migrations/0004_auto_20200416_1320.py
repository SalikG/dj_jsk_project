# Generated by Django 3.0.5 on 2020-04-16 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20200416_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(default='customer', on_delete=django.db.models.deletion.PROTECT, to='login_app.Role'),
        ),
    ]