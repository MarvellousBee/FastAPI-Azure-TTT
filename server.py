from fastapi import FastAPI
import numpy as np
import time
import starlette


app = FastAPI()

class Game:
    def __init__(self, p1, p2):
        arr = np.ndarray(shape=(3,3), dtype= int)
        arr.fill(-1)

        self.board_state = {
        "arena":arr,
        "players":[p1, p2],
        "current_player_turn":0,
        "winner":None,
        "message_log": [],
        "surrendered":False
                      }
    def move(self,par):
        #par:, x, y
        PlayerID = self.board_state["players"].index(par["playername"])
        x, y = int(par["x"]), int(par["y"])
        print("FEEDBACK")
        print(self.board_state["arena"][x][y], PlayerID, self.board_state["current_player_turn"])


        if self.board_state["arena"][x][y] != -1 or PlayerID != self.board_state["current_player_turn"]:
            print("spierdalaj")
            return False
        print("zapraszamy")
        self.board_state["current_player_turn"] = int(not self.board_state["current_player_turn"])
        self.board_state["arena"][x][y]=PlayerID
        return True
    def message(self,par):
        #par: Author, Message
        self.board_state["message_log"].append("<b>"+par["Author"]+":</b> "+par["Message"])
    def surrender(self,par):
        #get other player's name
        player = self.board_state["players"][:]
        player.remove(arg)
        self.board_state["surrendered"]=True
        self.board_state["winner"]=player[0]
    def get_state(self,par):
        return self.board_state
    def scan(self):
        arr = self.board_state["arena"]
        for i in range(0,3):
            a = arr[i]
            if a[0] != -1 and np.all(a == a[0]):
                return a[0]

        for i in range(0,3):
            a = arr[:,i]
            if a[0] != -1 and np.all(a == a[0]):
                return a[0]

        if arr.diagonal()[0] != -1 and np.all(arr.diagonal() == arr.diagonal()[0]):
            return arr.diagonal()[0]
        if np.flipud(arr).diagonal()[0] != -1 and np.all(np.flipud(arr).diagonal() == np.flipud(arr).diagonal()[0]):
            return np.flipud(arr).diagonal()[0]


        for i in arr:
            for j in i:
                if j==-1:
                    return "not_full"
                    break
        return "full"
    def __repr__(self):
        return str(self.board_state)

waiting_player = False
boards = []

@app.get("/find_a_game/{user_name}")
async def find_a_game(user_name):
    global waiting_player, boards


    if user_name==waiting_player:
        return "taken_username"

    if not waiting_player:
        waiting_player = user_name
        return False
    else:
        #start a match
        board_id = len(boards)
        boards.append(Game(user_name, waiting_player))
        print("match started!")
        waiting_player = False
        return board_id
        #uncomment to automatically remove empty games
        """
        i=0
        for board in boards:
            if not board.board_state["players"]:
                del boards[i]
            i+=1
        """

@app.get("/request_game_data/{player}")
async def request_game_data(player: str, board_id = None):
    global boards
    if board_id:
        #if boards[int(board_id)].board_state["winner"]!=None:
            #return f"WINNER={str(boards[int(board_idO)].board_state['winner'])}"
        print("okurwa", board_id)
        return str(boards[int(board_id)].board_state)
    print(boards)
    for id, board in enumerate(boards):
        if player in board.board_state["players"] and board.board_state["winner"]==None:
            return id
    return False
@app.get("/command/{board_id}/{username}/{command}")
async def command(board_id: int,username: str,command: str, request: starlette.requests.Request):
    #parameters for the command
    par = dict(request.query_params)
    #execute user's selected command
    value = getattr(boards[board_id], command)(par)
    #check if the game should end
    # int - winner's id
    # True - countinue the game
    # False - the board is full
    possi_winner = boards[board_id].scan()
    if possi_winner!="not_full":#In Python, 1==True
        print("JAAAAAAAAAAAAAAAAAAAAAAAS")
        print(possi_winner)
        boards[board_id].board_state["winner"]=possi_winner

    return value
