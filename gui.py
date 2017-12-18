import Tkinter
import datetime
import os
import socket
from PIL import ImageTk, Image


ad_hoc_wifi = 'RPiBatman'


def with_ping(hostname):
    return True if os.system("ping -c 1 " + hostname) is 0 else False


def is_connected(ip):
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection((ip, 80))
        return True
    except Exception as ex:
        print('connection error', ex)
        return False


def check_ad_hoc(ad_hoc_network):

    check = os.system("networksetup -setairportnetwork en0 " + ad_hoc_network)

    return True if check is 0 else False


def check_connectivity():

    result = with_ping('192.168.1.1')

    if result:
        print "Connection Available " + str(datetime.datetime.utcnow())
        return 'green'
    else:
        print('Ping unavailable')
        print "Offline:" + str(datetime.datetime.utcnow())
        print('Trying to connect to ad hoc network')

        result_ad_hoc = check_ad_hoc(ad_hoc_wifi)

        if result_ad_hoc:
            print('Connected successfully')
        else:
            print('Not able to connect in this moment')

        return 'red'


def junk():
    def color_poll():
        global alarm

        fill_color = check_connectivity()

        c.itemconfig(r, fill=fill_color)

        if fill_color == 'green':
            photo_online = ImageTk.PhotoImage(Image.open('images/online.jpg'))
            panel.configure(image=photo_online)
            panel.image= photo_online
        else:
            photo_offline = ImageTk.PhotoImage(Image.open('images/offline.jpg'))
            panel.configure(image=photo_offline)
            panel.image = photo_offline

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

    photo = ImageTk.PhotoImage(Image.open('images/online.jpg'))

    panel = Tkinter.Label(root, image=photo)

    global keep_going, alarm

    keep_going = False
    alarm = None

    change_color()

    c.pack(fill=Tkinter.BOTH, expand=Tkinter.YES)
    panel.pack(side="bottom", fill="both", expand="no")

    root.mainloop()


junk()
