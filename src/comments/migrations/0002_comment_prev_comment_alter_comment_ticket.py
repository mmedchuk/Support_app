# Generated by Django 4.1.5 on 2023-02-08 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='prev_comment',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='next',
                to='comments.comment',
            ),
        ),
        migrations.AlterField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tickets.ticket'
            ),
        ),
    ]
