import curses
import datetime
import traceback

from .getTimerDate import runDay
from .getTimerTime import runTime
from .getTimerDateTime import runDateTime

__all__ = ['getUserDate', 'getUserTime', 'getUserDateTime']

def _startWindow():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    curses.curs_set(0)
    return stdscr

def _stopWindow(stdscr):
    stdscr.erase()
    stdscr.refresh()
    stdscr.keypad(0)
    curses.echo()
    curses.curs_set(1)
    curses.nocbreak()
    curses.endwin() 

def _cleanup():
    curses.echo()
    curses.curs_set(1)
    curses.nocbreak()
    curses.endwin()
    traceback.print_exc()

def getUserDate(start = None, rollover = False, topString = "Input your Date", bottomString = "Press Enter when done"):
    try:
        scr = _startWindow()
        d = runDay(scr, rollover, topString, bottomString, start)
        _stopWindow(scr)
        return d
    except:
        _cleanup()

def getUserTime(start = None, rollover = False, topString = "Input your Time", bottomString = "Press Enter when done"):
    try:
        scr = _startWindow()
        d = runTime(scr, rollover, topString, bottomString, start)
        _stopWindow(scr)
        return d
    except:
        _cleanup()

def getUserDateTime(dt = None, rollover = False, topString = "Input your Timestamp", bottomString = "Press Enter when done"):
    try:
        scr = _startWindow()
        d = runDateTime(scr, rollover, topString, bottomString, start)
        _stopWindow(scr)
        return d
    except:
        _cleanup()