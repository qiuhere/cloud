# Generated by Django 3.1.4 on 2021-01-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='imgs')),
            ],
        ),
    ]
