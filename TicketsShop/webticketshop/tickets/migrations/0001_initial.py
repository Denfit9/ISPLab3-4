# Generated by Django 4.0.4 on 2022-05-30 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Name of ticket/coupon')),
                ('description', models.TextField(verbose_name='Ticket description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.category')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
    ]
