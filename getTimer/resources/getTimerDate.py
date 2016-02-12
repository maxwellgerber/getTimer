import curses
import datetime

class date(datetime.date):

    def _days_in_month(self, year, month):
        _DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if(self._is_leap_year(year) and month == 2):
            return 29
        else:
            return _DAYS_IN_MONTH[month]

    def _is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def replace(self, year=None, month=None, day=None):
        """Return a new date with new values for the specified fields."""
        if year is None:
            year = self.year
        if month is None:
            month = self.month
        if day is None:
            day = self.day

        if month >= 13:
            month = 1
            year += 1
        if month <= 0:
            month = 12
            year -= 1

        dim = self._days_in_month(year, month)

        if day > dim:
            month += 1
            day = 1
        if day <= 0:
            month -= 1
            if(month == 0):
                month = 12
                year -= 1
            day = self._days_in_month(year, month)

        if month >= 13:
            month = 1
            year += 1
        if month <= 0:
            month = 12
            year -= 1
        return date(year, month, day)

def _alterDigitDay(cursor, day, amount):
    try:
        if(cursor == 0):
            return day.replace(year = day.year + 1000 * amount)
        elif(cursor == 1):
            return day.replace(year = day.year + 100 * amount)
        elif(cursor == 2):
            return day.replace(year = day.year + 10 * amount)
        elif(cursor == 3):
            return day.replace(year = day.year + 1 * amount)
        elif(cursor == 5):
            return day.replace(month = day.month + 10 * amount)
        elif(cursor == 6):
            return day.replace(month = day.month + 1 * amount)
        elif(cursor == 8):
            return day.replace(day = day.day + 10 * amount)
        elif(cursor == 9):
            return day.replace(day = day.day + 1 * amount)
    except ValueError:
        return day

def updateDigitDay(cursor, day, amount):
    try:
        if(cursor == 0):
            newyear = day.year % 1000 + 1000 * amount
            return day.replace(year = newyear)
        elif(cursor == 1):
            newyear = day.year - day.year%1000 + day.year % 100  + 100 * amount
            return day.replace(year = newyear)
        elif(cursor == 2):
            newyear = day.year - day.year % 100 + day.year % 10 + 10 * amount
            return day.replace(year = newyear)
        elif(cursor == 3):
            newyear = day.year - day.year % 10 + 1 * amount
            return day.replace(year = newyear)
        elif(cursor == 5):
            newmonth = day.month % 10 + 10 * amount
            return day.replace(month = newmonth)
        elif(cursor == 6):
            newmonth = day.month  - day.month % 10 + 1 * amount
            return day.replace(month = newmonth)
        elif(cursor == 8):
            newday = day.day % 10 + 10 * amount
            return day.replace(day = newday)
        elif(cursor == 9):
            newday = day.day - day.day % 10 + 1 * amount
            return day.replace(day = newday)
    except ValueError:
        return day

def displayDay(scr, day, cursor, topString, bottomString):
    string = day.isoformat()
    max_y , max_x = scr.getmaxyx()
    y =  int(max_y/2)
    x = int(max_x/2) - 5
    scr.addstr(y - 2, x - int(len(topString)/2) + 5, topString)
    scr.addstr(y, x, string[0:cursor])
    scr.addstr(y, x + cursor, string[cursor:cursor+1], curses.A_REVERSE)
    scr.addstr(y, x + cursor + 1, string[cursor+1:])
    scr.addstr(y + 2, x - int(len(bottomString)/2) + 5, bottomString)
    scr.refresh()

def runDay(scr, rollover, topString, bottomString, day = None):

    if(rollover):
        if(day == None):
            day = date.today()
        else:
            day = date(day.year, day.month, day.day)
    else:
        if(day == None):
            day = datetime.date.today()

    c = curses.KEY_MAX
    cursor = 3
    while(c != 10):
        displayDay(scr, day, cursor, topString, bottomString)
        c = scr.getch()
        if(c == curses.KEY_RIGHT) and cursor < len(str(day))-1:
            cursor += 1
            if(cursor == 4 or cursor == 7):
                cursor += 1
        elif(c == curses.KEY_LEFT) and cursor > 0:
            cursor -= 1
            if(cursor == 4 or cursor == 7):
                cursor -= 1
        elif(c == curses.KEY_UP):
            day = _alterDigitDay(cursor, day, 1)
        elif(c == curses.KEY_DOWN):
            day = _alterDigitDay(cursor, day, -1)
        else:
            try:
                i = int(c) - 48
                if(i >= 0 and i < 10):
                    day = updateDigitDay(cursor, day, i)
            except ValueError:
                pass
    return day
