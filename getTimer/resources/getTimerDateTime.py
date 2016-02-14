import curses
import datetime

from .getTimerDate import *
from .getTimerTime import *


def displayDateTime(scr, day, time, cursor, topString, bottomString):
    string = day.isoformat() + " " + time.isoformat()
    max_y, max_x = scr.getmaxyx()
    y = int(max_y/2)
    x = int(max_x/2) - 9
    scr.addstr(y - 2, x - int(len(topString)/2) + 9, topString)
    scr.addstr(y, x, string[0:cursor])
    scr.addstr(y, x + cursor, string[cursor:cursor+1], curses.A_REVERSE)
    scr.addstr(y, x + cursor + 1, string[cursor+1:])
    scr.addstr(y + 2, x - int(len(bottomString)/2) + 9, bottomString)
    scr.refresh()


def runDateTime(scr, rollover, topString, bottomString, start=None):
    if(rollover):
        if(start is None):
            d = date.today()
            t = time()
        else:
            d = date(start.year, start.month, start.day)
            t = time(start.hour, start.minute, start.second)
    else:
        if(start is None):
            d = datetime.date.today()
            t = datetime.time()
        else:
            d = datetime.date(start.year, start.month, start.day)
            t = datetime.time(start.hour, start.minute, start.second)

    c = curses.KEY_MAX
    cursor = 3
    while(c != 10):
        displayDateTime(scr, d, t, cursor, topString, bottomString)
        c = scr.getch()
        if(c == curses.KEY_RIGHT) and cursor < 18:
            cursor += 1
            if(cursor in (4, 7, 10, 13, 16)):
                cursor += 1
        elif(c == curses.KEY_LEFT) and cursor > 0:
            cursor -= 1
            if(cursor in (4, 7, 10, 13, 16)):
                cursor -= 1
        elif(c == curses.KEY_UP):
            if(cursor < 10):
                d = alterDigitDay(cursor, d, 1)
            else:
                t = alterDigitTime(cursor - 11, t, 1)
        elif(c == curses.KEY_DOWN):
            if(cursor < 10):
                d = alterDigitDay(cursor, d, -1)
            else:
                t = alterDigitTime(cursor - 11, t, -1)
        else:
            try:
                i = int(c) - 48
                if(i >= 0 and i < 10):
                    if(cursor < 10):
                        d = updateDigitDay(cursor, d, i)
                    else:
                        t = updateDigitTime(cursor - 11, t, i)
            except ValueError:
                pass
    return datetime.datetime(d.year, d.month, d.day,
                             t.hour, t.minute, t.second)
