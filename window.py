from parkomat import *
from tkinter import *
from tkinter import Label
from tkinter import Button
from tkinter import Spinbox




Park = Parkomat()
window = Tk()
window.geometry('600x600')
window.resizable(width=False, height=False)
title = Label(window, text = 'Parkomat Box')
title.config( font=('Arial', 30,))
title.pack()

def number_of_coins(coin_button):
    return number_of_coins_spinbox.get()


button1 = Button(window, height=1, width=10, background='grey', text='1gr',
                 command=lambda: [Park.add_coins(0.01, number_of_coins(number_of_coins_spinbox)),
                                  date_of_departure.configure(text=str(Park.get_leaving_time()))])
button1.place(x=160, y=320)


button2 = Button(window, height=1, width=10, background='grey', text='2gr',
                 command=lambda: [Park.add_coins(0.02, number_of_coins(number_of_coins_spinbox)),
                                  date_of_departure.configure(text=str(Park.get_leaving_time()))])

button2.place(x=240, y=320)


button3 = Button(window, height=1, width=10, background='grey', text='5gr',
                 command=lambda: [Park.add_coins(0.05, number_of_coins(number_of_coins_spinbox)),
                                  date_of_departure.configure(text=str(Park.get_leaving_time()))])

button3.place(x=320, y=320)


button4 = Button(window, height=1, width=10, background='grey', text='10gr',
                 command=lambda: [Park.add_coins(0.1, number_of_coins(number_of_coins_spinbox)),
                                  date_of_departure.configure(text=str(Park.get_leaving_time()))])

button4.place(x=160, y=360)


button5 = Button(window, height=1, width=10, background='grey', text='20gr',
                 command=lambda: [Park.add_coins(0.2, number_of_coins(number_of_coins_spinbox)),
                                  date_of_departure.configure(text=str(Park.get_leaving_time()))])

button5.place(x=240, y=360)


button6 = Button(window, height=1, width=10, background='grey', text='50gr',
                 command=lambda: [Park.add_coins(0.5, number_of_coins(number_of_coins_spinbox)),
                                  date_of_departure.configure(text=str(Park.get_leaving_time()))])

button6.place(x=320, y=360)


button7 = Button(window, height=1, width=10, background='grey', text='1zł',
                 command=lambda: [Park.add_coins(1, number_of_coins(number_of_coins_spinbox)),
                                  date_of_departure.configure(text=str(Park.get_leaving_time()))])

button7.place(x=160, y=400)


button8 = Button(window, height=1, width=10, background='grey', text='2zł',
                 command=lambda: [Park.add_coins(2, number_of_coins(number_of_coins_spinbox)),
                                  date_of_departure.configure(text=str(Park.get_leaving_time()))])

button8.place(x=240, y=400)


button9 = Button(window, height=1, width=10, background='grey', text='5zł',
                 command=lambda: [Park.add_coins(5, number_of_coins(number_of_coins_spinbox)),
                                  date_of_departure.configure(text=str(Park.get_leaving_time()))])

button9.place(x=320, y=400)


button10 = Button(window, height=1, width=10, background='grey', text='10zł',
                  command=lambda: [Park.add_coins(0.01, number_of_coins(number_of_coins_spinbox)),
                                   date_of_departure.configure(text=str(Park.get_leaving_time()))])

button10.place(x=160, y=440)


button11 = Button(window, height=1, width=10, background='grey', text='20zł',
                  command=lambda: [Park.add_coins(10, number_of_coins(number_of_coins_spinbox)),
                                   date_of_departure.configure(text=str(Park.get_leaving_time()))])

button11.place(x=240, y=440)


button12 = Button(window, height=1, width=10, background='grey', text='50zł',
                  command=lambda: [Park.add_coins(20, number_of_coins(number_of_coins_spinbox)),
                                   date_of_departure.configure(text=str(Park.get_leaving_time()))])

button12.place(x=320, y=440)


def new_window(ticket):

    new_window = Toplevel(window)
    new_window.geometry('300x100')
    new_window.resizable(width=False, height=False)
    window_name = Label(new_window, text='Ticket')
    window_name.config(font=('Alias', 20,))
    window_name.pack()
    print(ticket)
    Label(new_window, text=ticket).pack()
    current_date.configure(text=str(Park.get_actual_time()))
    date_of_departure.configure(text=str(Park.get_actual_time()))


Label(window, text='Number of coins: ').place(x=230, y=255)
number_of_coins_spinbox = Spinbox(window, from_=1, to=200, width=30, bd=6, textvariable=IntVar())
number_of_coins_spinbox.place(x=180, y=280)


Label(window, text='Current date: ').place(x=20, y=40)
current_date = Label(window, width=30, text=Park.get_actual_time())
current_date.place(x=5, y=60)


Label(window, text='Date of departure: ').place(x=20, y=80)
date_of_departure = Label(window, width=30, text=Park.get_leaving_time())
date_of_departure.place(x=5, y=100)


def confirm_license_plate():

    window.license_plate = ''
    setattr(window, 'license_plate', license_plate_typed.get(1.0, END))
    return Park.confirm(window.license_plate)


Label(window, text="License plate: (MIN 5, MAX 11)").place(x=160, y=195)
license_plate_typed = Text(window, height=1, width=25)
license_plate_typed.place(x=180, y=215)


def actual_date():

    window.date = ''
    setattr(window, 'date', new_date_typed.get(1.0, END))
    window.date = window.date.split(" ", 5)
    Park.actual_time_change(window.date[0], window.date[1], window.date[2], int(window.date[3]), int(window.date[4]),
                            int(window.date[5]))


Label(window, text="Date change (should insert into format YYYY MM DD HH MM SS:)").place(x=160, y=140)

new_date_typed = Text(window, height=1, width=25)
new_date_typed.place(x=180, y=165)


def button_date_change_save(data):
    data.configure(text=str(Park.get_actual_time()))
    date_of_departure.configure(text=str(Park.get_leaving_time()))


button_date_change = Button(window, text="Change date", background = 'light green', width=10,
                            command=lambda: [actual_date(), button_date_change_save(current_date)]).place(x=390,
                                                                                                          y=160)



confirm_button = Button(window, height=5, width=50, background='green', text='Confirm',
                        command=lambda: [new_window(confirm_license_plate())]).place(x=100, y=500)



window.mainloop()