# Generated by Django 5.1.5 on 2025-01-28 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_chatmessage_message_file_chatmessage_message_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='message_file',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='message_image',
        ),
    ]
