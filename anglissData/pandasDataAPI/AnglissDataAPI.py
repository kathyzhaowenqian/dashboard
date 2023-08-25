# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 00:58:35 2022

@author: zhang
"""


from AnglissDataModel import pickDateRange,DashboardData

#print(pickDateRange().chooseDateRange('2020-01-01','2020-12-31'))

totaldf = pickDateRange()

chosen2020_df=totaldf.chooseDateRange('2020-01-01','2020-12-31')
chosen2019_df=totaldf.chooseDateRange('2019-01-01','2019-12-31')


#print(DashboardData(chosen2020_df,chosen2019_df).DrawTotalBar())

#print(DashboardData(chosen2020_df,chosen2019_df).MonthlyCompareLine())

#print(DashboardData(chosen2020_df,chosen2019_df).RegionComparePie())
#print(DashboardData(chosen2020_df,chosen2019_df).RegionCompareRadar())

#print(DashboardData(chosen2020_df,chosen2019_df).ChannelComparePie())
#print(DashboardData(chosen2020_df,chosen2019_df).ChannelCompareRadar())

#print(DashboardData(chosen2020_df,chosen2019_df).SKUComparebarandline())

#print(DashboardData(chosen2020_df,chosen2019_df).CustomerComparebarandline())

#print(DashboardData(chosen2020_df,chosen2019_df).SalesmanComparebar_race_cumsum())
#print(DashboardData(chosen2020_df,chosen2019_df).SalesmanComparebar_race_origin())