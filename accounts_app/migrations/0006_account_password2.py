# Generated by Django 4.1 on 2022-08-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0005_remove_account_password2_alter_account_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='password2',
            field=models.CharField(max_length=30, null=True, verbose_name='password'),
        ),
    ]