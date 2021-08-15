# Generated by Django 3.2.6 on 2021-08-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publication_date', models.DateTimeField(verbose_name='Data publikacji')),
                ('isbn_number', models.IntegerField()),
                ('pages_count', models.IntegerField()),
                ('cover_url', models.CharField(max_length=255)),
                ('publication_language', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
