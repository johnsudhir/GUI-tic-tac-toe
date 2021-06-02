data = {'1': "",
        '2': "",
        '3': "",
        '4': "",
        '5': "",
        '6': "",
        '7': "",
        '8': "",
        '9': ""}
userFirst = 'X'
userSecond = 'O'
currentUser = ""

def table(data):
    print(data.get('1'), "|", data.get("2"), "|", data.get("3"))
    print("------")
    print(data.get("4"), "|", data.get("5"), "|", data.get("6"))
    print("------")
    print(data.get("7"), "|", data.get("8"), "|", data.get("9"))



def winner(data, currentUser):
    if(data.get("1") == data.get("2") == data.get("3") == currentUser or data.get("4") == data.get("5") == data.get("6")
            == currentUser or data.get("7") == data.get("8") == data.get("9") == currentUser):
        return True
    elif(data.get("1") == data.get("4") == data.get("7")  == currentUser or data.get("2") == data.get("5") == data.get("8")
         == currentUser or data.get("3") == data.get("6") == data.get("9") == currentUser ):
        return True
    elif(data.get("1") == data.get("5") == data.get("9")  == currentUser or data.get("3") == data.get("5") ==
         data.get("7") == currentUser ):
        return True
def tictactoe(data, currentUser = "X"):
    for i in range(9):
        position = input(f"{currentUser} Please, enter the position: ")
        data[position] = currentUser
        table(data)
        if (winner(data, currentUser)):
            print(f'{currentUser} won the game')
            break;
        if currentUser == 'X':
            currentUser = 'Y'
        else:
            currentUser = 'X'





    print("Game Over")



table(data)

tictactoe(data)
