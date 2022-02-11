# Generated by Django 4.0.2 on 2022-02-09 16:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='actor_id',
            field=models.UUIDField(default=uuid.uuid1, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='director',
            name='director_id',
            field=models.UUIDField(default=uuid.uuid1, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='img_id',
            field=models.UUIDField(default=uuid.uuid1, editable=False, unique=True),
        ),
    ]