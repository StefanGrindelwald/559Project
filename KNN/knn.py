import Data_Process
import pandas as pd
import numpy as np
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib

# 采用函数将结果按等级转化
def change(data):
    for i in range(len(data)):
        if 0 <= data[i] <= 9:
            data[i] = 5
        elif 10 <= data[i] <= 11:
            data[i] = 4
        elif 12 <= data[i] <= 13:
            data[i] = 3
        elif 14 <= data[i] <= 15:
            data[i] = 2
        else:
            data[i] = 1
    return data



if __name__ == "__main__":

    DataTrain = pd.read_csv("../student_performance_train.csv")
    DataTest = pd.read_csv("../student_performance_test.csv")
    Data_Process.binary(DataTrain)
    Data_Process.binary(DataTest)
    # 按等级转化
    DataTrain_Label = Data_Process.Convert2Label(DataTrain)
    DataTest_Label = Data_Process.Convert2Label(DataTest)
    # 不按等级转化
    # DataTrain_Label = DataTrain
    # DataTest_Label = DataTest

    #print(DataTest)
    #print(DataTrain_Label)
    #print(DataTest_Label)


    TrainSet = DataTrain_Label.values

    #tmp = np.array([0,2,4,12,13,14])
    #tmp = np.array([12, 13, 14, 17])
    #tmp = np.array([9])

    TrainSet_feature = TrainSet[:,-3:-1]
    TrainSet_label = TrainSet[:, -1]

    TestSet = DataTest_Label.values

    TestSet_feature = TestSet[:, -3:-1]
    TestSet_label = TestSet[:, -1]
    # print(TrainSet)
    # print(TrainSet_feature)
    # print(TrainSet_label)
    transfer = StandardScaler()

    TrainSet_feature = transfer.fit_transform(TrainSet_feature)
    TestSet_feature = transfer.fit_transform(TestSet_feature)

    estimator = KNeighborsClassifier(n_neighbors=35)
    estimator.fit(TrainSet_feature, TrainSet_label)

    predict = estimator.predict(TestSet_feature)

    # predict = change(predict)
    # TestSet_label = change(TestSet_label)

    # print(predict)
    # print(TestSet_label)

    num = 0
    for j in range(len(predict)):
        if predict[j] == TestSet_label[j]:
            num += 1

    print("outcome of Mission1：",num/len(predict))
        #print(estimator.score(TestSet_feature,TestSet_label))