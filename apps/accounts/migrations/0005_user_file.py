# Generated by Django 2.1.5 on 2019-02-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190128_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='file',
            field=models.FileField(null=True, upload_to='userfiles/'),
        ),
    ]
