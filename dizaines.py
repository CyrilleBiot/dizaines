#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
from random import sample

class GridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")

        self.grid = Gtk.Grid()
        self.add(self.grid)

        # Création d'un grid de bouton 5 X 4
        self.btn = [0] * 21
        numberBtn = 1

        for j in range(0,4):
            for i in range(0,5):
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="images/0.png", width=100, height=100,
                                                                 preserve_aspect_ratio=True)
                img = Gtk.Image.new_from_pixbuf(pixbuf)
                self.btn[numberBtn]= Gtk.Button(image=img)
                #self.btn[numberBtn].connect("clicked", self.recup_valeur, '0.png')
                print(self.btn[numberBtn])
                self.grid.attach(self.btn[numberBtn],i,j,1,1)
                numberBtn += 1

        # Le bouton JOUER
        btnJouer = Gtk.Button(label="JOUER")
        btnJouer.connect('clicked', self.charger_jeu)
        self.grid.attach(btnJouer,0,j+1,5,1)

        # Les boutons de choix
        button1 = Gtk.RadioButton.new_with_label_from_widget(None, "01-10")
        button1.connect("toggled", self.on_button_toggled, "1")

        button2 = Gtk.RadioButton.new_from_widget(button1)
        button2.set_label("11-20")
        button2.connect("toggled", self.on_button_toggled, "2")

        button3 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1, "21-30")
        button3.connect("toggled", self.on_button_toggled, "3")

        button4 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1, "31-40")
        button4.connect("toggled", self.on_button_toggled, "4")

        button5 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1, "41-50")
        button5.connect("toggled", self.on_button_toggled, "5")

        button6 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1, "51-60")
        button6.connect("toggled", self.on_button_toggled, "6")

        button7 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1, "61-70")
        button7.connect("toggled", self.on_button_toggled, "7")

        button8 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1, "71-80")
        button8.connect("toggled", self.on_button_toggled, "8")

        button9 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1, "81-90")
        button9.connect("toggled", self.on_button_toggled, "9")

        button10 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1, "91-100")
        button10.connect("toggled", self.on_button_toggled, "100")

        self.grid.attach(button1,0,j+2,1,1)
        self.grid.attach(button2,1,j+2,1,1)
        self.grid.attach(button3,2,j+2,1,1)
        self.grid.attach(button4,3,j+2,1,1)
        self.grid.attach(button5,4,j+2,1,1)
        self.grid.attach(button6,0,j+3,1,1)
        self.grid.attach(button7,1,j+3,1,1)
        self.grid.attach(button8,2,j+3,1,1)
        self.grid.attach(button9,3,j+3,1,1)
        self.grid.attach(button10,4,j+3,1,1)

    def recup_valeur(self, button, value):

        print(value)

    def on_button_toggled(self, button, name):
        if button.get_active():
            plage = button.get_label()
            self.splitPlage = plage.split('-')
            print(self.splitPlage[0],self.splitPlage[1])

    def charger_jeu(self, button):
        print(int(self.splitPlage[0]), int(self.splitPlage[1])+1)
        liste = []
        for i in range(int(self.splitPlage[0]), int(self.splitPlage[1])+1,1):
            a = "C"+str(i)+".png"
            b = "L"+str(i)+".png"
            liste.append(a)
            liste.append(b)
        self.list_of_random_items = sample(liste, len(liste))
        print(liste)

        pos  = 0
        for i in range(1,21):
            print(i)
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="images/"+self.list_of_random_items[pos],
                                                             width=100, height=100,
                                                             preserve_aspect_ratio=True)
            img = Gtk.Image.new_from_pixbuf(pixbuf)
            self.btn[i].set_image(img)
            self.btn[i].connect("clicked", self.recup_valeur, self.list_of_random_items[pos] )

            pos += 1



win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()