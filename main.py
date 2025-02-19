from login import *
from register import RegisterWindow
from main_window import MainWindow

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación CRUD")
        #self.setGeometry(100, 100, 800, 600)
        
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        
        
        self.login_page = LoginWindow(self)
        self.register_page = RegisterWindow(self)
        self.main_page = MainWindow()
        
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.register_page)
        self.stack.addWidget(self.main_page)
        
        
        self.stack.setCurrentWidget(self.login_page)
        
    
    def switch_to_register(self):
        self.stack.setCurrentWidget(self.register_page)
        
        
    
    def switch_to_login(self):
        self.stack.setCurrentWidget(self.login_page)
    
        
    
    def switch_to_main(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()