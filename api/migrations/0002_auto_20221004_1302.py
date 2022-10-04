# Generated by Django 3.2.8 on 2022-10-04 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecuitmentAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_name', models.CharField(max_length=52, unique=True)),
                ('contact', models.CharField(max_length=52, unique=True)),
                ('email', models.CharField(blank=True, max_length=52, null=True)),
                ('premises', models.CharField(blank=True, max_length=52, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=52, null=True)),
                ('no_workers_affiliated', models.CharField(blank=True, max_length=52, null=True)),
                ('countries', models.CharField(blank=True, help_text='Please add a list of the countries the agency sends people to.', max_length=52, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Recuitment Agency',
                'verbose_name_plural': 'Recuitment Agencies',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=52)),
                ('contact', models.CharField(max_length=52, unique=True)),
                ('email', models.CharField(blank=True, max_length=52, null=True)),
                ('nin', models.CharField(blank=True, max_length=100, null=True)),
                ('origin_location', models.CharField(blank=True, max_length=52, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=52, null=True)),
                ('country_of_destination', models.CharField(choices=[('UAE', 'UAE'), ('Saudi Arabia', 'Saudi Arabia'), ('Bahrain', 'Bahrain'), ('Oman', 'Oman'), ('Somalia', 'Somalia'), ('Qatar', 'Qatar'), ('Iraq', 'Iraq'), ('Afganistan', 'Afganistan'), ('Mali', 'Mali'), ('Booking', 'Booking')], max_length=52)),
                ('countries_been_to', models.CharField(blank=True, help_text='Please add a list of the countries the agency sends people to.', max_length=52, null=True)),
                ('contract_start_date', models.DateField(auto_now_add=True, null=True)),
                ('contract_end_date', models.DateField(auto_now_add=True, null=True)),
                ('employment_company', models.CharField(blank=True, max_length=100, null=True)),
                ('work_place_location', models.CharField(blank=True, max_length=100, null=True)),
                ('employer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('employer_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('employer_email', models.CharField(blank=True, max_length=100, null=True)),
                ('employer_work_place', models.CharField(blank=True, max_length=100, null=True)),
                ('employer_company', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='agency', to='api.recuitmentagency')),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Workers',
            },
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.RemoveField(
            model_name='property',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='property',
            name='verified_by',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]