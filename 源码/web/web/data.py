import json

class SourceDataDemo:

    def __init__(self):
        self.title = '可视化展板通用模板'
        self.counter = {'name': '航线数量', 'value': 4573}
        self.counter2 = {'name': '缺失值', 'value': 0}
        self.echart1_data = {
            'title': '航空公司与票价关系',
            'data': [
                {"name": "Asia", "value": 7804.175},
                {"name": "India", "value": 10000.068273092369},
                {"name": "GoAir", "value": 6587.1578947368425},
                {"name": "IndiGo", "value": 7203.933333333333},
                {"name": "JA", "value": 12642.593316519546},
                {"name": "JAB", "value": 49387.5},
                {"name": "Mc", "value": 10902.678093645485},
                {"name": "McPe", "value": 11418.846153846154},
                {"name": "SJ", "value": 5916.35632183908},
                {"name": "Vistara", "value": 6465.644444444444},
            ]
        }
        self.echart2_data = {
            'title': '航班服务分布',
            'data': [
                {"name": "单次中转", "value": 41.4},
                {"name": "不含餐食", "value": 23.7},
                {"name": "不含托运", "value": 11.4},
                {"name": "No info", "value": 23.4},
            ]
        }
        self.echarts3_1_data = {
            'title': '年龄分布',
            'data': [
                {"name": "0岁以下", "value": 47},
                {"name": "20-29岁", "value": 52},
                {"name": "30-39岁", "value": 90},
                {"name": "40-49岁", "value": 84},
                {"name": "50岁以上", "value": 99},
            ]
        }
        self.echarts3_2_data = {
            'title': '职业分布',
            'data': [
                {"name": "电子商务", "value": 10},
                {"name": "教育", "value": 20},
                {"name": "IT/互联网", "value": 20},
                {"name": "金融", "value": 30},
                {"name": "学生", "value": 40},
                {"name": "其他", "value": 50},
            ]
        }
        self.echarts3_3_data = {
            'title': '兴趣分布',
            'data': [
                {"name": "汽车", "value": 4},
                {"name": "旅游", "value": 5},
                {"name": "财经", "value": 9},
                {"name": "教育", "value": 8},
                {"name": "软件", "value": 9},
                {"name": "其他", "value": 9},
            ]
        }
        self.echart4_data = {
            'title': '时间趋势',
            'data': [
                {"name": "票价均值", "value": [11531, 6358, 10810, 10328]},
                {"name": "航班次数", "value": [1094, 241, 1239, 1963]},
            ],
            'xAxis': ['3月', '4月', '5月', '6月'],
        }
        self.echart5_data = {
            'title': '天气与票价',
            'data': [
                {"name": "多云晴", "value": 11356.283100107643},
                {"name": "雨阴", "value": 11083.470588235294},
                {"name": "晴", "value": 10857.237012987012},
                {"name": "晴雨", "value": 10518.621276595744},
                {"name": "雨", "value": 10409.500910746812},
                {"name": "多云雨", "value": 10271.721428571429},
                {"name": "晴多云", "value": 9784.915549597856},
                {"name": "多云", "value": 9779.902985074626},# 5785.5
                {"name": "多云阴", "value": 5785.5},
                {"name": "雨晴", "value": 5747.1},
                {"name": "雨多云", "value": 5183.933333333333},
            ]
        }
        self.echart6_data = {
            'title': '斯皮尔曼相关系数影响因素分析',
            'data': [
                {"name": "航空公司", "value": 0.1907442704225672, "value2": 0.1907442704225672, "color": "01", "radius": ['59%', '70%']},
                {"name": "日期", "value": -0.0770130835137839, "value2": -0.0770130835137839, "color": "02", "radius": ['49%', '60%']},
                {"name": "出发时间", "value": 0.11625763547281855, "value2": 0.11625763547281855, "color": "03", "radius": ['39%', '50%']},
                {"name": "风向", "value": 0.14803283876592255, "value2": 0.14803283876592255, "color": "04", "radius": ['29%', '40%']},
                {"name": "停站数", "value": 0.16117754787703584, "value2": 0.16117754787703584, "color": "05", "radius": ['20%', '30%']},
            ]
        }
        self.map_1_data = {
            'symbolSize': 0,
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart

class SourceData(SourceDataDemo):

    def __init__(self):
        super().__init__()
        self.title = '新德里-科钦航线数据可视化大屏'