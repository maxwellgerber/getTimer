import curses
import sys
import os
import datetime
import traceback

def timer(scr, rollover = True, date = datetime.datetime.today()):
    stdscr.addstr(0, 0, "Current mode: Typing mode",
              curses.A_REVERSE)
    scr.refresh()
    scr.getkey()

def alterDigitDay(cursor, day, amount):
    try:
        if(cursor == 0):
            return day.replace(year = day.year + 1000 * amount)
        elif(cursor == 1):
            return day.replace(year = day.year + 100 * amount)
        elif(cursor == 2):
            return day.replace(year = day.year + 10 * amount)
        elif(cursor == 3):
            return day.replace(year = day.year + 1 * amount)
        elif(cursor == 4):
            return day
        elif(cursor == 5):
            return day.replace(month = day.month + 10 * amount)
        elif(cursor == 6):
            return day.replace(month = day.month + 1 * amount)
        elif(cursor == 7):
            return day
        elif(cursor == 8):
            return day.replace(day = day.day + 10 * amount)
        elif(cursor == 9):
            return day.replace(day = day.day + 1 * amount)
    except ValueError:
        return day


def updateDigitDay(cursor, day, new):
    return day

def displayDay(scr, day, cursor):
    string = day.isoformat()
    max_y , max_x = scr.getmaxyx() 
    scr.addstr(int(max_y/2), int(max_x/2) - 4, string[0:cursor])
    scr.addstr(int(max_y/2), int(max_x/2) - 4 + cursor, string[cursor:cursor+1], curses.A_REVERSE)
    scr.addstr(int(max_y/2), int(max_x/2) - 4 + cursor + 1, string[cursor+1:])
    scr.refresh()

def runDay(scr,day = None):
    if(day == None):
        day = datetime.date.today()
    c = curses.KEY_MAX
    cursor = 3
    while(c != 10):
        displayDay(scr, day, cursor)
        c = scr.getch()
        if(c == curses.KEY_RIGHT) and cursor < len(str(day))-1:
            cursor += 1
        elif(c == curses.KEY_LEFT) and cursor > 0:
            cursor -= 1
        elif(c == curses.KEY_UP):
            day = alterDigitDay(cursor, day, 1)
        elif(c == curses.KEY_DOWN):
            day = alterDigitDay(cursor, day, -1)
        else:
            try:
                i = int(c)
                day = updateDigitDay(cursor, day, i)
            except ValueError:
                pass
    return day

def startWindow():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    curses.curs_set(0)
    return stdscr

def stopWindow(stdscr):
    stdscr.erase()
    stdscr.refresh()
    stdscr.keypad(0)
    curses.echo()
    curses.curs_set(1)
    curses.nocbreak()
    curses.endwin() 

def cleanup():
    curses.echo()
    curses.curs_set(1)
    curses.nocbreak()
    curses.endwin()
    traceback.print_exc()

def getUserDay():
    try:
        scr = startWindow()
        d = runDay(scr)
        stopWindow(scr)
        return d
    except:
        cleanup()