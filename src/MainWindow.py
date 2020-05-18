# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, logic):
        # Set up same scheduler that was started in main
        self.logic = logic
        self.scheduler = logic.scheduler
        self.jobs = logic.idAndJob

        MainWindow.setObjectName("Aurora Forecast")
        MainWindow.resize(775, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(30, 50, 731, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(2)
        self.frame_3.setObjectName("frame_3")

        # Radio buttons
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton.setGeometry(QtCore.QRect(120, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        # Set default value to true
        self.radioButton.setChecked(True)

        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")


        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(240, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_2.setGeometry(QtCore.QRect(460, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox.setGeometry(QtCore.QRect(240, 80, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(410, 20, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_3)
        self.timeEdit.setGeometry(QtCore.QRect(460, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")

        # "Add rule" button
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.addLogicRule) 


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 190, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #####################                    
        self.formLayout = QtWidgets.QFormLayout()
        self.groupBox = QtWidgets.QGroupBox()

        # jobIDsAndRows = {job.id : Row nr}
        self.jobIDsAndRows = logic.jobIDsAndRows

        # Populate scroll area with currently running jobs
        for jobID, row in sorted(self.jobIDsAndRows.items(), key=lambda x: x[1]):
            self.addRuleToScrollArea(jobID, logic.printableRules[jobID], True)

        self.groupBox.setLayout(self.formLayout)
        #############

        # Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 240, 721, 181))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 719, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.groupBox)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStop_Notifications = QtWidgets.QAction(MainWindow)
        self.actionStop_Notifications.setObjectName("actionStop_Notifications")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionBout = QtWidgets.QAction(MainWindow)
        self.actionBout.setObjectName("actionBout")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addLogicRule(self):
        import functions
        #Todo: Lisa check, et ei oleks üle 100 reegli

        newID = str(self.generateNewId())  

        # Create cron rule ("on")
        if (self.radioButton.isChecked()):

            day = str(self.comboBox.currentText())
            hour = int(self.timeEdit.time().hour())
            minute = int(self.timeEdit.time().minute())
            
            printableText= self.logic.addJob(newID, 'cron', self.formLayout.rowCount(), day=day, hour=hour, minute=minute)

        # Create interval rule ("every")
        else:
            
            time = str(self.comboBox_2.currentText())
            val = int(self.spinBox.value())
            if time == 0:
                return

            printableText = self.logic.addJob(newID, 'interval', self.formLayout.rowCount(), freqMeasure=time, freqValue=val)
        
        self.addRuleToScrollArea(newID, printableText)
        
        print(self.scheduler.get_jobs())
        print(self.scheduler.print_jobs())

    def addRuleToScrollArea(self, id, printableText, initial=False):

        logicButton = QtWidgets.QPushButton("Delete")
        logicButton.clicked.connect(lambda: self.deleteRule(id))

        logicLabel = QtWidgets.QLabel(printableText)
        
        self.formLayout.addRow(logicButton, logicLabel)
    
    def deleteRule(self, id):
        currentLastIndex = self.formLayout.rowCount() - 1
        self.formLayout.removeRow(self.jobIDsAndRows[id])
        self.logic.deleteRule(id, currentLastIndex)

    def generateNewId(self):
        for i in range(99):
            taken = False
            for job in self.scheduler.get_jobs():
                if job.id == str(i):
                    taken = True
            if not taken:
                return i

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "on"))
        self.radioButton_2.setText(_translate("MainWindow", "every"))
        self.label_3.setText(_translate("MainWindow", "Notify me"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Mondays"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Tuesdays"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Wednesdays"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Thursdays"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Fridays"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Saturdays"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Sundays"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "hours"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "minutes"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "seconds"))
        self.label_4.setText(_translate("MainWindow", "at"))
        self.pushButton_2.setText(_translate("MainWindow", "Add rule"))
        self.label_2.setText(_translate("MainWindow", "Add logic rule"))
        self.label.setText(_translate("MainWindow", "Logic rules in place"))
        self.actionStop_Notifications.setText(_translate("MainWindow", "Stop Notifications"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionBout.setText(_translate("MainWindow", "About"))
