map_width = 5
map_height = 5
my_x = 0
my_y = 5

direction = "right"


way = ["up","right","down", "left"]
#오른쪽으로 돌기
def t_r():
    for i in range(3):
        turn_left()
        
#왼쪽으로 돌기
def t_l():
    turn_left()
#뒤로돌기
def turn_back():
    for i in range(2):
        turn_left()

#앞으로 한칸 가기
def go():
    move()

#원하는 만큼 앞으로 가기
def move_front_want(i = 2):
    for a in range(i):
        move()

def check_xy(w,my_y = my_y,my_x=my_x):
    if w == "up":
        my_y -=1
    elif w == "dwon":
        my_y +=1
    elif w == "right":
        my_x +=1
    elif w == "left":
        my_x -=1



def m_t(want, direction = direction):
    correction = -1
    
    global correction
    if direction == "up":
        correction = 0
    elif direction == "right":
        correction = 1
    elif direction == "down":
        correction = 2
    elif direction == "left":
        correction = 3
    
    print(direction,correction,"here") 

    if want == way[0-correction] :
        go()
        check_xy(want)
    elif want == way[1-correction]:
        t_l()
        go()
        check_xy(want)
    elif want == way[2-correction]:
        turn_back()
        go()
        check_xy(want)
    elif want == way[3-correction]:
        t_r()
        go()
        check_xy(want)
    else:
        print("error to> Short_fuction > m_up")


    direction = way[correction]


def m_f(want):
    if want == "front":
        go()
        if direction == way[0]:
            my_y -= 1
        elif direction == way[1]:
            my_x += 1
        elif direction == way[2]:
            my_y += 1
        elif direction == way[3]:
            my_x -= 1
        direction= "up"
        
    elif want == "right":
        t_r()
        go()
        if direction == way[0]:
            my_x += 1
        elif direction == way[1]:
            my_y += 1
        elif direction == way[2]:
            my_x -= 1
        elif direction == way[3]:
            my_y -= 1
        direction = "right"

    elif want == "left":
        t_l()
        go()
        if direction == way[0]:
            my_x -= 1
        elif direction == way[1]:
            my_y += 1
        elif direction == way[2]:
            my_x += 1
        elif direction == way[3]:
            my_y -= 1
        direction = "left"
        

    elif want == "back":
        turn_back()
        go()
        if direction == way[0]:
            my_y += 1
        elif direction == way[1]:
            my_x += 1
        elif direction == way[2]:
            my_y -= 1
        elif direction == way[3]:
            my_x -= 1
        direction = "back"


def setting (width, height, x, y, d):
    map_width = width
    map_height = height
    my_x = x
    my_y = y

    direction = d

#setting(5,5,0,5,"right")
map_width = 10
map_height = 10
my_x = 0
my_y = 10

direction = "right"
m_t("up", direction)
print(my_x,my_y,direction)

turn_off()