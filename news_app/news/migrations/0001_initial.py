# Generated by Django 5.0.4 on 2024-04-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('published_at', models.DateTimeField()),
            ],
        ),
    ]