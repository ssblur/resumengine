# Generated by Django 3.1 on 2020-08-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=128)),
                ('document_type', models.IntegerField(choices=[(1, 'Project'), (2, 'Education'), (3, 'Award'), (4, 'Experience')])),
                ('contents', models.TextField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons')),
                ('last_updated', models.DateField(auto_now=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('since', models.DateField()),
                ('visibility', models.IntegerField(choices=[(1, 'Public'), (2, 'Protected'), (3, 'Private')])),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.TextField()),
                ('description', models.TextField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons')),
                ('documents', models.ManyToManyField(to='portfolio.Document')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(to='portfolio.Tag'),
        ),
    ]
