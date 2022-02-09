from img.img import *
import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os
import csv
import keyboard
import mouse
import pyautogui
import time
import copy

class Main(QMainWindow) : 
    def __init__(self) : 
        super().__init__()

        self.mainUI()



    def mainUI(self) : 
        # basic_group
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(414, 695)
        self.setWindowTitle("The_King_of_Macro_v2.0")


        # body_group
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(4, 3, 406, 666)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")

        self.title_frm = QFrame(self.body_frm)
        self.title_frm.setGeometry(0, 0, 406, 41)
        self.title_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #484848;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        

        self.title_lb = QLabel(self.title_frm)
        self.title_lb.setGeometry(112, 11, 185, 24)
        self.title_lb.setPixmap(":/img/Logo.png")
        self.title_lb.setScaledContents(True)

        self.exit_bt = QPushButton(self.title_frm)
        self.exit_bt.setGeometry(377, 10, 22, 22)
        self.exit_bt.setStyleSheet("QPushButton{\n"
                                        "background-color : #aaaaaa;\n"
                                        "border-radius : 10px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "background-color : #666666;\n"
                                    "}")
        icon = QIcon()
        icon.addPixmap(":/img/exit.png")
        self.exit_bt.setIcon(icon)
        self.exit_bt.setIconSize(QSize(22, 11))

        self.keep_bt = QPushButton(self.title_frm)
        self.keep_bt.setGeometry(346, 10, 22, 22)
        self.keep_bt.setStyleSheet("QPushButton{\n"
                                        "background-color : #aaaaaa;\n"
                                        "border-radius : 10px;\n"
                                    "}\n" 
                                    "QPushButton:hover{\n"
                                        "background-color : #666666;\n"
                                    "}")
        icon = QIcon()
        icon.addPixmap(":/img/keep.png")
        self.keep_bt.setIcon(icon)
        self.keep_bt.setIconSize(QSize(12, 12))

        self.setting_bt = QPushButton(self.body_frm)
        self.setting_bt.setGeometry(374, 48, 24, 24)
        self.setting_bt.setStyleSheet("QPushButton{\n"
                                        "background-color : #aaaaaa;\n"
                                        "border-radius : 5px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "background-color : #666666;\n"
                                    "}")
        icon = QIcon()
        icon.addPixmap(":/img/setting.png")
        self.setting_bt.setIcon(icon)
        self.setting_bt.setIconSize(QSize(30, 30))

        self.line_1 = QLabel(self.body_frm)
        self.line_1.setGeometry(65, 160, 271, 16)
        self.line_1.setPixmap(":/img/Line.png")
        self.line_1.setScaledContents(True)

        self.line_2 = QLabel(self.body_frm)
        self.line_2.setGeometry(65, 280, 271, 16)
        self.line_2.setPixmap(":/img/Line.png")
        self.line_2.setScaledContents(True)

        self.line_3 = QLabel(self.body_frm)
        self.line_3.setGeometry(62, 407, 271, 16)
        self.line_3.setPixmap(":/img/Line.png")
        self.line_3.setScaledContents(True)

        self.noticeBoard = QListWidget(self.body_frm)
        self.noticeBoard.setGeometry(18, 529, 370, 118)
        self.noticeBoard.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.noticeBoard.setStyleSheet("QListWidget{\n"
                                            "background-color : #4d4d4d;\n"
                                            "border-radius : 8px;\n"
                                            "color : #dddddd;\n"
                                            "padding-left : 3px;\n"
                                        "}\n"
                                        "QListWidget::item{\n"
                                            "margin : 1.5px;\n"
                                        "}\n"
                                        "QListWidget QScrollBar{\n"
                                            "background : #aaaaaa;\n"
                                        "}\n"
                                        "QListWidget::item::selected{\n"
                                            "background : #2b2b2b;\n"
                                            "color : #dddddd;\n"
                                        "}\n"
                                        "QListWidget::item::hover{\n"
                                            "background : #434343;\n"
                                        "}")


        #addName_group
        self.addName_lb_title = QLabel(self.body_frm)
        self.addName_lb_title.setGeometry(20, 76, 151, 21)
        self.addName_lb_title.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
        self.addName_lb_title.setStyleSheet("QLabel{\n"
                                                "color : #b1b1b1;\n"
                                            "}")
        self.addName_lb_title.setText("Add Macro's Name")

        self.addName_le = QLineEdit(self.body_frm)
        self.addName_le.setGeometry(20, 107, 300, 24)
        self.addName_le.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.addName_le.setStyleSheet("QLineEdit{\n"
                                            "color : #dddddd;\n"
                                            "background-color : #303030;\n"
                                            "border : 2px solid #303030;\n"
                                            "border-radius : 5px;\n"
                                            "selection-color : #000000;\n"
                                            "selection-background-color : #ffffff;\n"
                                        "}\n"
                                        "QLineEdit::focus{\n"
                                            "border-color : #aaaaaa;\n"
                                        "}")

        self.addName_bt = QPushButton(self.body_frm)
        self.addName_bt.setGeometry(328, 107, 60, 24)
        self.addName_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.addName_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 8px;\n"
                                            "color : #cccccc;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "background-color : #aaaaaa;\n"
                                            "color : #222222;\n"
                                        "}")
        self.addName_bt.setText("추가")


        # edit_group
        self.edit_lb_title = QLabel(self.body_frm)
        self.edit_lb_title.setGeometry(20, 193, 81, 21)
        self.edit_lb_title.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
        self.edit_lb_title.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                            "}")
        self.edit_lb_title.setText("Edit Macro")

        self.edit_bt = QPushButton(self.body_frm)
        self.edit_bt.setGeometry(20, 227, 369, 24)
        self.edit_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.edit_bt.setStyleSheet("QPushButton{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 5px;\n"
                                        "color : #cccccc;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "background-color : #aaaaaa;\n"
                                        "color : #222222;\n"
                                    "}")
        self.edit_bt.setText("편집")


        # delete_group
        self.delete_lb_title = QLabel(self.body_frm)
        self.delete_lb_title.setGeometry(20, 313, 101, 21)
        self.delete_lb_title.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
        self.delete_lb_title.setStyleSheet("QLabel{\n"
                                                "color : #b1b1b1;\n"
                                            "}")
        self.delete_lb_title.setText("Delete Macro")

        self.delete_cb = QComboBox(self.body_frm)
        self.delete_cb.setGeometry(20, 347, 300, 24)
        self.delete_cb.setStyleSheet("QComboBox{\n"
                                        "font-family : 나눔고딕;\n"
                                        "font-weight : bold;\n"
                                        "font-size : 10pt;\n"
                                        "border-radius : 5px;\n"
                                        "color : #cccccc;\n"
                                        "background-color : #303030;\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 0px;\n"
                                        "background-color : #303030;\n"
                                        "color : #cccccc;\n"
                                        "selection-background-color : #ffffff;\n"
                                        "selection-color : #000000;\n"
                                    "}\n"
                                    "QComboBox::down-arrow{\n"
                                        "image : url(:/img/down.png);\n"
                                        "width : 18px;\n"
                                        "height : 18px;\n"
                                    "}\n"
                                    "QComboBox::drop-down{\n"
                                        "border-color : #b1b1b1;\n"
                                        "padding-right : 10px;\n"
                                    "}")
        self.delete_cb.addItem("테스트 매크로 1")       # Test code / please delete this line.
        self.delete_cb.addItem("테스트 매크로 2")       # Test code / please delete this line.
        self.delete_cb.addItem("테스트 매크로 3")       # Test code / please delete this line.

        self.delete_bt = QPushButton(self.body_frm)
        self.delete_bt.setGeometry(328, 347, 60, 24)
        self.delete_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.delete_bt.setStyleSheet("QPushButton{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 8px;\n"
                                        "color : #cccccc;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "background-color : #aaaaaa;\n"
                                        "color : #222222;\n"
                                    "}")
        self.delete_bt.setText("삭제")


        # start_group
        self.start_lb_title = QLabel(self.body_frm)
        self.start_lb_title.setGeometry(20, 442, 101, 21)
        self.start_lb_title.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
        self.start_lb_title.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                        "}")
        self.start_lb_title.setText("Start Macro")

        self.start_frm = QFrame(self.body_frm)
        self.start_frm.setGeometry(198, 443, 191, 21)
        self.start_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #4d4d4d;\n"
                                        "border-radius : 5px;\n"
                                    "}")

        self.start_rb_typeNum = QRadioButton(self.start_frm)
        self.start_rb_typeNum.setGeometry(6, 0, 91, 21)
        self.start_rb_typeNum.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.start_rb_typeNum.setStyleSheet("QRadioButton{\n"
                                                "color : #dddddd;\n"
                                            "}")
        self.start_rb_typeNum.setText("Num_type")
        self.start_rb_typeNum.setChecked(True)

        self.start_rb_typeTime = QRadioButton(self.start_frm)
        self.start_rb_typeTime.setGeometry(102, 0, 91, 21)
        self.start_rb_typeTime.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.start_rb_typeTime.setStyleSheet("QRadioButton{\n"
                                                "color : #dddddd;\n"
                                            "}")
        self.start_rb_typeTime.setText("Time_type")

        self.start_cb = QComboBox(self.body_frm)
        self.start_cb.setGeometry(20, 477, 163, 24)
        self.start_cb.setStyleSheet("QComboBox{\n"
                                        "font-family : 나눔고딕;\n"
                                        "font-weight : bold;\n"
                                        "font-size : 10pt;\n"
                                        "border-radius : 5px;\n"
                                        "color : #cccccc;\n"
                                        "background-color : #303030;\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 0px;\n"
                                        "color : #cccccc;\n"
                                        "selection-background-color : #ffffff;\n"
                                        "selection-color : #000000;\n"
                                    "}\n"
                                    "QComboBox::down-arrow{\n"
                                        "image : url(:/img/down.png);\n"
                                        "width : 18px;\n"
                                        "height : 18px;\n"
                                    "}\n"
                                    "QComboBox::drop-down{\n"
                                        "border-color : #b1b1b1;\n"
                                        "padding-right : 10px;\n"
                                    "}")
        self.start_cb.addItem("테스트 매크로 1")        # Test code / please delete this line.
        self.start_cb.addItem("테스트 매크로 2")        # Test code / please delete this line.
        self.start_cb.addItem("테스트 매크로 3")        # Test code / please delete this line.

        self.start_lb_1 = QLabel(self.body_frm)
        self.start_lb_1.setGeometry(192, 477, 41, 21)
        self.start_lb_1.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.start_lb_1.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                        "}")
        self.start_lb_1.setText("을(를)")

        self.start_sb = QSpinBox(self.body_frm)
        self.start_sb.setGeometry(235, 478, 60, 22)
        self.start_sb.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.start_sb.setStyleSheet("QSpinBox{\n"
                                            "color : #dddddd;\n"
                                            "background-color : #303030;\n"
                                            "border : 2px solid #303030;\n"
                                            "border-radius : 5px;\n"
                                            "selection-color : #000000;\n"
                                            "selection-background-color : #ffffff;\n"
                                            "}\n"
                                            "QSpinBox::focus{\n"
                                                "border-color : #aaaaaa;\n"
                                            "}")
        self.start_sb.setMaximum(999999999)

        self.start_lb_2 = QLabel(self.body_frm)
        self.start_lb_2.setGeometry(304, 477, 16, 21)
        self.start_lb_2.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.start_lb_2.setStyleSheet("QLabel{\n"
                                    "color : #b1b1b1;\n"
                                "}")
        self.start_lb_2.setText("번")

        self.start_bt = QPushButton(self.body_frm)
        self.start_bt.setGeometry(328, 477, 60, 24)
        self.start_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.start_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                            "color : #cccccc;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "color : #222222;\n"
                                            "background-color : #aaaaaa;\n"
                                        "}")
        self.start_bt.setText("실행")


        # When program is started (DEFAULT)
        global Load_status
        Load_status = False

        global stopKey
        stopKey = "esc"

        global startType
        startType = "typeNum"

        self.noticeBoard.addItem("[system] <The King of Macro_v2.0> - Made by. Yoonmen")
        self.noticeBoard.addItem("[system] 환영합니다. DATA.csv를 불러와주세요.")


        # If Signal is coming
        

        



        

        

if __name__ == '__main__' : 
    app = QApplication(sys.argv)
    global main
    main = Main()
    main.show()
    sys.exit(app.exec_())