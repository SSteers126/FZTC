import sys
import secrets
from PySide2.QtCore import (Qt, QSize, QRect)
from PySide2.QtGui import (QPalette, QColor, QConicalGradient, QBrush, QGradient, QFont, QPixmap, QIcon)
from PySide2.QtWidgets import (QVBoxLayout, QHBoxLayout, QStyleFactory, QLineEdit, QPushButton, QApplication,
                               QDialog, QLabel)
import datetime
import ctypes
import os


myappid = u'Zestyy.FZTC.GUI.V1' # these lines are used to seperate the app from the python 'umbrella'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

dir_path = os.path.dirname(os.path.realpath(__file__))
calc_path = dir_path + "\\FZTC-Calculations\\"
log_path = dir_path + "\\FZTC-Log\\"

try:
    os.mkdir(calc_path)
    os.mkdir(log_path)
except:
    pass

class FZTC_window(QDialog):
    def __init__(self, parent=None):
        super(FZTC_window, self).__init__(parent)

        self.setWindowTitle("FZTC")
        app.setWindowIcon(QIcon('src/Thumb.png'))
        QApplication.setStyle(QStyleFactory.create("fusion"))
        QApplication.setFont(QFont("Helvetica", 11, 60))  # Montserrat Medium


        self.createStatusBar()
        self.error_pallette = QPalette()
        r = secrets.randbelow(255)
        g = secrets.randbelow(255)
        b = secrets.randbelow(255)
        self.error_pallette.setColor(QPalette.Foreground, QColor(r, g, b))
        self.error_text.setPalette(self.error_pallette)

        bggradient = QConicalGradient(800.0, 420.0, 167.0)
        bggradient.setColorAt(0, QColor(120, 0, 0))
        bggradient.setColorAt(0.1, Qt.black)
        bggradient.setColorAt(0.95, QColor(150, 0, 0))
        bggradient.setColorAt(1.0, QColor(120, 0, 0))
        bggradient.setSpread(QGradient.RepeatSpread)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(56, 56, 56))
        palette.setColor(QPalette.WindowText, Qt.white)

        palette.setColor(QPalette.Button, QColor(70, 40, 40))
        palette.setColor(QPalette.ButtonText, QColor(255, 100, 100))#200, 150, 255
        palette.setColor(QPalette.Highlight, QColor(110, 0, 0))

        palette.setColor(QPalette.Base, QColor(100, 100, 100))
        palette.setColor(QPalette.Text, Qt.white)
        palette.setBrush(QPalette.Window, QBrush(bggradient))

        checkpalette = QPalette()
        palette.setColor(QPalette.Text, QColor(200, 0, 0))
        palette.setColor(QPalette.Base, QColor(60, 30, 30))

        self.setPalette(palette)
        self.setFixedSize(QSize(700, 600))

        self.logo = QLabel("")
        img = QPixmap("src/Logo.png")
        self.logo.setPixmap(img)
        self.logo.setGeometry(QRect(10, 40, img.width(), img.height()))
        self.logo.setAlignment(Qt.AlignCenter)

        self.title = QLabel("Forza drift tune calculator")
        self.title.setAlignment(Qt.AlignCenter)
        self.title_layout = QVBoxLayout()
        self.title_layout.addWidget(self.logo)
        self.title_layout.addWidget(self.title)

        self.ratio = QLineEdit()
        self.ratio.setFixedWidth(256)
        self.ratio_label = QLabel("Weight ratio (input as just the number):")
        self.ratio_layout = QHBoxLayout()
        self.ratio_layout.addWidget(self.ratio_label)
        self.ratio_layout.addWidget(self.ratio)

        self.name = QLineEdit()
        self.name.setFixedWidth(256)
        self.name_label = QLabel("Name for file output:")
        self.name_layout = QHBoxLayout()
        self.name_layout.addWidget(self.name_label)
        self.name_layout.addWidget(self.name)

        self.acc = QLineEdit()
        self.acc.setText("2")
        self.acc.setFixedWidth(256)
        self.acc_label = QLabel("Amount of digits after decimal point (2 is usually good):")
        self.acc_layout = QHBoxLayout()
        self.acc_layout.addWidget(self.acc_label)
        self.acc_layout.addWidget(self.acc)

        self.rb_stiffness_max = QLineEdit()
        self.rb_stiffness_max.setText("40")
        self.rb_stiffness_min = QLineEdit()
        self.rb_stiffness_min.setText("1")
        self.rb_stiffness_max.setFixedWidth(125)
        self.rb_stiffness_min.setFixedWidth(125)
        self.rollbar_label = QLabel("Rollbar stiffness max/min:")
        self.rb_stiffness_inputs = QHBoxLayout()
        self.rb_stiffness_inputs.addWidget(self.rb_stiffness_max)
        self.rb_stiffness_inputs.addWidget(self.rb_stiffness_min)
        self.rollbar_layout = QHBoxLayout()
        self.rollbar_layout.addWidget(self.rollbar_label)
        self.rollbar_layout.addLayout(self.rb_stiffness_inputs)

        self.stiffness_max = QLineEdit()
        self.stiffness_min = QLineEdit()
        self.stiffness_max.setFixedWidth(125)
        self.stiffness_min.setFixedWidth(125)
        self.suspension_label = QLabel("Suspension stiffness max/min:")
        self.stiffness_inputs = QHBoxLayout()
        self.stiffness_inputs.addWidget(self.stiffness_max)
        self.stiffness_inputs.addWidget(self.stiffness_min)
        self.suspension_layout = QHBoxLayout()
        self.suspension_layout.addWidget(self.suspension_label)
        self.suspension_layout.addLayout(self.stiffness_inputs)

        self.rebound_max = QLineEdit()
        self.rebound_min = QLineEdit()
        self.rebound_max.setFixedWidth(125)
        self.rebound_min.setFixedWidth(125)
        self.rebound_label = QLabel("Rebound stiffness max/min:")
        self.rebound_inputs = QHBoxLayout()
        self.rebound_inputs.addWidget(self.rebound_max)
        self.rebound_inputs.addWidget(self.rebound_min)
        self.rebound_layout = QHBoxLayout()
        self.rebound_layout.addWidget(self.rebound_label)
        self.rebound_layout.addLayout(self.rebound_inputs)

        self.inputs = QVBoxLayout()
        self.inputs.addLayout(self.ratio_layout)
        self.inputs.addLayout(self.rollbar_layout)
        self.inputs.addLayout(self.suspension_layout)
        self.inputs.addLayout(self.rebound_layout)
        self.inputs.addLayout(self.acc_layout)
        self.inputs.addLayout(self.name_layout)

        self.calc_button = QPushButton("Calculate!")

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.title_layout)
        self.layout.addLayout(self.inputs)
        self.layout.addWidget(self.calc_button)

        self.final_layout = QVBoxLayout()
        self.final_layout.addLayout(self.layout, 20)
        self.final_layout.addWidget(self.error_text)
        self.setLayout(self.final_layout)

        self.calc_button.clicked.connect(lambda: self.calc())

    def createStatusBar(self):
        self.error_text = QLabel("")
        self.error_text.setText("Ready!")

    def formula(self, max, min, ratio):
        result = (max - min)*ratio + min
        return result
        #(MAX - MIN)RATIO + MIN
    def calc(self):
        try:
            accuracy = int(self.acc.text())
            roll_max = float(self.rb_stiffness_max.text())
            roll_min = float(self.rb_stiffness_min.text())
            susp_max = float(self.stiffness_max.text())
            susp_min = float(self.stiffness_min.text())
            reb_max = float(self.rebound_max.text())
            reb_min = float(self.rebound_min.text())
            front_ratio = (float(self.ratio.text()))/100
            rear_ratio = 1 - front_ratio
            f_roll_result = round(self.formula(roll_max, roll_min, front_ratio), accuracy)
            r_roll_result = round(self.formula(roll_max, roll_min, rear_ratio), accuracy)
            f_susp_result = round(self.formula(susp_max, susp_min, front_ratio), accuracy)
            r_susp_result = round(self.formula(susp_max, susp_min, rear_ratio), accuracy)
            f_reb_result = round(self.formula(reb_max, reb_min, front_ratio), accuracy)
            r_reb_result = round(self.formula(reb_max, reb_min, rear_ratio), accuracy)
            f_bump_result = round(0.675*self.formula(reb_max, reb_min, front_ratio), accuracy)
            r_bump_result = round(0.675*self.formula(reb_max, reb_min, rear_ratio), accuracy)
            file_name = calc_path + (str(self.name.text())) + ".txt"
            with open(file_name, "a+") as f:
                f.write("Results (When in pairs, first value is front and second is rear):\n")
                f.write("Rollbars: " + str(f_roll_result) + ", " + str(r_roll_result) + "\n")
                f.write("Suspension stiffness: " + str(f_susp_result) + ", " + str(r_susp_result) + "\n")
                f.write("Rebound stiffness: " + str(f_reb_result) + ", " + str(r_reb_result) + "\n")
                f.write("Bump stiffness: " + str(f_bump_result) + ", " + str(r_bump_result) + "\n")
            r = secrets.randbelow(255)
            g = secrets.randbelow(255)
            b = secrets.randbelow(255)
            self.error_pallette.setColor(QPalette.Foreground, QColor(r, g, b))
            self.error_text.setPalette(self.error_pallette)
            self.error_text.setText("Calculated successfully!")
        except Exception as e:
            self.error_pallette.setColor(QPalette.Foreground, QColor(255, 0, 0))
            self.error_text.setPalette(self.error_pallette)
            with open((log_path + "log.txt"), "a+") as f:
                f.write((datetime.datetime.now() + ": " + str(e) + "\n"))
            self.error_text.setText("An error occured. Check the log for details")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    FZTC = FZTC_window()
    FZTC.show()
    sys.exit(app.exec_())