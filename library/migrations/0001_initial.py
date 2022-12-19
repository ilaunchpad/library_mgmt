# Generated by Django 4.1.3 on 2022-12-11 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.ForeignKey(blank=True, db_column='bookid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='library.book')),
                ('userid', models.ForeignKey(blank=True, db_column='userid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='library.member')),
            ],
        ),
    ]