import curses, datetime

stdscr = curses.initscr()
curses.noecho()

def sprint(string,x,y):
    stdscr.addstr(x,y,string)

what = ["st","nd","rd"]

while True:
    time = datetime.datetime.now()
    try:
        day = str(time.day) + what[time.day-1]
    except:
        day = str(time.day) + "th"
    real = time.strftime(f"%B {day} %Y, %H:%M:%S")
    sprint(real,0,0)
    stdscr.refresh()

curses.endwin()