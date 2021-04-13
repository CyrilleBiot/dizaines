#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
encoder-mots.py
Logiciel pour l'apprentissage de l'encodade
Niveaux Cycle 2, élèves à BEP.
__author__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__copyright__ = "Copyleft"
__credits__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__license__ = "GPL"
__version__ = "1.0"
__date__ = "2021/04/13"
__maintainer__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__email__ = "cyrille@cbiot.fr"
__status__ = "Devel"
"""
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
from random import sample

class DizainesWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Jouons avec les dizaines...")

        # Mise en mémoire des cartes cliquées
        # Comparaison de 2 cartes
        self.choix_cases = []
        # Mise en mémoire des cartes déjà jouées
        self.choix_tous_les = []
        self.score = 0
        self.tour = 0

        # Initialisation d'une zone de plage
        self.splitPlage = [1,10]

        # Style CSS
        self.dirBase = './'
        self.set_icon_from_file(self.dirBase+"apropos.png")

        # Le grid
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

        self.grid.attach(button1,0,j+1,1,1)
        self.grid.attach(button2,1,j+1,1,1)
        self.grid.attach(button3,2,j+1,1,1)
        self.grid.attach(button4,3,j+1,1,1)
        self.grid.attach(button5,4,j+1,1,1)
        self.grid.attach(button6,0,j+2,1,1)
        self.grid.attach(button7,1,j+2,1,1)
        self.grid.attach(button8,2,j+2,1,1)
        self.grid.attach(button9,3,j+2,1,1)
        self.grid.attach(button10,4,j+2,1,1)

        # Le bouton JOUER
        btnJouer = Gtk.Button(label="JOUER")
        btnJouer.connect('clicked', self.charger_jeu)
        btnJouer.set_name('btnJouer')
        self.grid.attach(btnJouer,0,j+3,2,2)

        # Les boutons de choix
        buttonChoix1 = Gtk.RadioButton.new_with_label_from_widget(None, "Simple : cartes découvertes")
        buttonChoix1.connect("toggled", self.on_button_toggled_choix, "1")

        buttonChoix2 = Gtk.RadioButton.new_from_widget(buttonChoix1)
        buttonChoix2.set_label("Difficile : cartes retournées")
        buttonChoix2.connect("toggled", self.on_button_toggled_choix, "2")

        self.grid.attach(buttonChoix1,2,j+3,2,1)
        self.grid.attach(buttonChoix2,2,j+4,2,1)

        # A propos
        btnAbout = Gtk.Button(label='A propos')
        btnAbout.connect('clicked', self.on_about)
        self.grid.attach(btnAbout,4,j+3,1,2)

        # Score
        self.labelScore = Gtk.Label(label="Score : ")
        self.labelScore.set_name('score')
        self.grid.attach(self.labelScore, 0, j + 5, 5, 1)

    def recup_valeur(self, button, value):

        print(value)
        # Enregistre tous les choix dans un tableau
        print("Liste de tous les choix", self.choix_tous_les)


        if value not in self.choix_tous_les:
            # Stockage de la variable
            # [0] le nom du premier button
            # [1] Sa valeur
            # [2] le nom du second button
            # [3] sa valeur
            self.choix_cases.append(button)
            self.choix_cases.append(value)
            print(self.choix_cases)


            # 1 clic. On desactive la case
            if len(self.choix_cases) == 2:
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="images/R" + value,
                                                                 width=100, height=100,
                                                                 preserve_aspect_ratio=True)
                img = Gtk.Image.new_from_pixbuf(pixbuf)
                button.set_image(img)

            # 2 clics. On compare les 2 choix
            if len(self.choix_cases) == 4:
                if self.choix_cases[1][1:-4] == self.choix_cases[3][1:-4]:
                    # GAGNE
                    print("gagné")
                    # On efface les cartes deja jouées
                    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="images/0.png",
                                                                     width=100, height=100,
                                                                     preserve_aspect_ratio=True)
                    img = Gtk.Image.new_from_pixbuf(pixbuf)
                    img2 = Gtk.Image.new_from_pixbuf(pixbuf)
                    # On colorie les cases déjà utilisées
                    self.choix_cases[0].set_image(img)
                    self.choix_cases[2].set_image(img2)
                    self.score += 1
                    self.tour += 1
                    print('score : ', self.score)
                    self.labelScore.set_text("Score : " +  str(self.score) + " sur " + str(self.tour))
                else:
                    # PERDU
                    print('perdu')
                    # On efface les cartes deja jouées
                    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="images/error.png",
                                                                     width=100, height=100,
                                                                     preserve_aspect_ratio=True)
                    img = Gtk.Image.new_from_pixbuf(pixbuf)
                    img2 = Gtk.Image.new_from_pixbuf(pixbuf)
                    # On colorie les cases déjà utilisées
                    self.choix_cases[0].set_image(img)
                    self.choix_cases[2].set_image(img2)
                    self.tour += 1
                    print('score : ', self.score)
                    self.labelScore.set_text("Score : " +  str(self.score) + " sur " + str(self.tour))

                # On réinitialise la zone de stockage
                self.choix_cases = []

        self.choix_tous_les.append(value)
        if self.tour == 10:
            print('fini')
            self.partie_terminee(self, "Partie terminée !", "Réessayer ou tenter un autre niveau ;)")

    def partie_terminee(self, widget, message1, message2):
        """
        FOnction ouvrant une dialog box d'alerte
        :param widget:
        :param message1: Le titre du message
        :param message2: Le contenu du message
        :return:
        """
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=message1,
        )
        dialog.format_secondary_text(message2)
        dialog.run()
        dialog.destroy()


    def on_button_toggled(self, button, name):
        if button.get_active():
            plage = button.get_label()
            self.splitPlage = plage.split('-')
            print(self.splitPlage[0],self.splitPlage[1])

    def on_button_toggled_choix(self, button, name):
        pass

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

    def gtk_style(self):
        """
        Fonction definition de CSS de l'application
        Le fichier css : pendu-peda-gtk.css
        :return:
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path(self.dirBase + 'style.css')

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
    def on_about(self, widget):
        """
        Fonction de la Boite de Dialogue About
        :param widget:
        :return:
        """
        # Recuperation n° de version
        print(__doc__)
        lignes = __doc__.split("\n")
        for l in lignes:
            if '__version__' in l:
                version = l[15:-1]
            if '__date__' in l:
                dateGtKBox = l[12:-1]

        authors = ["Cyrille BIOT"]
        documenters = ["Cyrille BIOT"]
        self.dialog = Gtk.AboutDialog()
        logo = GdkPixbuf.Pixbuf.new_from_file(self.dirBase+"apropos.png")
        if logo != None:
            self.dialog.set_logo(logo)
        else:
            print("A GdkPixbuf Error has occurred.")
        self.dialog.set_name("Gtk.AboutDialog")
        self.dialog.set_version(version)
        self.dialog.set_copyright("(C) 2020 Cyrille BIOT")
        self.dialog.set_comments("dizaines.py.\n\n" \
                                 "[" + dateGtKBox + "]")
        self.dialog.set_license("GNU General Public License (GPL), version 3.\n"
                                "This program is free software: you can redistribute it and/or modify\n"
                                "it under the terms of the GNU General Public License as published by\n"
                                "the Free Software Foundation, either version 3 of the License, or\n"
                                "(at your option) any later version.\n"
                                "\n"
                                "This program is distributed in the hope that it will be useful,\n"
                                "but WITHOUT ANY WARRANTY; without even the implied warranty of\n"
                                "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n"
                                "GNU General Public License for more details.\n"
                                "You should have received a copy of the GNU General Public License\n"
                                "along with this program.  If not, see <https://www.gnu.org/licenses/>\n")
        self.dialog.set_website("https://cbiot.fr")
        self.dialog.set_website_label("cbiot.fr")
        self.dialog.set_website("https://github.com/CyrilleBiot/dizaines")
        self.dialog.set_website_label("GIT ")
        self.dialog.set_authors(authors)
        self.dialog.set_documenters(documenters)
        self.dialog.set_translator_credits("Cyrille BIOT")
        self.dialog.connect("response", self.on_about_reponse)
        self.dialog.run()

    def on_about_reponse(self, dialog, response):
        """
        Fonction fermant la boite de dialogue About
        :param widget:
        :param response:
        :return:
        """
        self.dialog.destroy()

win = DizainesWindow()
win.gtk_style()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()