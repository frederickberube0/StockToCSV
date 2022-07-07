from tkinter import *
import csv
import requests
# FLUSH NUMBER

def buttonClick():
    # GET INFO FROM ENTRY
    x1 = EnterBox1.get()
    x2 = EnterBox2.get()
    x3 = EnterBox3.get()
    x4 = EnterBox4.get()
    x5 = EnterBox5.get()
    x6 = EnterBox6.get()
    x7 = EnterBox7.get()
    x8 = EnterBox8.get()
    x9 = EnterBox9.get()
    x10 = EnterBox10.get()
    x11 = EnterBox11.get()
    x12 = EnterBox12.get()
    x13 = EnterBox13.get()
    x14 = EnterBox14.get()
    x15 = EnterBox15.get()

    # COMPANY PROFILES
    # r1c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x1 + '&token=boi7alnrh5rab1ps36p0')
    # r2c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x2 + '&token=boi7alnrh5rab1ps36p0')
    # r3c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x3 + '&token=boi7alnrh5rab1ps36p0')
    # r4c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x4 + '&token=boi7alnrh5rab1ps36p0')
    # r5c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x5 + '&token=boi7alnrh5rab1ps36p0')
    # r6c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x6 + '&token=boi7alnrh5rab1ps36p0')
    # r7c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x7 + '&token=boi7alnrh5rab1ps36p0')
    # r8c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x8 + '&token=boi7alnrh5rab1ps36p0')
    # r9c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x9 + '&token=boi7alnrh5rab1ps36p0')
    # r10c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x10 + '&token=boi7alnrh5rab1ps36p0')
    # r11c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x11 + '&token=boi7alnrh5rab1ps36p0')
    # r12c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x12 + '&token=boi7alnrh5rab1ps36p0')
    # r13c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x13 + '&token=boi7alnrh5rab1ps36p0')
    # r14c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x14 + '&token=boi7alnrh5rab1ps36p0')
    # r15c = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=' + x15 + '&token=boi7alnrh5rab1ps36p0')

    # GET STOCK PRICE
    r1 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x1 + '&token=boi7alnrh5rab1ps36p0')
    r2 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x2 + '&token=boi7alnrh5rab1ps36p0')
    r3 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x3 + '&token=boi7alnrh5rab1ps36p0')
    r4 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x4 + '&token=boi7alnrh5rab1ps36p0')
    r5 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x5 + '&token=boi7alnrh5rab1ps36p0')
    r6 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x6 + '&token=boi7alnrh5rab1ps36p0')
    r7 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x7 + '&token=boi7alnrh5rab1ps36p0')
    r8 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x8 + '&token=boi7alnrh5rab1ps36p0')
    r9 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x9 + '&token=boi7alnrh5rab1ps36p0')
    r10 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x10 + '&token=boi7alnrh5rab1ps36p0')
    r11 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x11 + '&token=boi7alnrh5rab1ps36p0')
    r12 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x12 + '&token=boi7alnrh5rab1ps36p0')
    r13 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x13 + '&token=boi7alnrh5rab1ps36p0')
    r14 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x14 + '&token=boi7alnrh5rab1ps36p0')
    r15 = requests.get('https://finnhub.io/api/v1/quote?symbol=' + x15 + '&token=boi7alnrh5rab1ps36p0')

    # NAME IN GUI
    # print(r1c.json)
    # r = r1c.json()
    # for i in range(0,len(str(r))):
    #    if str(r)[i:i+4] == "name":
    #        for x in range(i, len(str(r))):
    #            if str(r)[x:x+1] == ',':
    #                print('t')
    #                print(str(r)[i+8:i+(i-x)])
    #                break
    # PriceBox1.config(text=r)

    # PRICE IN GUI
    r1 = r1.json()
    for i in range(0, len(str(r1))):
        if str(r1)[i:i + 1] == "c":
            for b in range(i, len(str(r1))):
                if str(r1)[b:b + 1] == ',':
                    r1 = str(r1)[i + 4:b]
    if str(r1) == str(0):
        print('error')
        CompanyName1.config(text="ERROR")
    PriceBox1.config(text=r1)

    r2 = r2.json()
    for i in range(0, len(str(r2))):
        if str(r2)[i:i + 1] == "c":
            for b in range(i, len(str(r2))):
                if str(r2)[b:b+1] == ',':
                    r2 = str(r2)[i+4:b]
    if str(r2) == str(0):
        print('error')
        CompanyName2.config(text="ERROR")
    PriceBox2.config(text=r2)

    r = r3.json()
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName3.config(text="ERROR")
    PriceBox3.config(text=r)
    r3 = r

    r4 = r4.json()
    for i in range(0, len(str(r4))):
        if str(r4)[i:i + 1] == "c":
            for b in range(i, len(str(r4))):
                if str(r4)[b:b + 1] == ',':
                    r4 = str(r4)[i + 4:b]
    if str(r4) == str(0):
        print('error')
        CompanyName4.config(text="ERROR")
    PriceBox4.config(text=r4)

    r = r5.json()  # 5
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName5.config(text="ERROR")
    PriceBox5.config(text=r)
    r5 = r

    r = r6.json()
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName6.config(text="ERROR")
    PriceBox6.config(text=r)
    r6 =r

    r = r7.json()
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName7.config(text="ERROR")
    PriceBox7.config(text=r)
    r7 = r

    r = r8.json()
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName8.config(text="ERROR")
    PriceBox8.config(text=r)
    r8 = r

    r = r9.json()
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName9.config(text="ERROR")
    PriceBox9.config(text=r)
    r9 = r

    r = r10.json()
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName10.config(text="ERROR")
    PriceBox10.config(text=r)
    r10 =r

    r = r11.json()
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName11.config(text="ERROR")
    PriceBox11.config(text=r)
    r11 = r

    r = r12.json()  # 12
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName12.config(text="ERROR")
    PriceBox12.config(text=r)
    r12 = r

    r = r13.json()
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName13.config(text="ERROR")
    PriceBox13.config(text=r)
    r13 = r

    r = r14.json()
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName14.config(text="ERROR")
    PriceBox14.config(text=r)
    r14 = r

    r = r15.json()
    for i in range(0, len(str(r))):
        if str(r)[i:i + 1] == "c":
            for b in range(i, len(str(r))):
                if str(r)[b:b + 1] == ',':
                    r = str(r)[i + 4:b]
    if str(r) == str(0):
        print('error')
        CompanyName15.config(text="ERROR")
    PriceBox15.config(text=r)
    r15 = r

    #### WRITE CSV

    with open('mycsv.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow([x1, r1])
        thewriter.writerow([x2, r2])
        thewriter.writerow([x3, r3])
        thewriter.writerow([x4, r4])
        thewriter.writerow([x5, r5])
        thewriter.writerow([x6, r6])
        thewriter.writerow([x7, r7])
        thewriter.writerow([x8, r8])
        thewriter.writerow([x9, r9])
        thewriter.writerow([x10, r10])
        thewriter.writerow([x11, r11])
        thewriter.writerow([x12, r12])
        thewriter.writerow([x13, r13])
        thewriter.writerow([x14, r14])
        thewriter.writerow([x15, r15])


##### GUI BELOW
root = Tk()

bigCanvas = Canvas(root)

leftCanvas = Canvas(bigCanvas)
Label1 = Label(leftCanvas, text='Enter stock name (AAPL, AMZN)')
EnterBox1 = Entry(leftCanvas)
EnterBox2 = Entry(leftCanvas)
EnterBox3 = Entry(leftCanvas)
EnterBox4 = Entry(leftCanvas)
EnterBox5 = Entry(leftCanvas)
EnterBox6 = Entry(leftCanvas)
EnterBox7 = Entry(leftCanvas)
EnterBox8 = Entry(leftCanvas)
EnterBox9 = Entry(leftCanvas)
EnterBox10 = Entry(leftCanvas)
EnterBox11 = Entry(leftCanvas)
EnterBox12 = Entry(leftCanvas)
EnterBox13 = Entry(leftCanvas)
EnterBox14 = Entry(leftCanvas)
EnterBox15 = Entry(leftCanvas)
EnterBox1.insert(0, 'VAB.TO')
EnterBox2.insert(0, 'CM.TO')
EnterBox3.insert(0, 'BCE.TO')
EnterBox4.insert(0, 'HHL.TO')
EnterBox5.insert(0, 'ZWE.TO')
EnterBox6.insert(0, 'ZWU.TO')
EnterBox7.insert(0, 'ZCS.TO')
EnterBox8.insert(0, 'ZDH.TO')
EnterBox9.insert(0, 'ZPR.TO')
EnterBox10.insert(0, 'ZWH.TO')
EnterBox11.insert(0, 'ZWC.TO')
EnterBox12.insert(0, 'ZRE.TO')
EnterBox13.insert(0, 'MDY')
EnterBox14.insert(0, 'IYZ')
EnterBox15.insert(0, 'TLT')
btn = Button(leftCanvas, text="Click to see price", command=buttonClick)

PriceBox = Label(leftCanvas, text="Stock Price:")
PriceBox1 = Label(leftCanvas, text="0$")
PriceBox2 = Label(leftCanvas, text="0$")
PriceBox3 = Label(leftCanvas, text="0$")
PriceBox4 = Label(leftCanvas, text="0$")
PriceBox5 = Label(leftCanvas, text="0$")
PriceBox6 = Label(leftCanvas, text="0$")
PriceBox7 = Label(leftCanvas, text="0$")
PriceBox8 = Label(leftCanvas, text="0$")
PriceBox9 = Label(leftCanvas, text="0$")
PriceBox10 = Label(leftCanvas, text="0$")
PriceBox11 = Label(leftCanvas, text="0$")
PriceBox12 = Label(leftCanvas, text="0$")
PriceBox13 = Label(leftCanvas, text="0$")
PriceBox14 = Label(leftCanvas, text="0$")
PriceBox15 = Label(leftCanvas, text="0$")

CompanyName = Label(leftCanvas, text="Company name")
CompanyName1 = Label(leftCanvas, text=" ")
CompanyName2 = Label(leftCanvas, text=" ")
CompanyName3 = Label(leftCanvas, text=" ")
CompanyName4 = Label(leftCanvas, text=" ")
CompanyName5 = Label(leftCanvas, text=" ")
CompanyName6 = Label(leftCanvas, text=" ")
CompanyName7 = Label(leftCanvas, text=" ")
CompanyName8 = Label(leftCanvas, text=" ")
CompanyName9 = Label(leftCanvas, text=" ")
CompanyName10 = Label(leftCanvas, text=" ")
CompanyName11 = Label(leftCanvas, text=" ")
CompanyName12 = Label(leftCanvas, text=" ")
CompanyName13 = Label(leftCanvas, text=" ")
CompanyName14 = Label(leftCanvas, text=" ")
CompanyName15 = Label(leftCanvas, text=" ")

leftCanvas.grid(column=1)

bigCanvas.grid()

leftCanvas.grid(column=1)
Label1.grid(column=1)
EnterBox1.grid(column=1, pady=5)
EnterBox2.grid(column=1, pady=5)
EnterBox3.grid(column=1, pady=5)
EnterBox4.grid(column=1, pady=5)
EnterBox5.grid(column=1, pady=5)
EnterBox6.grid(column=1, pady=5)
EnterBox7.grid(column=1, pady=5)
EnterBox8.grid(column=1, pady=5)
EnterBox9.grid(column=1, pady=5)
EnterBox10.grid(column=1, pady=5)
EnterBox11.grid(column=1, pady=5)
EnterBox12.grid(column=1, pady=5)
EnterBox13.grid(column=1, pady=5)
EnterBox14.grid(column=1, pady=5)
EnterBox15.grid(column=1, pady=5)

btn.grid(column=2, row=7, padx=30)

CompanyName.grid(row=0, column=3, pady=5)
CompanyName1.grid(row=1, column=3, pady=5, padx=20)
CompanyName2.grid(row=2, column=3, pady=5)
CompanyName3.grid(row=3, column=3, pady=5)
CompanyName4.grid(row=4, column=3, pady=5)
CompanyName5.grid(row=5, column=3, pady=5)
CompanyName6.grid(row=6, column=3, pady=5)
CompanyName7.grid(row=7, column=3, pady=5)
CompanyName8.grid(row=8, column=3, pady=5)
CompanyName9.grid(row=9, column=3, pady=5)
CompanyName10.grid(row=10, column=3, pady=5)
CompanyName11.grid(row=11, column=3, pady=5)
CompanyName12.grid(row=12, column=3, pady=5)
CompanyName13.grid(row=13, column=3, pady=5)
CompanyName14.grid(row=14, column=3, pady=5)
CompanyName15.grid(row=15, column=3, pady=5)

PriceBox.grid(row=0, column=4, pady=5, padx=30)
PriceBox1.grid(row=1, column=4, pady=5)
PriceBox2.grid(row=2, column=4, pady=5)
PriceBox3.grid(row=3, column=4, pady=5)
PriceBox4.grid(row=4, column=4, pady=5)
PriceBox5.grid(row=5, column=4, pady=5)
PriceBox6.grid(row=6, column=4, pady=5)
PriceBox7.grid(row=7, column=4, pady=5)
PriceBox8.grid(row=8, column=4, pady=5)
PriceBox9.grid(row=9, column=4, pady=5)
PriceBox10.grid(row=10, column=4, pady=5)
PriceBox11.grid(row=11, column=4, pady=5)
PriceBox12.grid(row=12, column=4, pady=5)
PriceBox13.grid(row=13, column=4, pady=5)
PriceBox14.grid(row=14, column=4, pady=5)
PriceBox15.grid(row=15, column=4, pady=5)

root.mainloop()
