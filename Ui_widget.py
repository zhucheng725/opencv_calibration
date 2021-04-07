# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\procedure\test\widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# 导入依赖
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from xml.dom.minidom import parse
import xml.dom.minidom
import cv2
import numpy as np
import os


class Ui_Widget(object):
    # 窗口ui布置
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(959, 571)
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(680, 460, 121, 91))
        self.pushButton.setObjectName("pushButton") # 开始按钮
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 640, 400))
        self.label.setObjectName("label") # 图像显示区域
        self.textBrowser = QtWidgets.QTextBrowser(Widget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 450, 641, 111))
        self.textBrowser.setObjectName("textBrowser") # 文字输出区域
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 460, 121, 91))
        self.pushButton_2.setObjectName("pushButton_2") # 结束按钮

        self.retranslateUi(Widget)
        
        self.pushButton.clicked.connect(self.on_pushButton_1_clicked) # 启动按钮 触发 on_pushButton_1_clicked槽函数
        self.pushButton_2.clicked.connect(self.button2_clicked)# 结束按钮 触发 button2_clicked
        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.readFrame) # 定时器触发读取摄像头资源 
        
        QtCore.QMetaObject.connectSlotsByName(Widget)


    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "顶置二维码测试软件1.0"))
        self.pushButton.setText(_translate("Widget", "开始"))
        self.label.setText(_translate("Widget", "原始图像"))
        self.pushButton_2.setText(_translate("Widget", "结束"))
        

    #启动按钮
    def on_pushButton_1_clicked(self): 
        self.readXml() # 读取配置文件
        self.checkCam() # 打开摄像头
        
        
       
        
    # 结束按钮
    def button2_clicked(self): 
        self.timer1.stop() # 定时器关闭
        self.cap.release() # 释放摄像头资源
        self.close # 关闭窗口
        
        
        
        
    def readFrame(self):
        
        detectRed = 0
        detectGreen = 0
        
        ret, srcImage = self.cap.read() # 读取摄像头内容
        srcImageClone = srcImage.copy()

        m = np.zeros((srcImageClone.shape[1], srcImageClone.shape[0], 3), dtype = np.uint8)
        m[self.ROI_tl_y:self.ROI_br_y, self.ROI_tl_x:self.ROI_br_x] = srcImageClone[self.ROI_tl_y:self.ROI_br_y, self.ROI_tl_x:self.ROI_br_x] # 将指定的区域原位复制到全为0的矩阵中， 效果为指定区域有颜色，其余地方为黑色效果
        srcGray = cv2.cvtColor(m, cv2.COLOR_BGR2GRAY) # 灰度图

        ret, BinaryImage = cv2.threshold(srcGray,  80, 255, cv2.THRESH_BINARY) #二值化
        
        contours, hierarchy = cv2.findContours(BinaryImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # 边缘提取
        contoursOutside, hierarchyOutside = cv2.findContours(BinaryImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 边缘提取

        cv2.rectangle(srcImageClone, (self.ROI_tl_x,self.ROI_tl_y), (self.ROI_br_x,self.ROI_br_y), (0, 255, 255), 1, 8) # 绘制检测框区域
        
        # 面积 长宽为指定范围内提取轮廓
        # hierarchy[0][idx][2] hierarchy[0][idx][3] 大于0 为父子关系
        if len(contours) != 0 :
            for idx in range(len(contours)):
                if cv2.contourArea(contours[idx]) < self.max_area and cv2.contourArea(contours[idx]) > self.min_area:
                    if cv2.arcLength(contours[idx], True) < self.max_length and cv2.arcLength(contours[idx], True) > self.min_length:
                        if hierarchy[0][idx][2] >= 0 or hierarchy[0][idx][3] >= 0:
                            color_red = (255,0,0)
                            cv2.drawContours(srcImageClone, contours, idx,  color_red, 1, 8, hierarchy)
                            detectRed += 1
                        else:
                            color_green = (0,255,64)
                            cv2.drawContours(srcImageClone, contours, idx,  color_green, 1, 8, hierarchy)
                            detectGreen += 1

            text = "Test:" + str(self.DetectPoint) + ", Acc:" + str(detectGreen) + ", Err:" + str(len(contoursOutside) - detectGreen)

            # 判断检测是否为指定数目
            if detectRed >0 or detectGreen != self.DetectPoint:
                text = text + ", failed"
            else:
                text = text + ", success"
        else:
            text = "Test:" + str(self.DetectPoint) + ", Acc:0"  + ", Err:0" +  ", failed"
            
        cv2.putText(srcImageClone, text, (10, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 1, 8, 0) # 文字绘制到图像

        # 图像显示转换
        height, width, bytesPerComponent = srcImageClone.shape
        bytesPerLine = bytesPerComponent * width
        qimg = QtGui.QImage(srcImageClone.data, width, height, bytesPerLine,  QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(qimg))





        
        
        
        
    def readXml(self):
        # 获取路径 ， 读取xml配置文件内容
        path = os.getcwd()
        DOMTree = xml.dom.minidom.parse(path + "\\config.xml")
        collection = DOMTree.documentElement
        
        self.deviceAddr = int(collection.getElementsByTagName("deviceAddr")[0].childNodes[0].data)
        self.DetectPoint = int(collection.getElementsByTagName("DetectPoint")[0].childNodes[0].data)
        
        self.ROI_tl_x = int(collection.getElementsByTagName("ROI_tl_x")[0].childNodes[0].data)
        self.ROI_tl_y = int(collection.getElementsByTagName("ROI_tl_y")[0].childNodes[0].data)
        self.ROI_br_x = int(collection.getElementsByTagName("ROI_br_x")[0].childNodes[0].data)
        self.ROI_br_y = int(collection.getElementsByTagName("ROI_br_y")[0].childNodes[0].data)

        self.max_area = int(collection.getElementsByTagName("circle_max_area")[0].childNodes[0].data)
        self.min_area = int(collection.getElementsByTagName("circle_min_area")[0].childNodes[0].data)
        self.max_length = int(collection.getElementsByTagName("circle_max_length")[0].childNodes[0].data)
        self.min_length = int(collection.getElementsByTagName("circle_min_length")[0].childNodes[0].data)


        
    def checkCam(self):
        # 读取摄像头端口号
        self.cap =  cv2.VideoCapture(self.deviceAddr)

        
        # 判断是否打开成功
        if self.cap.isOpened() != True:
            self.textBrowser.append(' 不能打开摄像头，请检查是否插入摄像头')
        else:

            #_ = self.cap.set(3,640)
            #_ = self.cap.set(4,400)
            # 摄像头配置
            self.cap.set(6,cv2.VideoWriter.fourcc('M','J','P','G'))
            self.textBrowser.append(' 已打开摄像头')
            self.pushButton.setEnabled(False) # 开始按钮变灰
            self.timer1.start(24) # 定时器开始
            
        



if __name__ == "__main__":
    # 窗口启动
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
    
    
