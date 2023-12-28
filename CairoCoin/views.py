from django.http import JsonResponse
from .models import *
from .serializers import *
from .functions import *
from rest_framework.decorators import api_view
from dateutil.relativedelta import relativedelta
import json



@api_view(['GET'])
def index(request):
    x_ = x.objects.last()
    x_data = XSerializer(x_)

    binance1 = binance.objects.last()
    binance_data = binanceSerializer(binance1)

    binance2_ = binance2.objects.last()
    binance2_data = binance2Serializer(binance2_)

    blackmarket1 = blackmarket.objects.last()
    blackmarket_data = blackmarketSerializer(blackmarket1)
    blackmarket_data_2 = blackmarket2Serializer(blackmarket1)

    bankrate_ = bankrate.objects.last()
    bankrate_data = bankrateSerializer(bankrate_)

    ForeignCurrency = blackmarket2.objects.last()
    ForeignCurrency_data = blackmarket3Serializer(ForeignCurrency)

    arbitrageStocks = arbitrage.objects.last()
    arbitrageStocks_data = arbitrageStocks_Serializer(arbitrageStocks)
    arbitrageStocks_time_data = arbitragetime_Serializer(arbitrageStocks)

    arbitrage_ = arbitrage2.objects.last()
    arbitrage_data = arbitrage_Serializer(arbitrage_)

    gold_gram_price = gold_Final.objects.last()
    gold_gram_buy_data = GoldGramBuySerializer(gold_gram_price)
    gold_gram_sell_data = GoldGramSellSerializer(gold_gram_price)

    gold2_ = gold2.objects.last()
    gold_gram_rate_data = GoldGramRateSerializer(gold2_)
    gold_dollar_data = GoldDollarSerializer(gold2_)

    gold_global = gold_usd.objects.last()
    gold_global_data = GoldGlobalSerializer(gold_global)

    gold_ingot = gold_Final_ingot.objects.last()
    gold_ingot_buy_data = GoldIngotBuySerializer(gold_ingot)
    gold_ingot_sell_data = GoldIngotSellSerializer(gold_ingot)

    credit_rating_sp = creditRating.objects.filter(Agency = 'S&P').last()
    credit_rating_sp_data = CreditRatingSerializer(credit_rating_sp)

    credit_rating_m = creditRating.objects.filter(Agency = "Moody's").last()
    credit_rating_m_data = CreditRatingSerializer(credit_rating_m)
    
    response = {
        "status": "success",
        "message": "Request successful",
    }

    response["data"] = {
        'X': x_data.data,

        'Binance': {
            'Trading': binance_data.data,
            'Rate': binance2_data.data
        },

        'BlackMarket': {
            'Trading': blackmarket_data.data,
            'Rate': blackmarket_data_2.data
        },

        'Bank': bankrate_data.data,

        'ForeignCurrencyBlackMarket': ForeignCurrency_data.data,

        'Cib': {
            'Data': arbitrage_data.data,
            'Details': {
                'Stocks': arbitrageStocks_data.data,
                'Market': arbitrageStocks_time_data.data
            }
        },

        'Gold': {
            'Gram': {
                'Buy': gold_gram_buy_data.data,
                'Sell': gold_gram_sell_data.data,
                'Rate': gold_gram_rate_data.data,
                'GlobalPrice': gold_global_data.data
            },

            'Dollar': gold_dollar_data.data,

            'Ingot': {
                'Buy': gold_ingot_buy_data.data,
                'Sell': gold_ingot_sell_data.data
            }
        },

        'CreditRating': {
            'S&P': credit_rating_sp_data.data,
            "Moody's": credit_rating_m_data.data
        }      
    }    
    return JsonResponse(response)


@api_view(['GET'])
def history(request):
    indicator = request.GET.get("Indicator")
    unit = request.GET.get("Unit")
    period = request.GET.get("Period")

    unit_mapping = {'Hour': 'hours', 'Day': 'days', 'Month': 'months'}

    field_mapping = {
        'Binance': 'bi_buy',
        'BlackMarket': 'bm_buy',
        'BankRate': 'br_usd2egp',
        'CIB': 'cib_comi2cbkd',
        'Gold24': 'gold_24',
        'Gold21': 'gold_21',
        'GoldDollar': 'gold_dollar',
        'GoldGlobal': 'gold_usd'
    }

    field = field_mapping.get(indicator)

    if not field:
        return JsonResponse({'error': 'Invalid indicator'}, status=400)

    if unit not in unit_mapping:
        return JsonResponse({'error': 'Invalid unit'}, status=400)
    
    model = history_hour if unit == "Hour" else history_day
    
    time = datetime.now(timezone.utc) - relativedelta(**{unit_mapping[unit]: int(period)})

    first = model.objects.values('time').first()
    last = model.objects.values('time').last()

    # Check if first and last are not None before proceeding
    if first and last:
        time_difference = last['time'] - first['time']

        if unit == "Hour":
            # Convert seconds to hours
            limit = time_difference.total_seconds() / 3600 + 1
        elif unit == "Day":
            # Convert seconds to days
            limit = time_difference.total_seconds() / (3600 * 24) + 1
        elif unit == "Month":
            # Calculate the difference in months
            limit = time_difference.total_seconds() / (3600 * 24 * 30) + 1

        # Now 'limit' represents the time difference in the selected unit
    else:
        # Handle the case where first or last is None
        limit = 0

    response = {
        "status": "success",
        "message": "Request successful",
    }

    response["UnitLimit"] = int(limit)

    dic = model.objects.filter(time__gte=time).values('time', field).order_by('-time')

    response["data"] = [{'Time': item['time'], 'Value': item[field]} for item in dic]
   
    return JsonResponse(response, safe=False)



@api_view(['GET'])
def historyCreditRating(request):

    credit_rating_sp = creditRating.objects.filter(Agency = 'S&P').order_by('-time')
    credit_rating_sp_data = []

    for rate in credit_rating_sp :
        credit_rating_sp_data.append(CreditRatingSerializer(rate).data)

    credit_rating_m = creditRating.objects.filter(Agency = "Moody's").order_by('-time')
    credit_rating_m_data = []

    for rate in credit_rating_m :
        credit_rating_m_data.append(CreditRatingSerializer(rate).data)

    response = {
        "status": "success",
        "message": "Request successful",
    }

    response["data"] = {  
            'S&P': credit_rating_sp_data,
            "Moody's": credit_rating_m_data       
    }    
   
    return JsonResponse(response, safe=False)
   



@api_view(['POST'])
def Update5Min(request):
    data = json.loads(request.body)
    # Helper function to save objects
    def save_instance(model, instance_data):
        obj = model.objects.create(**instance_data)
        obj.save()
    # Create and save sarf object
    save_instance(sarf, data["blackMarket"]["sarf"])

    # Create and save egcurrency object
    save_instance(egcurrency, data["blackMarket"]["egcurrency"])

    # Create and save GPN object
    save_instance(GPN, data["blackMarket"]["GPN"])

    # Create and save realegp object
    save_instance(realegp, data["blackMarket"]["realegp"])

    # Create and save parallelrate object
    save_instance(parallelrate, data["blackMarket"]["parallelrate"])

    # Create and save souqtoday object
    save_instance(souqtoday, data["blackMarket"]["souqtoday"])

    # Create and save blackmarket object with additional ccr fields
    black_market_average_instance = data["blackMarketAverage"]
    black_market_average_instance["ccr_buy"] = round(ccr(blackmarket, "average_buy", black_market_average_instance["average_buy"]), 4)
    black_market_average_instance["ccr_sell"] = round(ccr(blackmarket, "average_sell", black_market_average_instance["average_sell"]), 4)
    save_instance(blackmarket, black_market_average_instance)

    # Create and save binance object
    save_instance(binance, data["binance"])

    # Create and save binance2 object with additional ccr fields
    binance_ccr = {
        "buy_egp_ccr": round(ccr(binance, "buy_egp", data["binance"]["buy_egp"]), 4),
        "sell_egp_ccr": round(ccr(binance, "sell_egp", data["binance"]["sell_egp"]), 4),
    }
    save_instance(binance2, binance_ccr)

    # Create and save gold_BTC object
    save_instance(gold_BTC, data["gold_BTC"])
    # Create and save gold_BTC_ingot object
    save_instance(gold_BTC_ingot, data["gold_BTC_ingot"])

    # Create and save gold_GPN object
    save_instance(gold_GPN, data["gold_GPN"])
    # Create and save gold_GPN_ingot object
    save_instance(gold_GPN_ingot, data["gold_GPN_ingot"])

    # Create and save gold_Final object
    save_instance(gold_Final, data["gold_Final"])
    # Create and save gold_Final_ingot object
    save_instance(gold_Final_ingot, data["gold_Final_ingot"])

    # Create and save gold_usd object
    save_instance(gold_usd, data["gold_usd"])
    # Create and save arbitrage object
    arbitrage_instance = {
        "comi": data["arbitrage"]["comi"],
        "egstock": (data["arbitrage"]["egstock"] == "Open"),
        "cbkd": data["arbitrage"]["cbkd"],
        "ukstock": (data["arbitrage"]["ukstock"] == "Open"),
    }
    save_instance(arbitrage, arbitrage_instance)

    # Create and save bankrate object
    bankrate_instance = data["bankrate"]
    bankrate_instance["Rub"] = round(float(rub()), 4)
    bankrate_instance["usd_ccr"] = round(ccr(bankrate, "usd", data["bankrate"]["usd"]), 4)
    save_instance(bankrate, bankrate_instance)

    # Create and save blackmarket2 object
    blackmarket2_instance = {
        "eur2egp" : round((data["blackMarketAverage"]["average_buy"] / data["bankrate"]["eur"]),4) ,
        "sar2egp" : round((data["blackMarketAverage"]["average_buy"] / data["bankrate"]["sar"]),4) ,
        "kwd2egp" : round((data["blackMarketAverage"]["average_buy"] / data["bankrate"]["kwd"]),4) ,
        "aed2egp" : round((data["blackMarketAverage"]["average_buy"] / data["bankrate"]["aed"]),4) ,
        "Qar2egp" : round((data["blackMarketAverage"]["average_buy"] / data["bankrate"]["Qar"]),4) ,
        "Rub2egp" : round((data["blackMarketAverage"]["average_buy"] / bankrate_instance["Rub"]),4) ,
    }
    save_instance(blackmarket2, blackmarket2_instance)
    # Create and save arbitrage2 object
    comi2cbkd = data["arbitrage"]["comi"] / data["arbitrage"]["cbkd"]
    arbitrage2_instance = {
        "comi2cbkd": round(comi2cbkd, 4),
        "ccr_comi2cbkd": round(ccr(arbitrage2, "comi2cbkd", comi2cbkd), 4),
    }
    save_instance(arbitrage2, arbitrage2_instance)

    # Create and save gold2 object
    gold2_instance = {
        'gold_dollar': round(data["gold_Final"]["buy24"] / data["gold_usd"]["global_price"], 4),
        'ccr_21': round(ccr(gold_Final, "buy21", data["gold_Final"]["buy21"]), 4),
        'ccr_24': round(ccr(gold_Final, "buy24", data["gold_Final"]["buy24"]), 4),
        'ccr_gold_dollar': round(ccr(gold2, "gold_dollar", data["gold_Final"]["buy24"] / data["gold_usd"]["global_price"]), 4),
    }
    save_instance(gold2, gold2_instance)

    return JsonResponse({"status": "success","message": "Update5Min successful"}, safe=False)





@api_view(['POST'])
def UpdateHour(request):
    update_x()
    return JsonResponse({"status": "success","message": "UpdateHour successful"}, safe=False)



@api_view(['POST'])
def UpdateDay(request):
    try:
        latest_credit_date = creditRating.objects.order_by('-time').first().Date
    except AttributeError:
        latest_credit_date = 0
    CreditRating(latest_credit_date)
    update_history(history_day,24)
    return JsonResponse({"status": "success","message": "UpdateDay successful"}, safe=False)



