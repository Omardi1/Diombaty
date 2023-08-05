# Generated by Django 4.1.1 on 2022-12-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agence', '0002_alter_room_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='author_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='suite',
            old_name='author_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='rooms/'),
        ),
        migrations.AlterField(
            model_name='suite',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='suites/'),
        ),
    ]
