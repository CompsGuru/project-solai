from django.contrib import admin
from stocks_v1.models import Stock, Tracker, Notification
from simple_history.admin import SimpleHistoryAdmin


class StockHistoryAdmin(SimpleHistoryAdmin):
    history_list_display = ['price', 'prev_price',
                            'open_price', 'percentage_change', 'max_price', 'min_price']


admin.site.register(Stock, StockHistoryAdmin)
admin.site.register(Tracker)
admin.site.register(Notification)
