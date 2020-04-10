# import random
# #关键字参数
# def info(**dict):
#     print(dict)
# #info(name='admin',age=18)#第一种注意会跟缺省参数冲突
# d={'name':'admin','age':18}
# info(**d)#关键字参数的时序解包是两个星号


#dataZoom效果
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("商家A", Faker.days_values)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
        datazoom_opts=opts.DataZoomOpts(),
    )
    .render("bar_datazoom_slider.html")
)