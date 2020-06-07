# Generated by Django 2.2.4 on 2020-06-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascarilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='mascarilla')),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]