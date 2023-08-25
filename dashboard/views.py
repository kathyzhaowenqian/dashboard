from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from anglissData.pandasDataAPI.AnglissDataModel import pickDateRange, DashboardData,InitData
from dashboard.models import SalesOrderTotal,CustomerInfo


# Create your views here.
class SalesData(View):

    def get(self, request):
      
        return render(request, 'dashboards_pink/index.html')


class SalesDataDetail(View):

    # def __init__(self):
    #     self.totaldf = pickDateRange()
    #     self.chosen2020_df = self.totaldf.chooseDateRange(
    #         '2020-01-01', '2020-12-31')
    #     self.chosen2019_df = self.totaldf.chooseDateRange(
    #         '2019-01-01', '2019-12-31')

    def get(self,request):

        # 获取 SaleOrderTotal和customerInfo 的queryset
        saledata_queryset = SalesOrderTotal.objects.all()
        customerinfo_queryset = CustomerInfo.objects.all()
        # 把上面的两个queryset装换成 dataframe
        saledata_df = saledata_queryset.to_dataframe()
        customerinfo_df = customerinfo_queryset.to_dataframe()
        
        # 初始化数据(合并customerinfo表  并做清洗)
        saledata_df = InitData(customerinfo_df,saledata_df)
        #生成实例化对象，传入被清洗后的总数据，这个对象开始有了skulist和选择时间段的函数的功能了
        totaldf = pickDateRange(saledata_df)
        
        #根据上述生成的实例化对象，开始调用选择时间段的函数功能
        chosen2020_df = totaldf.chooseDateRange(
            '2020-01-01', '2020-12-31')
        chosen2019_df = totaldf.chooseDateRange(
            '2019-01-01', '2019-12-31')

        #生成dashboard图表中的data 的类的实例化对象，其中totaldf是上述pickDateRange实例化对象（给sku数据用）
        dashboarddata_obj= DashboardData(
            chosen2020_df, chosen2019_df,totaldf)

        MonthlyCompareLine = dashboarddata_obj.MonthlyCompareLine()        
        RegionComparePie = dashboarddata_obj.RegionComparePie()        
        ChannelComparePie = dashboarddata_obj.ChannelComparePie()
        SKUComparebar = dashboarddata_obj.SKUComparebarandline()  
        CustomerComparebar = dashboarddata_obj.CustomerComparebarandline()            
        SalesmanComparebar = dashboarddata_obj.SalesmanComparebar_race_origin()
        SalesmanComparebar_cumsum=dashboarddata_obj.SalesmanComparebar_race_cumsum()
                    
        result1 = {'code': 200, "MonthlyCompareLine": MonthlyCompareLine,
                   'RegionComparePie': RegionComparePie, 'ChannelComparePie': ChannelComparePie,
                   'SKUComparebar':SKUComparebar,'CustomerComparebar':CustomerComparebar,
                   'SalesmanComparebar':SalesmanComparebar,'SalesmanComparebar_cumsum':SalesmanComparebar_cumsum
                    }

        return JsonResponse(result1)



class Test404(View):
    def get(self,request):
        return render(request,'dashboards_pink/404.html')

class Barrace(View):
    def get(self,request):
        return render(request,'dashboards_pink/barrace.html')