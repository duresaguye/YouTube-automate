# Generated by Django 5.0.7 on 2024-08-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('embed_url', models.URLField(max_length=500)),
                ('published_at', models.DateTimeField()),
                ('is_recent', models.BooleanField(default=True)),
            ],
        ),
    ]