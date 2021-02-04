# Generated by Django 3.1.5 on 2021-02-02 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='author',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='body',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated',
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]