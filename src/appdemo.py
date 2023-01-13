def verify(x):
    try:
        if x > 0:
            return "Good accepted value"
        else:
            return "Value not accepted"
    except:
       return "Verify your input"

"""def play():
    from PyQt5.uic import loadUi
    from PyQt5.QtWidgets import QApplication
    x = int(window.txt.text())
    msg = verify(x)
    window.result.setText(msg)

app = QApplication([])
window = loadUi("test.ui")
window.show()
window.verify.clicked.connect(play)
app.exec_()"""



