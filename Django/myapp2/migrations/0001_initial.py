# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-24 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basiccompanyinfo',
            fields=[
                ('share_code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('share_name', models.TextField(blank=True, null=True)),
                ('english_name', models.TextField(blank=True, null=True)),
                ('company_marketname', models.TextField(blank=True, db_column='Company_MarketName', null=True)),
                ('industry', models.TextField(blank=True, null=True)),
                ('company_create_date', models.TextField(blank=True, db_column='Company_Create_Date', null=True)),
                ('company_share_open_date', models.TextField(blank=True, db_column='Company_Share_Open_Date', null=True)),
                ('kesan', models.TextField(blank=True, null=True)),
                ('company_address', models.TextField(blank=True, db_column='Company_Address', null=True)),
                ('company_summary', models.TextField(blank=True, null=True)),
                ('company_total_share', models.TextField(blank=True, null=True)),
                ('company_total_market_price', models.TextField(blank=True, null=True)),
                ('return_rate', models.TextField(blank=True, null=True)),
                ('return_per_share', models.TextField(blank=True, null=True)),
                ('return_yymm', models.TextField(blank=True, null=True)),
                ('limit_price', models.TextField(blank=True, null=True)),
                ('per', models.TextField(blank=True, null=True)),
                ('pbr', models.TextField(blank=True, null=True)),
                ('eps1', models.TextField(blank=True, null=True)),
                ('eps2', models.TextField(blank=True, null=True)),
                ('high_price_thisyear', models.TextField(blank=True, null=True)),
                ('high_price_thisyear_date', models.TextField(blank=True, null=True)),
                ('low_price_thisyear', models.TextField(blank=True, null=True)),
                ('low_price_thisyear_date', models.TextField(blank=True, null=True)),
                ('credit_buy', models.TextField(blank=True, null=True)),
                ('credit_sale', models.TextField(blank=True, null=True)),
                ('current_price', models.TextField(blank=True, null=True)),
                ('current_price_time', models.TextField(blank=True, null=True)),
                ('yestoday_price', models.TextField(blank=True, null=True)),
                ('start_price', models.TextField(blank=True, null=True)),
                ('high_price', models.TextField(blank=True, null=True)),
                ('low_price', models.TextField(blank=True, null=True)),
                ('total_trade_share', models.TextField(blank=True, null=True)),
                ('total_trade_money', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'BasicCompanyInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CaclValuesTbl',
            fields=[
                ('share_code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('data_type', models.CharField(max_length=20)),
                ('data_json', models.TextField()),
            ],
            options={
                'db_table': 'Cacl_Values_TBL',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dailyshareinfo',
            fields=[
                ('trade_date', models.DateField(primary_key=True, serialize=False)),
                ('share_code', models.CharField(max_length=4)),
                ('industry_code', models.CharField(max_length=4)),
                ('share_name', models.TextField()),
                ('start_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('finishi_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trade_total', models.BigIntegerField()),
                ('market', models.TextField()),
            ],
            options={
                'db_table': 'DailyShareInfo',
                'managed': False,
            },
        ),
    ]
