# Copyright (c) 2026 Alessio Ziami — alessioziami.dev
# All rights reserved.

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Carica il file .ui creato con Qt Designer
        loader = QUiLoader()
        ui_file = QFile("calculator.ui")
        self.ui = loader.load(ui_file)
        ui_file.close()

        # Collegamento bottoni
        self.ui.btn_0.clicked.connect(lambda: self.premi_numero("0"))
        self.ui.btn_1.clicked.connect(lambda: self.premi_numero("1"))
        self.ui.btn_2.clicked.connect(lambda: self.premi_numero("2"))
        self.ui.btn_3.clicked.connect(lambda: self.premi_numero("3"))
        self.ui.btn_4.clicked.connect(lambda: self.premi_numero("4"))
        self.ui.btn_5.clicked.connect(lambda: self.premi_numero("5"))
        self.ui.btn_6.clicked.connect(lambda: self.premi_numero("6"))
        self.ui.btn_7.clicked.connect(lambda: self.premi_numero("7"))
        self.ui.btn_8.clicked.connect(lambda: self.premi_numero("8"))
        self.ui.btn_9.clicked.connect(lambda: self.premi_numero("9"))
        self.ui.btn_dot.clicked.connect(lambda: self.premi_numero("."))

        # Operazioni
        self.ui.btn_add.clicked.connect(lambda: self.premi_numero("+"))
        self.ui.btn_sub.clicked.connect(lambda: self.premi_numero("-"))
        self.ui.btn_mul.clicked.connect(lambda: self.premi_numero("*"))
        self.ui.btn_div.clicked.connect(lambda: self.premi_numero("/"))

        self.ui.btn_ritorna.clicked.connect(self.ritorna)
        self.ui.btn_clear.clicked.connect(self.premi_clear)
        self.ui.btn_equal.clicked.connect(self.premi_uguale)

        self.ui.show()
    
    def premi_numero(self, numero):
        testo_attuale = self.ui.display.text()
        self.ui.display.setText(testo_attuale + numero)

    def ritorna(self, numero):
        testo_attuale = self.ui.display.text()
        self.ui.display.setText(testo_attuale[:-1])

    def premi_clear(self):
        self.ui.display.setText("")

    def premi_uguale(self):
        try:
            risultato = eval(self.ui.display.text())
            self.ui.display.setText(str(risultato))
        except Exception:
            self.ui.display.setText("Errore")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec())