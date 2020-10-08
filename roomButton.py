from PyQt5 import QtCore, QtGui, QtWidgets
from frameClick import framebutton

class roomButtons():
        def __init__(self, window):
            self.room = framebutton(window.main)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.room.sizePolicy().hasHeightForWidth())
            self.room.setSizePolicy(sizePolicy)
            self.room.setMinimumSize(QtCore.QSize(0, 150))
            self.room.setStyleSheet("background-color: rgb(189, 215, 238);\n"
    "border-radius:30px;")
            self.room.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.room.setFrameShadow(QtWidgets.QFrame.Raised)
            self.room.setObjectName("room")
            self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.room)
            self.horizontalLayout_13.setObjectName("horizontalLayout_13")
            self.roomImg = QtWidgets.QLabel(self.room)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.roomImg.sizePolicy().hasHeightForWidth())
            self.roomImg.setSizePolicy(sizePolicy)
            self.roomImg.setMinimumSize(QtCore.QSize(110, 110))
            self.roomImg.setMaximumSize(QtCore.QSize(110, 110))
            self.roomImg.setAlignment(QtCore.Qt.AlignCenter)
            self.roomImg.setObjectName("roomImg")
            self.horizontalLayout_13.addWidget(self.roomImg)
            self.roomText = QtWidgets.QFrame(self.room)
            self.roomText.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.roomText.setFrameShadow(QtWidgets.QFrame.Raised)
            self.roomText.setObjectName("roomText")
            self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.roomText)
            self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_5.setObjectName("verticalLayout_5")
            self.roomTitle = QtWidgets.QLabel(self.roomText)
            font = QtGui.QFont()
            font.setFamily("나눔고딕")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.roomTitle.setFont(font)
            self.roomTitle.setAlignment(QtCore.Qt.AlignCenter)
            self.roomTitle.setObjectName("roomTitle")
            self.verticalLayout_5.addWidget(self.roomTitle)
            self.nameNnum = QtWidgets.QFrame(self.roomText)
            self.nameNnum.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.nameNnum.setFrameShadow(QtWidgets.QFrame.Raised)
            self.nameNnum.setObjectName("nameNnum")
            self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.nameNnum)
            self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_7.setObjectName("horizontalLayout_7")
            self.num = QtWidgets.QLabel(self.nameNnum)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.num.sizePolicy().hasHeightForWidth())
            self.num.setSizePolicy(sizePolicy)
            self.num.setMinimumSize(QtCore.QSize(200, 0))
            font = QtGui.QFont()
            font.setFamily("나눔고딕")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.num.setFont(font)
            self.num.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.num.setObjectName("num")
            self.horizontalLayout_7.addWidget(self.num)
            self.hostname = QtWidgets.QLabel(self.nameNnum)
            font = QtGui.QFont()
            font.setFamily("나눔고딕")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.hostname.setFont(font)
            self.hostname.setAlignment(QtCore.Qt.AlignCenter)
            self.hostname.setObjectName("hostname")
            self.horizontalLayout_7.addWidget(self.hostname)
            self.verticalLayout_5.addWidget(self.nameNnum)
            self.horizontalLayout_13.addWidget(self.roomText)
            _translate = QtCore.QCoreApplication.translate
            self.roomImg.setText(_translate("MainWindow", "img"))
            self.roomTitle.setText(_translate("MainWindow", "title"))
            self.num.setText(_translate("MainWindow", "hostname"))
            self.hostname.setText(_translate("MainWindow", "1/n"))
            self.window = window
            self.parent = self.room.parent()

        def addWid(self, title, hostname, num, x, y):
            self.window.roomList.addWidget(self.room, x, y, 1, 1)
            self.room.setParent(self.parent)
            self.roomTitle.setText(title)
            self.num.setText(hostname)
            self.hostname.setText(str(num) + "/5")

        def delWid(self):
            self.room.setParent(None)
        
        def setWid(self, title, hostname, num):
            self.roomTitle.setText(title)
            self.num.setText(hostname)
            self.hostname.setText(str(num) + "/5")

