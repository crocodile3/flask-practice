# -*- coding: utf-8 -*-

from numpy import *
import matplotlib.pyplot as plt


def loadDataSet(filename):
    numFeat = len(open(filename).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


def standRegres(xArr, yArr):
    """
    求回归系数
    :param xArr:
    :param yArr:
    :return:
    """
    
    xMat = mat(xArr)
    yMat = mat(yArr).T
    # 计算X矩阵乘以X转置的值
    xTx = xMat.T * xMat
    # 判断行列式是否为0
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular ,cannot do inverse")
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws


def plot_reg(xMat, yMat, ws):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xMat[:, -1].flatten().A[0], yMat.T[:, 0].flatten().A[0])
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy * ws
    ax.plot(xCopy[:, 1], yHat)
    plt.show()


def plot_mul_reg(xMat, yMat, yHat):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xSort[:, 1], yHat[srtInd])
    ax.scatter(xMat[:, -1].flatten().A[0], yMat.T[:, 0].flatten().A[0], s=2, c='red')
    plt.show()


def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))
    for j in range(m):
        diffMat = testPoint - xMat[j, :]
        weights[j, j] = exp(diffMat * diffMat.T / (-2.0 * k ** 2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular,cannot do inverse")
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws


def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat


def part_re():
    xArr, yArr = loadDataSet('ex0.txt')
    # ws = standRegres(xArr,yArr)
    xMat = mat(xArr)
    yMat = mat(yArr)
    # yHat = xMat*ws
    # plot_reg(xMat,yMat,ws)
    yHat = lwlrTest(xArr, xArr, yArr, 0.003)
    srtInd = xMat[:, 1].argsort(0)
    xSort = xMat[srtInd][:, 0, :]
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xSort[:, 1], yHat[srtInd])
    ax.scatter(xMat[:, 1].flatten().A[0], mat(yArr).T.flatten().A[0], s=2, c="red")
    plt.show()


def rssError(yArr, yHatArr):
    return ((yArr - yHatArr) ** 2).sum()


def abblone_predict():
    """
    鲍鱼年龄预测
    :return:
    """
    abX, abY = loadDataSet("abalone.txt")
    # yHat01 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 0.1)
    # yHat1 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 1)
    # yHat10 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 10)
    
    yHat01 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 0.1)
    yHat1 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 1)
    yHat10 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 10)
    
    s1 = rssError(abY[100:199], yHat01.T)
    s2 = rssError(abY[100:199], yHat1.T)
    s3 = rssError(abY[100:199], yHat10.T)
    print(s1)
    print(s2)
    print(s3)


if __name__ == '__main__':
    abblone_predict()
