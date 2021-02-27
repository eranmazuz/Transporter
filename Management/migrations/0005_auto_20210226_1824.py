# Generated by Django 3.1.7 on 2021-02-26 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0004_auto_20210226_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transporterforcity',
            name='soliders',
        ),
        migrations.AddField(
            model_name='soldier',
            name='transporter',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soldiers', related_query_name='soldier', to='Management.transporter', verbose_name="Soldier's Transportation"),
        ),
    ]