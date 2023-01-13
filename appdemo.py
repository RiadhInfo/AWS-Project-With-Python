from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def play():
  try:
    x = int(window.txt.text())
    if x > 0:
      window.result.setText("Good accepted value")
    else:
      window.result.setText("Value not accepted")
  except ValueError:
       window.result.setText("Verify your input")

app = QApplication([])
window = loadUi("test.ui")
window.show()
window.verify.clicked.connect(play)
app.exec_()



