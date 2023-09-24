import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import random
import os

# last move
cached_choice = ''

# manually set here for debug
debug = True

# dic-list: this lists the element's list of things he cant defeat
weaknesses = {
    'Rock' : ['Scissors'],
    'Paper' : ['Rock'],
    'Scissors' : ['Paper'],
}

# checks how often you use a move for the cpu to strategize
weight = 0

### functions
def debug_print(msg):
    global debug
    if debug:
        print(msg)

def update_points(result):
    if result:
        score2_str.set(int(score2_str.get()) + 1)
    else:
        score_str.set(int(score_str.get()) + 1)

def check_player_win(you, cpu):
    selected_element = weaknesses[you]
    if cpu in selected_element:
        return False
    return True


def game_result(you, cpu):
    if you == cpu:
        # enemy_str.set('Both got a tie!')
        enemy_str.set(str(cpu) + ' = ' + str(you))
        annc_str.set("Tie!")
    else:
        result = check_player_win(you, cpu)
        if result:
            # enemy_str.set('The enemy and their ' + str(cpu) + ' destroyed your ' + str(you) + '...')
            enemy_str.set(str(you) + ' < ' + str(cpu))
            annc_str.set("You lose!")
        else:
            # enemy_str.set('You destroyed the ' + str(cpu) + ' of the enemy with your ' + str(you) + '!')
            enemy_str.set(str(you) + ' > ' + str(cpu))
            annc_str.set("You win!")
        update_points(result)

def print_value(value):
    enemy_value = pick_move(value)

    game_result(value, enemy_value)

def modify_weight(player_move):
    global weight
    global cached_choice

    # if player picked the same move as last time
    if cached_choice == player_move:
        weight += 1
    else:
        weight = 0
    cached_choice = player_move

def pick_move(player_move):
    # i didnt know global stuff had to be set up like this but oh well
    global weight
    global cached_choice
    
    debug_print('weight:' + str(weight))

    # if player isn't consistent with a pick
    if weight < 1:
        modify_weight(player_move)
        return random.choice(list(weaknesses))
    else:
        rng = random.randint(1, 4)
        # var that saves the list of things the player can defeat
        player_choice_victors = random.choice(weaknesses[cached_choice])
        # var that shows the weaknesses of player
        weakness = weaknesses[player_choice_victors]

        # if rng hits higher than 4
        if rng + weight >= 4:
            # make the cpu do your weakness
            debug_print("counter")
            value = random.choice(weakness)
            modify_weight(player_move)
            return value
        else:
            # make the cpu predict your counter and counter your counter!

            debug_print("counter counter")
            value = random.choice(weaknesses[random.choice(weakness)])
            modify_weight(player_move)

            return value
            # return random.choice(list(weaknesses))
### page

## window
window = ttk.Window(themename= 'darkly') # tk.Tk()
window.title('Rock Paper Scissors but Smart')
window.geometry('1100x800')

# title
title_label = ttk.Label(master = window, text = 'Rock Paper Scissors SMART', font = ' Calibri 24 bold')
title_label.pack()

# announcement
annc_str = tk.StringVar()
annc_label = ttk.Label(
    master = window, 
    text = '-Result-',
    font = ' Calibri 32 bold',
    textvariable = annc_str
)
annc_label.pack()

## score
score_frame = ttk.Frame(master = window)

# For player score
score_str = tk.StringVar()
score_label = ttk.Label(
    master = score_frame,
    text = 'Output',
    font = ' Calibri 36',
    textvariable = score_str
)
score_label.pack(side = 'left', padx = 5)
score_str.set('0')

# Divider
scoredivider_label = ttk.Label(
    master = score_frame,
    text = ' - ',
    font = ' Calibri 36',
)
scoredivider_label.pack(side = 'left', padx = 5)

# For enemy score
score2_str = tk.StringVar()
score2_label = ttk.Label(
    master = score_frame,
    text = 'Output',
    font = ' Calibri 36',
    textvariable = score2_str
)
score2_label.pack(side = 'left', padx = 5)
score2_str.set('0')

score_frame.pack(pady = 10)

## enemy choice
enemy_str = tk.StringVar()
enemy_label = ttk.Label(
    master = window,
    text = 'Output',
    font = ' Calibri 20',
    textvariable = enemy_str
)
enemy_label.pack(pady = 80)
# enemy_str.set('Rock!')

## images

filename = os.path.basename(__file__)
path = __file__
new_path = path.removesuffix(filename)


rock_image = tk.PhotoImage(file=new_path+r'images/rock.png')
paper_image = tk.PhotoImage(file=new_path+r'images/paper.png')
scissors_image = tk.PhotoImage(file=new_path+r'images/scissors.png')

## button
frame_1 = ttk.Frame(master = window)
rockbtn = ttk.Button(master = frame_1, text = 'Rock', command = lambda: print_value("Rock"), image=rock_image)
paperbtn = ttk.Button(master = frame_1, text = 'Paper', command = lambda: print_value("Paper"), image=paper_image)
scissorbtn = ttk.Button(master = frame_1, text = 'Scissors', command = lambda: print_value("Scissors"), image=scissors_image)

rockbtn.pack(side = 'left', padx = 30)
paperbtn.pack(side = 'left', padx = 30)
scissorbtn.pack(side = 'left', padx = 30)

frame_1.pack(pady = 10)

## run
window.mainloop()


'''def print2(name="", name2="", name3=""):
    debug_print(name3)

print2(name3 = "donut")'''