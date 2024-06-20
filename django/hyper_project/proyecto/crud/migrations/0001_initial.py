# Generated by Django 5.0.6 on 2024-06-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrudUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('apellido', models.TextField(max_length=100, null=True)),
                ('edad', models.IntegerField(null=True)),
                ('fecha_de_creacion', models.DateField(auto_now=True)),
            ],
        ),
    ]
