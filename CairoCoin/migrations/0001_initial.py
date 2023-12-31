# Generated by Django 4.2.8 on 2023-12-27 23:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='arbitrage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('comi', models.FloatField()),
                ('egstock', models.BooleanField()),
                ('cbkd', models.FloatField()),
                ('ukstock', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='arbitrage2',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('comi2cbkd', models.FloatField()),
                ('ccr_comi2cbkd', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='bankrate',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('usd', models.FloatField()),
                ('eur', models.FloatField()),
                ('sar', models.FloatField()),
                ('kwd', models.FloatField()),
                ('aed', models.FloatField()),
                ('Qar', models.FloatField()),
                ('Rub', models.FloatField()),
                ('usd_ccr', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='binance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy_egp', models.FloatField()),
                ('sell_egp', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='binance2',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy_egp_ccr', models.FloatField()),
                ('sell_egp_ccr', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='blackmarket',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('average_buy', models.FloatField()),
                ('average_sell', models.FloatField()),
                ('ccr_buy', models.FloatField()),
                ('ccr_sell', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='blackmarket2',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('eur2egp', models.FloatField()),
                ('sar2egp', models.FloatField()),
                ('kwd2egp', models.FloatField()),
                ('aed2egp', models.FloatField()),
                ('Qar2egp', models.FloatField()),
                ('Rub2egp', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='creditRating',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('Agency', models.TextField()),
                ('Rating', models.TextField()),
                ('Outlook', models.TextField()),
                ('Date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='egcurrency',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy', models.FloatField()),
                ('sell', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='gold2',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('gold_dollar', models.FloatField()),
                ('ccr_21', models.FloatField()),
                ('ccr_24', models.FloatField()),
                ('ccr_gold_dollar', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='gold_BTC',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy21', models.FloatField()),
                ('sell21', models.FloatField()),
                ('buy24', models.FloatField()),
                ('sell24', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='gold_BTC_ingot',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy_5g', models.FloatField()),
                ('sell_5g', models.FloatField()),
                ('buy_10g', models.FloatField()),
                ('sell_10g', models.FloatField()),
                ('buy_20g', models.FloatField()),
                ('sell_20g', models.FloatField()),
                ('buy_ounce', models.FloatField()),
                ('sell_ounce', models.FloatField()),
                ('buy_50g', models.FloatField()),
                ('sell_50g', models.FloatField()),
                ('buy_100g', models.FloatField()),
                ('sell_100g', models.FloatField()),
                ('buy_halfPound', models.FloatField()),
                ('sell_halfPound', models.FloatField()),
                ('buy_pound', models.FloatField()),
                ('sell_pound', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='gold_GPN',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy21', models.FloatField()),
                ('sell21', models.FloatField()),
                ('buy24', models.FloatField()),
                ('sell24', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='gold_GPN_ingot',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy_5g', models.FloatField()),
                ('sell_5g', models.FloatField()),
                ('buy_10g', models.FloatField()),
                ('sell_10g', models.FloatField()),
                ('buy_20g', models.FloatField()),
                ('sell_20g', models.FloatField()),
                ('buy_ounce', models.FloatField()),
                ('sell_ounce', models.FloatField()),
                ('buy_50g', models.FloatField()),
                ('sell_50g', models.FloatField()),
                ('buy_100g', models.FloatField()),
                ('sell_100g', models.FloatField()),
                ('buy_halfPound', models.FloatField()),
                ('sell_halfPound', models.FloatField()),
                ('buy_pound', models.FloatField()),
                ('sell_pound', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='gold_usd',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('global_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GPN',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy', models.FloatField()),
                ('sell', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='history_day',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('bm_buy', models.FloatField()),
                ('bm_ccr_buy', models.FloatField()),
                ('bi_buy', models.FloatField()),
                ('bi_ccr_buy', models.FloatField()),
                ('br_usd2egp', models.FloatField()),
                ('br_ccr_usd2egp', models.FloatField()),
                ('cib_comi2cbkd', models.FloatField()),
                ('cib_ccr_comi2cbkd', models.FloatField()),
                ('gold_24', models.FloatField()),
                ('gold_21', models.FloatField()),
                ('gold_dollar', models.FloatField()),
                ('gold_ccr_dollar', models.FloatField()),
                ('gold_usd', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='history_hour',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('bm_buy', models.FloatField()),
                ('bm_ccr_buy', models.FloatField()),
                ('bi_buy', models.FloatField()),
                ('bi_ccr_buy', models.FloatField()),
                ('br_usd2egp', models.FloatField()),
                ('br_ccr_usd2egp', models.FloatField()),
                ('cib_comi2cbkd', models.FloatField()),
                ('cib_ccr_comi2cbkd', models.FloatField()),
                ('gold_24', models.FloatField()),
                ('gold_21', models.FloatField()),
                ('gold_dollar', models.FloatField()),
                ('gold_ccr_dollar', models.FloatField()),
                ('gold_usd', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='parallelrate',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy', models.FloatField(default=0)),
                ('sell', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='realegp',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy', models.FloatField()),
                ('sell', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='sarf',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy', models.FloatField()),
                ('sell', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='souqtoday',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buy', models.FloatField()),
                ('sell', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='x',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('rate', models.FloatField()),
                ('index', models.FloatField()),
            ],
        ),
    ]
