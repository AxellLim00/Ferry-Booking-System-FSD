import datetime
import pickle

ferry_date = ''
departure = ''
destination = ''
FID = '000'
snl = 0
f = 0
t = 0
T = 0
F = ''
time = ''
UI = ''
sn = 50
fn = 8
seat_indication = 0
ferry_indication = 0
dd = ''
temp = 0
s = []
day = 0
year = 0
month = 0
Date = ''
a = ['a', 'A']
b = ['b', 'B']
back = ['b', 'B', 'BACK', 'back', 'Back']
ferry = ['001', '002', '003', '004', '005', '006', '007', '008']
y = ['Yes', 'YES', 'Y', 'y', 'yes', 'yup', 'YUP', 'yup']
n = ['No', 'NO', 'no', 'n', 'N', 'NOPE', 'Nope', 'nope']
e = ['e', 'E', 'Edit', 'EDIT', 'edit']
c = ['c', 'C', 'Cancel', 'CANCEL', 'cancel']
name_list = ['n', 'N', 'NAME', 'name', 'Name']
class_list = ['c', 'C', 'CLASS', 'class', 'Class']
seat_number_list = ['Seat Number', 'SN', 'sn']


def var():
    global departure, destination, FID, f, t, T, F, time, sn, fn, seat_indication, ferry_indication, dd, temp
    global Date, month, year, d, snl
    departure = ''
    destination = ''
    FID = '000'
    snl = 0
    f = 0
    t = 0
    T = 0
    F = ''
    time = ''
    sn = 50
    fn = 8
    seat_indication = 0
    ferry_indication = 0
    dd = ''
    temp = 0
    d = 0
    year = 0
    month = 0
    Date = ''


def ent():  # ent is \n
    print('\n')


def fid():
    global f, t, T, time, fn
    f = int(FID[2])
    if dd in a:
        t = f + 9
    elif dd in b:
        if f < 8:
            t = f + 10
        elif f == 8:
            t = f + 2

    if t > 12:
        t = t - 12
        T = str(t)
        time = T + ' p.m.'
    elif t == 12:
        T = str(t)
        time = T + ' p.m.'
    else:
        T = str(t)
        time = T + ' a.m.'
    fn = f + ferry_indication - 1


def TIME():
    global f, T, time, FID, t, fn, F

    if dd in a:
        f = t - 9
    elif dd in b:
        if t < 17:
            f = t - 10
        elif t == 17:
            f = t - 2

    if t > 12:
        t = t - 12
        T = str(t)
        time = T + ' p.m.'

    else:
        T = str(t)
        time = T + ' a.m.'

    F = str(f)
    FID = '00' + F
    fn = f + ferry_indication - 1


def user_input():
    global UI
    UI = input('Please enter one of the Letters above : ')  # UI = User Input


def error():
    ent()
    print('Input Error, Please enter according to the menu or instructions.\n'
          '                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'
          '                ░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░\n'
          '                ░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░\n'
          '                ░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░\n'
          '                ░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░\n'
          '                ░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░\n'
          '                ░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░\n'
          '                ░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░\n'
          '                ░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░\n'
          '                ░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░\n'
          '                ░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░\n'
          '                ░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░\n'
          '                ░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░\n'
          '                ░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░\n'
          '                ░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░\n'
          '                ░░░░█░░░░░░░░░░░░░░░░░░░░░█░░\n'
          '                ░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░\n'
          '                ░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░\n'
          '                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    ent()


def seat():
    print('*********************************************************************************')
    print('*\tFerry ID : ', FID, ' \t\t\t\tDate: ', Date, '\t*')
    print('*********************************************************************************')
    print('*\t\tBUSINESS CLASS\t\t\t\t\t\t\t*')
    print('*********************************************************************************')
    print('*\t', s[fn][0], '\t*\t', s[fn][1], '\t*\t', s[fn][2], '\t*\t', s[fn][3], '\t*\t', s[fn][4], '\t*')
    print('*********************************************************************************')
    print('*\t', s[fn][5], '\t*\t', s[fn][6], '\t*\t', s[fn][7], '\t*\t', s[fn][8], '\t*\t', s[fn][9], '\t*')
    print('*********************************************************************************')
    print('*\t\tECONOMY CLASS\t\t\t\t\t\t\t*')
    print('*********************************************************************************')
    print('*\t', s[fn][10], '\t*\t', s[fn][11], '\t*\t', s[fn][12], '\t*\t', s[fn][13], '\t*\t', s[fn][14], '\t*')
    print('*********************************************************************************')
    print('*\t', s[fn][15], '\t*\t', s[fn][16], '\t*\t', s[fn][17], '\t*\t', s[fn][18], '\t*\t', s[fn][19], '\t*')
    print('*********************************************************************************')
    print('*\t', s[fn][20], '\t*\t', s[fn][21], '\t*\t', s[fn][22], '\t*\t', s[fn][23], '\t*\t', s[fn][24], '\t*')
    print('*********************************************************************************')
    print('*\t', s[fn][25], '\t*\t', s[fn][26], '\t*\t', s[fn][27], '\t*\t', s[fn][28], '\t*\t', s[fn][29], '\t*')
    print('*********************************************************************************')
    print('*\t', s[fn][30], '\t*\t', s[fn][31], '\t*\t', s[fn][32], '\t*\t', s[fn][33], '\t*\t', s[fn][34], '\t*')
    print('*********************************************************************************')
    print('*\t', s[fn][35], '\t*\t', s[fn][36], '\t*\t', s[fn][37], '\t*\t', s[fn][38], '\t*\t', s[fn][39], '\t*')
    print('*********************************************************************************')
    print('*\t', s[fn][40], '\t*\t', s[fn][41], '\t*\t', s[fn][42], '\t*\t', s[fn][43], '\t*\t', s[fn][44], '\t*')
    print('*********************************************************************************')
    print('*\t', s[fn][45], '\t*\t', s[fn][46], '\t*\t', s[fn][47], '\t*\t', s[fn][48], '\t*\t', s[fn][49], '\t*')
    print('*********************************************************************************')
    print('The Seat Arrangement above is shown as BOOKED as "1" and AVAILABLE as "0"')
    ent()


def busi():
    global sn, s, snl, temp
    while True:
        ent()
        print('*********************************************************************************')
        print('*\tFerry ID : ', FID, ' \t\t\t\tDate: ', Date, '\t*')
        print('*********************************************************************************')
        print('*\t\tBUSINESS CLASS\t\t\t\t\t\t\t*')
        print('*********************************************************************************')
        print('*\t', s[fn][0], '\t*\t', s[fn][1], '\t*\t', s[fn][2], '\t*\t', s[fn][3], '\t*\t', s[fn][4], '\t*')
        print('*********************************************************************************')
        print('*\t', s[fn][5], '\t*\t', s[fn][6], '\t*\t', s[fn][7], '\t*\t', s[fn][8], '\t*\t', s[fn][9], '\t*')
        print('*********************************************************************************')
        print('The Seat Arrangement above is shown as BOOKED as "1" and AVAILABLE as "0"')
        ent()
        sn = input('The Seats are Ordered from LEFT to RIGHT then TOP to BOTTOM.\nPlease enter a seat number '
                   'from 1 - 10 or "B" to go back: ')
        if sn in back:
            temp = 1
            break
        else:
            try:
                sn = int(sn)
            except:
                error()
                continue
        if (sn > 0) and (sn < 11):
            snl = sn + seat_indication - 1
            if s[fn][snl] == 1:
                print("I'm sorry, as you can see above the SEAT you picked is TAKEN")
                continue
            else:
                s[fn][snl] = 1
                break
        else:
            ent()
            print('Error, Please type according to the instruction')
            ent()
            continue


def eco():
    global sn, s, snl, temp
    while True:
        ent()
        print('*********************************************************************************')
        print('*\tFerry ID : ', FID, ' \t\t\t\tDate: ', Date, '\t*')
        print('*********************************************************************************')
        print('*\t\tECONOMY CLASS\t\t\t\t\t\t\t*')
        print('*********************************************************************************')
        print('*\t', s[fn][10], '\t*\t', s[fn][11], '\t*\t', s[fn][12], '\t*\t', s[fn][13], '\t*\t', s[fn][14], '\t*')
        print('*********************************************************************************')
        print('*\t', s[fn][15], '\t*\t', s[fn][16], '\t*\t', s[fn][17], '\t*\t', s[fn][18], '\t*\t', s[fn][19], '\t*')
        print('*********************************************************************************')
        print('*\t', s[fn][20], '\t*\t', s[fn][21], '\t*\t', s[fn][22], '\t*\t', s[fn][23], '\t*\t', s[fn][24], '\t*')
        print('*********************************************************************************')
        print('*\t', s[fn][25], '\t*\t', s[fn][26], '\t*\t', s[fn][27], '\t*\t', s[fn][28], '\t*\t', s[fn][29], '\t*')
        print('*********************************************************************************')
        print('*\t', s[fn][30], '\t*\t', s[fn][31], '\t*\t', s[fn][32], '\t*\t', s[fn][33], '\t*\t', s[fn][34], '\t*')
        print('*********************************************************************************')
        print('*\t', s[fn][35], '\t*\t', s[fn][36], '\t*\t', s[fn][37], '\t*\t', s[fn][38], '\t*\t', s[fn][39], '\t*')
        print('*********************************************************************************')
        print('*\t', s[fn][40], '\t*\t', s[fn][41], '\t*\t', s[fn][42], '\t*\t', s[fn][43], '\t*\t', s[fn][44], '\t*')
        print('*********************************************************************************')
        print('*\t', s[fn][45], '\t*\t', s[fn][46], '\t*\t', s[fn][47], '\t*\t', s[fn][48], '\t*\t', s[fn][49], '\t*')
        print('*********************************************************************************')
        print('The Seat Arrangement above is shown as BOOKED as "1" and AVAILABLE as "0"')
        ent()
        sn = input('The Seats are Ordered from LEFT to RIGHT then TOP to BOTTOM.\nPlease enter a seat number'
                   ' from 1 - 40 or "B" to go back: ')
        if sn in back:
            temp = 1
            break
        else:
            try:
                sn = int(sn)
            except:
                error()
                continue

        if (sn > 0) and (sn < 41):
            snl = sn + seat_indication - 1
            if s[fn][snl] == 1:
                print("I'm sorry, as you can see above the SEAT you picked is TAKEN")
                continue
            else:
                s[fn][snl] = 1
                break
        else:
            ent()
            print('Error, Please type according to the instruction')
            ent()
            continue


def FID_input():
    global FID
    while True:
        ent()
        print('Before Purchasing a ticket, please type the Ferry ID you wanted.')
        if dd in a:
            print('Here are our List of Ferry ID :\n001 - leaves at 10 a.m.\n002 - leaves at 11 a.m.\n003 - leaves '
                  'at 12 p.m.\n004 - leaves at 1 p.m.\n005 - leaves at 2 p.m.\n006 - leaves at 3 p.m.\n007 - leaves'
                  ' at 4 p.m.\n008 - leaves at 5 p.m.\n')
        elif dd in b:
            print('Here are our List of Ferry ID :\n001 - leaves at 11 a.m.\n002 - leaves at 12 p.m.\n003 - leaves '
                  'at 1 p.m.\n004 - leaves at 2 p.m.\n005 - leaves at 3 p.m.\n006 - leaves at 4 p.m.\n007 - leaves '
                  'at 5 p.m.\n008 - leaves at 10 a.m.\n')

        FID = str(input('Please enter the Ferry ID in this Format (###, E.g. [007]) : '))
        if FID in ferry:
            fid()
            if 0 in s[fn]:
                print("Thank you for choosing Ferry", FID)
                break
            else:
                print("I'm sorry, The ferry with the ID (#", FID, ") is FULL.\n Please be free to choose another "
                      "ferry in the options provided")
                continue
        else:
            error()
            continue


def welcome():
    print('           ____________________________________________________\n'
          '           _____________________¶¶¶____________________________\n'
          '           ______________________¶_____________________________\n'
          '           ______________________¶¶¶¶¶¶¶¶¶¶¶¶¶_________________\n'
          '           ______________________¶¶¶___¶__¶_¶¶¶¶_______________\n'
          '           ______________________¶¶¶___¶¶¶¶___¶¶_______________\n'
          '           ______________________¶¶¶__¶¶¶¶¶___¶¶_______________\n'
          '           ______________________¶¶¶__¶¶¶¶¶___¶________________\n'
          '           ______________________¶¶¶¶¶¶__¶¶___¶________________\n'
          '           ______________________¶_________¶¶¶¶________________\n'
          '           ______________¶¶¶¶¶¶¶¶¶¶¶¶¶_________________________\n'
          '           ______________¶¶___________¶¶_______________________\n'
          '           _______________¶____________¶_______________________\n'
          '           _______________¶_____________¶______________________\n'
          '           ________________¶____________¶______________________\n'
          '           ________________¶____________¶_¶¶___________________\n'
          '           ________________¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________________\n'
          '           ______¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶_________________\n'
          '           ______¶____________¶¶_____________¶¶____¶___________\n'
          '           ______¶¶____________¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________\n'
          '           _______¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶_________\n'
          '           _______¶¶_____¶¶___________¶______________¶¶________\n'
          '           ________¶______¶____________¶______________¶________\n'
          '           ________¶______¶¶___________¶_____________¶¶________\n'
          '           ________¶_______¶___________¶_____________¶¶________\n'
          '           _______¶¶_______¶___________¶¶____________¶_________\n'
          '           _______¶¶¶¶¶¶¶¶¶¶¶__________¶¶___________¶¶_________\n'
          '           ____________¶_¶_¶¶________¶¶¶_____¶¶¶¶¶¶¶¶_____¶¶¶__\n'
          '           ____________¶_¶_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶_______¶¶¶¶¶__¶¶_\n'
          '           _¶¶¶¶¶¶_____¶_¶______¶¶_¶_______¶_¶¶¶¶¶¶¶¶¶___¶¶¶¶¶_\n'
          '           _¶¶___¶¶¶¶¶¶¶¶¶______¶¶_¶____¶¶¶¶¶¶¶________¶¶______\n'
          '           ___¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶______¶________\n'
          '           _____¶____________________________¶¶_¶____¶_________\n'
          '           ______¶_____¶¶¶_____¶¶_____¶¶¶_____¶¶¶___¶¶_________\n'
          '           _______¶___¶¶_¶¶___¶¶_¶____¶_¶¶__________¶__________\n'
          '           _______¶¶____¶¶_____¶¶¶_____¶¶__________¶¶__________\n'
          '           ________¶¶_____________________________¶¶___________\n'
          '           _________¶¶___________________________¶¶____________\n'
          '           __________¶¶________________________¶¶¶_____________\n'
          '           ____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______________\n'
          '           ____________________________________________________')
    print('                       █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n'
          '                       █░░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░░█\n'
          '                       █░░░║║║╠─║─║─║║║║║╠─░░░█\n'
          '                       █░░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░░█\n'
          '                       █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█')
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n'
          '▌            Welcome to the Ferry Ticketing System of ACX Inc.        ▐\n'
          '▌   Where the ONLY Destination and departure is PENANG and LANGKAWI.  ▐\n'
          '▌                   We hope you enjoy our Ferry Ride.                 ▐\n'
          '▌  Please be free to contact 010-2818-246 for any further information ▐\n'
          '▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
    ent()


def ticket():
    print('Here is your TICKET :')
    print('Name\t\t:', Name)
    print('Date\t\t:', Date)
    print('Time\t\t:', time)
    print('Departure\t:', departure)
    print('Destination\t:', destination)
    print('Ferry ID\t:', FID, '\n')
    print('Class\t\t:', seat_class)
    print('Seat number\t:', sn)


def finalizing_ticket():
    global UI, Name, sn, temp, seat_class, seat_indication
    while True:
        ticket()
        ent()
        UI = input('Would you like to Finalize your ticket(s)[Y/N] :')
        if UI in y:
            save_list()
            break
        elif UI in n:
            edit_cancel_ticket()
            break
        else:
            error()
            continue


def edit_cancel_ticket():
    global UI, Name, snl, temp, seat_class, seat_indication
    while True:
        ent()
        UI = input('Would you like to Edit(E) or Cancel(C) your ticket or go Back(B)? [E/C/B] :')
        if UI in e:
            ent()
            edit_ticket()
        elif UI in c:
            var()
            s[fn][snl] = 0
            break
        elif UI in back:
            finalizing_ticket()
            break
        else:
            error()
            continue


def edit_ticket():
    global UI, Name, snl, temp, seat_class, seat_indication
    while True:
        temp = 0
        print(
            'Note❗ that You can only edit the NAME(N), SEAT NUMBER(SN) and CLASS(C) of your seat\nIf you '
            'we to change OTHER information on your Ticket, we suggest CANCELing the Ticket in the '
            'Previous Menu')
        UI = input('What would you like to EDIT or would you go BACK(B)? [N/SN/C/B] : ')
        if UI in name_list:
            temp2 = Name
            ent()
            Name = input('What would you like to change it into or would you like to go back(B) to the'
                         ' previous menu\n Please input new name or Enter "B" :')
            if Name in back:
                Name = temp2
                continue
            else:
                ent()
                finalizing_ticket()
                break
        elif UI in seat_number_list:
            temp2 = snl
            s[fn][snl] = 0
            if seat_class == 'Economic':
                eco()
            elif seat_class == 'Business':
                busi()
            if temp == 1:
                snl = temp2
                s[fn][snl] = 1
                temp = 0
                continue
            else:
                ent()
                finalizing_ticket()
                break
        elif UI in class_list:
            temp2 = seat_class
            temp3 = seat_indication
            temp4 = snl
            seat_class_change()
            if temp == 1:
                seat_class = temp2
                seat_indication = temp3
                snl = temp4
                s[fn][snl] = 1
                temp = 0
                continue
            else:
                ent()
                finalizing_ticket()
                break
        elif UI in back:
            break
        else:
            error()
            continue


def seat_class_change():
    global UI, Name, sn, temp, seat_class, seat_indication, snl
    temp2 = seat_class
    while True:
        ent()
        temp4 = snl
        s[fn][snl] = 0
        UI = input('Are you sure? [Y/N] :')
        if UI in y:
            if temp2 == 'Economic':
                seat_indication = 0
                busi()
                seat_class = 'Business'
                break
            elif temp2 == 'Business':
                seat_indication = 10
                eco()
                seat_class = 'Economic'
                break
        elif UI in n:
            temp = 1
            snl = temp4
            s[fn][snl] = 1
            break
        else:
            error()
            continue


def destination_and_departure():
    global destination, departure, ferry_indication, dd
    while True:
        print('Please pick your destination and departure for the trip.\nhere are the list of the trip :')
        print('A. From Penang to Langkawi\nB. From Langkawi to Penang')
        dd = input('Please type in A or B : ')
        if dd in a:
            destination = 'Langkawi'
            departure = 'Penang'
            ferry_indication = 0
            break

        elif dd in b:
            destination = 'Penang'
            departure = 'Langkawi'
            ferry_indication = 8
            break

        else:
            error()
            continue


def date():
    global Date, day, month, year, date_input
    while True:
        ent()
        Date = input('Please Enter the DATE for your TRIP\nIn DD-MM-YYYY Format (E.g.[17-12-2018]): ')

        try:
            day, month, year = map(int, Date.split('-'))
        except:
            error()
            continue

        try:
            date_input = datetime.datetime.strptime(Date, "%d-%m-%Y")
        except:
            ent()
            print('Please Enter in a Ʀ℮Ⱥℓ(REAL) Date, Thank you')
            continue

        date_today = datetime.datetime.now()
        date_delta = date_input - date_today

        if date_delta.days >= 7:
            print("I'm Sorry, Customers are ONLY allowed to purchase any ticket within 7 days")
            continue
        if year == int(datetime.datetime.today().year):
            if month == int(datetime.datetime.today().month):
                if day == int(datetime.datetime.today().day):
                    break
                elif day < int(datetime.datetime.today().day):
                    ent()
                    print(
                        "I'm Sorry, You have input a date from the PAST.\nSeats in the PAST are not available to see "
                        "or purchase a ticket")
                    continue
            elif month < int(datetime.datetime.today().month):
                ent()
                print("I'm Sorry, You have input a date from the PAST.\nWhich is not available to see nor purchase a"
                      " ticket")
                continue
        elif year < int(datetime.datetime.today().year):
            ent()
            print("I'm Sorry, You have input a date from the PAST.\nWhich is not available to see nor purchase a"
                  " ticket")
            continue
        break
    ferry_file()


def ferry_file():
    global s
    try:
        file = open('.\\FerryListSubFolder\\' + Date, 'rb')
        s = pickle.load(file)
        file.close()
    except:
        for i in range(0, 16, 1):
            s.append([])
        for i in range(0, 16, 1):
            for j in range(0, 50, 1):
                s[i].append(0)


def save_list():
    global s
    file = open('.\\FerryListSubFolder\\' + Date, 'wb')
    pickle.dump(s, file)
    file.close()


def time_list():
    print('Here are the list of Departure and Arriving Times for out Ferry :')
    print('- 10 a.m. to 11 a.m.\n- 11 a.m. to 12 p.m.\n- 12 p.m. to 1 p.m.\n- 1 p.m. to 2 p.m.\n- 2 p.m. to 3 p.m.\n- 3'
          ' p.m. to 4 p.m.\n- 4 p.m. to 5 p.m.\n- 5 p.m. to 6 p.m.')


# THE PROGRAM
welcome()
while True:
    var()
    print('Note❗❗❗ :\nthat your tickets will be printed when you purchased a ticket!\nYour trip back from your '
          'destination will have to be purchase separately\n\n')
    print('FERRY TICKETING SYSTEM \nP – to Purchase Ticket \nV – to View Seating Arrangement \nQ – to Quit the system')
    user_input()

    if (UI == 'P') or (UI == 'p'):
        ent()
        date()
        ent()
        destination_and_departure()
        ent()
        FID_input()
        while True:
            ent()
            temp = 0
            print('PURCHASING MODULE \nB – to purchase ticket for Business class \nE – to purchase ticket for Economy '
                  'class \nM – to return to Main Menu')
            user_input()

            if (UI == 'B') or (UI == 'b'):

                if 0 in s[fn][0:10]:
                    seat_indication = 0
                    busi()
                    ent()
                    if temp == 0:
                        Name = str(input('Please enter your NAME for your ticket : '))
                        seat_class = 'Business'
                    else:
                        temp = 0
                        break
                else:
                    print('We are Sorry, The Business Class seat in the ferry is FULL.')
                    while True:
                        UI = str(input('Would you like to purchase an Economy Class seat instead? (Y/N) : '))

                        if UI in y:
                            seat_indication = 10
                            eco()
                            ent()
                            Name = str(input('Please enter your NAME for your ticket : '))
                            seat_class = 'Economic'
                            break

                        elif UI in n:
                            break

                        else:
                            error()
                            continue
                if sn != 50:
                    finalizing_ticket()
                UI = str(input('Would you like to go BACK to the main menu...?\nEntering "No" will EXIT you out of the '
                               'Program [Y/N] :'))

                if UI in y:
                    break

                elif UI in n:
                    exit()

            elif (UI == 'E') or (UI == 'e'):

                if 0 in s[fn][11:50]:
                    seat_indication = 10
                    ent()
                    eco()
                    if temp == 0:
                        Name = str(input('Please enter your NAME for your ticket : '))
                        seat_class = 'Economic'
                    else:
                        temp = 0
                        break
                else:
                    print('We are Sorry, The Economic Class seat in the ferry is FULL.')
                    while True:
                        UI = str(input('Would you like to purchase an Business Class seat instead? (Y/N) : '))

                        if UI in y:
                            seat_indication = 0
                            ent()
                            Name = str(input('Please enter your NAME for your ticket : '))
                            busi()
                            seat_class = 'Business'
                            break

                        elif UI in n:
                            break

                        else:
                            error()
                            continue
                if sn != 50:
                    finalizing_ticket()
                ent()
                UI = str(input('Would you like to go BACK to the main menu...?\nEntering no will EXIT you out of the '
                               'Program [Y/N] :'))
                ent()
                if UI in y:
                    break

                elif UI in n:
                    print('Thank you for using the Ferry Program. I hope you enjoy your day. :)')
                    print('        ────│─────────────────────────────────────────────\n'
                          '        ────│────────▄▄───▄▄───▄▄───▄▄───▄▄───▄▄─────│────\n'
                          '        ────▌────────▒▒───▒▒───▒▒───▒▒───▒▒───▒▒─────▌────\n'
                          '        ────▌──────▄▀█▀█▀█▀█▀█▀█▀█▀█▀█▀█▀█▀█▀█▀█▀▄───▌────\n'
                          '        ────▌────▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄─▋────\n'
                          '        ─▀█████████████████████████████████████████████▄──\n'
                          '        ───▀███    █ ▀▀ █▗▖█  █ █ ▀▄██ █ █ ▄ █ █ ████▀───\n'
                          '        ──────▀█▌▐██ ██ █ █ █ █  █ █ ███ ██ ▀ █ ▀ ██▀─────\n'
                          '        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
                          '        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
                          '        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n')
                    print('Press Enter to exit')
                    input()
                    exit()

            elif (UI == 'M') or (UI == 'm'):
                break

            else:
                error()
                continue

    elif (UI == 'V') or (UI == 'v'):
        ent()
        date()
        ent()
        destination_and_departure()
        while True:
            temp = 0
            ent()
            print('SEATING ARRANGEMENT MODULE\nF - to select Ferry ID\nT - to select Trip Time\nM - to return to Main M'
                  'enu')
            user_input()

            if (UI == 'F') or (UI == 'f'):
                while True:
                    ent()
                    print('There are 8 ferries on this service.\nHere are the List Of their ID :\n-001\n-002\n-003'
                          '\n-004\n-005\n-006\n-007\n-008\nIf you wish to go back to the SEATING ARRANGEMENT MODULE, pl'
                          'ease type in "BACK" in the next line')
                    ui = str(input('Please enter the Ferry ID in this Format (###, E.g. [007]) or Tpye in "BACK" to ret'
                                   'urn to the previous menu: '))
                    ent()
                    if ui in ferry:
                        FID = ui
                        fid()
                        break

                    elif ui in back:
                        temp = 1
                        break
                    else:
                        error()
                        continue
                break

            elif (UI == 'T') or (UI == 't'):
                while True:
                    while True:
                        ent()
                        print('Our boat comes every hour starting from 10a.m. to 5 p.m.')
                        time_list()
                        try:
                            t = int(input('Please Enter the Departure time (Left One) in a 24 hour format\n(E.g.[10 is '
                                          '10 a.m] and [15 is 3 p.m.]) or Type in "0" to go back the Previous menu: '))
                            break
                        except:
                            error()
                            continue
                    ent()

                    if (t >= 10) and (t <= 17):
                        TIME()
                        break
                    elif t == 0:
                        temp = 1
                    else:
                        error()
                        continue
                break

            elif (UI == 'M') or (UI == 'm'):
                temp = 1

            else:
                error()
                continue
        ent()
        if temp == 0:
            seat()
            UI = str(input('Press M to go back to the main menu : '))
            ent()
            ent()
            ent()
            while True:
                if (UI == 'M') or (UI == 'm'):
                    break
                else:
                    error()
                    continue

        elif temp == 1:
            temp = 0
            break

    elif (UI == 'Q') or (UI == 'q'):
        ent()
        ent()
        print('Thank you for using the Ferry Program. I hope you enjoy your day. :)')
        print('        ────│─────────────────────────────────────────────\n'
              '        ────│────────▄▄───▄▄───▄▄───▄▄───▄▄───▄▄─────│────\n'
              '        ────▌────────▒▒───▒▒───▒▒───▒▒───▒▒───▒▒─────▌────\n'
              '        ────▌──────▄▀█▀█▀█▀█▀█▀█▀█▀█▀█▀█▀█▀█▀█▀█▀▄───▌────\n'
              '        ────▌────▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄─▋────\n'
              '        ─▀█████████████████████████████████████████████▄──\n'
              '        ───▀███    █ ▀▀ █▗▖█  █ █ ▀▄██ █ █ ▄ █ █ ████▀───\n'
              '        ──────▀█▌▐██ ██ █ █ █ █  █ █ ███ ██ ▀ █ ▀ ██▀─────\n'
              '        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
              '        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
              '        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n')
        print('Press Enter to exit')
        input()
        break

    else:
        error()
        ent()
        continue
exit()
