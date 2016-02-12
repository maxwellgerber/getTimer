import curses
import datetime
import traceback

from pytimer_date import runDay
from pytimer_time import runTime
# from pytimer_dateTime import runDateTime

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

def getUserDate(day = None, rollover = False, topString = "Input your Date", bottomString = "Press Enter when done"):
    try:
        scr = startWindow()
        d = runDay(scr, rollover, topString, bottomString, day)
        stopWindow(scr)
        return d
    except:
        cleanup()

def getUserTime(time = None, rollover = False, topString = "Input your Time", bottomString = "Press Enter when done"):
    try:
        scr = startWindow()
        d = runTime(scr, rollover, topString, bottomString, time)
        stopWindow(scr)
        return d
    except:
        cleanup()

# def getUserDateTime(dt = None, rollover = False, topString = "Input your Date", bottomString = "Press Enter when done"):
#     try:
#         scr = startWindow()
#         d = runDateTime(scr, rollover, topString, bottomString, dt)
#         stopWindow(scr)
#         return d
#     except:
#         cleanup()