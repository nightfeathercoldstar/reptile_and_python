from pyecharts.charts import Map
map=Map()
data=[
    ("北京",99),
    ("上海",199),
    ("湖南",299),
    ("台湾",399),
    ("广东",499)
]
map.add("测试地图",data,"china")
map.render()