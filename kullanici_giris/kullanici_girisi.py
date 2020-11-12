import sys
import sqlite3 as sql
from PyQt5 import QtWidgets as q

class Pencere(q.QWidget):

    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):
        baglanti = sql.connect("kullaniciGirisi.db")

        self.cursor = baglanti.cursor()

        self.cursor.execute("create table if not exists uyeler ( kullanici_adi TEXT, parola TEXT)")

        baglanti.commit()
        
    def init_ui(self):
        self.kullanici_adi = q.QLineEdit()
        self.parola = q.QLineEdit()
        self.parola.setEchoMode(q.QLineEdit.Password)
        self.giris = q.QPushButton("Giriş Yap")
        self.yazi_alani = q.QLabel("")


        v_box = q.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box = q.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")

        self.giris.clicked.connect(self.login)

        self.show()

    def login(self):
        username = self.kullanici_adi.text()
        password = self.parola.text()

        self.cursor.execute("select * from uyeler where kullanici_adi = ? and parola = ?", (username, password))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok!\nLütfen tekrar deneyin...")
        else:
            self.yazi_alani.setText("Hoşgeldin")


app = q.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec())