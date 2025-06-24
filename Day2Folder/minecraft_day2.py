# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER

def on_chat():
    agent.teleport_to_player()
player.on_chat("tp", on_chat)

def turnleft():
    agent.turn(LEFT)
player.on_chat("tl", turnleft)

def turnright():
    agent.turn(RIGHT)
player.on_chat("tr", turnright)

def on_chat2(steps):
    agent.move(FORWARD, steps)
player.on_chat("fw", on_chat2)

def on_chat3(steps):
    agent.move(UP, steps)
player.on_chat("up", on_chat3)

def on_chat4(steps):
    agent.move(DOWN, steps)
player.on_chat("down", on_chat4)

def on_chat5(steps):
    agent.move(BACK, steps)
player.on_chat("back", on_chat5)


#### day 2 starts here

def on_chat6(height):
    for count in range(height):
        agent.destroy(UP) # destroy leaves above agent's head
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, height)
    agent.collect_all()
player.on_chat("chop", on_chat6)


