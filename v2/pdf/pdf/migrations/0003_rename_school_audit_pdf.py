# Generated by Django 3.2.8 on 2021-10-30 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0002_alter_audit_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audit',
            old_name='school',
            new_name='pdf',
        ),
    ]
