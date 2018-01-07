# Generated by Django 2.0.1 on 2018-01-07 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnCallPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_ending', models.DateField(verbose_name='week ending')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(verbose_name='end date')),
                ('hours', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('u_name', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='oncallperiod',
            name='team_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='on_call_me.TeamMember'),
        ),
    ]
