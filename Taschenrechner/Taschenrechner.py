
import tkinter as tk
import math
from tkinter import font as tkFont

class Taschenrechner(object):
    def __init__(self, root):

        self.anzeige = tk.Entry(root, relief='flat',font = ('calibri', 18), textvariable=1, justify="right", bd=15, bg='black', fg = 'white')
        self.anzeige.pack(side='top')
#        self.unten = tk.Entry(root, relief='flat',font = ('calibri', 18), textvariable=1, justify="right", bd=15, bg='lightblue')
#        self.unten.pack(side='top')
        self.zahl1 = 0.00
        self.operator = ''
        self.operatorgesetzt = 'false'
        self.memorywert = 0.00
        self.kursor = 0
        #---------------------Memmorytasten----------------------------------------
        self.memtasten = tk.LabelFrame(root, padx=11, pady=3, labelanchor = "se", bg = "lightblue")
        self.memtasten.pack()

        self.mctaste = tk.Button(self.memtasten, text = "MC", height = 3, width = 5, bg = "beige", command = lambda: self.memoryloeschen())
        self.mctaste.grid(row=0, column = 1, padx = 2, pady = 2)

        self.mrtaste = tk.Button(self.memtasten, text = "MR", height = 3, width = 5, bg = "beige", command = lambda: self.memoryladen())
        self.mrtaste.grid(row=0, column = 2, padx = 2, pady = 2)

        self.mstaste = tk.Button(self.memtasten, text = "MS", height = 3, width = 5, bg = "beige", command = lambda: self.memoryueberschreiben())
        self.mstaste.grid(row=0, column = 3, padx = 2, pady = 2)

        self.mplustaste = tk.Button(self.memtasten, text = "M+", height = 3, width = 5, bg = "beige", command = lambda: self.memoryink())
        self.mplustaste.grid(row=0, column = 4, padx = 2, pady = 2)

        self.mminustaste = tk.Button(self.memtasten, text = "M-", height = 3, width = 5, bg = "beige", command = lambda: self.memorydek())
        self.mminustaste.grid(row=0, column = 5, padx = 2, pady = 2)
        #-----------------------Funktionstasten--------------------------------------
        self.funktionstasten = tk.LabelFrame(root, padx=11, pady=3, bg = "lightblue")
        self.funktionstasten.pack()

        self.loeschentaste = tk.Button(self.funktionstasten, text = "â†", height = 3, width = 5, bg = "beige", command = lambda: self.loeschen())
        self.loeschentaste.grid(row=0, column = 1, padx = 2, pady = 2)

        self.cetaste = tk.Button(self.funktionstasten, text = "CE", height = 3, width = 5, bg = "beige", command = lambda: self.zahlloeschen())
        self.cetaste.grid(row=0, column = 2, padx = 2, pady = 2)

        self.ctaste = tk.Button(self.funktionstasten, text = "C", height = 3, width = 5, bg = "beige", command = lambda: self.allesloeschen())
        self.ctaste.grid(row=0, column = 3, padx = 2, pady = 2)

        self.plusminustaste = tk.Button(self.funktionstasten, text = "Â±", height = 3, width = 5, bg = "beige", command = lambda: self.vorzeichen())
        self.plusminustaste.grid(row=0, column = 4, padx = 2, pady = 2)

        self.wurzeltaste = tk.Button(self.funktionstasten, text = "âˆš", height = 3, width = 5, bg = "beige", command = lambda: self.wurzelrechnen())
        self.wurzeltaste.grid(row=0, column = 5, padx = 2, pady = 2)

        #------------------------Zifferntasten-------------------------------------
        self.ziffern = tk.LabelFrame(root, padx=5, pady=3, bg = "lightblue", labelanchor="e")
        self.ziffernfont=tkFont.Font(family = 'Arial', size= 9, weight= tkFont.BOLD)
        self.ziffern.pack(side=tk.LEFT)
        self.ziffer1 = tk.Button(self.ziffern, font = self.ziffernfont,text = "1", height = 3, width = 5, bg = "beige", command = lambda: self.ink(1))
        self.ziffer1.grid(row=2, column= 0, padx = 1, pady = 1)
        self.ziffer2 = tk.Button(self.ziffern, font = self.ziffernfont, text = "2", height = 3, width = 5, bg = "beige", command = lambda: self.ink(2))
        self.ziffer2.grid(row=2, column= 1, padx = 2, pady = 2)
        self.ziffer3 = tk.Button(self.ziffern, font = self.ziffernfont, text = "3", height = 3, width = 5, bg = "beige", command = lambda: self.ink(3))
        self.ziffer3.grid(row=2, column= 2, padx = 2, pady = 2)
        self.ziffer4 = tk.Button(self.ziffern, font = self.ziffernfont, text = "4", height = 3, width = 5, bg = "beige", command = lambda: self.ink(4))
        self.ziffer4.grid(row=1, column= 0, padx = 2, pady = 2)
        self.ziffer5 = tk.Button(self.ziffern, font = self.ziffernfont, text = "5", height = 3, width = 5, bg = "beige", command = lambda: self.ink(5))
        self.ziffer5.grid(row=1, column= 1, padx = 2, pady = 2)
        self.ziffer6 = tk.Button(self.ziffern, font = self.ziffernfont, text = "6", height = 3, width = 5, bg = "beige", command = lambda: self.ink(6))
        self.ziffer6.grid(row=1, column= 2, padx = 2, pady = 2)
        self.ziffer7 = tk.Button(self.ziffern, font = self.ziffernfont, text = "7", height = 3, width = 5, bg = "beige", command = lambda: self.ink(7))
        self.ziffer7.grid(row=0, column= 0, padx = 2, pady = 2)
        self.ziffer8 = tk.Button(self.ziffern, font = self.ziffernfont, text = "8", height = 3, width = 5, bg = "beige", command = lambda: self.ink(8))
        self.ziffer8.grid(row=0, column= 1, padx = 2, pady = 2)
        self.ziffer9 = tk.Button(self.ziffern, font = self.ziffernfont, text = "9", height = 3, width = 5, bg = "beige", command = lambda: self.ink(9))
        self.ziffer9.grid(row=0, column= 2, padx = 2, pady = 2)
        self.ziffer0 = tk.Button(self.ziffern, font = self.ziffernfont, text = "0", height = 3, width = 12, bg = "beige", command = lambda: self.ink(0))
        self.ziffer0.grid(row=3, column= 0, columnspan = 2, padx = 2, pady = 2)
        self.kommataste = tk.Button(self.ziffern, font = self.ziffernfont, text = ".", height = 3, width = 5, bg = "beige", command = lambda: self.kommasetzen())
        self.kommataste.grid(row=3, column= 2, padx = 2, pady = 2)
        #--------------------------Operatorentasten-----------------------------------
        self.operatoren = tk.LabelFrame(root, padx=4, pady=3, bg = "lightblue", labelanchor = "w")
        self.operatoren.pack(side=tk.RIGHT)

        self.teiletaste = tk.Button(self.operatoren, font = self.ziffernfont, text = "/", height = 3, width = 5, bg = "beige", command = lambda: self.operatorsetzen('/'))
        self.teiletaste.grid(row=0, column = 3, padx = 2, pady = 2)

        self.multiplizieretaste = tk.Button(self.operatoren, font = self.ziffernfont, text = "*", height = 3, bg = "beige", width = 5, command = lambda: self.operatorsetzen('*'))
        self.multiplizieretaste.grid(row=1, column = 3, padx = 2, pady = 2)

        self.minustaste = tk.Button(self.operatoren, font = self.ziffernfont, text = "-", height = 3, width = 5, bg = "beige", command = lambda: self.operatorsetzen('-'))
        self.minustaste.grid(row=2, column = 3, padx = 2, pady = 2)

        self.plustaste = tk.Button(self.operatoren, font = self.ziffernfont, text = "+", height = 3, width = 5, bg = "beige", command = lambda: self.operatorsetzen('+'))
        self.plustaste.grid(row=3, column = 3, padx = 2, pady = 2)

        self.prozenttaste = tk.Button(self.operatoren, font = self.ziffernfont, text = "%", height = 3, width = 5, bg = "beige", command = lambda: self.operatorsetzen('%'))
        self.prozenttaste.grid(row=0, column = 4, padx = 2, pady = 2)

        self.inverstaste = tk.Button(self.operatoren, font = self.ziffernfont, text = "1/x", height = 3, width = 5, bg = "beige", command = lambda: self.inversrechnen())
        self.inverstaste.grid(row=1, column = 4, padx = 2, pady = 2)

        self.istgleichtaste = tk.Button(self.operatoren, font = self.ziffernfont, text = "=", height = 7, width = 5, bg = "beige", command = lambda: self.rechnen())
        self.istgleichtaste.grid(row=2, column = 4,rowspan = 2, padx = 2, pady = 2)

    #------------------------Anzeige + Eingabe-------------------------------------
    def ink(self, i):
        self.anzeige.insert(self.kursor, str(i))
        self.kursor += 1

    def loeschen(self):
        self.kursor -= 1
        self.anzeige.delete(self.kursor)

    def allesloeschen(self):
        self.anzeigeaktualisieren('')
        self.zahl1 = 0.00
        self.operator = ''
        self.operatorgesetzt = 'false'


    def zahlloeschen(self):
        self.anzeigeaktualisieren('')

    def vorzeichen(self):
        if self.anzeige.get()[0] == '-':
            self.anzeige.delete(0)
            self.kursor -= 1
        else:
            self.anzeige.insert(0,'-')
            self.kursor += 1

    def kommasetzen(self):
        self.anzeige.insert(self.kursor,'.')
        self.kursor += 1

    def anzeigeaktualisieren(self, tempstring):
        self.anzeige.delete(0,'end')
        self.anzeige.insert(0,tempstring)
        self.kursor = len(tempstring)

#------------------------Memory Ã¤ndern/laden-------------------------------------
    def memoryloeschen(self):
        self.memorywert = 0.00
        print('memory = ',"{:.2f}".format(self.memorywert) )
        self.mctaste.config(relief="raised")

    def memoryladen(self):
        memstring = str(self.memorywert)
        self.anzeige.delete(0,'end')
        self.anzeige.insert(0,memstring)
        self.kursor = len(memstring)
        print('memory = ',"{:.2f}".format(self.memorywert) )

    def memoryueberschreiben(self):
        if self.anzeige.get() != '':
            self.memorywert = float(self.anzeige.get())
            self.mctaste.config(relief="ridge")
        print('memory = ',"{:.2f}".format(self.memorywert) )

    def memoryink(self):
        if self.anzeige.get() != '':
            self.memorywert += float(self.anzeige.get())
            self.mctaste.config(relief="ridge")
        print('memory = ',"{:.2f}".format(self.memorywert) )

    def memorydek(self):
        self.memorywert -= float(self.anzeige.get())
        print('memory = ',"{:.2f}".format(self.memorywert) )

#------------------------Rechenoperationen-------------------------------------
    def inversrechnen(self):
        temp = float(self.anzeige.get())
        temp = 1/temp
        if temp == int(temp):
            tempstring = str(int(temp))
        else:
            tempstring = str(temp)
        self.anzeigeaktualisieren(tempstring)


    def wurzelrechnen(self):
        temp = float(self.anzeige.get())
        temp = math.sqrt(temp)
        if temp == int(temp):
            tempstring = str(int(temp))
        else:
            tempstring = str(temp)
        self.anzeigeaktualisieren(tempstring)

    def operatorsetzen(self, operator):
        if self.operatorgesetzt == 'true':
            self.rechnen()
        self.operator = operator
        self.operatorgesetzt = 'true'
        self.zahl1 = float(self.anzeige.get())
        self.anzeigeaktualisieren('')

    def rechnen(self):
        ergebnis = 0.00
        if self.operatorgesetzt == 'true':
            if self.anzeige.get() != '':
                if self.operator =='+':
                    ergebnis = self.zahl1 + float(self.anzeige.get())
                elif self.operator =='-':
                    ergebnis = self.zahl1 - float(self.anzeige.get())
                elif self.operator == '*':
                    ergebnis = self.zahl1 * float(self.anzeige.get())
                elif self.operator == '/':
                    ergebnis = self.zahl1 / float(self.anzeige.get())
                elif self.operator == '%':
                    ergebnis = self.zahl1 * float(self.anzeige.get()) / 100
                else:
                    print ('fehler, den es nicht gibt')
                    self.allesloeschen()
                self.zahl1 = 0.00
                if int(ergebnis) == ergebnis:
                    tempstring = str(int(ergebnis))
                else:
                    tempstring = str(ergebnis)
                self.anzeigeaktualisieren(tempstring)
                self.zahl1 = 0.0
                self.operatorgesetzt = 'false'
                self.operator = ''

root = tk.Tk()
Taschenrechner(root)
root.mainloop()
