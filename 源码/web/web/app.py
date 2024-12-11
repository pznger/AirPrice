import pandas as pd
from flask import Flask, render_template, jsonify, request
from data import *

app = Flask(__name__)
app.config.from_object('config')

# 读取数据集
train_df = pd.read_excel("F:\\endWork\\merged_data.xlsx")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/people')
def people():
    data = SourceData()
    return render_template('green.html', form=data, title=data.title)

@app.route('/model_predict')
def model_predict():
    return render_template('model_predict.html')


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 特征选择
features = ['Airline', 'Date_of_Journey', 'Source', 'Destination', 'Route',
       'Dep_Time', 'Arrival_Time', 'Duration', 'Total_Stops',
       'Additional_Info', '最高温度', '最低温度', 'AQI', '风向', '降水量', '天气']

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
for column in train_df.columns:
    if train_df[column].dtype == 'object':
        train_df[column] = label_encoder.fit_transform(train_df[column])

X = train_df[features]
y = train_df['Price']

# 划分训练集和测试集
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.1, random_state=42)

# 使用随机森林回归模型
rf_model = RandomForestRegressor()

# 模型训练
rf_model.fit(X_train, y_train)

# 预测并评估模型
y_pred = rf_model.predict(X_valid)
mse = mean_squared_error(y_valid, y_pred)
print("Mean Squared Error:", mse)




@app.route('/submit_and_predict', methods=['POST'])
def submit_and_predict():
    # 获取上传的文件
    test_file = request.files['file']
    filename = test_file.filename
    # 保存上传的文件
    test_file_path = './data/{}'.format(filename)
    test_file.save(test_file_path)

    # 读取测试集数据
    test_data = pd.read_excel(test_file_path)
    orignal_test_data = test_data

    # 特征选择
    X_test = test_data[features]

    for column in X_test.columns:
        if X_test[column].dtype == 'object':
            X_test[column] = label_encoder.fit_transform(X_test[column])

    print('-------X_test-------')
    print(X_test)

    # 模型预测
    print('-------test1-------')
    y_pred = rf_model.predict(X_test)

    header = ''
    cols = [
        '预测票价', '航空公司', '日期', '出发地', '目的地', '路线',
       '起飞时间', '到达时间', '途径时间', '停留地数',
       '提供服务', '最高温度', '最低温度', 'AQI', '风向', '降水量', '天气'
            ]

    for col in cols:
        if col == '预测':
            header += '<th style="color: red">' + col + '</th>'
        else:
            header += '<th>'+col+'</th>'
    print('-------test2-------')

    rows = ''
    test_data_orignal = pd.read_excel(test_file_path)
    X_test_orignal = test_data_orignal[features]
    for i in range(len(y_pred)):
        row = '<tr><td>{}</td>'.format(y_pred[i])
        #print(X_test)
        for d in X_test_orignal.iloc[i]:
            # print("------------",d)
            row += '<td>' + str(d) + '</td>'
        row += '</tr>'
        rows += row
    print('-------test3-------')

    return jsonify({
         'success': True,
        'acc': 0,
        'precision': 0,
        'recall': 0,
        'header': header,
        'rows': rows
    })


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3389)