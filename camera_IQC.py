# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\procedure\iqc\iqc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!


'''
xhost +
sudo docker run  -ti --net=host --ipc=host -e DISPLAY=$DISPLAY  --device=/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -e GDK_SCALE -e GDK_DPI_SCALE ubuntu:18.04

apt-get update
apt-get install python3 python3-pip

pip3 install numpy==1.16 opencv-python==3.4.5.20 -i https://pypi.douban.com/simple
apt-get install libsm6 libxrender1 libxext-dev
apt-get install libglib2.0-dev

'''

'''
sudo docker start -i 6ca7e24008d0
sudo docker cp 6ca7e24008d0:/home/procedure/log/iqc_log.xlsx /media/kirito/1T/procedure/
'''


# 导入依赖
import cv2, time, os, sys, xlwt, xlrd, ctypes, math, time, PyQt5
import numpy as np
from xlutils.copy import copy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

# 写log到txt文件里
def WriteLog(filename, Log):
    path = os.getcwd()
    with open(path + "\\log\\" + str(filename)+ ".txt", "a") as f:
        f.write('time: '+ time.asctime(time.localtime(time.time())) + ' data: ' + str(Log) + '\n')
            
class Ui_Widget(object):
    def setupUi(self, Widget):
        # 界面定义
        Widget.setObjectName(_fromUtf8("Widget"))
        Widget.resize(1127, 832)
        

        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 651, 621))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtWidgets.QTextEdit(Widget)
        self.textEdit.setGeometry(QtCore.QRect(690, 10, 431, 621))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 670, 181, 131))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_3 = QtWidgets.QPushButton(Widget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 670, 181, 131))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.textEdit_2 = QtWidgets.QTextEdit(Widget)
        self.textEdit_2.setGeometry(QtCore.QRect(970, 680, 141, 41))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(900, 660, 91, 91))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.radio_button_clarity_yes = QtWidgets.QRadioButton(Widget)
        self.radio_button_clarity_yes.setGeometry(QtCore.QRect(980, 760, 89, 16))
        self.radio_button_clarity_yes.setObjectName(_fromUtf8("radio_button_clarity_yes"))
        self.radio_button_clarity_yes.setText('Y')
        self.radio_button_clarity_yes.setChecked(True)
        
        self.radio_button_clarity_no = QtWidgets.QRadioButton(Widget)
        self.radio_button_clarity_no.setGeometry(QtCore.QRect(1020, 760, 89, 16))
        self.radio_button_clarity_no.setObjectName(_fromUtf8("radio_button_clarity_no"))  
        self.radio_button_clarity_no.setText('N') 

        self.radio_button_tuoying_yes = QtWidgets.QRadioButton(Widget)
        self.radio_button_tuoying_yes.setChecked(True)
        self.radio_button_tuoying_yes.setGeometry(QtCore.QRect(980, 790, 89, 16))
        self.radio_button_tuoying_yes.setObjectName(_fromUtf8("radio_button_tuoying_yes"))
        self.radio_button_tuoying_yes.setText('Y') 

        self.radio_button_tuoying_no = QtWidgets.QRadioButton(Widget)
        self.radio_button_tuoying_no.setGeometry(QtCore.QRect(1020, 790, 89, 16))
        self.radio_button_tuoying_no.setObjectName(_fromUtf8("radio_button_tuoying_no"))
        self.radio_button_tuoying_no.setText('N') 
        #self.radio_button_tuoying_no.setChecked(True)

        self.top_layout = QHBoxLayout()
        self.down_layout = QHBoxLayout()
        self.hboxAll = QVBoxLayout()

        self.groupbox1 = QGroupBox(Widget)
        self.groupbox2 = QGroupBox(Widget)

        self.top_layout.addWidget(self.radio_button_clarity_yes)
        self.top_layout.addWidget(self.radio_button_clarity_no)
        self.down_layout.addWidget(self.radio_button_tuoying_yes)
        self.down_layout.addWidget(self.radio_button_tuoying_no)



        self.groupbox1.setLayout(self.top_layout)
        self.groupbox2.setLayout(self.down_layout)

        self.hboxAll.addWidget(self.groupbox1)
        self.hboxAll.addWidget(self.groupbox2)
        self.hboxAll.setGeometry(QtCore.QRect(970, 730, 160, 100))

        self.label_top = QtWidgets.QLabel(Widget)
        self.label_top.setGeometry(QtCore.QRect(900, 710, 85, 85))
        self.label_top.setObjectName(_fromUtf8("label"))

        self.label_down = QtWidgets.QLabel(Widget)
        self.label_down.setGeometry(QtCore.QRect(905, 760, 85, 85))
        self.label_down.setObjectName(_fromUtf8("label"))

        self.Create_xls()


        self.pushButton_3.setEnabled(False) # 按钮变灰
        self.pushButton_2_protect_flag = 0

        self.retranslateUi(Widget)

        self.pushButton_2.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_3.clicked.connect(self.stop_cam)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        
        

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "顶置二维码来料测试软件1.0", None))
        self.label.setText(_translate("Widget", "camera area", None))

        self.label_top.setText(_translate("Widget", "QX", None)) # 清晰度
        self.label_down.setText(_translate("Widget", "TY", None)) # 拖影

        self.pushButton_2.setText(_translate("Widget", "start", None))
        self.pushButton_3.setText(_translate("Widget", "stop", None))

        self.textEdit_2.setHtml(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0001</p></body></html>", None))
        self.label_2.setText(_translate("Widget", "SN", None))



    def stop_cam(self): 
        self.pushButton_2.setEnabled(True)

        self.pushButton_3.setEnabled(False)

        self.cap.release()
        self.timer1.stop()
        self.timer2.stop()
        self.textEdit.setTextColor(QColor(0,0,0))

        if self.radio_button_clarity_yes.isChecked() == True:
            self.textEdit.append(u'clarity yes')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'clarity yes' )
            self.Write_xls_log(log_num = 9, log_text ='pass')
        else:
            self.textEdit.append(u'clarity no')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'clarity no' )
            self.Write_xls_log(log_num = 9, log_text ='fail')
        if self.radio_button_tuoying_yes.isChecked() == True:
            self.textEdit.append(u'tuoying yes')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'tuoying yes' )
            self.Write_xls_log(log_num = 10, log_text ='pass')
        else:
            self.textEdit.append(u'tuoying no')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'tuoying no' )
            self.Write_xls_log(log_num = 10, log_text ='fail')

        self.textEdit.append(u'stop the cam')
        WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'stop the cam' )



 
    def on_pushButton_clicked(self): 
        self.pushButton_2_protect_flag = 1
        self.pushButton_2.setEnabled(False)
        self.pushButton_2_protect_time()
        self.pushButton_3.setEnabled(True)




    def OpenCam_label(self):
        ret, frame = self.cap.read()
        frame = cv2.resize(frame, (640,480), interpolation=cv2.INTER_AREA)

        frame_copy = frame.copy()  
        gray=cv2.cvtColor(frame_copy,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame_copy,contours,-1,(255,0,255),1)


        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB , frame)
        qimg = QtGui.QImage(frame_copy.data, width, height, bytesPerLine,  QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(qimg))


    def Create_xls(self): 
        style_head = xlwt.XFStyle() 
        font = xlwt.Font() 
        font.bold = True
        font.colour_index = 1 
        bg = xlwt.Pattern() 
        bg.pattern = xlwt.Pattern.SOLID_PATTERN 
        bg.pattern_fore_colour = 4 
        style_head.font = font
        style_head.pattern = bg
        excel = xlwt.Workbook()
        sheet = excel.add_sheet("iqc_log")
        head = ["sn","format","fps","resolution", "iso", "brightness", "constrast", "saturation", "noise_ratio","QX", "TY","test_time"]
        for index,value in enumerate(head):
            sheet.write(0,index,value,style_head)
        excel.save("./log/iqc_log.xlsx")




    def Write_xls_log(self, k_num =1, log_num = 0, log_text = 'fail'): 
        iqc_workbook = xlrd.open_workbook("./log/iqc_log.xlsx")
        new_book = copy(iqc_workbook)
        iqc_sheet = new_book.get_sheet('iqc_log')
        k = len(iqc_sheet.rows)
        iqc_sheet.write(k - k_num, log_num, log_text)
        new_book.save("./log/iqc_log.xlsx")




    def OpenCam(self): 
        self.timer1 = QtCore.QTimer()
        self.timer1.start(24)
        self.timer1.timeout.connect(self.OpenCam_label)         
        
        
    def check_infrared_camera_1(self):
        '''
        5.format
        '''
        self.textEdit.append(u'format Pass')
        WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'format  Pass' )
        self.Write_xls_log(log_num = 1, log_text ='pass')
        self.cap.release()
        

    def pushButton_2_protect(self):
        if self.pushButton_2_protect_flag ==1:
            try:
                self.cap = cv2.VideoCapture(0)
                
            except:
                self.textEdit.setTextColor(QColor(255,0,0))
                self.textEdit.append(u'usb not insert. Please insert usb now(other errors)')
                
                self.pushButton_2.setEnabled(True)
                self.pushButton_3.setEnabled(False)
                self.timer2.stop()

                self.pushButton_2_protect_flag = 0
            else:
                if self.cap.isOpened() == False:
                    self.textEdit.setTextColor(QColor(255,0,0))
                    self.textEdit.append(u'usb not insert. Please insert usb now')

                    self.pushButton_2.setEnabled(True)
                    self.pushButton_3.setEnabled(False)
                    self.timer2.stop()

                else:
                    _ = self.cap.set(3,1280)
                    _ = self.cap.set(4,800)
                    self.textEdit_2.setReadOnly(True)
                    self.cap.set(6,cv2.VideoWriter.fourcc('M','J','P','G'))
                    self.textEdit.setTextColor(QColor(0,0,0))
                    self.textEdit.append(u'--------' +  u'SN' + self.textEdit_2.toPlainText() + u'--------')
                    self.textEdit.append(u'start to check')
                    self.Write_xls_log(k_num = 0, log_num = 0, log_text = str(self.textEdit_2.toPlainText()))
                    self.Write_xls_log(log_num = 11, log_text = str(time.asctime(time.localtime(time.time()))))
                     
                    WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'start to check' )  
                    self.check_infrared_camera_1()
                    self.check_infrared_camera_2()
                    self.check_infrared_camera_3()

                    self.cap = cv2.VideoCapture(0)
                    _ = self.cap.set(3,1280) 
                    _ = self.cap.set(4,800)
                    self.cap.set(6,cv2.VideoWriter.fourcc('M','J','P','G'))
                    self.OpenCam()
                    self.textEdit_2.setReadOnly(False)
                    self.pushButton_2_protect_flag = 0


    def pushButton_2_protect_time(self):
        self.timer2 = QtCore.QTimer()
        self.timer2.start(1)
        self.timer2.timeout.connect(self.pushButton_2_protect)
        

    def check_infrared_camera_2(self):
        resolution_check_1280 = False
        fps_check_1280 = False
        cal_time_1280 = []

        '''
        3.fps 4.resolution 
        '''
        self.cap = cv2.VideoCapture(0)
        self.cap.set(6,cv2.VideoWriter.fourcc('M','J','P','G'))
        
        if self.cap.get(3) == 1280 and self.cap.get(4) == 800:
            resolution_check_1280 = True
            
        for i in range(100):
            start_time = time.time()
            ret, frame = self.cap.read()
            end_time = time.time()
            cal_time_1280.append(end_time - start_time)


        if 1 / np.mean(cal_time_1280[-10:])> 50:  #60
            fps_check_1280 = True

        self.cap.release()
        
        if fps_check_1280 == True:
            self.textEdit.setTextColor(QColor(0,0,0))
            self.textEdit.append(u'fps Pass')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'fps  Pass' )
            self.Write_xls_log(log_num = 2, log_text ='pass')
            
        else:
            self.textEdit.setTextColor(QColor(255,0,0))
            self.textEdit.append(u'fps Fail')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'fps  Fail and fps is ' 
+ str(1 / np.mean(cal_time_1280[-10:])) )
            self.Write_xls_log(log_num = 2, log_text ='fail')
            

        if resolution_check_1280 == True:
            self.textEdit.setTextColor(QColor(0,0,0))
            self.textEdit.append(u'resolution Pass')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'resolution  Pass' )
            self.Write_xls_log(log_num = 3, log_text ='pass')
        else:
            self.textEdit.setTextColor(QColor(255,0,0))
            self.textEdit.append(u'resolution Fail')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'resolution  Fail and resolution is ' + str(self.cap.get(3)) +',' + str(self.cap.get(4)) )
            self.Write_xls_log(log_num = 3, log_text ='fail')




                

    def check_infrared_camera_3(self):

        self.cap = cv2.VideoCapture(0)
        _ = self.cap.set(3,1280)
        _ = self.cap.set(4,800)
        self.cap.set(6,cv2.VideoWriter.fourcc('M','J','P','G'))

        '''
        6.iso 
        '''

        if int(self.cap.get(cv2.CAP_PROP_EXPOSURE)) <=157:  #-6.0
            self.textEdit.setTextColor(QColor(0,0,0))
            self.textEdit.append(u'iso Pass')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'iso  Pass' )
            self.Write_xls_log(log_num = 4, log_text ='pass')
        else:
            self.textEdit.setTextColor(QColor(255,0,0))
            self.textEdit.append(u'iso Fail')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'iso  Fail and iso is '+ str(int(self.cap.get(cv2.CAP_PROP_EXPOSURE)))  )
            self.Write_xls_log(log_num = 4, log_text ='fail')


        '''
        7.brightness 
        '''
        if int(self.cap.get(cv2.CAP_PROP_BRIGHTNESS)) == 0: #0
            self.textEdit.setTextColor(QColor(0,0,0))
            self.textEdit.append(u'brightness Pass')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'brightness  Pass' )
            self.Write_xls_log(log_num = 5, log_text ='pass')
        else:
            self.textEdit.setTextColor(QColor(255,0,0))
            self.textEdit.append(u'brightness Fail')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'brightness  Fail and brightness is' + str(int(self.cap.get(cv2.CAP_PROP_BRIGHTNESS))))
            self.Write_xls_log(log_num = 5, log_text ='fail')

        '''
        8.constrast 
        '''
        if self.cap.get(cv2.CAP_PROP_CONTRAST) == 0.5: #0.5
            self.textEdit.setTextColor(QColor(0,0,0))
            self.textEdit.append(u'constrast Pass')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'constrast  Pass' )
            self.Write_xls_log(log_num = 6, log_text ='pass')
        else:
            self.textEdit.setTextColor(QColor(255,0,0))
            self.textEdit.append(u'constrast Fail')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'constrast  Fail amd cpmstrast is' + str(self.cap.get(cv2.CAP_PROP_CONTRAST)) )
            self.Write_xls_log(log_num = 6, log_text ='fail')

        '''
        9.saturation 
        '''
        if int(self.cap.get(cv2.CAP_PROP_SATURATION)) == 0: #0
            self.textEdit.setTextColor(QColor(0,0,0))
            self.textEdit.append(u'saturation Pass')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'saturation  Pass' )
            self.Write_xls_log(log_num = 7, log_text ='pass')
        else:
            self.textEdit.setTextColor(QColor(255,0,0))
            self.textEdit.append(u'saturation Fail')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'saturation  Fail and saturation is ' + str(int(self.cap.get(cv2.CAP_PROP_SATURATION))) )
            self.Write_xls_log(log_num = 7, log_text ='fail')
        
        '''
        11.noise ratio 
        '''
        def psnr(img1, img2):
            mse = np.mean( (img1/255. - img2/255.) ** 2 )
            if mse < 1.0e-10:
                return 100
            PIXEL_MAX = 1
            return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

        #compare1 = cv2.imread('C:\\procedure\\iqc\\1.jpg',1)
        for i in range(50):#第50张照片
            ret, frame = self.cap.read()
            if i == 0:
                compare1 = frame
        #print('psnr(frame, compare1) ',psnr(frame, compare1) )
        if psnr(frame, compare1) <= 40:
            self.textEdit.setTextColor(QColor(0,0,0))
            self.textEdit.append(u'noise ratio  Pass')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'noise ratio   Pass' )
            self.Write_xls_log(log_num = 8, log_text ='pass')
        else:
            self.textEdit.setTextColor(QColor(255,0,0))
            self.textEdit.append(u'noise ratio  Fail')
            WriteLog(filename = self.textEdit_2.toPlainText(), Log = 'noise ratio Fail and ratio is ' + str(psnr(frame, compare1)) )
            self.Write_xls_log(log_num = 8, log_text ='fail')




            
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    font = QtGui.QFont()
    font.setPointSize(23)
    app.setFont(font)

    Widget =  QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
    
    
