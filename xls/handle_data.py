# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'handle_data.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
from change_to_sheets import change_to_sheets
from process_xls import process_xls
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(690, 540)
        self.source_label = QtGui.QLabel(Dialog)
        self.source_label.setGeometry(QtCore.QRect(120, 140, 91, 31))
        Dialog.setWindowIcon(QtGui.QIcon('icons/handledata.png'))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.source_label.setFont(font)
        self.source_label.setObjectName(_fromUtf8("source_label"))
        self.view_button = QtGui.QPushButton(Dialog)
        self.view_button.setGeometry(QtCore.QRect(520, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.view_button.setFont(font)
        self.view_button.setObjectName(_fromUtf8("view_button"))
        self.handle_data_button = QtGui.QPushButton(Dialog)
        self.handle_data_button.setGeometry(QtCore.QRect(290, 380, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.handle_data_button.setFont(font)
        self.handle_data_button.setObjectName(_fromUtf8("handle_data_button"))
        self.sys_invoice_num_label = QtGui.QLabel(Dialog)
        self.sys_invoice_num_label.setGeometry(QtCore.QRect(70, 200, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.sys_invoice_num_label.setFont(font)
        self.sys_invoice_num_label.setObjectName(_fromUtf8("sys_invoice_num_label"))
        self.invoice_num_label = QtGui.QLabel(Dialog)
        self.invoice_num_label.setGeometry(QtCore.QRect(90, 280, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.invoice_num_label.setFont(font)
        self.invoice_num_label.setObjectName(_fromUtf8("invoice_num_label"))
        self.sys_invoice_num = QtGui.QLineEdit(Dialog)
        self.sys_invoice_num.setGeometry(QtCore.QRect(220, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.sys_invoice_num.setFont(font)
        self.sys_invoice_num.setObjectName(_fromUtf8("sys_invoice_num"))
        self.invoice_num = QtGui.QLineEdit(Dialog)
        self.invoice_num.setGeometry(QtCore.QRect(220, 280, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.sys_invoice_num.setText('24')
        self.invoice_num.setFont(font)
        self.invoice_num.setObjectName(_fromUtf8("invoice_num"))
        self.file_path = QtGui.QLineEdit(Dialog)
        self.file_path.setGeometry(QtCore.QRect(220, 140, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.invoice_num.setText('4')
        self.file_path.setFont(font)
        self.file_path.setObjectName(_fromUtf8("file_path"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 430, 411, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        QtCore.QObject.connect(self.view_button,QtCore.SIGNAL('clicked()'),self.showDialog)

        QtCore.QObject.connect(self.handle_data_button, QtCore.SIGNAL('clicked()'), self.handle_data)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "数据处理", None))
        self.source_label.setText(_translate("Dialog", "原始数据：", None))
        self.view_button.setText(_translate("Dialog", "浏览", None))
        self.handle_data_button.setText(_translate("Dialog", "处理数据", None))
        self.sys_invoice_num_label.setText(_translate("Dialog", "系统发票所在列：", None))
        self.invoice_num_label.setText(_translate("Dialog", "发票号所在列：", None))
        self.label.setText(_translate("Dialog", "备注：该软件用于从excle文件中提取定制的数据。\n"
                                                "原始数据只能添加xls或者xlsx格式文件。", None))

    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(None, 'Open xls file', './','(*.xls;*.xlsx)')
        self.file_path.setText(filename)

    def handle_data(self):
        try:
            filepath = self.file_path.text()
            print filepath
            sys_invoie_col = int(self.sys_invoice_num.text())
            invoice_col = int(self.invoice_num.text())
            change_to_sheets(filepath,sys_invoie_col,invoice_col)
            process_xls()
            QtGui.QMessageBox.about(None,_fromUtf8('提示消息'),_fromUtf8('处理成功，文件保存路径D:\processed_data.xls'))
        except:
            QtGui.QMessageBox.critical(None, _fromUtf8('提示消息'), _fromUtf8('遇到问题，处理失败，请联系开发人员。'))
            info = sys.exc_info()
            print info[0],info[1]

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())