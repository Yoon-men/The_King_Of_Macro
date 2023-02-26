from img.img import *
import sys
from PySide2.QtWidgets import QApplication, QDialog, QFrame, QGraphicsDropShadowEffect, QLabel, QPushButton, QComboBox, QListWidget
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon, QFontDatabase, QFont


class EditUI(QDialog) : 
    def __init__(self) : 
        super().__init__()
        
        self. editUI()
    
    def editUI(self) : 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(448, 598)
        self.setWindowTitle("Edit")
        self.setWindowIcon(QIcon("KOM.ico"))
        QFontDatabase.addApplicationFont("./NanumGothicBold.otf")
        

        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(3, 2, 441, 591)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_frm.setGraphicsEffect(self.shadow)
        
        self.title_frm = QFrame(self.body_frm)
        self.title_frm.setGeometry(0, 0, 441, 41)
        self.title_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #464646;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        
        self.title_frm.mousePressEvent = self.setCenterPoint
        self.title_frm.mouseMoveEvent = self.moveWindow

        self.title_lb = QLabel(self.title_frm)
        self.title_lb.setGeometry(200, 14, 51, 18)
        self.title_lb.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/logo_edit.png);\n"
                                    "}")
        
        self.exit_bt = QPushButton(self.title_frm)
        self.exit_bt.setGeometry(410, 10, 22, 22)
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


        # setMacro_part
        self.setMacro_lb = QLabel(self.body_frm)
        self.setMacro_lb.setGeometry(71, 70, 111, 21)
        self.setMacro_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.setMacro_lb.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                        "}")
        self.setMacro_lb.setText("편집할 매크로 : ")

        self.setMacro_cb = QComboBox(self.body_frm)
        self.setMacro_cb.setGeometry(191, 69, 191, 24)
        self.setMacro_cb.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.setMacro_cb.setStyleSheet("QComboBox{\n"
                                            "background-color : #303030;\n"
                                            "border-radius : 5px;\n"
                                            "color : #cccccc;\n"
                                        "}\n"
                                        "QComboBox QAbstractItemView{\n"
                                            "background-color : #303030;\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 0px;\n"
                                            "color : #cccccc;\n"
                                            "selection-background-color : #ffffff;\n"
                                            "selection-color : #000000;\n"
                                            "outline : 0px;\n"
                                        "}\n"
                                        "QComboBox::donw-arrow{\n"
                                            "image : url(:/img/down.png);\n"
                                            "width : 18px;\n"
                                            "height : 18px;\n"
                                        "}\n"
                                        "QComboBox::drop-down{\n"
                                            "border-color : #b1b1b1;\n"
                                            "padding-right : 10px;\n"
                                        "}")
        
        self.line_1 = QLabel(self.body_frm)
        self.line_1.setGeometry(101, 114, 241, 16)
        self.line_1.setStyleSheet("QLabel{\n"
                                    "image : url(:/img/line.png);\n"
                                "}")
        

        # editMacro_part
        self.editMacro_lw = QListWidget(self.body_frm)
        self.editMacro_lw.setGeometry(16, 159, 294, 416)
        self.editMacro_lw.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.editMacro_lw.setStyleSheet("QListWidget{\n"
                                            "background-color : #4d4d4d;\n"
                                            "border-radius : 8px;\n"
                                            "color : #dddddd;\n"
                                            "padding-left : 3px;\n"
                                            "padding-top : 3px;\n"
                                        "}\n"
                                        "QListWidget QScrollBar{\n"
                                            "background-color : #aaaaaa;\n"
                                        "}\n"
                                        "QListWidget::item{\n"
                                            "margin : 1.3px;\n"
                                        "}\n"
                                        "QListWidget::item::selected{\n"
                                            "background-color : #2b2b2b;\n"
                                            "color : #dddddd;\n"
                                        "}\n"
                                        "QListWidget::item::hover{\n"
                                            "background-color : #434343;\n"
                                        "}")
        self.editMacro_lw.setFocusPolicy(Qt.NoFocus)

        normal_bt_styleSheet = ("QPushButton{\n"
                                    "background-color : #202020;\n"
                                    "border : 2px solid #aaaaaa;\n"
                                    "border-radius : 6px;\n"
                                    "color : #cccccc;\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                    "background-color : #aaaaaa;\n"
                                    "color : #222222;\n"
                                "}")

        working_bt_styleSheet = ("QPushButton{\n"
                                    "background-color : #aaaaaa;\n"
                                    "border : 2px solid #aaaaaa;\n"
                                    "border-radius : 5px;\n"
                                    "color : #222222;\n"
                                "}")
        
        self.addClick_bt = QPushButton(self.body_frm)
        self.addClick_bt.setGeometry(326, 159, 100, 24)
        self.addClick_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addClick_bt.setStyleSheet(normal_bt_styleSheet)
        self.addClick_bt.setText("클릭 추가")

        self.addKeyboard_bt = QPushButton(self.body_frm)
        self.addKeyboard_bt.setGeometry(326, 200, 100, 24)
        self.addKeyboard_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addKeyboard_bt.setStyleSheet(normal_bt_styleSheet)
        self.addKeyboard_bt.setText("키보드 추가")

        self.addDelay_bt = QPushButton(self.body_frm)
        self.addDelay_bt.setGeometry(326, 241, 100, 24)
        self.addDelay_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addDelay_bt.setStyleSheet(normal_bt_styleSheet)
        self.addDelay_bt.setText("딜레이 추가")

        self.addColorChecker_bt = QPushButton(self.body_frm)
        self.addColorChecker_bt.setGeometry(326, 282, 100, 24)
        self.addColorChecker_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addColorChecker_bt.setStyleSheet(normal_bt_styleSheet)
        self.addColorChecker_bt.setText("컬러체커 추가")

        self.frameLine = QFrame(self)
        self.frameLine.setGeometry(343, 329, 71, 20)
        self.frameLine.setFrameShape(QFrame.HLine)
        self.frameLine.setStyleSheet("QFrame{\n"
                                            "color : #585858;\n"
                                        "}")
        
        self.delete_bt = QPushButton(self.body_frm)
        self.delete_bt.setGeometry(326, 367, 100, 24)
        self.delete_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.delete_bt.setStyleSheet(normal_bt_styleSheet)
        self.delete_bt.setText("삭제")



    def setCenterPoint(self, event) : 
        self.centerPoint = event.globalPos()

    def moveWindow(self, event) : 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    editUI = EditUI()
    editUI.show()
    sys.exit(app.exec_())
