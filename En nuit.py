from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon
import pygame
import sys

#Class to build everything in it
class Window(QWidget):
    def __init__(self, timings, play_music=False):
        super().__init__()
        self.setWindowTitle("En nuit")
        self.resize(500, 500)
        self.setWindowIcon(QIcon("ennuit.jpeg"))

        #Plays music
        if play_music:
            pygame.mixer.init()
            pygame.mixer.music.load("et toi.mp3")
            pygame.mixer.music.play(loops=-1)

        #Shows the label
        self.label = QLabel("", self)
        self.label.setStyleSheet("font-size: 30px; font-family: Arial;")
        self.label.setAlignment(Qt.AlignCenter)

        #Manages the position
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        #Inserts the timings to the function
        self.schedule_texts(timings)

    #Shows text in order
    def schedule_texts(self, timings):
        for time, text in timings:
            QTimer.singleShot(time, lambda t=text: self.label.setText(t))

#Make's sure it's in main file
if __name__ == "__main__":
    app = QApplication(sys.argv)

    #Texts
    timings1 = [
        (0, ""),
        (4000, "Et moi"),
        (4600, "Et moi, j'écris"),
        (5200, "Et moi, j'écris le temps"),
        (5800, "Et moi, j'écris le temps qui passe"),
        (6400, ""),
        (8800, "La nuit"),
        (9400, "La nuit, la lune"),
        (10000, "La nuit, la lune, le feu"),
        (10600, "La nuit, la lune, le feu, l'orage"),
        (11200, ""),
        (13500, "C'est dans"),
        (14100, "C'est dans ta tête"),
        (14700, "C'est dans ta tête que tout"),
        (15300, "C'est dans ta tête que tout s'efface"),
        (16000, ""),
        (18400, "Et on se rejoint"),
        (19600, "Et on se rejoint à la sonnerie"),
        (20800, ""),
        (21400, "la nostalgie"),
        (22000, "la nostalgie"),

    ]
    timings2 = [
        (0, ""),
        (6400, "Et toi"),
        (7000, "Et toi, tu vis"),
        (7600, "Et toi, tu vis tout ce qu'on"),
        (8200, "Et toi, tu vis tout ce qu'on se dit"),
        (8800, ""),
        (11200, "Dans les rues sombres"),
        (12400, "Dans les rues sombres, on bat l'ennui"),
        (13000, ""),
        (16000, "Les bons"),
        (16600, "Les bons moments"),
        (17200, "Les bons moments, mes fautes"),
        (17800, "Les bons moments, mes fautes, ta rage"),
        (18400, ""),
        (20800, "Crier l'espoir"),
        (21401, "la nostalgie "),
        (22000, "la nostalgie"),
    ]

    #Make's windows appear in a middle
    screen = app.primaryScreen().availableGeometry()
    center_x = screen.width() // 2
    center_y = screen.height() // 2

    #Make's each window display texts and play music
    window1 = Window(timings=timings1, play_music=True)
    window2 = Window(timings=timings2, play_music=False)

    #The space between two windows and total width
    spacing = 5
    total_width = window1.width() * 2 + spacing

    #Calculates the area between two windows
    window1.move(center_x - total_width // 2, center_y - window1.height() // 2)
    window2.move(center_x - total_width // 2 + window1.width() + spacing,
                 center_y - window2.height() // 2)

    #Executes the windows
    window1.show()
    window2.show()
    sys.exit(app.exec_())
