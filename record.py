import subprocess
import os
import sys
from PyQt4 import uic, QtCore
from PyQt4.QtGui import *


class Record(QMainWindow):
    profile = ""
    ip = ""
    login = ""
    password = ""
    port = ""
    filename = ""

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('record.ui', self)
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.start_recording_button.clicked.connect(self.record)

    def record(self):
        self.read_data()
        if self.check_data():
            try:
                subprocess.check_output([".\\ffmpeg\\bin\\ffmpeg", "-i", ".\\vid\\strzyza1.mp4", "-acodec", "copy", "-vcodec", "copy", "-t", "00:05", self.filename, "-y", "-loglevel", "quiet"])
                # subprocess.check_output([".\\ffmpeg\\bin\\ffmpeg", "-i", "rtsp://"+self.login+":"+self.password+"@"+self.ip+":"+self.port.__str__()+"/profile"+self.profile.__str__()+"/media.smp", "-acodec", "copy", "-vcodec", "copy", "-t", "00:05", self.filename, "-y", "-loglevel", "quiet"])
                subprocess.Popen(r'explorer /select, "' + os.path.abspath(self.filename) + '"')
            except subprocess.CalledProcessError as error:
                self.show_error(error)
        else:
            self.show_warning()

    def check_data(self):
        if self.profile != "" and self.login != "" and self.password != "" and self.ip != "" and self.port != "" and self.filename != "":
            return True
        else:
            return True
            return False

    def read_data(self):
        self.profile = self.profile_combo_box.currentText()
        self.ip = self.ip_combo_box.currentText()
        self.login = self.login_line_edit.text()
        self.password = self.password_line_edit.text()
        self.port = self.port_line_edit.text()
        self.filename = "vid/"+self.filename_line_edit.text()

    def show_warning(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText("Niepoprawne dane:")
        message_box.setInformativeText("Sprawdź poprawność wpisanych danych.")
        message_box.setWindowTitle("Ostrzeżenie")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    def show_error(self, error):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Critical)
        message_box.setText("Wystąpił błąd:")
        message_box.setInformativeText("Polecenie " +
                                       str(error.cmd).replace('\'', '').replace(',', '') +
                                       " zwróciło kod " +
                                       str(error.returncode) + ".")
        message_box.setWindowTitle("Błąd")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    record_gui = Record()
    record_gui.show()

    sys.exit(qApp.exec_())
