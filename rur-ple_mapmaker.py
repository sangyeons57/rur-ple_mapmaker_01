

    # 러플 코딩 프로그램


    #전역 변수
map_width = -1
map_height = -1
my_x = -1
my_y = -1
direction = ""

way = ["up","right","down", "left"]


    # 함수 정의
class Short_function:

    #오른쪽으로 돌기
    def t_r(self):
        for i in range(3):
            turn_left()
            
    #왼쪽으로 돌기
    def t_l(self):
        turn_left()
    #뒤로돌기
    def turn_back(self):
        for i in range(2):
            turn_left()

    #앞으로 한칸 가기
    def go(self):
        move()

    #원하는 만큼 앞으로 가기
    def move_front_want(self,i = 2):
        for a in range(i):
            move()

    def check_xy(w):
        if w == "up":
            my_y -=1
        elif w == "dwon":
            my_y +=1
        elif w == "right":
            my_x +=1
        elif w == "left":
            my_x -=1



    def m_t(self,want):
        if direction == "up":
            correction = 0
        elif direction == "right":
            correction = 1
        elif direction == "down":
            correction = 2
        elif direction == "left":
            correction = 3

        if want == way[0-correction] :
            self.go()
            self.check_xy(want)
        elif want == way[1-correction]:
            self.t_l()
            self.go()
            self.check_xy(want)
        elif want == way[2-correction]:
            self.turn_back()
            self.go()
            self.check_xy(want)
        elif want == way[3-correction]:
            self.t_r()
            self.go()
            self.check_xy(want)
        else:
            print("error to> Short_fuction > m_up")


        direction = way[correction]
    

    def m_f(self,want):
        if want == "front":
            self.go()
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
            self.t_r()
            self.go()
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
            self.t_l()
            self.go()
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
            self.turn_back()
            self.go()
            if direction == way[0]:
                my_y += 1
            elif direction == way[1]:
                my_x += 1
            elif direction == way[2]:
                my_y -= 1
            elif direction == way[3]:
                my_x -= 1
            direction = "back"
        

sf = Short_function()

#좌표로 움직이기
class Move_To:
    now_x = my_x
    now_y = my_y

    def take_beeper(self):
        if on_beeper():
            pick_beeper()
            self.take_beeper()

    def left_hand_rule(self,wx, wy):
        while(my_x == wx & my_y == wy):
            if not left_is_clear():
                sf.go()
            else:
                sf.t_l()
            self.take_beeper()


    # 가려는곳 
    def go(self, want_x, want_y):
        wx = want_x
        wy = want_y


# way 는 지금까지의 갈림길 게수, walk 는 움직인거리
    def makeing_log(wx, wy,bx, by, way, walk):
        log_line = []
        log_line.append([now_x, now_y])
        log_line.append([wx, wy])
        log_line.append([bx, by])
        log_line.append(way)
        log_line.append(walk)
        return log_line











mt = Move_To()


    # 2중 리스트만들기 기본형태 [y][x]
def makemap( width = 1 , height = 1):
    answer_list = [[-1 for x in range(width)] for y in range(height)]
    return answer_list


def userinput(width,height,x,y,d):
    map_width = width
    map_height = height
    my_x = x
    my_y = y

    direction = d

def main():
    makemap(5,5)
    user_input(5,5,0,5,"right")


main()