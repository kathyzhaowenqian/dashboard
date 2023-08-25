from django.db import models
from django_pandas.managers import DataFrameManager


# Create your models here.


class SalesOrderTotal(models.Model):
    
    orderid = models.CharField('orderid', max_length=255)
    ordertime = models.DateField('ordertime',null=True)
    customerid = models.CharField('customerid', max_length=255,null=True)
    warehouse = models.CharField('warehouse', max_length=255,null=True)
    Customer = models.CharField('Customer', max_length=255,null=True)
    salesman = models.CharField('salesman', max_length=255,null=True)
    skuid = models.CharField('skuid', max_length=255,null=True)
    skuname = models.CharField('skuname', max_length=255,null=True)
    Category = models.CharField('Category', max_length=255,null=True)
    SPEC = models.CharField('SPEC', max_length=255,null=True)
    unit = models.CharField('unit', max_length=255,null=True)
    quantity = models.DecimalField('quantity', max_digits=12,decimal_places=2,null=True)
    Volume = models.DecimalField('Volume', max_digits=12,decimal_places=2,null=True)
    Value = models.DecimalField('Value', max_digits=12,decimal_places=2,null=True)
    Cost = models.DecimalField('Cost', max_digits=12,decimal_places=2,null=True)
    GP = models.DecimalField('GP', max_digits=12,decimal_places=2,null=True)
    Channel = models.CharField('Channel', max_length=255,null=True)


    objects = DataFrameManager()

    class Meta:
        db_table = 'salesordertotal'


class CustomerInfo (models.Model):
    customerid = models.CharField('customerid', max_length=255,primary_key=True)
    customername = models.CharField('customername', max_length=255,null=True)
    channel = models.CharField('channel', max_length=255, null=True)
    Region = models.CharField('Region', max_length=255,null=True)
    contact = models.CharField('contact', max_length=255,null=True)
    address = models.CharField('address', max_length=255,null=True)

    objects = DataFrameManager()

    class Meta:
        db_table = 'customerinfo'