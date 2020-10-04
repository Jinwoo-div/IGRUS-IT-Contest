from PyQt5 import QtCore, QtGui, QtWidgets

class userChat():
    def __init__(self, window):
        self.chatBox = QtWidgets.QFrame(window.chatContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatBox.sizePolicy().hasHeightForWidth())
        self.chatBox.setSizePolicy(sizePolicy)
        self.chatBox.setMinimumSize(QtCore.QSize(0, 65))
        self.chatBox.setObjectName("chatBox")
        self._2 = QtWidgets.QHBoxLayout(self.chatBox)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setSpacing(10)
        self._2.setObjectName("_2")
        self.chatUserBox = QtWidgets.QFrame(self.chatBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatUserBox.sizePolicy().hasHeightForWidth())
        self.chatUserBox.setSizePolicy(sizePolicy)
        self.chatUserBox.setMinimumSize(QtCore.QSize(60, 0))
        self.chatUserBox.setObjectName("chatUserBox")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.chatUserBox)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.chatUserImg = QtWidgets.QLabel(self.chatUserBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatUserImg.sizePolicy().hasHeightForWidth())
        self.chatUserImg.setSizePolicy(sizePolicy)
        self.chatUserImg.setMinimumSize(QtCore.QSize(60, 60))
        self.chatUserImg.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.chatUserImg.setFont(font)
        self.chatUserImg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chatUserImg.setStyleSheet("border-radius: 30px;\n"
"background-color: rgb(255, 170, 0);")
        self.chatUserImg.setAlignment(QtCore.Qt.AlignCenter)
        self.chatUserImg.setObjectName("chatUserImg")
        self.verticalLayout_14.addWidget(self.chatUserImg)
        spacerItem27 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem27)
        self._2.addWidget(self.chatUserBox)
        self.chatting = QtWidgets.QLabel(self.chatBox)
        self.chatting.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatting.sizePolicy().hasHeightForWidth())
        self.chatting.setSizePolicy(sizePolicy)
        self.chatting.setMinimumSize(QtCore.QSize(0, 60))
        self.chatting.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.chatting.setFont(font)
        self.chatting.setStyleSheet("border: 2px solid rgb(255, 170, 0);\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.chatting.setObjectName("chatting")
        self._2.addWidget(self.chatting)
        spacerItem28 = QtWidgets.QSpacerItem(50, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._2.addItem(spacerItem28)
        _translate = QtCore.QCoreApplication.translate
        self.chatUserImg.setText(_translate("MainWindow", "img"))
        self.chatting.setText(_translate("MainWindow", "user님이 입장하셨습니다."))
        self.window = window

    def addWid(self):
        self.window.gridLayout_3.addWidget(self.chatBox, 1, 0, 1, 1)
        self.chatting.setText("user님이 입장하셨습니다.")