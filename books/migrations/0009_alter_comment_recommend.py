# Generated by Django 5.0.2 on 2024-03-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_comment_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='recommend',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5),
        ),
    ]
