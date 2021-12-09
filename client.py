import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QEvent, QObject, QThread
from QTgui import Ui_MainWindow
import time
import requests
import ast

#local, change to your public app's ID
ip = "http://127.0.0.1:8000/"



gamedata = {}

class APIWorker(QObject):

    def update_board(self, data):
        signs_out = []
        for i in data:
            for j in i:
                if j==-1:
                    signs_out.append("zone_empty")
                elif j==0:
                    signs_out.append("O")
                elif j==1:
                    signs_out.append("X")

        #for loop? what is that?
        window.ui.zone_0.setStyleSheet(f"background-image : url(media/{signs_out[0]}.png);")
        window.ui.zone_1.setStyleSheet(f"background-image : url(media/{signs_out[1]}.png);")
        window.ui.zone_2.setStyleSheet(f"background-image : url(media/{signs_out[2]}.png);")
        window.ui.zone_3.setStyleSheet(f"background-image : url(media/{signs_out[3]}.png);")
        window.ui.zone_4.setStyleSheet(f"background-image : url(media/{signs_out[4]}.png);")
        window.ui.zone_5.setStyleSheet(f"background-image : url(media/{signs_out[5]}.png);")
        window.ui.zone_6.setStyleSheet(f"background-image : url(media/{signs_out[6]}.png);")
        window.ui.zone_7.setStyleSheet(f"background-image : url(media/{signs_out[7]}.png);")
        window.ui.zone_8.setStyleSheet(f"background-image : url(media/{signs_out[8]}.png);")

    def listen(self):
        first = True
        while True:
            if window.in_game:
                string=f"request_game_data/{window.playername}?board_id={window.lobby_id}"
                gamedata = self.worker_get_dict(string)
                if window.public_messages_len!=len(gamedata["message_log"]):
                    num_new_msg = len(gamedata["message_log"])-window.public_messages_len
                    arr = gamedata["message_log"][-num_new_msg:]

                    long_user= "<b>"+window.playername
                    len_long_user = len(long_user)
                    for text in arr:
                        if not text[:len_long_user]==long_user:
                            window.update_chatbox(text)
                    window.public_messages_len+=num_new_msg

                if gamedata["winner"] != None:
                    if gamedata['winner'] == 0:
                        window.update_chatbox(f"<b>O</b> wins!")
                    elif gamedata['winner'] == 1:
                        window.update_chatbox(f"<b>X</b> wins!")
                    else:
                        window.update_chatbox(f"Looks like we have a <b>draw</b>!")

                    window.clean_state()

                self.update_board(gamedata['arena'])

                if first:
                    window.player_id = gamedata["players"].index(window.playername)
                    first=False
            else:
                first=True

                val = get(f"request_game_data/{window.playername}")
                if val != "false":
                    window.lobby_id = int(val)
                    window.in_game = True
            time.sleep(.5)


    def worker_get_dict(self, req):
        data = requests.get(window.server_ip+req).text
        if data[:7]=="WINNER=":
            return data[7:]
        data = data.replace('array(','').replace(']])', ']]')
        #eval but safe
        return ast.literal_eval(ast.literal_eval(data))

def get(req):
    return requests.get(window.server_ip+req).text


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.chatbox_text_log = ["<b>Hello!</b> change your name with ", "/name your_name", "Then, join a game with", "/join"]
        self.update_chatbox()
        self.installEventFilter(self)
        self.ui.sendButton.clicked.connect(self.send_message)
        self.playername = "NewPlayer"
        self.clean_state()
        self.thread = QThread()
        self.worker = APIWorker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.listen)
        self.thread.start()
        #convenience 1st!
        self.server_ip = ip


        #for loop? what is that?
        self.ui.zone_0.clicked.connect(lambda: self.zone_onclick(0, self.ui.zone_0))
        self.ui.zone_1.clicked.connect(lambda: self.zone_onclick(1, self.ui.zone_1))
        self.ui.zone_2.clicked.connect(lambda: self.zone_onclick(2, self.ui.zone_2))
        self.ui.zone_3.clicked.connect(lambda: self.zone_onclick(3, self.ui.zone_3))
        self.ui.zone_4.clicked.connect(lambda: self.zone_onclick(4, self.ui.zone_4))
        self.ui.zone_5.clicked.connect(lambda: self.zone_onclick(5, self.ui.zone_5))
        self.ui.zone_6.clicked.connect(lambda: self.zone_onclick(6, self.ui.zone_6))
        self.ui.zone_7.clicked.connect(lambda: self.zone_onclick(7, self.ui.zone_7))
        self.ui.zone_8.clicked.connect(lambda: self.zone_onclick(8, self.ui.zone_8))

    def clean_state(self):
        self.in_game = False
        self.waiting = False
        self.lobby_id = None
        self.player_id = None
        self.board_state = {}
        self.public_messages_len = 0

    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyPress:
            if str(event.key()) == "16777220":#Enter
                self.send_message()

        return QWidget.eventFilter(self, widget, event)

    def update_chatbox(self, text=False):
        if text:
            self.chatbox_text_log.append(text)
        out = ""
        if len(self.chatbox_text_log)>23:#limit messages to 23
            self.chatbox_text_log=self.chatbox_text_log[-23:]
        for msg in self.chatbox_text_log:
            out+=msg+"<br>"

        self.ui.chatbox.setText(out)


    def send_message(self):
        lineEdit_input = self.ui.lineEdit.text()
        if not lineEdit_input:
            return
        self.ui.lineEdit.setText("")

        self.update_chatbox("<b>"+self.playername+":</b> "+lineEdit_input)

        #check if this is a valid command
        if lineEdit_input[0]=="/":#TODO : update python to 3.10 and use "case"
            if   lineEdit_input[1:] == "join":
                if not self.playername:
                    self.update_chatbox("<b>Pick your name!</b>")
                    self.update_chatbox("/name {name}")
                    return

                answer = get(f"find_a_game/{self.playername}")
                if answer == 'false':
                    self.update_chatbox("Waiting for a player to join....")
                    self.waiting = True
                    self.player_id = 0
                elif answer == '"taken_username"':
                    self.update_chatbox(f"'{self.playername}' is already in a lobby!")
                elif answer == '0':
                    self.update_chatbox("Joining a lobby...")
                    self.in_game = True
                    self.lobby_id = answer
                    self.player_id = 1
                else:
                    print("SERVER ERROR:", answer)
                    raise Exception("Internal Server Error")
                    exit()

            elif lineEdit_input[1:] == "surrender":
                print("surrender")# TODO : properly implement /surrender
            elif lineEdit_input[1:5] == "name":
                self.playername = " ".join(lineEdit_input.split(" ")[1:])
            elif lineEdit_input[1:5] == "help":
                self.update_chatbox("<b>*</b> /join - Join a game")
                self.update_chatbox("<b>*</b> /surrender - surrender the match")
                self.update_chatbox("<b>*</b> /name {name} - pick your name")
            else:
                self.chatbox_text_log.append(f"'{lineEdit_input[0:]}' is not a valid command!")
        else:#send to the enemy
            get(f"command/{window.lobby_id}/{window.playername}/message?Author={self.playername}&Message={lineEdit_input}")


    #TODO : un-lazy this code
    arr = [
        [0,0],
        [0,1],
        [0,2],
        [1,0],
        [1,1],
        [1,2],
        [2,0],
        [2,1],
        [2,2]
    ]
    def zone_onclick(self, inp, object):
        if self.in_game:

            out = self.arr[inp]

            if get(f"command/{self.lobby_id}/{self.playername}/move?playername={self.playername}&x={out[0]}&y={out[1]}")=='true':
                print("ZONE", inp)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()


    sys.exit(app.exec())
