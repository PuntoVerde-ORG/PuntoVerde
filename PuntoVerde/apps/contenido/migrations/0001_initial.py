# Generated by Django 2.2.6 on 2019-11-03 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='')),
                ('fechacreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaupdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
