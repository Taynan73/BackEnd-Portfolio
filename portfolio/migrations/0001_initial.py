# Generated by Django 5.0 on 2023-12-08 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, upload_to='')),
                ('titulo', models.CharField(max_length=30)),
                ('categoria', models.CharField(choices=[('B', 'Back-end'), ('F', 'Front-end'), ('D', 'DevOps')], default='F', max_length=1)),
                ('descricao', models.TextField(max_length=255)),
            ],
        ),
    ]
