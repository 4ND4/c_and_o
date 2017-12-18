import Tkinter
import datetime
import os

def with_ping(hostname):
    return True if os.system("ping -c 1 " + hostname) is 0 else False


def check_connectivity():

    result = with_ping('192.168.1.1')

    if result:
        print "Connection Available " + str(datetime.datetime.utcnow())
        return 'green'

    else:
        print "Offline" + str(datetime.datetime.utcnow())
        print "Trying to connect to the ad-hoc network"
        result = os.system("networksetup -setairportnetwork en0 RPiBatman")
        print(result)
        return 'red'
        #return 'images/offline.jpg'


def junk():
    def color_poll():
        global alarm
        c.itemconfig(r, fill=check_connectivity())

        #c.itemconfig(photo, file=check_connectivity())

        if keep_going:
            alarm = c.after(1000, color_poll)

    def change_color():
        global keep_going, alarm
        if not keep_going:
            keep_going = True
            color_poll()
        else:
            keep_going = False
            c.after_cancel(alarm)
            alarm = None

    root = Tkinter.Tk()

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()

    c = Tkinter.Canvas(master=root)


    #x.overrideredirect(True)

    #root.attributes("-fullscreen", True)

    root.geometry("%dx%d+0+0" % (w, h))

    r = c.create_rectangle(0, 0, w, h)

    global keep_going, alarm

    keep_going = False
    alarm = None

    change_color()

    c.pack(fill=Tkinter.BOTH, expand=Tkinter.YES)
    root.mainloop()


junk()
