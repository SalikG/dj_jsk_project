# Generated by Django 3.0.5 on 2020-04-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCreditAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_profile_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=150)),
                ('credit_change', models.DecimalField(decimal_places=2, max_digits=6)),
                ('credit_before', models.DecimalField(decimal_places=2, max_digits=6)),
                ('credit_after', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]