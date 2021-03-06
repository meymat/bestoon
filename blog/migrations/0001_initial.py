# Generated by Django 2.2.3 on 2019-08-05 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.BigIntegerField()),
                ('text', models.CharField(max_length=255)),
                ('user', models.ForeignKey(blank=True, help_text='Choose Auther', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='مولف')),
            ],
        ),
    ]
