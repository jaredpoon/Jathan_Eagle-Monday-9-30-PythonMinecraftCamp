# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def Teleport():
    agent.teleport_to_player()
def moveForward(steps):
    agent.move(FORWARD, steps)
def moveBackward(steps):
    agent.move(BACK, steps)
def moveUp(steps):
    agent.move(UP, steps)
def moveDown(steps):
    agent.move(DOWN, steps)
def turnLeft():
    agent.turn(TurnDirection.LEFT)
def turnRight():
    agent.turn(TurnDirection.RIGHT)
def moveRight(steps):
    agent.move(RIGHT, steps)
def moveLeft(steps):
    agent.move(LEFT, steps)

player.on_chat("fw", moveForward)
player.on_chat("bk", moveBackward)
player.on_chat("tl", turnLeft)
player.on_chat("tr", turnRight)
player.on_chat("up", moveUp)
player.on_chat("down", moveDown)
player.on_chat("mr", moveRight)
player.on_chat("ml", moveLeft)
player.on_chat("come", Teleport)

def kill():
    mobs.kill(mobs.target(NEAREST_PLAYER))
player.on_chat("a", kill)


def destroyTree(steps):
    for i in range(steps):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, steps)
    agent.collect_all()
player.on_chat("dup", destroyTree)


def mine(steps):
    for i in range(steps):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)
player.on_chat("mine", mine)

def buildwall():
    for i in range(5):
        for i in range(3):
            agent.place(FORWARD)
            agent.move(UP, 1)
        agent.move(DOWN, 3)
        agent.move(RIGHT, 1)
player.on_chat("wall", buildwall)


def solvemaze(): 
    while agent.inspect(AgentInspection.BLOCK, DOWN) != DIAMOND_BLOCK:  
        if not agent.detect(AgentDetection.BLOCK, RIGHT):
            agent.turn(RIGHT)
        agent.move(FORWARD, 1)
player.on_chat("IDK", solvemaze)


def solve():
    while agent.detect(AgentDetection.BLOCK, DOWN) == True:
        if not agent.detect(AgentDetection.BLOCK, LEFT):
            agent.turn(LEFT)
            agent.move(FORWARD, 1)
        elif not agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.move(FORWARD, 1)
        else:
            agent.turn(RIGHT)
            agent.move(FORWARD, 1)
player.on_chat("solve", solve)


def dig():
    while agent.detect(AgentDetection.BLOCK, DOWN) == True:
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
        agent.collect_all()
player.on_chat("dig", dig)