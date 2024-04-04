# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ejercicio_3A_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import smbus
import time

# Dirección del sensor HMC5883L
HMC5883L_ADDRESS = 0x1E

# Registro de control
HMC5883L_REGISTER_MODE = 0x02

# Modo de operación continuo
HMC5883L_MODE_CONTINUOUS = 0x00

# Registro de datos de lectura
HMC5883L_REGISTER_DATA = 0x03

# Factor de conversión para convertir valores crudos en micro teslas
CONVERSION_FACTOR = 0.92

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 280, 191, 141))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 280, 181, 111))
        self.label_5.setPixmap(QtGui.QPixmap("ecci.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 131, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 190, 341, 61))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 100, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 321, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 141, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Conexión de la señal del botón con el método para iniciar la lectura del sensor
        self.pushButton.clicked.connect(self.read_sensor)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Diana Avendaño 81912</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Karen Mantilla 100088</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Electiva de Robótica</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2024-1</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br /></span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Lectura Sensor Magnetometro</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Inserte el tiempo (s):"))
        self.label_6.setText(_translate("MainWindow", "Lectura Sensor :"))

    # Método para iniciar la lectura del sensor
    def read_sensor(self):
        # Obtener el tiempo de lectura ingresado por el usuario
        time_seconds = int(self.textEdit.toPlainText())

        # Inicializar el bus I2C
        bus = smbus.SMBus(1)

        # Configurar el modo de operación continuo en el sensor HMC5883L
        bus.write_byte_data(HMC5883L_ADDRESS, HMC5883L_REGISTER_MODE, HMC5883L_MODE_CONTINUOUS)

        # Esperar un tiempo para que el sensor estabilice
        time.sleep(0.1)

        # Realizar la lectura del sensor y mostrarla en el QTextEdit
        start_time = time.time()
        while (time.time() - start_time) < time_seconds:
            # Leer los datos del sensor
            data = bus.read_i2c_block_data(HMC5883L_ADDRESS, HMC5883L_REGISTER_DATA, 6)

            # Convertir los datos en valores de ángulos
            x = data[0] << 8 | data[1]
            z = data[2] << 8 | data[3]
            y = data[4] << 8 | data[5]

            # Calcular el ángulo
            angle = round((180 * (180 * (math.atan2(y, x) / math.pi)) / 360), 2)

            # Actualizar el texto en el QTextEdit
            self.textEdit.setPlainText("Ángulo: {} grados".format(angle))

            # Esperar un breve tiempo antes de la próxima lectura
            time.sleep(0.5)


if __name__ == "__main__":
    import sys
    import math
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
