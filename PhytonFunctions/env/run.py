class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700,500)
        self.setWindowTitle("Giris Ekrani")
        self.openWidowButton=QPushButton("Umumi xercleri qeyd et")
        self.adLineEdit=QLineEdit("Adiniz",self)
        