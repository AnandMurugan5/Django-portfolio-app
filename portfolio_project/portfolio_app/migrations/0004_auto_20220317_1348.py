# Generated by Django 3.2.3 on 2022-03-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_auto_20220317_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='username',
            new_name='Name',
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]