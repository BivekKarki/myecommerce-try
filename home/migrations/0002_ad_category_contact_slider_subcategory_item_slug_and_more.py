# Generated by Django 4.1.1 on 2022-09-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.TextField()),
                ('rank', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('slug', models.CharField(max_length=400, unique=True)),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('contact_id', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.TextField()),
                ('rank', models.IntegerField()),
                ('description', models.TextField()),
                ('status', models.CharField(blank=True, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('', 'Default')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('slug', models.CharField(max_length=400, unique=True)),
                ('image', models.TextField()),
                ('labels', models.CharField(choices=[('special', 'special'), ('', 'Non special')], max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.CharField(default='product', max_length=400),
        ),
        migrations.AlterField(
            model_name='item',
            name='labels',
            field=models.CharField(choices=[('special', 'special'), ('', 'Non special')], max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('', 'Default')], max_length=200),
        ),
    ]
