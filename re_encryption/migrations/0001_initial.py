# Generated by Django 2.1.2 on 2018-10-24 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_office', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delegation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delegated_at', models.DateTimeField(auto_now_add=True)),
                ('recepient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delegations', to='data_office.Recepient')),
                ('records_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delegations', to='data_office.RecordsSet')),
            ],
        ),
        migrations.CreateModel(
            name='KeyFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.BinaryField()),
                ('delegation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='key_fragments', to='re_encryption.Delegation')),
            ],
        ),
    ]
