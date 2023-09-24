# algorithm of rps game based on this research paper told by this youutube video https://www.youtube.com/watch?v=z6ANTFiTo7s

import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import random
import os

# tells if the match started
first_move = True
# saves the last move you did
cached_move = ''
# saves the previous result of your match
previous_result = ''

# dic-list: this lists the element's list of things he cant defeat
weaknesses = {
    'Rock' : ['Scissors'],
    'Paper' : ['Rock'],
    'Scissors' : ['Paper'],
}

### functions
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
    global previous_result

    if you == cpu:
        # enemy_str.set('Both got a tie!')
        enemy_str.set(str(cpu) + ' = ' + str(you))
        annc_str.set("Tie!")
        previous_result = 'Tie'
    else:
        result = check_player_win(you, cpu)
        if result:
            # enemy_str.set('The enemy and their ' + str(cpu) + ' destroyed your ' + str(you) + '...')
            enemy_str.set(str(you) + ' < ' + str(cpu))
            annc_str.set("You lose!")
            previous_result = 'Lose'
        else:
            # enemy_str.set('You destroyed the ' + str(cpu) + ' of the enemy with your ' + str(you) + '!')
            enemy_str.set(str(you) + ' > ' + str(cpu))
            annc_str.set("You win!")
            previous_result = 'Win'
        update_points(result)

def print_value(value):
    enemy_value = pick_move(value)

    game_result(value, enemy_value)

def pick_move(player_move):
    # i didnt know global stuff had to be set up like this but oh well
    global first_move
    global cached_move
    global previous_result

    if first_move:
        first_move = False
        cached_move = player_move
        return 'Paper'
    else:
        # var that saves the list of things the player can defeat
        print("start")
        player_choice_victors = random.choice(weaknesses[cached_move])
        # var that shows the weaknesses of player
        weakness = weaknesses[player_choice_victors]

        if previous_result == 'Lose' or previous_result == 'Win':
            value = random.choice(weaknesses[random.choice(weaknesses[cached_move])])
            print(value)

            cached_move = player_move
            return value
        elif previous_result == 'Tie':
            value = random.choice(weakness)
            print(value)

            cached_move = player_move
            return value

   
### page

## window
window = ttk.Window(themename= 'darkly') # tk.Tk()
window.title('Rock Paper Scissors but Quirky')
window.geometry('1100x800')

# title
title_label = ttk.Label(master = window, text = 'Rock Paper Scissors ULTRA', font = ' Alsina 24 bold')
title_label.pack()

# announcement
annc_str = tk.StringVar()
annc_label = ttk.Label(
    master = window, 
    text = '-Result-',
    font = ' Alsina 32 bold',
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
    font = ' Alsina 36',
    textvariable = score_str
)
score_label.pack(side = 'left', padx = 5)
score_str.set('0')

# Divider
scoredivider_label = ttk.Label(
    master = score_frame,
    text = ' - ',
    font = ' Alsina 36',
)
scoredivider_label.pack(side = 'left', padx = 5)

# For enemy score
score2_str = tk.StringVar()
score2_label = ttk.Label(
    master = score_frame,
    text = 'Output',
    font = ' Alsina 36',
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
    font = ' Alsina 20',
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
    print(name3)

print2(name3 = "donut")'''