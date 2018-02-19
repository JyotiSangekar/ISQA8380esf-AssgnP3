from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
            model = Customer
            fields = ('name', 'address', 'cust_number', 'city', 'state', 'zipcode', 'email', 'email', 'cell_phone')

    # class StockSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Stock
    #         fields = ('customer','symbol', 'name', 'purchase_date','shares','purchase_price','initial_stock_value',
    #                   'current_stock_price','current_stock_value','result')