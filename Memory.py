# simple state example for Memory

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import pygame
import random
CELLS = 16
WIDTH = 1000
HEIGHT = 100
DIVIDER = 8
deck = []
answers = []
state = 0
spacing = float(WIDTH // CELLS)
CellClicked = 0
CellsPlayed = [0,0]
     
# define event handlers
def init():
    global MATCHES, state
    global deck
    global answers
    state = 0
    deck = list(range(CELLS // 2))
    deck = deck + list(range(CELLS // 2))
    random.shuffle(deck)
    print (deck)
    print (len(deck))
    y = 0
    while y < len(deck):
        answers.append('?')
        y = y + 1
    print (answers)
    
def buttonclick():
    pass
    
def mouse_click(pos):
    global spacing
    global deck
    global state, CellClicked
    global CellsPlayed
    
    clickpos = list(pos)
    CellClicked = int(clickpos[0] // spacing)
    if state == 0:
        state = 1
        CellsPlayed[0] = CellClicked
        print ("CellsPlayed ", CellsPlayed, state)
    elif state == 1:
        state = 2
        CellsPlayed[1] = CellsPlayed[0]
        CellsPlayed[0] = CellClicked
        print ("CellsPlayed ", CellsPlayed, state)
    else:
        state = 1    
        CellsPlayed[1] = ""
        CellsPlayed[0] = CellClicked
        print ("CellsPlayed ", CellsPlayed, state)
        
    print (clickpos[0], CellClicked, "Is card ", deck[CellClicked])
       
def draw(canvas):
    global CELLS, WIDTH, HEIGHT, DIVIDER
    global deck, CellsPlayed, answers
    global spacing

    frame.set_canvas_background("GREEN")    
    x = 0
    cards = len(deck)
    deal = ""
    
    while x <= cards:
        if x < cards:
            if state == 0:
                deal = str(answers[x])
                #canvas.draw_text("Game beginning", [30, 62], 24, "White")
            elif state == 1:
                if CellClicked == x:
                    deal = str(deck[x])
                else:
                    deal = str(answers[x])
                #canvas.draw_text("One card exposed", [30, 62], 24, "White")
            else:
                if CellClicked == x:
                    deal = str(deck[x])
                else:
                    deal = str(answers[x])
                if deck[CellsPlayed[0]] == deck[CellsPlayed[1]]:
                    answers[CellsPlayed[0]] = deck[CellsPlayed[0]]
                    answers[CellsPlayed[1]] = deck[CellsPlayed[1]]                   
                # canvas.draw_text("Two cards exposed", [30, 62], 24, "White")
            #deal = str(answers[x])
        horiz = float(spacing * (x+1))
        canvas.draw_line((horiz, 0), (horiz, HEIGHT), 8, "Blue")
        canvas.draw_text(deal, ((horiz - (spacing//1.5)), (HEIGHT // 1.5)), 50, "White")
        x = x + 1
      #  print x, cards, deal, horiz, str(spacing), str(HEIGHT) 

# create frame and add a button and labels
frame = simplegui.create_frame("Memory states", WIDTH, HEIGHT)
frame.add_button("Restart", init, 200)
frame.add_button("Simulate mouse click", buttonclick, 200)
frame.set_mouseclick_handler(mouse_click)

# initialize global variables
init()

# register event handlers
frame.set_draw_handler(draw)

# get things rolling
frame.start()