
from PyQt6.QtWidgets import QMainWindow, QFrame, QLabel
from .app import app 


main_window = QMainWindow()
WIDTH_WINDOW = 1024
HEIGHT_WINDOW = 800


primary_screen = app.primaryScreen()  
screen_size = primary_screen.size() 
width_screen = screen_size.width()    
height_screen = screen_size.height()  


main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2),
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW,
    HEIGHT_WINDOW
)

main_frame = QFrame(parent=main_window)
main_frame.setStyleSheet("background-color:black")
main_frame.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW)

frame1 = QFrame(parent=main_frame)
frame1.setStyleSheet("background-color:grey")
frame1.setGeometry(5, 350, 500, 250)


frame2 = QFrame(parent=main_frame)
frame2.setStyleSheet("background-color:white")
frame2.setGeometry(5, 705, 500, 80)
frame2.show()

label1 = QLabel(text= "ENGINE   RADAR   NAVIGATION", parent= frame2)
label1.setStyleSheet("font-size:16px; font-weight: 600; color: black")

label2 = QLabel(text= "SPACE CONTROL", parent= main_frame)
label2.setStyleSheet("font-size:25px; font-weight: 400; color: white")
label2.setGeometry(10, 100, 200, 100)

label2 = QLabel(text= "SYSTEM ONLINE", parent= frame1)
label2.setStyleSheet("font-size:20px; font-weight: 500; color: white")

frame_red = QFrame(parent=main_frame)
frame_red.setStyleSheet("background-color: red;")
frame_red.setGeometry(140, 607, 100, 90)

frame_blue = QFrame(parent=main_frame)
frame_blue.setStyleSheet("background-color: blue;")
frame_blue.setGeometry(450, 607, 100, 90)

frame_green = QFrame(parent=main_frame)
frame_green.setStyleSheet("background-color: green;")
frame_green.setGeometry(750, 607, 100, 90)
