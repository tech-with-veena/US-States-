import turtle
import pandas
screen=turtle.Screen()
screen.title("US STATES GAME")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
allstates=data.state.to_list()
guessedstates=[]
while len(guessedstates) < 50:
    answer=screen.textinput(title=f"{len(guessedstates)}/50 state name",prompt="Whats another state game?").title()
    if answer=="Exit":
        missingstates=[]
        for state in allstates:
            if state not in guessedstates:
                missingstates.append(state)
            newdata=pandas.DataFrame(missingstates)
            newdata.to_csv("Statestolearn.csv")
        break
    if answer in allstates:
        guessedstates.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        statedata=data[data.state==answer]
        t.goto(int(statedata.x),int(statedata.y))
        t.write(answer)
