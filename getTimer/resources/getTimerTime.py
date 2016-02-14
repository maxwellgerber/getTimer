import curses
import datetime

class time(datetime.time):

    def replace(self, hour=None, minute=None, second=None):
        """Return a new date with new values for the specified fields."""
        if(hour == None):
            hour = self.hour
        if(minute == None):
            minute = self.minute
        if(second == None):
            second = self.second

        if(second >= 60):
            second = 0
            minute += 1
        if(second < 0):
            second = 59
            minute -= 1

        if(minute >= 60):
            minute = 0
            hour += 1
        if(minute < 0):
            minute = 59
            hour -= 1

        return time(hour, minute, second)


def alterDigitTime(cursor, t, amount):
    try:
        if(cursor == 0):
            return t.replace(hour = t.hour + 10 * amount)
        elif(cursor == 1):
            return t.replace(hour = t.hour + 1 * amount)
        elif(cursor == 3):
            return t.replace(minute = t.minute + 10 * amount)
        elif(cursor == 4):
            return t.replace(minute = t.minute + 1 * amount)
        elif(cursor == 6):
            return t.replace(second = t.second + 10 * amount)
        elif(cursor == 7):
            return t.replace(second = t.second + 1 * amount)
    except ValueError:
        return t

def updateDigitTime(cursor, t, amount):
    try:
        if(cursor == 0):
            newHour = t.hour % 10 + 10 * amount
            return t.replace(hour = newHour)
        elif(cursor == 1):
            newHour = t.hour - t.hour % 10 + 1 * amount
            return t.replace(hour = newHour)
        elif(cursor == 3):
            newMin = t.minute % 10 + 10 * amount
            return t.replace(minute = newMin)
        elif(cursor == 4):
            newMin = t.minute - t.minute % 10 + 1 * amount
            return t.replace(minute = newMin)
        elif(cursor == 6):
            newSecond = t.second % 10 + 10 * amount
            return t.replace(second = newSecond)
        elif(cursor == 7):
            newSecond = t.second - t.second % 10 + 1 * amount
            return t.replace(second = newSecond)
    except ValueError:
        return t

def displayTime(scr, time, cursor, topString, bottomString):
    string = time.isoformat()
    max_y , max_x = scr.getmaxyx()
    y =  int(max_y/2)
    x = int(max_x/2) - 4
    scr.addstr(y - 2, x - int(len(topString)/2) + 4, topString)
    scr.addstr(y, x, string[0:cursor])
    scr.addstr(y, x + cursor, string[cursor:cursor+1], curses.A_REVERSE)
    scr.addstr(y, x + cursor + 1, string[cursor+1:])
    scr.addstr(y + 2, x - int(len(bottomString)/2) + 4, bottomString)
    scr.refresh()

def runTime(scr, rollover, topString, bottomString, t = None):
    if(rollover):
        if(t == None):
            t = time()
        else:
            t = time(t.hour, t.minute, t.second)
    else:
        if(t == None):
            t = datetime.time()

    c = curses.KEY_MAX
    cursor = 3
    while(c != 10):
        displayTime(scr, t, cursor, topString, bottomString)
        c = scr.getch()
        if(c == curses.KEY_RIGHT) and cursor < len(str(t))-1:
            cursor += 1
            if(cursor == 2 or cursor == 5):
                cursor += 1
        elif(c == curses.KEY_LEFT) and cursor > 0:
            cursor -= 1
            if(cursor == 2 or cursor == 5):
                cursor -= 1
        elif(c == curses.KEY_UP):
            t = alterDigitTime(cursor, t, 1)
        elif(c == curses.KEY_DOWN):
            t = alterDigitTime(cursor, t, -1)
        else:
            try:
                i = int(c) - 48
                if(i >= 0 and i < 10):
                    t = updateDigitTime(cursor, t, i)
            except ValueError:
                pass
    return datetime.time(t.hour, t.minute, t.second)
