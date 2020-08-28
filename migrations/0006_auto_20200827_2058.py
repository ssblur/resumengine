# Generated by Django 3.1 on 2020-08-28 01:01

from django.db import migrations, models

def migrate(apps, schema_editor):
    DocumentCategory = apps.get_model('portfolio', 'DocumentCategory')
    DocumentCategory.objects.bulk_create([
        DocumentCategory(name = "Project"),
        DocumentCategory(name = "Education"),
        DocumentCategory(name = "Award"),
        DocumentCategory(name = "Experience"),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200827_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.RunPython(migrate, migrations.RunPython.noop)
    ]