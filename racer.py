#!/usr/bin/env python3


import random
import os
import json
import re
import keyboard
from math import sqrt
from graphics import GraphWin, Rectangle, Line, Point, Circle, Text, update, Image, Entry
from time import time,sleep
from datetime import datetime
from screeninfo import get_monitors
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits


car_db = {}
car_db["Jones C180"] = {"max_speed": 110, "acceleration": 6, "braking": 6, "handling": 6, "max_speed_offroad": 50, "details": "An entry-level luxury vehicle.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 3500}

car_db["Jones C300"] = {"max_speed": 120, "acceleration": 7, "braking": 6, "handling": 6, "max_speed_offroad": 50, "details": "An entry-level luxury vehicle.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 5000}

car_db["Jones C420"] = {"max_speed": 130, "acceleration": 8, "braking": 6, "handling": 6, "max_speed_offroad": 50, "details": "An entry-level luxury vehicle.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 8000}

car_db["Jones C560"] = {"max_speed": 140, "acceleration": 9, "braking": 6, "handling": 6, "max_speed_offroad": 50, "details": "An entry-level luxury vehicle.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 10000}

car_db["Jones C800"] = {"max_speed": 160, "acceleration": 10, "braking": 6, "handling": 6, "max_speed_offroad": 50, "details": "Top-of-the-line entry-level luxury vehicle.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 15000}

car_db["Salvo Gallant"] = {"max_speed": 165, "acceleration": 8, "braking": 8, "handling": 8, "max_speed_offroad": 50, "details": "A very fine automobile.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 20000}

car_db["Salvo Valiant"] = {"max_speed": 180, "acceleration": 7, "braking": 7, "handling": 7, "max_speed_offroad": 50, "details": "A very fine automobile.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 26000}

car_db["Salvo Intrepid"] = {"max_speed": 195, "acceleration": 6, "braking": 6, "handling": 6, "max_speed_offroad": 50, "details": "A very fine automobile.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 32000}

car_db["Banzai Sapporo"] = {"max_speed": 170, "acceleration": 10, "braking": 4, "handling": 8, "max_speed_offroad": 50, "details": "A purpose-built imported street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 40000}

car_db["Banzai Okinawa"] = {"max_speed": 180, "acceleration": 10, "braking": 4, "handling": 8, "max_speed_offroad": 50, "details": "A purpose-built imported street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 45000}

car_db["Banzai Kirin"] = {"max_speed": 190, "acceleration": 10, "braking": 4, "handling": 8, "max_speed_offroad": 50, "details": "A purpose-built imported street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 50000}

car_db["Banzai Yokohama"] = {"max_speed": 195, "acceleration": 11, "braking": 4, "handling": 8, "max_speed_offroad": 50, "details": "A purpose-built imported street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 55000}

car_db["Banzai Asahi"] = {"max_speed": 200, "acceleration": 12, "braking": 4, "handling": 8, "max_speed_offroad": 50, "details": "A purpose-built imported street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 60000}

car_db["Fork Copperhead"] = {"max_speed": 200, "acceleration": 9, "braking": 9, "handling": 5, "max_speed_offroad": 50, "details": "A purpose-built domestic street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 60000}

car_db["Fork Rattler"] = {"max_speed": 210, "acceleration": 9, "braking": 9, "handling": 5, "max_speed_offroad": 50, "details": "A purpose-built domestic street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 70000}

car_db["Fork Python"] = {"max_speed": 220, "acceleration": 9, "braking": 9, "handling": 5, "max_speed_offroad": 50, "details": "A purpose-built domestic street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 80000}

car_db["Fork Cobra"] = {"max_speed": 230, "acceleration": 9, "braking": 9, "handling": 5, "max_speed_offroad": 50, "details": "A purpose-built domestic street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 90000}

car_db["Fork Viper"] = {"max_speed": 240, "acceleration": 10, "braking": 9, "handling": 5, "max_speed_offroad": 50, "details": "A purpose-built domestic street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 100000}

car_db["Brodan Speedster"] = {"max_speed": 280, "acceleration": 12, "braking": 6, "handling": 5, "max_speed_offroad": 50, "details": "A purpose-built imported street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 150000}

car_db["Brodan SuperSport"] = {"max_speed": 300, "acceleration": 16, "braking": 8, "handling": 6, "max_speed_offroad": 50, "details": "A purpose-built imported street racer.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3, "value": 250000}


car_db["Fork Haulerton"] = {"max_speed": 95, "acceleration": 5, "braking": 5, "handling": 6, "max_speed_offroad": 60, "details": "A large transport vehicle.", "gear": 3, "brakes": 3, "tires": "Street", "camber": 3, "toe": 3}




## Key repeat delay modification
def set_xset():
    os.system('xset r rate {}'.format(20))
    
def reset_xset():
    os.system('xset r rate')
    


def get_screen_size():
    m = get_monitors()
    return(m[0].width,m[0].height)



## Open a window of given size x and y ##
def open_window(name,x,y):
    win = {}
    win["x"],win["y"] = x,y
    win["win"] = GraphWin(name,x,y,autoflush=False)
    win["win"].setBackground("black")
    return(win)


## Take a list of all drawn items and copy it ##
## Iterate through the copied list, removing each item from original list ##
## If we were to iterate through the original list, we would end up skipping every other item ##
## Ex: We delete item 0: item 1 becomes item 0.  We then delete item 1, leaving the new item 0 in place ##
## This would repeat as we iterate through the list, leaving half the list intact ##
def undraw_all(win):
    item_list = win["win"].items
    item_list = item_list.copy()
    for i in item_list:
        i.undraw()
    return(win)


## Close the window, return the window object ##

def close_window(win):
    win["win"].close()
    return(win)



def gen_new_road(lanes):
    road = {}
    road["length"] = 1000
    road["width"] = int(lanes*52.5)
    road["speed_limit"] = 14
    
    road["lanes"] = []
    ## Find center of each lane, store those numbers to spawn cars with ##
    for i in range(lanes):
        road["lanes"].append(int((road["width"]/lanes)*i)+int((road["width"]/lanes)/2))
    
    
    return(road)
    
    
def gen_road_marks():
    mark = {}
    mark["length"] = 100
    mark["width"] = 10
    mark["color"] = "white"
    return(mark)


def gen_stat_bar(x,y):
    bar = {}
    bar["width"] = x
    bar["height"] = 80
    bar["color"] = "black"
    bar["outline"] = "white"
    return(bar)


def gen_random_obstacle(x,y,road_width,obstacle_imgs):
    road_edge_left = (x/2)-road_width
    road_edge_right = (x/2)+road_width
    obstacle_x = random.randrange(x)
    obstacle_y = 100
    obstacle_width = 40
    obstacle_height = 40
    
    
    while obstacle_x > road_edge_left and obstacle_x < road_edge_right:
        obstacle_x = random.randrange(x)
    
    if len(obstacle_imgs) > 0:
        obstacle_img = random.choice(obstacle_imgs)
        obstacle = Image(Point(obstacle_x,obstacle_y),obstacle_img)
    else:
        obstacle = Rectangle(Point(obstacle_x-(obstacle_width/2),obstacle_y-(obstacle_height/2)),
                             Point(obstacle_x+(obstacle_width/2),obstacle_y+(obstacle_height/2)))
        obstacle.setFill("green4")
        obstacle.setOutline("brown")
        obstacle.setWidth(2)
    
    return(obstacle)


def gen_random_car(x,y,road,speed):
    road_width = road["width"]
    
    car = {}
    car["length"] = random.randrange(50,70)
    car["width"] = 25
    car["color"] = random.choice(["blue","aqua","yellow","red4","white"])
    car["outline"] = "red"
    #car["speed"] = random.randrange(road["speed_limit"]-2,road["speed_limit"]+2)
    car["speed"] = road["speed_limit"]
    
    left_align = (x/2)-(road["width"]/2)
    
    lane = random.choice(road["lanes"])
    if lane < road["width"]/2:
        ## Road side left
        car_obj = Rectangle(
            Point(left_align+lane-(car["width"]/2),80), 
            Point(left_align+lane+(car["width"]/2),80+car["length"]))
    else:
        ## Road side right
        if speed > road["speed_limit"]:
            car_obj = Rectangle(
                Point(left_align+lane-(car["width"]/2),80), 
                Point(left_align+lane+(car["width"]/2),80+car["length"]))
        else:
            car_obj = Rectangle(
                Point(left_align+lane-(car["width"]/2),y-80-car["length"]), 
                Point(left_align+lane+(car["width"]/2),y-80))
        car["speed"] = -car["speed"]
        
    car_obj.setFill(car["color"])
    car_obj.setOutline(car["outline"])
    car_obj.setWidth(2)
    car["obj"] = car_obj
    
    return(car)


def can_car_spawn(new_car,car_list):
    #print("\n -----")
    can_spawn = True
    for car in car_list:
        #print("checking car {}".format(car))
        p1 = new_car["obj"].getP1().getY()
        p2 = car["obj"].getP1().getY()
        p3 = car["obj"].getP2().getY()
        if is_point_between_points(p1,p2,p3):
            #print("Can't spawn due to collision")
            can_spawn = False
        p1 = new_car["obj"].getP2().getY()
        if is_point_between_points(p1,p2,p3):
            #print("Can't spawn due to collision")
            can_spawn = False
    
    return(can_spawn)


def is_point_between_points(point1,point2,point3):
    if point1 >= point2 and point1 <= point3:
        return(True)
    return(False)


def collision_check(car1,car2):
    l1 = car1["obj"].getP1()
    l1x,l1y = l1.getX(),l1.getY()
    r1 = car1["obj"].getP2()
    r1x,r1y = r1.getX(),r1.getY()
    l2 = car2["obj"].getP1()
    l2x,l2y = l2.getX(),l2.getY()
    r2 = car2["obj"].getP2()
    r2x,r2y = r2.getX(),r2.getY()
    
    if l2y < r2y:
        l2y,r2y = r2y,l2y
    
    ## Uncomment to debug collision check ##
    #print("l1: {}, r1: {}, l2: {}, r2: {}".format(l1,r1,l2,r2))
    
    if l1x >= r2x or l2x >= r1x:
        return(False)
    
    if r1y >= l2y or r2y >= l1y:
        return(False)
    
    return(True)


def is_car_on_road(x,car,road):
    left_bounds = (x/2)-(road["width"]/2)
    right_bounds = (x/2)+(road["width"]/2)
    
    if car["obj"].getP1().getX() < left_bounds:
        return(False)
    if car["obj"].getP2().getX() > right_bounds:
        return(False)
    
    return(True)


def show_info_box(x,y,win,text,subtext):
    box = Rectangle(
        Point((x/2)-200,(y/2)-100),Point((x/2)+200,(y/2)+100))
    box.setFill("blue")
    box.setOutline("yellow")
    box.setWidth(2)
    
    box_text = Text(
        Point(x/2,(y/2)-35),text)
    box_text.setTextColor("white")
    box_text.setStyle("bold")
    box_text.setSize(24)
    
    box_subtext = Text(
        Point(x/2,(y/2)+35),subtext)
    box_subtext.setTextColor("white")
    box_subtext.setSize(16)
    
    box.draw(win["win"])
    box_text.draw(win["win"])
    box_subtext.draw(win["win"])
    
    win["win"].getMouse()
    box.undraw()
    box_text.undraw()
    box_subtext.undraw()
    return



def show_info_box_tall(x,y,win,text,subtext):
    box = Rectangle(
        Point((x/2)-200,(y/2)-300),Point((x/2)+200,(y/2)+300))
    box.setFill("blue")
    box.setOutline("yellow")
    box.setWidth(2)
    
    box_text = Text(
        Point(x/2,(y/2)-265),text)
    box_text.setTextColor("white")
    box_text.setStyle("bold")
    box_text.setSize(24)
    
    box_subtext = Text(
        Point(x/2,(y/2)+30),subtext)
    box_subtext.setTextColor("white")
    box_subtext.setSize(16)
    
    box.draw(win["win"])
    box_text.draw(win["win"])
    box_subtext.draw(win["win"])
    
    win["win"].getMouse()
    box.undraw()
    box_text.undraw()
    box_subtext.undraw()
    return


def text_bar(stat,maximum,max_len):
    tick = maximum/max_len
    string = "["
    for i in range(int(round(stat/tick))):
        string += "|"
    for i in range(int(round((maximum-stat)/tick))):
        string += "-"
    ## Correct for rounding errors so total bar length remains constant ##
    for i in range(int((max_len+2)-len(string)-1)):
        string += "-"
    string += "]"
    return(string)


## Returns DEFAULT car stats and a randomized plate
## IF creating a NEW car object, take a .copy() of the returned item
def get_car_stats(car_name):
    car = car_db[car_name]#
    car["name"] = car_name
    car["plate"] = new_license_plate()
    return(car)


def new_shop():
    shop = {}
    shop["name"] = random.choice(["Zeek's Motors","Al's Lube N Tube","Mace Hardware"])
    
    
    shop["items"] = [
        {"name": "Fuel", "type": "item", "price": 5, "details": "Standard car fuel"},
    ]
    
    for car_name in ["Jones C180","Jones C300","Jones C420","Salvo Gallant","Salvo Valiant","Fork Viper","Brodan SuperSport"]:
        car = get_car_stats(car_name)
        details = format_car_details(car)
        shop["items"].append(
            {"name": car["name"],"type": "car", "price": car["value"], "details": details})
    
    return(shop)

def format_car_details(car):
    details = "{}\n\nMax Speed: {}mph\nMax Speed Off-Road: {}mph\nAcceleration: {}\nBraking: {}\nHandling: {}".format(
        car["details"],car["max_speed"],car["max_speed_offroad"],
        car["acceleration"],car["braking"],car["handling"])
    return(details)



def new_license_plate():
    plate = ""
    choices = ["upper","number"]
    for i in range(6):
        letter_type = random.choice(choices)
        if letter_type == "upper":
            plate = plate + random.choice(ascii_uppercase)
        else:
            plate = plate + random.choice(digits)
            
    return(plate)
                                   
    
def clear_win(win):
    ## Iterate through list and undraw all items ##
    for item in win["win"].items.copy():
        item.undraw()
    
    return(win)


def next_car(player):
    if len(player["storage"]["cars"]) > 0:
        player["storage"]["cars"].append(player["car"])
        player["car"] = player["storage"]["cars"][0]
    
    return(player)


def switch_cars(player,car1,car2):
    player["storage"]["cars"].append(car1)
    player["car"] = car2
    player["storage"]["cars"].remove(car2)
    return(player)


def garage_menu(win,player,shop):
    x,y = get_screen_size()
    win = clear_win(win)
    win["win"].setBackground("black")
    win,bar = draw_player_bar(win,player,shop["name"])
    
    ## Get current settings and save as default for reset ##
    default = player["car"].copy()
    default["tires"] = player["car"]["tires"]
    default["brakes"] = player["car"]["brakes"]
    default["camber"] = player["car"]["camber"]
    default["toe"] = player["car"]["toe"]
    default["gear"] = player["car"]["gear"]
    default["acceleration"] = player["car"]["acceleration"]
    default["max_speed"] = player["car"]["max_speed"]
    default["braking"] = player["car"]["braking"]
    default["handling"] = player["car"]["handling"]
    default["max_speed_offroad"] = player["car"]["max_speed_offroad"]
            
    ## Temp holds modded values until applied to car ##
    temp = default.copy()
    
    ## Display players car in detail, with buttons to modify certain parts
    to_draw, to_format, to_format_small, buttons = [], [], [], []
    
    car_name = Text(Point(250,200),player["car"]["name"])
    car_name.setTextColor("white")
    car_name.setSize(36)
    car_name.setStyle("bold")
    to_draw.append(car_name)
    
    car_detail_text = ""
    car_detail_text += player["car"]["plate"]+"\n"
    car_detail_text += player["car"]["details"]
    
    car_details = Text(Point(250,300),car_detail_text)
    to_format.append(car_details)
    
    
    car_max_speed = Text(Point(x-250,200),"Max Speed: {}mph".format(str(player["car"]["max_speed"])))
    to_format.append(car_max_speed)
    car_max_speed_mod = Text(Point(x-250,225),"")
    to_format.append(car_max_speed_mod)
    
    car_max_speed_offroad = Text(
        Point(x-250,300),"Max Speed Off-Road: {}mph".format(str(player["car"]["max_speed_offroad"])))
    to_format.append(car_max_speed_offroad)
    car_max_speed_offroad_mod = Text(Point(x-250,325),"")
    to_format.append(car_max_speed_offroad_mod)
    
    car_acceleration = Text(Point(x-250,400),"Acceleration: {}".format(str(player["car"]["acceleration"])))
    to_format.append(car_acceleration)
    car_acceleration_mod = Text(Point(x-250,425),"")
    to_format.append(car_acceleration_mod)
    
    car_handling = Text(Point(x-250,500),"Handling: {}".format(str(player["car"]["handling"])))
    to_format.append(car_handling)
    car_handling_mod = Text(Point(x-250,525),"")
    to_format.append(car_handling_mod)
    
    car_braking = Text(Point(x-250,600),"Braking: {}".format(str(player["car"]["braking"])))
    to_format.append(car_braking)
    car_braking_mod = Text(Point(x-250,625),"")
    to_format.append(car_braking_mod)

    
    
    ## Tuning Buttons ##
    ## Buttons for Toe Adjustment (5 ticks, default middle)
    ## +Handling, -Top Speed
    toe = player["car"]["toe"]
    toe_text = Text(Point(x/2,200),"Toe")
    toe_text.setStyle("bold")
    to_format.append(toe_text)
    toe_subtext = Text(Point(x/2,235),toe)
    to_format_small.append(toe_subtext)
    
    toe_left_button = new_button((x/2)-125,190,50,50,"<-","toe left","blue","white","yellow",14)
    buttons.append(toe_left_button)
    to_draw.append(toe_left_button["button"])
    to_draw.append(toe_left_button["text"])
    
    toe_right_button = new_button((x/2)+75,190,50,50,"->","toe right","blue","white","yellow",14)
    buttons.append(toe_right_button)
    to_draw.append(toe_right_button["button"])
    to_draw.append(toe_right_button["text"])
    
    ## Buttons for Camber Adjustment (5 ticks, default middle)
    ## +Handling, -Acceleration
    camber = player["car"]["camber"]
    camber_text = Text(Point(x/2,300),"Camber")
    camber_text.setStyle("bold")
    to_format.append(camber_text)
    camber_subtext = Text(Point(x/2,335),camber)
    to_format_small.append(camber_subtext)
    
    camber_left_button = new_button((x/2)-125,290,50,50,"<-","camber left","blue","white","yellow",14)
    buttons.append(camber_left_button)
    to_draw.append(camber_left_button["button"])
    to_draw.append(camber_left_button["text"])
    
    camber_right_button = new_button((x/2)+75,290,50,50,"->","camber right","blue","white","yellow",14)
    buttons.append(camber_right_button)
    to_draw.append(camber_right_button["button"])
    to_draw.append(camber_right_button["text"])
    
    ## Buttons for Tire Type (3 ticks, default Street)
    ## +-Max Speed, +-Max Speed Offroad
    tires = player["car"]["tires"]
    tire_text = Text(Point(x/2,400),"Tire Type")
    tire_text.setStyle("bold")
    to_format.append(tire_text)
    tire_subtext = Text(Point(x/2,435),tires)
    to_format_small.append(tire_subtext)
    
    tire_left_button = new_button((x/2)-125,390,50,50,"<-","tire left","blue","white","yellow",14)
    buttons.append(tire_left_button)
    to_draw.append(tire_left_button["button"])
    to_draw.append(tire_left_button["text"])
    
    tire_right_button = new_button((x/2)+75,390,50,50,"->","tire right","blue","white","yellow",14)
    buttons.append(tire_right_button)
    to_draw.append(tire_right_button["button"])
    to_draw.append(tire_right_button["text"])
    
    ## Buttons for Brake Adjustment (5 ticks, default middle)
    ## +Braking, -Handling
    brakes = player["car"]["brakes"]
    brake_text = Text(Point(x/2,500),"Brakes")
    brake_text.setStyle("bold")
    to_format.append(brake_text)
    brake_subtext = Text(Point(x/2,535),brakes)
    to_format_small.append(brake_subtext)
    
    brake_left_button = new_button((x/2)-125,490,50,50,"<-","brake left","blue","white","yellow",14)
    buttons.append(brake_left_button)
    to_draw.append(brake_left_button["button"])
    to_draw.append(brake_left_button["text"])
    
    brake_right_button = new_button((x/2)+75,490,50,50,"->","brake right","blue","white","yellow",14)
    buttons.append(brake_right_button)
    to_draw.append(brake_right_button["button"])
    to_draw.append(brake_right_button["text"])
    
    ## Buttons for Gear Tuning (5 ticks, default middle)
    ## +-Max Speed, +-Acceleration
    gear = player["car"]["gear"]
    gear_text = Text(Point(x/2,600),"Gearing")
    gear_text.setStyle("bold")
    to_format.append(gear_text)
    gear_subtext = Text(Point(x/2,635),gear)
    to_format_small.append(gear_subtext)
    
    gear_left_button = new_button((x/2)-125,590,50,50,"<-","gear left","blue","white","yellow",14)
    buttons.append(gear_left_button)
    to_draw.append(gear_left_button["button"])
    to_draw.append(gear_left_button["text"])
    
    gear_right_button = new_button((x/2)+75,590,50,50,"->","gear right","blue","white","yellow",14)
    buttons.append(gear_right_button)
    to_draw.append(gear_right_button["button"])
    to_draw.append(gear_right_button["text"])
    
    
    ## Format pending texts ##
    for item in to_format:
        item.setTextColor("white")
        item.setSize(16)
        to_draw.append(item)
        
    for item in to_format_small:
        item.setTextColor("white")
        item.setSize(12)
        to_draw.append(item)
    
    
    ## Control Buttons ##
    confirm_button = new_button(100,y-250,250,100,"CONFIRM","confirm","green3","white","yellow",30)
    buttons.append(confirm_button)
    to_draw.append(confirm_button["button"])
    to_draw.append(confirm_button["text"])
                                
    reset_button = new_button((x/2)-125,y-250,250,100,"RESET","reset","yellow2","black","black",30)
    buttons.append(reset_button)
    to_draw.append(reset_button["button"])
    to_draw.append(reset_button["text"])
                                
    go_back_button = new_button(x-350,y-250,200,100,"BACK","go back","red3","white","yellow",30)
    buttons.append(go_back_button)
    to_draw.append(go_back_button["button"])
    to_draw.append(go_back_button["text"])
                             
    ## Draw pending items
    for item in to_draw:
        item.draw(win["win"])
    
    
    
    play = True
    
    while play:
        click = win["win"].getMouse()
        clicked_on = interpret_click(win,buttons,click)
        
        if clicked_on == "toe left":
            if temp["toe"] > 1:
                temp["toe"] -= 1
                temp["handling"] -= 0.5
                temp["max_speed"] += 2.5
        elif clicked_on == "toe right":
            if temp["toe"] < 5:
                temp["toe"] += 1
                temp["handling"] += 0.5
                temp["max_speed"] -= 2.5
                
        elif clicked_on == "camber left":
            if temp["camber"] > 1:
                temp["camber"] -= 1
                temp["handling"] -= 0.5
                temp["acceleration"] += 0.5
        elif clicked_on == "camber right":
            if temp["camber"] < 5:
                temp["camber"] += 1
                temp["handling"] += 0.5
                temp["acceleration"] -= 0.5
                
        elif clicked_on == "tire left":
            if temp["tires"] == "Street":
                temp["tires"] = "Hybrid"
                temp["max_speed"] -= 5
                temp["max_speed_offroad"] += 5
            elif temp["tires"] == "Hybrid":
                temp["tires"] = "Off-Road"
                temp["max_speed"] -= 5
                temp["max_speed_offroad"] += 5
        elif clicked_on == "tire right":
            if temp["tires"] == "Off-Road":
                temp["tires"] = "Hybrid"
                temp["max_speed"] += 5
                temp["max_speed_offroad"] -= 5
            elif temp["tires"] == "Hybrid":
                temp["tires"] = "Street"
                temp["max_speed"] += 5
                temp["max_speed_offroad"] -= 5
                
        elif clicked_on == "brake left":
            if temp["brakes"] > 1:
                temp["brakes"] -= 1
                temp["braking"] -= 0.5
                temp["handling"] += 0.5
        elif clicked_on == "brake right":
            if temp["brakes"] < 5:
                temp["brakes"] += 1
                temp["braking"] += 0.5
                temp["handling"] -= 0.5
        
        elif clicked_on == "gear left":
            if temp["gear"] > 1:
                temp["gear"] -= 1
                temp["acceleration"] += 0.5
                temp["max_speed"] -= 2.5
        elif clicked_on == "gear right":
            if temp["gear"] < 5:
                temp["gear"] += 1
                temp["acceleration"] -= 0.5
                temp["max_speed"] += 2.5
        
        if clicked_on == "confirm":
            player["car"] = temp.copy()
            default = temp.copy()
            car_max_speed.setText("Max Speed: {}mph".format(str(player["car"]["max_speed"])))
            car_max_speed_offroad.setText(
                "Max Speed Off-Road: {}mph".format(str(player["car"]["max_speed_offroad"])))
            car_acceleration.setText("Acceleration: {}".format(str(player["car"]["acceleration"])))
            car_braking.setText("Braking: {}".format(str(player["car"]["braking"])))
            car_handling.setText("Handling: {}".format(str(player["car"]["handling"])))
                                  
        elif clicked_on == "reset":
            temp = player["car"].copy()
            temp["toe"] = player["car"]["toe"]
            temp["camber"] = player["car"]["camber"]
            temp["tires"] = player["car"]["tires"]
            temp["brakes"] = player["car"]["brakes"]
            temp["gear"] = player["car"]["gear"]
            temp["acceleration"] = player["car"]["acceleration"]
            temp["max_speed"] = player["car"]["max_speed"]
            temp["max_speed_offroad"] = player["car"]["max_speed_offroad"]
            temp["braking"] = player["car"]["braking"]
            temp["handling"] = player["car"]["handling"]
        elif clicked_on == "go back":
            play = False
            return(player)
                                
        ## Update text to show pending changes ##
        if temp["toe"] != player["car"]["toe"]:
            toe_text,toe_subtext = set_style_modded(toe_text,toe_subtext,temp["toe"])
        elif temp["toe"] == player["car"]["toe"]:
            toe_text,toe_subtext = set_style_unmodded(toe_text,toe_subtext,temp["toe"])
            
        if temp["camber"] != player["car"]["camber"]:
            camber_text,camber_subtext = set_style_modded(camber_text,camber_subtext,temp["camber"])
        elif temp["camber"] == player["car"]["camber"]:
            camber_text,camber_subtext = set_style_unmodded(camber_text,camber_subtext,temp["camber"])
            
        if temp["tires"] != player["car"]["tires"]:
            tire_text,tire_subtext = set_style_modded(tire_text,tire_subtext,temp["tires"])
        elif temp["tires"] == player["car"]["tires"]:
            tire_text,tire_subtext = set_style_unmodded(tire_text,tire_subtext,temp["tires"])


        if temp["gear"] != player["car"]["gear"]:
            gear_text,gear_subtext = set_style_modded(gear_text,gear_subtext,temp["gear"])
        elif temp["gear"] == player["car"]["gear"]:
            gear_text,gear_subtext = set_style_unmodded(gear_text,gear_subtext,temp["gear"])
            
            
        if temp["brakes"] != player["car"]["brakes"]:
            brake_text,brake_subtext = set_style_modded(brake_text,brake_subtext,temp["brakes"])
        elif temp["brakes"] == player["car"]["brakes"]:
            brake_text,brake_subtext = set_style_unmodded(brake_text,brake_subtext,temp["brakes"])
            
            
        if temp["acceleration"] != player["car"]["acceleration"]:
            car_acceleration_mod.setText(temp["acceleration"])
            car_acceleration_mod.setStyle("bold")
            if temp["acceleration"] > player["car"]["acceleration"]:
                car_acceleration_mod.setTextColor("green")
            else:
                car_acceleration_mod.setTextColor("red")
        else:
            car_acceleration_mod.setText("")
            
        if temp["max_speed"] != player["car"]["max_speed"]:
            car_max_speed_mod.setText(temp["max_speed"])
            car_max_speed_mod.setStyle("bold")
            if temp["max_speed"] > player["car"]["max_speed"]:
                car_max_speed_mod.setTextColor("green")
            else:
                car_max_speed_mod.setTextColor("red")
        else:
            car_max_speed_mod.setText("")
            
        if temp["max_speed_offroad"] != player["car"]["max_speed_offroad"]:
            car_max_speed_offroad_mod.setText(temp["max_speed_offroad"])
            car_max_speed_offroad_mod.setStyle("bold")
            if temp["max_speed_offroad"] > player["car"]["max_speed_offroad"]:
                car_max_speed_offroad_mod.setTextColor("green")
            else:
                car_max_speed_offroad_mod.setTextColor("red")
        else:
            car_max_speed_offroad_mod.setText("")
            
        if temp["braking"] != player["car"]["braking"]:
            car_braking_mod.setText(temp["braking"])
            car_braking_mod.setStyle("bold")
            if temp["braking"] > player["car"]["braking"]:
                car_braking_mod.setTextColor("green")
            else:
                car_braking_mod.setTextColor("red")
        else:
            car_braking_mod.setText("")
            
        if temp["handling"] != player["car"]["handling"]:
            car_handling_mod.setText(temp["handling"])
            car_handling_mod.setStyle("bold")
            if temp["handling"] > player["car"]["handling"]:
                car_handling_mod.setTextColor("green")
            else:
                car_handling_mod.setTextColor("red")
        else:
            car_handling_mod.setText("")
        
        update()
    return(player)


def set_style_modded(text,subtext,new_subtext):
    text.setTextColor("yellow")
    subtext.setTextColor("yellow")
    subtext.setStyle("bold")
    subtext.setText(new_subtext)
    return(text,subtext)
                         
    
def set_style_unmodded(text,subtext,new_subtext):
    text.setTextColor("white")
    subtext.setTextColor("white")
    subtext.setStyle("normal")
    subtext.setText(new_subtext)
    return(text,subtext)


##
##  Save functions ##
##

## Collect all save folders and return as a list ##
def import_saves():
    saves = []
    for folder in os.listdir('saves'):
        saves.append(folder)
    for save in saves:
        print(save)
    return(saves)


## Given a save file name, search for and delete that folder and all files contained therein ##
def delete_save(save_name):
    save_path = os.path.join('saves',save_name)
    for file in os.listdir(save_path):
        os.remove(os.path.join(save_path,file))
    os.rmdir(save_path)

    
    
## Delete ALL save game folders ##
def purge_saves():
    check_folder('saves')
    for folder in os.listdir('saves'):
        delete_save(folder)
    
    
## Loads dmap and character data from a save folder ##
## Right now, it only chooses the most recent save ##
## In future, we will present a choice box with all saves ##
def load_game(win,filename):
    file_path = 'saves/{}'.format(filename)
    
    with open(file_path,'r') as file:
        character = json.load(file)
        
    return(character)

## Convert the dmap and character data into a JSON file to be used later ##
## Save name is character name + date + seconds from epoch ##
## This is to make sure we can never have two folders with the same name ##
def save_game(character,filename):
    save_path = 'saves/{}.json'.format(filename)
    try:
        with open(save_path,'w') as file:
            json.dump(character, file)
    except:
        print("Could not save char!  Dumping char info")
        print(character)
        raise
        
    print("Saved!")
    
    
def save_menu(win,x,y,player):
    win = clear_win(win)
    win["win"].setBackground("black")
    reset_xset()
    
    to_draw,buttons = [],[]
    
    title = Text(Point(x/2,50),"Save Game")
    title.setTextColor("white")
    title.setSize(28)
    title.setStyle("bold")
    to_draw.append(title)
    
    
    save_button = new_button(100,y-350,200,200,"Save","save","blue","white","yellow",30)
    buttons.append(save_button)
    to_draw.append(save_button["button"])
    to_draw.append(save_button["text"])
    
    entry_box = Rectangle(Point((x/2)-500,(y/2)-300),Point((x/2)+500,(y/2)+100))
    entry_box.setFill("white")
    entry_box.setOutline("yellow")
    entry_box.setWidth(3)
    to_draw.append(entry_box)
    
    entry_text = Text(Point(x/2,(y/2)-200),"Save File Name")
    entry_text.setTextColor("black")
    entry_text.setSize(28)
    to_draw.append(entry_text)
    
    name_entry = Entry(Point(x/2,y/2),40)
    name_entry.setSize(20)
    to_draw.append(name_entry)
    
    
    exit_button = new_button(x-200,y-300,150,150,"BACK","go back","red3","white","yellow",30)
    buttons.append(exit_button)
    to_draw.append(exit_button["button"])
    to_draw.append(exit_button["text"])
    
    
    for item in to_draw:
        item.draw(win["win"])
    
    play = True
    while play:
        click = win["win"].checkMouse()
        key = win["win"].checkKey()
        
        if click != None:
            clicked_on = interpret_click(win,buttons,click)
        
            if clicked_on == "save":
                ## Check if save with that name already exists ##
                ## If so, give option to abort ##
                saves = import_saves()

                ## If all checks pass, save file ##
                save_game(player,name_entry.getText())
                show_info_box(x,y,win,"Saved game!","Click screen\nto continue")

            elif clicked_on == "go back":
                play = False

        
        if key == "Escape":
            play = False
    
    set_xset()
    win = clear_win(win)
    return

    
def load_menu(win,x,y,player):
    win = clear_win(win)
    win["win"].setBackground("black")
    
    to_draw,buttons = [],[]
    
    title = Text(Point(x/2,100),"Load Game")
    title.setTextColor("white")
    title.setSize(28)
    title.setStyle("bold")
    to_draw.append(title)
    
    saves = import_saves()
    
    y_top = 0
    for save in saves:
        y_top += 150
        nb = new_button(50,y_top,500,100,save,save,"green","white","white",18)
        buttons.append(nb)
        to_draw.append(nb["button"])
        to_draw.append(nb["text"])
    
    
    exit_button = new_button(x-200,y-300,150,150,"BACK","go back","red3","white","yellow",30)
    buttons.append(exit_button)
    to_draw.append(exit_button["button"])
    to_draw.append(exit_button["text"])
    
    
    for item in to_draw:
        item.draw(win["win"])
    
    play = True
    while play:
        click = win["win"].checkMouse()
        key = win["win"].checkKey()
        
        if click != None:
            clicked_on = interpret_click(win,buttons,click)
            
            if clicked_on == "go back":
                play = False
            elif clicked_on != None:
                player = load_game(win,clicked_on)
                play = False
                show_info_box(x,y,win,"Loaded game!","Click screen\nto continue")
                print("Loaded game!")
        
        if key == "Escape":
            play = False
    
    win = clear_win(win)
    return(player)
    
## ##
## ## Save functions end
## ##


    
def shop_menu(win,x,y,player,shop):
    ## Clear the screen
    win = clear_win(win)
    
    win["win"].setBackground(random.choice(["green4","blue4","red4","orange4"]))
    
    
    bottom_row_top = y-200
    
    ## Title, player name, player cash
    win,bar = draw_player_bar(win,player,shop["name"])
    

    
    to_draw = []
    
    ## Current item display
    item_text = Text(Point(x/2,200),"This is text about an item")
    item_text.setTextColor("white")
    item_text.setSize(28)
    item_text.setStyle("bold")
    to_draw.append(item_text)
    
    item_subtext = Text(Point(x/2,400),"This is  descriptive text about an item")
    item_subtext.setTextColor("white")
    item_subtext.setSize(16)
    to_draw.append(item_subtext)
    
    price_text = Text(Point(x/2,y-400),"This is the items price")
    price_text.setTextColor("white")
    price_text.setSize(16)
    price_text.setStyle("bold")
    to_draw.append(price_text)
    
    
    ## Buttons
    buttons = []
    
    
    buy_button = new_button((x/2)-100,bottom_row_top-150,200,200,"BUY","buy","blue","white","yellow",30)
    buttons.append(buy_button)
    to_draw.append(buy_button["button"])
    to_draw.append(buy_button["text"])
    
    left_button = new_button(
        (x/2)-400,bottom_row_top-100,250,100,"<-","left arrow","blue2","white","yellow",30)
    buttons.append(left_button)
    to_draw.append(left_button["button"])
    to_draw.append(left_button["text"])
    
    right_button = new_button(
        (x/2)+150,bottom_row_top-100,250,100,"->","right arrow","blue2","white","yellow",30)
    #right_button["button"] = Rectangle(Point((x/2)+150,bottom_row_top),Point((x/2)+400,bottom_row_top-100))
    buttons.append(right_button)
    to_draw.append(right_button["button"])
    to_draw.append(right_button["text"])
    
    exit_button = new_button(x-200,bottom_row_top-100,150,150,"BACK","go back","red3","white","yellow",30)
    #exit_button["button"] = Rectangle(Point(x-150,bottom_row_top),Point(x-50,bottom_row_top-100))
    buttons.append(exit_button)
    to_draw.append(exit_button["button"])
    to_draw.append(exit_button["text"])
    
    
    ## Draw all pending items
    for item in to_draw:
        item.draw(win["win"])
        
        
    ## User Interaction Phase ##
    items = len(shop["items"])
    item = shop["items"][0]
    item_index = 0
    
    play = True
    
    while play:
        item = shop["items"][item_index]
        item_text.setText(shop["items"][item_index]["name"])
        item_subtext.setText(shop["items"][item_index]["details"])
        price_text.setText("${}".format(shop["items"][item_index]["price"]))
        
        click = win["win"].getMouse()
        clicked_on = interpret_click(win,buttons,click)
        if clicked_on == "go back":
            choice = "go back"
            play = False
        elif clicked_on == "race":
            choice = "race"
            play = False
        elif clicked_on == "buy":
            if player["cash"] >= shop["items"][item_index]["price"]:
                player["cash"] -= shop["items"][item_index]["price"]
                bar["player_cash"].setText(
                    "${}\nRep: {}".format(str(player["cash"]),str(player["reputation"])))
                update()
                
                if item["type"] == "car":
                    car = get_car_stats(item["name"]).copy()
                    player["storage"]["cars"].append(car)
                    show_info_box(x,y,win,"Sold!","Your new car has been\nplaced in your storage")
                    
                else:
                    if item["name"] in list(player["storage"]["items"].keys()):
                        player["storage"]["items"][item["name"]] += 1
                    else:
                        player["storage"]["items"][item["name"]] = 1
                
            else:
                show_info_box(x,y,win,"Sorry","You don't have enough money!")
            
        elif clicked_on == "left arrow":
            if item_index == 0:
                item_index = items-1
            else:
                item_index -= 1
        elif clicked_on == "right arrow":
            if item_index == items-1:
                item_index = 0
            else:
                item_index += 1
    
    return(player,choice)


def confirm_box(win,text,subtext):
    x,y = get_screen_size()
    
    to_draw, buttons = [], []
    
    box = Rectangle(
        Point((x/2)-200,(y/2)-300),Point((x/2)+200,(y/2)+300))
    box.setFill("black")
    box.setOutline("yellow")
    box.setWidth(4)
    to_draw.append(box)
    
    box_text = Text(
        Point(x/2,(y/2)-265),text)
    box_text.setTextColor("white")
    box_text.setStyle("bold")
    box_text.setSize(24)
    to_draw.append(box_text)
    
    box_subtext = Text(
        Point(x/2,(y/2)+30),subtext)
    box_subtext.setTextColor("white")
    box_subtext.setSize(16)
    to_draw.append(box_subtext)
    
    confirm_button = new_button((x/2)-150,(y/2)+250,300,60,"CONFIRM","confirm","blue","white","yellow",18)
    buttons.append(confirm_button)
    to_draw.append(confirm_button["button"])
    to_draw.append(confirm_button["text"])
    
    for item in to_draw:
        item.draw(win["win"])
    
    
    click = win["win"].getMouse()
    clicked_on = interpret_click(win,buttons,click)
    if clicked_on != None:
        choice = True
    else:
        choice = False
    
    for item in to_draw:
        item.undraw()
    
    return(choice)



def draw_player_bar(win,player,location_name):
    x,y = get_screen_size()
    
    bar = {}
    
    ## Status bar (player name, cash, reputation)
    to_draw = []
    top_bar = Rectangle(Point(0,0),Point(x,100))
    top_bar.setFill("blue")
    to_draw.append(top_bar)
    
    title = Text(Point(200,50),location_name)
    title.setTextColor("white")
    title.setSize(24)
    title.setStyle("bold")
    to_draw.append(title)
    bar["title"] = title
    
    player_name = Text(Point(x-400,50),player["name"])
    player_name.setTextColor("white")
    player_name.setSize(18)
    to_draw.append(player_name)
    bar["player_name"] = player_name
    
    player_cash = Text(Point(x-200,50),"${}\nRep: {}".format(str(player["cash"]),str(player["reputation"])))
    player_cash.setTextColor("yellow")
    player_cash.setStyle("bold")
    player_cash.setSize(18)
    to_draw.append(player_cash)
    bar["player_cash"] = player_cash
    
    for item in to_draw:
        item.draw(win["win"])
    
    return(win,bar)


## Rather than type out 11 lines of code per button, use this function to do it in 1 line ##
def new_button(x1,y1,x_size,y_size,text,function,fill_color,text_color,outline_color,text_size):
    button = {}
    button["button"] = Rectangle(Point(x1, y1),Point(x1+x_size,y1+y_size))
    button["button"].setFill(fill_color)
    button["button"].setOutline(outline_color)
    button["button"].setWidth(2)
    button["text"] = Text(Point(x1+(x_size/2),y1+(y_size/2)),text)
    button["text"].setTextColor(text_color)
    button["text"].setSize(text_size)
    button["function"] = function
    button["fill_color"] = fill_color
    button["text_color"] = text_color
    
    return(button)


## RETURNS to RACER MENU
def storage_menu(win,player):
    win = clear_win(win)
    x,y = get_screen_size()
    
    win,bar = draw_player_bar(win,player,"Storage Warehouse")
    
    buttons = []
    to_draw = []
    
    ## Back (to racer menu)
    go_back = new_button(x-400,600,200,200,"BACK","go back","red4","white","yellow",30)
    buttons.append(go_back)
    to_draw.append(go_back["button"])
    to_draw.append(go_back["text"])
    
    cars_heading = Text(Point(250,200),"Stored Cars")
    cars_heading.setTextColor("white")
    cars_heading.setSize(28)
    to_draw.append(cars_heading)
    
    button_y = 260
    
    for item in player["storage"]["cars"]:
        car_button = new_button(
            50,button_y,400,80,item["name"]+"\n"+item["plate"],item["plate"],"blue","white","yellow",18)
        button_y += 120
        buttons.append(car_button)
        to_draw.append(car_button["button"])
        to_draw.append(car_button["text"])

        
    for item in to_draw:
        item.draw(win["win"])
    
    play = True
    
    while play:
        click = win["win"].getMouse()
        clicked_on = interpret_click(win,buttons,click)
        if clicked_on != "go back":
            
            car_list = player["storage"]["cars"]
            for car in car_list:
                if clicked_on == car["plate"]:
                    chosen_car = car
                    
                    car_subtext = ""
                    for item in list(car.keys()):
                        car_subtext += (item+": "+str(car[item])+"\n")

                    show_info_box_tall(x,y,win,car["name"],car_subtext)
                    player = switch_cars(player,player["car"],car)
                    choice = clicked_on
                    play = False

        elif clicked_on == "go back":
            choice = "go back"
            play = False
    
    return(choice,player)


## RETURNS to RACER MENU
def hotel_menu(win,player):
    win = clear_win(win)
    x,y = get_screen_size()
    
    win,bar = draw_player_bar(win,player,"Le Hotel")
    
    buttons = []
    to_draw = []

    ## Save Game (not yet functioning)
    save_button = new_button(200,200,200,200,"SAVE","save","blue","white","yellow",30)
    buttons.append(save_button)
    to_draw.append(save_button["button"])
    to_draw.append(save_button["text"])
    
    
    ## Load Game (not yet functioning)
    load_button = new_button((x/2)-100,200,200,200,"LOAD","load","blue","white","yellow",30)
    buttons.append(load_button)
    to_draw.append(load_button["button"])
    to_draw.append(load_button["text"])
    
    
    ## Back (to racer menu)
    back_button = new_button(x-400,200,200,200,"BACK","back","blue","white","yellow",30)
    buttons.append(back_button)
    to_draw.append(back_button["button"])
    to_draw.append(back_button["text"])
    
    
    ## Exit (to main menu)
    exit_button = new_button(x-400,600,200,200,"EXIT\nGAME","exit","red3","white","yellow",30)
    buttons.append(exit_button)
    to_draw.append(exit_button["button"])
    to_draw.append(exit_button["text"])
    
    
    for item in to_draw:
        item.draw(win["win"])
    
    play = True
    
    while play:
        click = win["win"].getMouse()
        clicked_on = interpret_click(win,buttons,click)
        if clicked_on == "exit":
            choice = "exit"
            play = False
        elif clicked_on == "save":
            choice = "save"
            #show_info_box(x,y,win,"Sorry!","This feature is not reay yet!")
            save_menu(win,x,y,player)
            for item in to_draw:
                item.draw(win["win"])
        elif clicked_on == "load":
            choice = "load"
            #show_info_box(x,y,win,"Sorry!","This feature is not reay yet!")
            player = load_menu(win,x,y,player)
            for item in to_draw:
                item.draw(win["win"])
        elif clicked_on == "back":
            choice = "back"
            play = False
    
    return(choice,player)


## RETURNS to MAIN
def racer_menu(win,player):
    ## An array of buttons
    ## Eventually replace by images?
    win = clear_win(win)
    x,y = get_screen_size()
    bottom_row_top = y-200
    
    win["win"].setBackground(random.choice(["green4","blue4","red4","orange4"]))
    
    
    win,bar = draw_player_bar(win,player,"Main Street")
    
    
    ## ## Buttons ## ##    
    buttons = []
    to_draw = []

    
    ## Shop (purchase items or cars)
    shop_button = new_button(200,200,200,200,"SHOP","shop","blue","white","yellow",30)
    buttons.append(shop_button)
    to_draw.append(shop_button["button"])
    to_draw.append(shop_button["text"])
    
    
    ## Garage (modify or repair current car)
    garage_button = new_button((x/2)-125,200,250,200,"GARAGE","garage","blue","white","yellow",30)
    buttons.append(garage_button)
    to_draw.append(garage_button["button"])
    to_draw.append(garage_button["text"])
    
    
    ## Road (start next race)
    road_button = new_button(x-400,200,200,200,"ROAD","road","green3","white","yellow",30)
    buttons.append(road_button)
    to_draw.append(road_button["button"])
    to_draw.append(road_button["text"])
    
    
    ## Storage (manage cars and inventory)
    storage_button = new_button((x/2)-125,600,250,200,"STORAGE","storage","blue","white","yellow",28)
    buttons.append(storage_button)
    to_draw.append(storage_button["button"])
    to_draw.append(storage_button["text"])
    
    
    ## Hotel (save/load/exit)
    hotel_button = new_button(x-400,600,200,200,"HOTEL","hotel","blue","white","yellow",30)
    buttons.append(hotel_button)
    to_draw.append(hotel_button["button"])
    to_draw.append(hotel_button["text"])

    
    ## Render all pending items
    for item in to_draw:
        item.draw(win["win"])
        
        
    ## Begin loop
    play = True
    while play:
        click = win["win"].getMouse()
        clicked_on = interpret_click(win,buttons,click)
        choice = clicked_on
        if choice != None:
            play = False
    
    return(player,choice)



def choose_race(win,player):
    win = clear_win(win)
    x,y = get_screen_size()
    win,bar = draw_player_bar(win,player,"Main Street")
    
    ## Create empty lists
    buttons, to_draw = [], []
    
    easy_race = new_button(200,200,200,200,"EASY","easy race","green3","white","black",30)
    buttons.append(easy_race)
    to_draw.append(easy_race["button"])
    to_draw.append(easy_race["text"])
    
    test_race = new_button(200,600,200,200,"TEST","test race","blue3","white","black",30)
    buttons.append(test_race)
    to_draw.append(test_race["button"])
    to_draw.append(test_race["text"])
    
    mid_race = new_button((x/2)-125,200,250,200,"MEDIUM","mid race","yellow2","black","black",30)
    buttons.append(mid_race)
    to_draw.append(mid_race["button"])
    to_draw.append(mid_race["text"])
    
    hard_race = new_button(x-400,200,200,200,"HARD","hard race","orange","white","black",30)
    buttons.append(hard_race)
    to_draw.append(hard_race["button"])
    to_draw.append(hard_race["text"])
    
    go_back = new_button(x-400,600,200,200,"BACK","go back","red4","white","yellow",30)
    buttons.append(go_back)
    to_draw.append(go_back["button"])
    to_draw.append(go_back["text"])
    
    ## Render all pending items
    for item in to_draw:
        item.draw(win["win"])
        
    ## Begin loop
    play = True
    while play:
        click = win["win"].getMouse()
        clicked_on = interpret_click(win,buttons,click)
        choice = clicked_on
        if choice != None:
            text = choice
            if text == "easy race":
                subtext = "Prize: $1000\n\nDistance: 2km\nLanes: 8\nTraffic: 10\nPar Speed: 100mph"
            elif text == "mid race":
                subtext = "Prize: $1500\n\nDistance: 5km\nLanes: 6\nTraffic: 10\nPar Speed: 110mph"
            elif text == "hard race":
                subtext = "Prize: $2500\n\nDistance: 5km\nLanes: 4\nTraffic: 10\nPar Speed: 120mph"
            elif text == "test race":
                subtext = "Prize: $0\n\nDistance: 5km\nLanes: 8\nTraffic: 0\nPar Speed: 120mph"
            elif text == "go back":
                play = False
                return(choice)
                
            if confirm_box(win,text.capitalize(),subtext): #Returns a bool
                play = False
    
    return(choice)

    
    
def main_menu(win):
    x,y = get_screen_size()
    
    win = clear_win(win)
    
    win["win"].setBackground("black")
    
    title = Text(Point(x/2,100),"RACER!")
    title.setTextColor("white")
    title.setStyle("bold")
    title.setSize(36)
    title.draw(win["win"])
    
    subtitle = Text(Point(x/2,200),"Slam Jones 2023")
    subtitle.setTextColor("white")
    subtitle.setSize(24)
    subtitle.draw(win["win"])
    
    buttons = []
    to_draw = []
    
    new_game = new_button((x/2)-400,300,800,150,"NEW GAME","start new game","blue","white","yellow",30)
    to_draw.append(new_game["button"])
    to_draw.append(new_game["text"])
    buttons.append(new_game)
    
    load_game = new_button((x/2)-400,500,800,150,"LOAD GAME","load game","blue","white","yellow",30)
    to_draw.append(load_game["button"])
    to_draw.append(load_game["text"])
    buttons.append(load_game)
    
    exit = {}
    exit = new_button((x/2)-400,700,800,100,"EXIT","exit","red3","white","yellow",30)
    to_draw.append(exit["button"])
    to_draw.append(exit["text"])
    buttons.append(exit)
    
    for item in to_draw:
        item.draw(win["win"])
    
    play = True
    
    while play:
        click = win["win"].getMouse()
        clicked_on = interpret_click(win,buttons,click)
        if clicked_on != None:
            play = False
            return(win,clicked_on)
    
    
    return(win,None)


## Takes a list of buttons and a click ##
## Returns the function of the button, if any, that was clicked on ##
## Otherwise returns None ##
def interpret_click(win,buttons,click):
    click_x, click_y = click.getX(), click.getY()
    for button in buttons:
        x1 = button["button"].getP1().getX()
        y1 = button["button"].getP1().getY()
        x2 = button["button"].getP2().getX()
        y2 = button["button"].getP2().getY()
        
        if x1 > x2:
            x1,x2 = x2,x1
        if y1 > y2:
            y1,y2 = y2,y1
        
        if click_x >= x1 and click_x <= x2 and click_y >= y1 and click_y <= y2:
            button["button"].setFill("white")
            button["text"].setTextColor("black")
            update()
            sleep(0.15)
            button["button"].setFill(button["fill_color"])
            button["text"].setFill(button["text_color"])
            update()
            sleep(0.05)
            print("Clicked on {}".format(button["function"]))
            return(button["function"])
    
    return(None)



def new_race(distance,cash_prize,lanes,traffic_level,par_speed):
    road = gen_new_road(lanes)
    road["finish"] = distance
    road["win_cash"] = cash_prize
    
    
    x,y = get_screen_size()
    x_center = x/2
    y_center = y/2
    
    road_obj = Rectangle(Point(x_center-(road["width"]/2), 0), Point(x_center+(road["width"]/2), y))
    road_obj.setFill("gray")
    
    par_time = int((distance*3600)/par_speed) #par_time in seconds, distance in miles, par_speed in miles per hour
    
    return(road,road_obj,distance,traffic_level,par_time)
    


def main():
    print("Let's race!!")
    x,y = get_screen_size()
    x_center = x/2
    y_center = y/2
    
    win = open_window("Racer",x,y)
    choice = ""
    
    run = True
    while run:
        ## Bring up Main Menu first ##
        ## Options are start new game or exit ##
        win,clicked_on = main_menu(win)
        if clicked_on == "exit":
            win = close_window(win)
            print("Cya!!")
            return

        elif clicked_on == "start new game":
            win = clear_win(win)
            ## Establish player ##
            player = {}
            player["name"] = "Player 1"
            player["cash"] = 4000
            player["reputation"] = 0
            player["car"] = get_car_stats("Jones C180").copy()
            player["car"]["name"] = "Jones C180"
            player["storage"] = {}
            player["storage"]["cars"] = []
            player["storage"]["items"] = {}

            results = ""
            run = False

        elif clicked_on == "load game":
            player = {}
            win = clear_win(win)
            player = load_menu(win,x,y,player)
            if player != {}:
                run = False
    
    ## After Race ##
    while choice != "exit":
        
        player,choice = racer_menu(win,player)
        win = clear_win(win)
        
        if choice == "race" or choice == "road":
            choice = choose_race(win,player)
            start = True
            if choice == "easy race":
                distance = 2
                cash_prize = 1000
                rep_prize = 5
                lanes = 8
                traffic = 10
                par_speed = 100
                biome = "grass"
            elif choice == "mid race":
                distance = 5
                cash_prize = 1500
                rep_prize = 10
                lanes = 6
                traffic = 10
                par_speed = 110
                biome = "desert"
            elif choice == "hard race":
                distance = 5
                cash_prize = 2500
                rep_prize = 20
                lanes = 4
                traffic = 10
                par_speed = 120
                biome = "snow"
            elif choice == "test race":
                distance = 5
                cash_prize = 0
                rep_prize = 0
                lanes = 8
                traffic = 0
                par_speed = 120
                biome = "grass"
            else:
                start = False
            if start:
                road,road_obj,distance,traffic_level,par_time = new_race(
                    distance,cash_prize,lanes,traffic,par_speed)
                results = play(
                    win,player,road,road_obj,distance,traffic_level,par_time,cash_prize,rep_prize,biome)
                
        elif choice == "shop":
            shop = new_shop()
            player,choice = shop_menu(win,x,y,player,shop)
            win = clear_win(win)
            
        elif choice == "storage":
            while choice != "go back":
                choice,player = storage_menu(win,player)
            
        elif choice == "hotel":
            choice,player = hotel_menu(win,player)
            if choice == "exit":
                win = close_window(win)
                print("Cya!!")   
                return
            
        elif choice == "garage":
            shop = {}
            shop["name"] = "Cool Dude Garage"
            player = garage_menu(win,player,shop)
            win = clear_win(win)
            
        else:
            win = close_window(win)
            print("Cya!!")
            return
    else:
        win = close_window(win)
        print("Cya!!")
        return
    
def calc_distance_to_next_turn(distance_covered,turns):
    for turn in turns:
        if turn["start"] > distance_covered:
            if turn["severity"] > 0:
                turn_dir = "<"
            else:
                turn_dir = ">"
            return(abs(distance_covered - turn["start"]),turn_dir)
    return(None,None)

        
        
        
    
def play(win,player,road,road_obj,distance,traffic_level_base,par_time,cash_prize,rep_prize,biome):
    x,y = get_screen_size()
    x_center,y_center = x/2, y/2
    
    set_xset()
    
    win = clear_win(win)
    
    distance_covered = 0
    
    obstable_imgs = []
    
    if biome == "grass":
        win["win"].setBackground("green")
        obstacle_imgs = ["img/Tree.png","img/Grass.png"]
    elif biome == "desert":
        win["win"].setBackground("bisque")
        obstacle_imgs = ["img/Rock.png","img/Bush.png"]
    elif biome == "snow":
        win["win"].setBackground("snow")
        obstacle_imgs = ["img/Rock.png","img/Wolf1.png"]
    
    #road,road_obj = new_race(5,1000,8,10)
    
    ## Prepare empty Lists ##
    obstacle_list = []
    car_list = []
    
    ## Establish road ##
    road_obj.draw(win["win"])
    
    ## Establish center divider marks
    mark = gen_road_marks()
    mark_obj = Rectangle(
        Point(x_center-(mark["width"]/2), 0), Point(x_center+(mark["width"]/2), mark["length"]))
    mark_obj.setFill(mark["color"])
    mark_list = []
    mark_list.append(mark_obj)
    marks_to_draw = int(y/(mark["length"]*2))
    mark_top = 0
    
    for i in range(marks_to_draw):
        mark_top += mark["length"]*2
        mark_obj = Rectangle(
            Point(x_center-(mark["width"]/2), mark_top), 
            Point(x_center+(mark["width"]/2), mark_top + mark["length"]))
        mark_obj.setFill(mark["color"])
        mark_list.append(mark_obj)
        
    for obj in mark_list:
        obj.draw(win["win"])
    
    
    
    player_car = player["car"]
    
    ## Establish player car ##
    car = {}
    car["length"] = 65
    car["width"] = 25
    car["color"] = "blue"
    car["outline"] = "yellow"
    car_obj = Rectangle(
        Point(x_center*(9/8),y_center*1.5), Point(x_center*(9/8)+car["width"],(y_center*1.5)-car["length"]))
    car_obj.setFill(car["color"])
    car_obj.setOutline(car["outline"])
    car_obj.setWidth(2)
    car["obj"] = car_obj
    car_obj.draw(win["win"])
    
    ## Starting speed, a bit below road speed limit ##
    speed = 12
    turning = 0
    
    max_speed = int(player["car"]["max_speed"]/5)
    max_onroad_speed = int(player["car"]["max_speed"]/5)
    max_offroad_speed = int(player["car"]["max_speed_offroad"])/5
    acceleration = player["car"]["acceleration"]
    braking = player["car"]["braking"]
    handling = player["car"]["handling"]
    if handling == 0:
        handling = 0.5
    
    
    
    ## Establish info bar ##
    bar = gen_stat_bar(x,y)
    
    bar_obj = Rectangle(Point(0,0),(Point(bar["width"],bar["height"])))
    bar_obj.setFill(bar["color"])
    bar_obj.setOutline(bar["outline"])
    bar_obj.setWidth(2)
    bar_obj.draw(win["win"])
    
    speed_x = int(bar["width"]*0.8)
    speed_y = int(bar["height"]/2)
    speed_obj = Text(Point(speed_x,speed_y),"Speed: 0mph")
    speed_obj.setTextColor("white")
    speed_obj.setSize(16)
    speed_obj.draw(win["win"])
    
    dist_x = int(bar["width"]*0.15)
    dist_y = int(bar["height"]/2)
    dist_obj = Text(Point(dist_x,dist_y),"Distance Covered: 0 / 0 miles")
    dist_obj.setTextColor("white")
    dist_obj.setSize(16)
    dist_obj.draw(win["win"])
    
    time_x = int(bar["width"]*0.5)
    time_y = int(bar["height"]/2)
    time_obj = Text(Point(time_x,time_y),"Par Time: {} seconds".format(par_time))
    time_obj.setTextColor("white")
    time_obj.setSize(16)
    time_obj.draw(win["win"])
    
    turn_x = int(bar["width"]*0.65)
    turn_y = int(bar["height"]/2)
    turn_obj = Text(Point(turn_x,turn_y),"^\n|")
    turn_obj.setTextColor("white")
    turn_obj.setSize(16)
    turn_obj.draw(win["win"])
    
    
    timer_start = time()
    
    turns = [{"start": 0.5, "end": 1, "severity": 1},
            {"start": 1.5, "end": 2, "severity": -2},
            {"start": 2.5, "end": 3, "severity": 3},
            {"start": 3.5, "end": 4, "severity": -4},
            {"start": 4.5, "end": 5, "severity": 5}]
    
    
    show_info_box(x,y,win,"READY TO RACE!","Click screen to begin!")
    
    paused = False
    play = True
    while play:
        while paused:
            key = win["win"].getKey()
            if key != "Escape":
                paused = False
                
        for mark_obj in mark_list:
            mark_obj.move(0,speed)
            
            if mark_obj.getP2().getY() >= y:
                mark_obj.move(0,-y)
                
        for obstacle in obstacle_list:
            obstacle.move(0,speed)
            
            #if obstacle.getP2().getY() >= y:
            try:
                if obstacle.getCenter().getY() >= y:
                    obstacle.undraw()
                    obstacle_list.remove(obstacle)
            except:
                if obstacle.getAnchor().getY() >= y:
                    obstacle.undraw()
                    obstacle_list.remove(obstacle)
                
        for ai_car in car_list:
            ai_car["obj"].move(0,ai_car["speed"]+speed)
            
            if ai_car["obj"].getP2().getY() >= y or ai_car["obj"].getP1().getY() <= 80:
                ai_car["obj"].undraw()
                car_list.remove(ai_car)
                
            crashed = collision_check(car,ai_car)
            if crashed:
                show_info_box(x,y,win,"You crashed!","Game over man, game over!")
                print("You crashed!!  Game over, man, game over!!")
                return("Crashed")
                play = False
                
                
        if is_car_on_road(x,car,road):
            max_speed = max_onroad_speed
        else:
            max_speed = max_offroad_speed
            if speed > max_offroad_speed:
                speed -= 1
        
        if traffic_level_base != 0:
            traffic_level = traffic_level_base + distance_covered
        else:
            traffic_level = 0
            
        string = text_bar(speed,max_speed,20)
        speed_obj.setText("Speed: {}mph\n{}".format(str(int(speed*5)),string))
        speed_obj.setFace("courier")
        string = text_bar(distance_covered,road["finish"],20)
        dist_obj.setText("Distance Covered: {} miles\n{}".format(
            str('{0:.2f}'.format(distance_covered)), string))
        dist_obj.setFace("courier")
        timer = time() - timer_start
        #mins = timer % 60
        #secs = timer - (60*mins)
        #time_obj.setText("Time Elapsed: {}:{}".format(str(mins),str(secs)))
        time_obj.setText("Par Time: {} seconds\nTime Elapsed: {} seconds".format(par_time,str(round(timer))))
        if par_time < timer:
            time_obj.setTextColor("red")
            time_obj.setStyle("bold")
        
        ## Yes, it's a magic number ##
        ## No, I don't feel like making it dynamic ##
        distance_covered += speed/21600
        
        if distance_covered >= road["finish"]:
            if par_time > timer:
                show_info_box(x,y,win,"You reached the\nfinish line!","You win ${}!".format(cash_prize))
                player["cash"] += cash_prize
                player["reputation"] += rep_prize
            else:
                show_info_box(x,y,win,"Too slow!","Better luck next time!")
            print("You reached the finish!  Congrats!")
            return("Finished")
                
        distance_to,turn_dir = calc_distance_to_next_turn(distance_covered,turns)
        if distance_to != None:
            if turn_dir == "<":
                turn_obj.setText("<-\nin {:0.2f}km".format(distance_to))
            else:
                turn_obj.setText("->\nin {:0.2f}km".format(distance_to))
        else:
            turn_obj.setText("^\n|")
            
        for turn in turns:
            if turn["start"] < distance_covered and turn["end"] > distance_covered:
                if turn["severity"] > 0:
                    turn_obj.setText("<-- {}\n{:0.2f}km".format(
                        abs(turn["severity"]),abs(distance_covered - turn["end"])))
                else:
                    turn_obj.setText("--> {}\n{:0.2f}km".format(
                        abs(turn["severity"]),abs(distance_covered - turn["end"])))
                    
                if speed > 0:
                    car_obj.move((turn["severity"]/(70/speed)),0)
        
        
        update(30)
        
        
        
        
        
        ## USER INPUT VIA KEYBOARD MODULE ##
        ## ONLY WORKS IN ROOT, WHERE GRAHPICS MODULE DOESN'T WORK ^*!$@&!*$ ##
        #if keyboard.is_pressed('escape'):
        #    play = False
        
        
        ## USER INPUT VIA GRAPHICS MODULE ##
        ## ONLY ALLOWS ONE CONCURRENT KEYPRESS ##
        key = win["win"].checkKey()
        if key == "Escape":
            paused = True
        if key == "Up":
            if speed < max_speed:
                speed += acceleration/10
                if speed > max_speed:
                    speed = max_speed
        if key == "Down":
            if speed > 0:
                speed -= braking/10
                if speed < 0:
                    speed = 0
        if key == "Left":
            if speed > 0:
                if -turning < handling:
                    turning -= handling/5
                    if -turning > handling:
                        turning = -handling
                #turning = -handling
                #car_obj.move(-handling,0)
        if key == "Right":
            if speed > 0:
                if turning < handling:
                    turning += handling/5
                    if turning > handling:
                        turning = handling
                #turning = handling
                #car_obj.move(handling,0)
                
        if turning > 0:
            turning -= (turning/10)
        elif turning < 0:
            turning -= (turning/10)
                
                
        if speed > 0:
            car_obj.move(turning,0)
            new_obstacle_check = random.randrange(int(100/speed))
            if new_obstacle_check < 10:
                obstacle = gen_random_obstacle(x,y,road["width"],obstacle_imgs)
                obstacle.draw(win["win"])
                obstacle_list.append(obstacle)
                
        new_car_check = random.randrange(int(100))
        if new_car_check < traffic_level:
            ai_car = gen_random_car(x,y,road,speed)
            spawn_check = can_car_spawn(ai_car,car_list)
            if spawn_check:
                ai_car["obj"].draw(win["win"])
                car_list.append(ai_car)
    
    reset_xset()
    return
    
    
main()
    
## -------------- ##
    