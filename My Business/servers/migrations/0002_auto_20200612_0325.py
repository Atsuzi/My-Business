# Generated by Django 2.2.12 on 2020-06-12 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='server',
            name='linode_label',
        ),
        migrations.AlterField(
            model_name='server',
            name='services',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='server',
            name='uid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]