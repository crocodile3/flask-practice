# -*- coding: utf-8 -*-

from math import *

from numpy import *


def loadsimpData():
    datMat = matrix([
        [1., 2.1],
        [2., 1.1],
        [1.3, 1.],
        [1., 1.],
        [2., 1.]
    ])
    classLabels = [1., 1., -1., -1., 1.]
    return datMat, classLabels


def stumpClassify(dataMatix, dimen, threshVal, threshIneq):
    """
    通过阈值比较对数据进行分类
    :param dataMatix:
    :param dimen:
    :param threshVal:
    :param threshIneq:
    :return:
    """
    retArray = ones((shape(dataMatix)[0], 1))
    if threshIneq == "lt":
        retArray[dataMatix[:, dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatix[:, dimen] > threshVal] = -1.0
    return retArray


def buildStump(dataArray, classLabels, D):
    """
    构建单层决策树函数，
    找到数据集上的最佳单层决策树
    :param dataArray:数据矩阵
    :param classLabels:标签向量
    :param D:基于数据权重的向量D
    :return:
    """
    # 将特征值和标签值转为数组
    dataMat = mat(dataArray)
    labelsMat = mat(classLabels).T
    m, n = shape(dataMat)
    # 步长设为10
    numSteps = 10.0
    # 最佳单层决策树
    bestStump = {}
    # 初始化最小误差,无穷大
    minError = inf
    # 定义一个最好的预测标签结果
    bestclasEst = mat(zeros((m, 1)))
    # 遍历每个特征值
    for i in range(n):
        # 特征的最小值
        rangeMin = dataMat[:, i].min()
        # 特征的最大值
        rangeMax = dataMat[:, i].max()
        stepSize = (rangeMax - rangeMin) / numSteps
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']:
                threshVal = rangeMin + float(j) * stepSize
                predictedVal = ones((m, 1))
                if inequal == 'lt':
                    predictedVal[dataMat[:, i] <= threshVal] = -1.0
                else:
                    predictedVal[dataMat[:, i] > threshVal] = -1.0
                # 预测正确为0，错误为1
                errorArr = ones((m, 1))
                errorArr[predictedVal == labelsMat] = 0
                weightedError = float(D.T * errorArr)
                # print("dimen:%d,thresh:%.2f,thresh inequal:,%s,weighted error: %.3f"%(i,threshVal,inequal,weightedError))
                # 得到最小的误差值
                if weightedError < minError:
                    minError = weightedError
                    bestclasEst = predictedVal.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestclasEst


def adaBoostTrainDS(dataArr, classLabels, numIt=40):
    """
    adaBoost算法训练函数
    :param dataArr:数据集
    :param classLabels: 类别标签
    :param numIt: 迭代次数，需要用户指定（注：在迭代过程中，当错误率为0时，即使设定的迭代次数没迭代完，迭代就会终止）
    :return:
    """
    # 创建一个弱分类器来储存数据
    weakClassArr = []
    # 获取数据集中的数目
    m = shape(dataArr)[0]
    # 创建列向量，并将值设定为1/m，表示分类数据的权重
    D = mat(ones((m, 1)) / m)
    # 每个数据点的类别估计累计值
    aggClassEst = mat(zeros((m, 1)))
    
    for i in range(numIt):
        """
        循环numIt次，直到错误率为0跳出循环
        """
        # 创建一个单层决策树
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)
        # print("D:{}".format(D.T))
        # max(error,1e-16)用于确保没有错误时不会发生除零溢出
        alpha = float(0.5 * log((1.0 - error) / max(error, 1e-16)))
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        # print("classEst:{}".format(classEst.T))
        # 计算下一次迭代中的新权重向量D
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
        D = multiply(D, exp(expon))
        D = D / D.sum()
        aggClassEst += alpha * classEst
        # print("aggClassEst:{}".format(aggClassEst.T))
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggErrors.sum() / m
        print("total error:{}".format(errorRate))
        if errorRate == 0.0:
            break
    return weakClassArr, aggClassEst


'''根据学习得到的弱分类器队列来对数据进行分类，第一个参数为数据，第二个参数为弱分类器队列'''


def adaClassify(datToClass, classifierArr):
    dataMatrix = mat(datToClass)  # do stuff similar to last aggClassEst in adaBoostTrainDS
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m, 1)))  # 用于累计分类结果
    for i in range(len(classifierArr)):  # 将数据输入、通过这m个弱分类器
        classEst = stumpClassify(dataMatrix, classifierArr[i]['dim'], classifierArr[i]['thresh'],
                                 classifierArr[i]['ineq'])
        aggClassEst += classifierArr[i]['alpha'] * classEst  # 累加分类结果
        print(aggClassEst)
    return sign(aggClassEst)  # 将累加结果输入到sign()函数中，得到最终的分类结果


def loadDataSet(filename):
    """
    加载数据
    :param filename:
    :return:
    """
    numFeat = len(open(filename).readline().split("\t"))
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat - 1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


def plotROC(predStrenghts, classLabels):
    """
    绘制ROC曲线的函数
    :param predStrenghts:numpy数组，代表分类器的预测强度
    :param classLabels: 类标签
    :return:
    """
    import matplotlib.pyplot as plt
    cur = (1.0, 1.0)
    # 用于计算AUC的值
    ySum = 0.0
    numPosClas = sum(array(classLabels) == 1.0)
    # y轴上的步长
    yStep = 1 / float(numPosClas)
    # x轴上的步长
    xStep = 1 / float(len(classLabels) - numPosClas)
    # 排序索引
    sortedIndicies = predStrenghts.argsort()
    fig = plt.figure()
    fig.clf()
    ax = plt.subplot(111)
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] == 1.0:
            delx = 0
            dely = yStep
        else:
            delx = xStep
            dely = 0
            ySum += cur[1]
        ax.plot([cur[0], cur[0] - delx], [cur[1], cur[1] - dely], c='b')
        cur = (cur[0] - delx, cur[1] - dely)
    ax.plot([0, 1], [0, 1], 'b--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title("ROC curve for AdaBoost Horse Colic Detection System")
    ax.axis([0, 1, 0, 1])
    plt.show()
    print("the Area Under the Curve is :{}".format(ySum * xStep))


if __name__ == '__main__':
    # datMat,classLabels = loadsimpData()
    # D = mat(ones((5,1))/5)
    # buildStump(datMat,classLabels,D)
    # classifierArray = adaBoostTrainDS(datMat,classLabels,9)
    # adaClassify([[5,5],[0,0]],classifierArray)
    datArr, labelArr = loadDataSet('horseColicTraining2.txt')
    classifierArray, aggClassEst = adaBoostTrainDS(datArr, labelArr, 50)
    testArr, testLabelArr = loadDataSet('horseColicTest2.txt')
    prediction10 = adaClassify(testArr, classifierArray)
    errArr = mat(ones((67, 1)))
    s = errArr[prediction10 != mat(testLabelArr).T].sum()
    plotROC(aggClassEst.T, labelArr)
