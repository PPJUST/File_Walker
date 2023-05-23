# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWeKHnG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os

class DropLineEdit(QLineEdit):
    """Qt的QLineEdit类复写，拖入文件后将控件文本设置为拖入文件所属的文件夹路径/拖入文件夹的路径"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)  # 设置可拖入

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            path = urls[0].toLocalFile()  # 获取路径
            if os.path.isdir(path):
                self.setText(path)
            elif os.path.isfile(path):
                self.setText(os.path.split(path)[0])
                # self.setText(path)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(282, 81)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(80, 0, 201, 81))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.lineedit_path = DropLineEdit(self.page)
        self.lineedit_path.setObjectName(u"lineedit_path")
        self.lineedit_path.setGeometry(QRect(60, 10, 101, 21))
        self.button_ask_path = QToolButton(self.page)
        self.button_ask_path.setObjectName(u"button_ask_path")
        self.button_ask_path.setGeometry(QRect(170, 10, 21, 21))
        self.button_walk = QPushButton(self.page)
        self.button_walk.setObjectName(u"button_walk")
        self.button_walk.setGeometry(QRect(10, 40, 61, 31))
        self.button_open_result = QPushButton(self.page)
        self.button_open_result.setObjectName(u"button_open_result")
        self.button_open_result.setEnabled(False)
        self.button_open_result.setGeometry(QRect(80, 40, 61, 31))
        self.button_open_path = QPushButton(self.page)
        self.button_open_path.setObjectName(u"button_open_path")
        self.button_open_path.setGeometry(QRect(10, 10, 41, 23))
        self.button_quit = QPushButton(self.page)
        self.button_quit.setObjectName(u"button_quit")
        self.button_quit.setGeometry(QRect(150, 40, 41, 31))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.checkbox_hyperlink = QCheckBox(self.page_2)
        self.checkbox_hyperlink.setObjectName(u"checkbox_hyperlink")
        self.checkbox_hyperlink.setGeometry(QRect(10, 50, 83, 16))
        self.checkbox_hyperlink.setChecked(True)
        self.combobox_byte = QComboBox(self.page_2)
        self.combobox_byte.addItem("")
        self.combobox_byte.addItem("")
        self.combobox_byte.addItem("")
        self.combobox_byte.addItem("")
        self.combobox_byte.setObjectName(u"combobox_byte")
        self.combobox_byte.setGeometry(QRect(100, 10, 38, 20))
        self.checkbox_size = QCheckBox(self.page_2)
        self.checkbox_size.setObjectName(u"checkbox_size")
        self.checkbox_size.setGeometry(QRect(10, 10, 95, 16))
        self.checkbox_size.setChecked(True)
        self.checkbox_folder = QCheckBox(self.page_2)
        self.checkbox_folder.setObjectName(u"checkbox_folder")
        self.checkbox_folder.setGeometry(QRect(10, 30, 83, 16))
        self.checkbox_folder.setChecked(True)
        self.stackedWidget.addWidget(self.page_2)
        self.button_page_setting = QPushButton(Form)
        self.button_page_setting.setObjectName(u"button_page_setting")
        self.button_page_setting.setGeometry(QRect(0, 40, 75, 40))
        self.button_page_setting.setMinimumSize(QSize(0, 40))
        self.button_page_main = QPushButton(Form)
        self.button_page_main.setObjectName(u"button_page_main")
        self.button_page_main.setGeometry(QRect(0, 0, 75, 40))
        self.button_page_main.setMinimumSize(QSize(0, 40))

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)
        self.combobox_byte.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"File Walker", None))
        self.button_ask_path.setText(QCoreApplication.translate("Form", u"...", None))
        self.button_walk.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u904d\u5386", None))
        self.button_open_result.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u7ed3\u679c", None))
        self.button_open_path.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.button_quit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.checkbox_hyperlink.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u8d85\u94fe\u63a5", None))
        self.combobox_byte.setItemText(0, QCoreApplication.translate("Form", u"B", None))
        self.combobox_byte.setItemText(1, QCoreApplication.translate("Form", u"KB", None))
        self.combobox_byte.setItemText(2, QCoreApplication.translate("Form", u"MB", None))
        self.combobox_byte.setItemText(3, QCoreApplication.translate("Form", u"GB", None))

        self.checkbox_size.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u6587\u4ef6\u5927\u5c0f", None))
        self.checkbox_folder.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u6587\u4ef6\u5939", None))
        self.button_page_setting.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.button_page_main.setText(QCoreApplication.translate("Form", u"\u4e3b\u9875\u9762", None))
    # retranslateUi

