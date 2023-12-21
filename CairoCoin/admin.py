from django.contrib import admin
from .models import binance, binance2, blackmarket, blackmarket2, bankrate, gold_BTC, gold_BTC_ingot, gold_usd, gold2, arbitrage, arbitrage2, creditRating, blackmarket3, history_hour, history_day, x

class binanceAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "buy_egp", "sell_egp")

class binance2Admin(admin.ModelAdmin):
    list_display = ("id", "time", "buy_egp_ccr", "sell_egp_ccr")

class blackmarketAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "sarf_buy", "sarf_sell", "eg_buy", "eg_sell", "gpn_buy", "real_buy", "parallel_sell")

class blackmarket2Admin(admin.ModelAdmin):
    list_display = ("id", "time", "average_buy", "average_sell", "ccr_buy", "ccr_sell")

class bankrateAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "usd", "eur", "sar", "kwd", "aed", "usd_ccr")

class gold_btcAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "buy21", "sell21", "buy24", "sell24")

class gold_btc_ingotAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "buy_5g", "sell_5g", "buy_10g", "sell_10g", "buy_20g", "sell_20g", "buy_ounce", "sell_ounce", "buy_50g", "sell_50g", "buy_100g", "sell_100g", "buy_halfPound", "sell_halfPound", "buy_pound", "sell_pound")

class gold_usdAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "global_price")
    
class gold2Admin(admin.ModelAdmin):
    list_display = ("id", "time", "gold_dollar", "ccr_21", "ccr_24", "ccr_gold_dollar")

class arbitrageAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "cbkd", "ukstock", "comi", "egstock")

class arbitrage2Admin(admin.ModelAdmin):
    list_display = ("id", "time", "comi2cbkd", "ccr_comi2cbkd")

class creditRatingAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "Agency", "Rating", "Outlook", "Date")   

class blackmarket3Admin(admin.ModelAdmin):
    list_display = ("id", "time", "eur2egp", "sar2egp", "kwd2egp", "aed2egp")

class history_hourAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "bm_buy", "bm_ccr_buy", "bi_buy", "bi_ccr_buy", "br_usd2egp", "br_ccr_usd2egp", "cib_comi2cbkd", "cib_ccr_comi2cbkd", "gold_24", "gold_21", "gold_dollar", "gold_ccr_dollar", "gold_usd")

class history_dayAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "bm_buy", "bm_ccr_buy", "bi_buy", "bi_ccr_buy", "br_usd2egp", "br_ccr_usd2egp", "cib_comi2cbkd", "cib_ccr_comi2cbkd", "gold_24", "gold_21", "gold_dollar", "gold_ccr_dollar", "gold_usd")

class xAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "rate", "index")

admin.site.register(binance, binanceAdmin)
admin.site.register(binance2, binance2Admin)
admin.site.register(blackmarket, blackmarketAdmin)
admin.site.register(blackmarket2, blackmarket2Admin)
admin.site.register(bankrate, bankrateAdmin)
admin.site.register(gold_BTC, gold_btcAdmin)
admin.site.register(gold_BTC_ingot, gold_btc_ingotAdmin)
admin.site.register(gold_usd, gold_usdAdmin)
admin.site.register(gold2, gold2Admin)
admin.site.register(arbitrage, arbitrageAdmin)
admin.site.register(arbitrage2, arbitrage2Admin)
admin.site.register(creditRating, creditRatingAdmin)
admin.site.register(blackmarket3, blackmarket3Admin)
admin.site.register(history_hour, history_hourAdmin)
admin.site.register(history_day, history_dayAdmin)
admin.site.register(x, xAdmin)



