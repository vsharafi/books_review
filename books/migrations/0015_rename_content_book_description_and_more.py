# Generated by Django 5.0.2 on 2024-03-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_comment_is_active_comment_recommend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='datetime_created',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='writer',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True),
        ),
    ]
