# Generated by Django 2.1.3 on 2019-01-03 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Stop')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewBucketList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucketList', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trips.BucketListItem')),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Stop')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip')),
            ],
        ),
    ]
