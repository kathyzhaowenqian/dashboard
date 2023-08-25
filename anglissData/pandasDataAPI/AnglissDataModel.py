# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 00:58:33 2022

@author: zhang
"""

import pandas as pd
import numpy as np

# 返回一个 Connection 对象
# db_conn = pymysql.connect(
#     host='47.100.100.241',
#     port=13306,
#     user='kathy',
#     password='83305136',
#     database='anglissdata',
#     charset='utf8'
# )
# customerinfo_sql = "select * from customerinfo"
# saledata_sql = "select * from salesordertotal"

# customerinfo_df = pd.read_sql(customerinfo_sql, con=db_conn)
# saledata_df = pd.read_sql(saledata_sql, con=db_conn)

    # 合并客户信息表
def InitData(customerinfo_df,saledata_df):
    saledata_df = pd.merge(saledata_df, customerinfo_df,
                        on='customerid', how='left')
    saledata_df.drop(columns=['id', 'Customer', 'warehouse',
                    'contact', 'address', 'Channel'], inplace=True)

    # 整理时间格式
    saledata_df['ordertime'] = pd.to_datetime(saledata_df['ordertime'])
    saledata_df['year'] = saledata_df['ordertime'].dt.year
    saledata_df['month'] = saledata_df['ordertime'].dt.month

    # 分季度
    season_dict = {1: 'Q1', 2: 'Q1', 3: 'Q1',
                4: 'Q2', 5: 'Q2', 6: 'Q2',
                7: 'Q3', 8: 'Q3', 9: 'Q3',
                10: 'Q4', 11: 'Q4', 12: 'Q4',
                }
    saledata_df['season'] = saledata_df['month'].map(season_dict)

    return saledata_df
# =======================================================================


def monthlyRevenue(data):
    monthlyRevenue = data.groupby('month')['Value'].sum()
    return monthlyRevenue


def QuarterlyRevenue(data):
    QuarterlyRevenue = data.groupby('season')['Value'].sum()
    return QuarterlyRevenue

# 每时间段SKU销售额函数


def totalRevenueBySKU(data):
    # pandas 函数里
    totalRevenueBySKU = data.groupby('skuid')['Value'].sum()
    # result 返回的是当月的 每个sku销售收入的series
    # 理想结果 index 是skuid, value 是收入
    return totalRevenueBySKU
# 每时间段客户销售额函数


def totalRevenueByCustomer(data):
    totalRevenueByCustomer = data.groupby('customername')['Value'].sum()
    return totalRevenueByCustomer
# 每时间段区域销售额函数


def totalRevenueByRegion(data):
    totalRevenueByRegion = data.groupby('Region')['Value'].sum()
    return totalRevenueByRegion
# 每时间段渠道销售额函数


def totalRevenueByChannel(data):
    totalRevenueByRegion = data.groupby('channel')['Value'].sum()
    return totalRevenueByRegion
# 每时间段销售人员销售额函数


def totalRevenueBysalesman(data):
    totalRevenueBysalesman = data.groupby('salesman')['Value'].sum()
    return totalRevenueBysalesman


def monthlyGP(data):
    monthlyGP = data.groupby('month')['GP'].sum()
    return monthlyGP


def QuarterlyGP(data):
    QuarterlyGP = data.groupby('season')['GP'].sum()
    return QuarterlyGP
# 每时间段SKU GP函数


def totalGPBySKU(data):
    # pandas 函数里
    totalGPBySKU = data.groupby('skuid')['GP'].sum()
    # result 返回的是当月的 每个sku销售收入的series
    # 理想结果 index 是skuid, value 是收入
    return totalGPBySKU
# 每时间段客户GP函数


def totalGPByCustomer(data):
    totalGPByCustomer = data.groupby('customername')['GP'].sum()
    return totalGPByCustomer
# 每时间段区域GP函数


def totalGPByRegion(data):
    totalGPByRegion = data.groupby('Region')['GP'].sum()
    return totalGPByRegion
# 每时间段渠道GP函数


def totalGPByChannel(data):
    totalGPByChannel = data.groupby('channel')['GP'].sum()
    return totalGPByChannel
# 每时间段销售人员GP函数


def totalGPBysalesman(data):
    totalGPBysalesman = data.groupby('salesman')['GP'].sum()
    return totalGPBysalesman

# 每月数量、每季度数量、每时间段SKU、客户、地域、渠道、销售人员Volume函数


def monthlyVolume(data):
    monthlyVolume = data.groupby('month')['Volume'].sum()
    return monthlyVolume


def QuarterlyVolume(data):
    QuarterlyVolume = data.groupby('season')['Volume'].sum()
    return QuarterlyVolume
# 每时间段SKU Volume函数


def totalVolumeBySKU(data):
    totalVolumeBySKU = data.groupby('skuid')['Volume'].sum()
    return totalVolumeBySKU
# 每时间段客户Volume函数


def totalVolumeByCustomer(data):
    totalVolumeByCustomer = data.groupby('customername')['Volume'].sum()
    return totalVolumeByCustomer
# 每时间段区域Volume函数


def totalVolumeByRegion(data):
    totalVolumeByRegion = data.groupby('Region')['Volume'].sum()
    return totalVolumeByRegion
# 每时间段渠道Volume函数


def totalVolumeByChannel(data):
    totalVolumeByChannel = data.groupby('channel')['Volume'].sum()
    return totalVolumeByChannel
# 每时间段销售人员Volume函数


def totalVolumeBysalesman(data):
    totalVolumeBysalesman = data.groupby('salesman')['Volume'].sum()
    return totalVolumeBysalesman

# =====================================================================


class pickDateRange():
    def __init__(self, salesdata):
        self.df = salesdata

    def skulist(self):
        # 拎出SKU表
        skulist_df = self.df.groupby(['skuid', 'skuname'])['Value'].sum(
        ).reset_index().drop_duplicates(subset=['skuid', 'skuname'])
        skulist_df = skulist_df.drop(['Value'], axis=1)
        return skulist_df

    def chooseDateRange(self, startDate, endDate):
        #print(startDate)
        #print(endDate)
        chooseDateRange_df = self.df[(self.df['ordertime'] >= pd.to_datetime(
            startDate)) & (self.df['ordertime'] <= pd.to_datetime(endDate))]
        return chooseDateRange_df

    # lastArgDays是计算 从今天开始前n天的 df,需要传入两个参数 今天日期(str)，以及需要查看的天数(int)
    def lastArgDays(self, today, days):
        today = pd.to_datetime(today)
        startdate = today - pd.Timedelta('{} days'.format(days))
        result_df = self.df[(self.df['ordertime'] >= startdate)
                            & (self.df['ordertime'] <= today)]
        return result_df

 # =========================================================================


class DashboardData():
    def __init__(self, chosen2020_df, chosen2019_df,pickDateRange_obj):#传入选择时段类的实例化对象，方便sku那里整理
        self.chosen2020_df = chosen2020_df
        self.chosen2019_df = chosen2019_df
        self.pickDateRange_obj = pickDateRange_obj

    def ChosenTotalcompare(self):
        Chosen2020Revenue = self.chosen2020_df['Value'].sum()
        Chosen2019Revenue = self.chosen2019_df['Value'].sum()

        Chosen2020Volume = self.chosen2020_df['Volume'].sum()
        Chosen2019Volume = self.chosen2019_df['Volume'].sum()

        Chosen2020GP = self.chosen2020_df['GP'].sum()
        Chosen2019GP = self.chosen2019_df['GP'].sum()

        Chosencompare = pd.DataFrame({'2019': [Chosen2019Volume, Chosen2019Revenue, Chosen2019GP], '2020': [
                                     Chosen2020Volume, Chosen2020Revenue, Chosen2020GP]})
        Chosencompare.index = ['Volume', 'Value', 'GP']
        return Chosencompare

    def DrawTotalBar(self):
        TotalCompare_xaxis = self.ChosenTotalcompare().index.tolist()

        TotalCompare2019_yaxis = self.ChosenTotalcompare()[
            '2019'].values.tolist()
        TotalCompare2020_yaxis = self.ChosenTotalcompare()[
            '2020'].values.tolist()

        result = {}
        result['total_bar'] = {}
        result['total_bar']['x_axis'] = TotalCompare_xaxis
        result['total_bar']['2019_yaxis'] = TotalCompare2019_yaxis
        result['total_bar']['2020_yaxis'] = TotalCompare2020_yaxis
        return result

    def MonthlyCompareLine(self):
        monthlyRevenue2020 = monthlyRevenue(self.chosen2020_df)
        monthlyRevenue2019 = monthlyRevenue(self.chosen2019_df)
        result = {}
        result['Monthly_value_line'] = {}
        result['Monthly_value_line']['x_axis'] = monthlyRevenue2020.index.tolist()
        result['Monthly_value_line']['2019_yaxis'] = monthlyRevenue2019.values.tolist()
        result['Monthly_value_line']['2020_yaxis'] = monthlyRevenue2020.values.tolist()
        return result

    def RegionComparePie(self):
        RegionValue2020 = totalRevenueByRegion(self.chosen2020_df)
        RegionValue2019 = totalRevenueByRegion(self.chosen2019_df)
        result = {}
        result['Region_value_pie'] = {}
        result['Region_value_pie']['2020_pie'] = []
        result['Region_value_pie']['2019_pie'] = []
        for i in RegionValue2020.index.tolist():
            element = {}
            element['value'] = RegionValue2020[i]
            element['name'] = i
            result['Region_value_pie']['2020_pie'].append(element)
        for i in RegionValue2019.index.tolist():
            element = {}
            element['value'] = RegionValue2019[i]
            element['name'] = i
            result['Region_value_pie']['2019_pie'].append(element)
        return result

    def RegionCompareRadar(self):
        RegionValue2020 = totalRevenueByRegion(self.chosen2020_df)
        RegionValue2019 = totalRevenueByRegion(self.chosen2019_df)
        result = {}
        result['Region_value_radar'] = {}
        result['Region_value_radar']['indicator'] = []

        for i in RegionValue2020.index.tolist():
            element = {}
            element['name'] = i
            if RegionValue2020[i] <= RegionValue2019[i]:
                element['max'] = RegionValue2019[i]+1000
            else:
                element['max'] = RegionValue2020[i]+1000
            result['Region_value_radar']['indicator'].append(element)

        radarvalue2020 = {}
        radarvalue2020['value'] = RegionValue2020.values.tolist()
        radarvalue2020['name'] = '2020Value'
        radarvalue2019 = {}
        radarvalue2019['value'] = RegionValue2019.values.tolist()
        radarvalue2019['name'] = '2019Value'
        result['Region_value_radar']['data'] = [radarvalue2020, radarvalue2019]
        return result

    def ChannelComparePie(self):
        ChannelValue2020 = totalRevenueByChannel(self.chosen2020_df)
        ChannelValue2019 = totalRevenueByChannel(self.chosen2019_df)
        result = {}
        result['Channel_value_pie'] = {}
        result['Channel_value_pie']['2020_pie'] = []
        result['Channel_value_pie']['2019_pie'] = []
        for i in ChannelValue2020.index.tolist():
            element = {}
            element['value'] = ChannelValue2020[i]
            element['name'] = i
            result['Channel_value_pie']['2020_pie'].append(element)
        for i in ChannelValue2019.index.tolist():
            element = {}
            element['value'] = ChannelValue2019[i]
            element['name'] = i
            result['Channel_value_pie']['2019_pie'].append(element)
        return result

    def ChannelCompareRadar(self):
        ChannelValue2020 = totalRevenueByChannel(self.chosen2020_df)
        ChannelValue2019 = totalRevenueByChannel(self.chosen2019_df)
        result = {}
        result['Channel_value_radar'] = {}
        result['Channel_value_radar']['indicator'] = []

        for i in ChannelValue2020.index.tolist():
            element = {}
            element['name'] = i
            if ChannelValue2020[i] <= ChannelValue2019[i]:
                element['max'] = ChannelValue2019[i]+1000
            else:
                element['max'] = ChannelValue2020[i]+1000
            result['Channel_value_radar']['indicator'].append(element)

        radarvalue2020 = {}
        radarvalue2020['value'] = ChannelValue2020.values.tolist()
        radarvalue2020['name'] = '2020Value'
        radarvalue2019 = {}
        radarvalue2019['value'] = ChannelValue2019.values.tolist()
        radarvalue2019['name'] = '2019Value'
        result['Channel_value_radar']['data'] = [
            radarvalue2020, radarvalue2019]
        return result

    def SKUComparebarandline(self): #用到了上述的pickDateRange类的实例化对象，调用其中的skulist方法，直接生成了个sku的表格
        SKUValue2020 = totalRevenueBySKU(self.chosen2020_df)
        SKUValue2019 = totalRevenueBySKU(self.chosen2019_df)
        SKUGP2020 = totalGPBySKU(self.chosen2020_df)
        SKUGP2019 = totalGPBySKU(self.chosen2019_df)
        SKUGPpercent2020 = (SKUGP2020/SKUValue2020)
        SKUGPpercent2019 = (SKUGP2019/SKUValue2019)
        SKUcompare = pd.DataFrame(
            [SKUValue2020, SKUGPpercent2020, SKUValue2019, SKUGPpercent2019])
        SKUcompare.index = ['2020Value', '2020GP%', '2019Value', '2019GP%']
        SKUcompare = SKUcompare.T.sort_values(
            by='2020Value', ascending=False).fillna(0)
        SKUcompare = pd.merge(SKUcompare.reset_index(),
                              self.pickDateRange_obj.skulist(), on='skuid', how='left')
        result = {}
        result['SKUComparebarandline'] = {}
        result['SKUComparebarandline']['legend_data'] = [
            '2020Value', '2020GP%', '2019Value', '2019GP%']
        result['SKUComparebarandline']['x_axis'] = SKUcompare['skuname'].values.tolist()
        result['SKUComparebarandline']['2020Value_bar'] = SKUcompare['2020Value'].values.tolist()
        result['SKUComparebarandline']['2019Value_bar'] = SKUcompare['2019Value'].values.tolist()
        result['SKUComparebarandline']['2020GP_line'] = SKUcompare['2020GP%'].values.tolist()
        result['SKUComparebarandline']['2019GP_line'] = SKUcompare['2019GP%'].values.tolist()
        return result

    def CustomerComparebarandline(self):
        CustomerValue2020 = totalRevenueByCustomer(self.chosen2020_df)
        CustomerValue2019 = totalRevenueByCustomer(self.chosen2019_df)
        CustomerGP2020 = totalGPByCustomer(self.chosen2020_df)
        CustomerGP2019 = totalGPByCustomer(self.chosen2019_df)
        CustomerGPpercent2020 = (CustomerGP2020/CustomerValue2020)
        CustomerGPpercent2019 = (CustomerGP2019/CustomerValue2019)
        Customercompare = pd.DataFrame(
            [CustomerValue2020, CustomerGPpercent2020, CustomerValue2019, CustomerGPpercent2019])
        Customercompare.index = ['2020Value',
                                 '2020GP%', '2019Value', '2019GP%']
        Customercompare = Customercompare.T.sort_values(
            by='2020Value', ascending=False).fillna(0)
       

        result = {}
        result['CustomerComparebarandline'] = {}
        result['CustomerComparebarandline']['legend_data'] = [
            '2020Value', '2020GP%', '2019Value', '2019GP%']
        result['CustomerComparebarandline']['x_axis'] = Customercompare.index.tolist()
        result['CustomerComparebarandline']['2020Value_bar'] = Customercompare['2020Value'].values.tolist()
        result['CustomerComparebarandline']['2019Value_bar'] = Customercompare['2019Value'].values.tolist()
        result['CustomerComparebarandline']['2020GP_line'] = Customercompare['2020GP%'].values.tolist()
        result['CustomerComparebarandline']['2019GP_line'] = Customercompare['2019GP%'].values.tolist()
        return result

    def SalesmanComparebar_race_cumsum(self):
        # self.chosen2020_df['salesman'].replace('赵伟伟Anson', '赵伟伟', inplace=True)
        # self.chosen2020_df['salesman'] = self.chosen2020_df['salesman'].apply(
        #     lambda x: x.strip())
        salesman_pivot = pd.pivot_table(self.chosen2020_df, index=['salesman'], values=[
                                        'Value'], columns='month', aggfunc={'Value': [np.sum]}, fill_value=0)
        for i in salesman_pivot.index:
            salesman_pivot.loc[i] = salesman_pivot.loc[i].cumsum()
        salesmanvaluerank = salesman_pivot['Value', 'sum']
        salesmanvaluerank
        result = {}
        result['SalesmanComparebar_race_cumsum'] = {}
        result['SalesmanComparebar_race_cumsum']['data'] = []

        for i in salesmanvaluerank.index:
            salesdata = {}
            salesdata[i] = {}
            for j in salesmanvaluerank.columns:
                salesdata[i][j] = salesmanvaluerank.loc[i, j]
            result['SalesmanComparebar_race_cumsum']['data'].append(salesdata)
        return result

    def SalesmanComparebar_race_origin(self):
        # self.chosen2020_df['salesman'].replace('赵伟伟Anson', '赵伟伟', inplace=True)
        # self.chosen2020_df['salesman'] = self.chosen2020_df['salesman'].apply(
        #      lambda x: x.strip())
        salesman_pivot = pd.pivot_table(self.chosen2020_df, index=['salesman'], values=[
                                        'Value'], columns='month', aggfunc={'Value': [np.sum]}, fill_value=0)
        salesmanvaluerank = salesman_pivot['Value', 'sum']
        salesmanvaluerank
        result = {}
        result['SalesmanComparebar_race_origin'] = {}
        result['SalesmanComparebar_race_origin']['data'] = []

        for i in salesmanvaluerank.index:
            salesdata = {}
            salesdata[i] = {}
            for j in salesmanvaluerank.columns:
                salesdata[i][j] = salesmanvaluerank.loc[i, j]
            result['SalesmanComparebar_race_origin']['data'].append(salesdata)
        return result
