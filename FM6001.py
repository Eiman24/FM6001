import sys

from PySide2.QtWidgets import QGridLayout, QLabel, QTextEdit, QFileDialog, QPushButton, QWidget, QApplication
from PySide2 import QtCore, QtGui
import fishrename

import os

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # 绑定信号与槽函数
        self.pbtn_file.clicked.connect(self.select_file)
        self.submit.clicked.connect(self.get_text)

    def init_ui(self):
        # 手动布局
        self.setWindowTitle("FM6001")
        self.setGeometry(300, 300, 600, 120)
        self.vl = QGridLayout(self)
        self.lb_info = QLabel("NULL")
        self.pbtn_file = QPushButton("File")
        self.vl.addWidget(self.lb_info, 0, 0)
        self.vl.addWidget(self.pbtn_file, 0, 2)
        self.lb_notic = QLabel("Write new names below for those files in selected folder:")
        plt = QtGui.QPalette()
        plt.setColor(QtGui.QPalette.WindowText, QtCore.Qt.gray)
        self.lb_notic.setPalette(plt)
        self.vl.addWidget(self.lb_notic, 1, 0)
        self.textEdit = QTextEdit()
        self.textEdit.setPlaceholderText("You can type in here if you like...")
        self.submit = QPushButton("Submit")
        self.vl.addWidget(self.textEdit, 2, 0)
        self.vl.addWidget(self.submit, 2, 1)

    def select_file(self):
        # 获取目录路径
        file_path = QFileDialog.getExistingDirectory(caption="选择文件")  # getOpenFileName() 获取文件路径
        self.lb_info.setText(file_path)
        self.my_filepath = file_path

    def get_text(self):
        # 获取输入的文字
        input_text = self.textEdit.toPlainText()
        print(input_text)
        fishrename.name_changer(self.my_filepath, input_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
