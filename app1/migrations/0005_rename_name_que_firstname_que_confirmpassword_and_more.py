# Generated by Django 4.1.2 on 2022-11-05 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_que_email_que_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='que',
            old_name='name',
            new_name='firstName',
        ),
        migrations.AddField(
            model_name='que',
            name='confirmPassword',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='que',
            name='emailId',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='que',
            name='lastName',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]