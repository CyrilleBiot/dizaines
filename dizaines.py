#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
encoder-mots.py
Logiciel pour l'apprentissage des correspondances
Ecriture Lettrée / Chiffrée des nombres de 0 à 100
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

class Printer:
    '''
    Classe de debug
    '''
    def __init__(self, debug=True):
        self.debug = debug
    def dprint(self,message):
        if not self.debug:
            return
        print(message)

class DizainesWindow(Gtk.Window):
    '''
    Classe principales
    '''
    def __init__(self):
        Gtk.Window.__init__(self, title="Jouons avec les dizaines...")

        # Initialisation de la classe de debug
        self.p = Printer()
        self.p.dprint("Initialisation")

        # Mise en mémoire des cartes cliquées
        # Comparaison de 2 cartes
        self.choix_cases = []

        # Mise en mémoire des cartes déjà jouées
        self.choix_tous_les = []
        self.list_of_random_items = []
        self.score = 0
        self.tour = 0
        self.niveau = 1

        # Dictionnaire des signaux passés via les boutons
        # afin de pouvoir les réinitialiser en cas de nouveau jeu
        self.handles = {}

        # Initialisation d'une zone de plage
        self.splitPlage = [1,10]

        # Style CSS
        self.dirBase = './'
        self.set_icon_from_file(self.dirBase+"apropos.png")

        # Le grid
        self.grid = Gtk.Grid()
        self.add(self.grid)

        # Score
        self.labelScore = Gtk.Label(label="Score : ")
        self.labelScore.set_name('score')
        self.grid.attach(self.labelScore, 0, 0, 5, 1)

        # Création d'un grid de bouton 5 X 4
        self.btn = [0] * 20
        numberBtn = 0

        for j in range(1,5):
            for i in range(0,5):
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="images/0.png", width=100, height=100,
                                                                 preserve_aspect_ratio=True)
                img = Gtk.Image.new_from_pixbuf(pixbuf)
                self.btn[numberBtn]= Gtk.Button(image=img)
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
        button10.connect("toggled", self.on_button_toggled, "10")

        button11 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1, "61-80")
        button11.connect("toggled", self.on_button_toggled, "11")

        button12 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1, "81-100")
        button12.connect("toggled", self.on_button_toggled, "12")


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
        self.grid.attach(button11,0,j+3,1,1)
        self.grid.attach(button12,1,j+3,1,1)


        # Le bouton JOUER
        btnJouer = Gtk.Button(label="JOUER")
        btnJouer.connect('clicked', self.charger_jeu)
        btnJouer.set_name('btnJouer')
        self.grid.attach(btnJouer,0,j+5,5,1)

        # Les boutons de choix
        buttonChoix1 = Gtk.RadioButton.new_with_label_from_widget(None, "Simple : cartes découvertes")
        buttonChoix1.connect("toggled", self.on_button_toggled_choix, 1)

        buttonChoix2 = Gtk.RadioButton.new_from_widget(buttonChoix1)
        buttonChoix2.set_label("Difficile : cartes retournées")
        buttonChoix2.connect("toggled", self.on_button_toggled_choix, 2)

        self.grid.attach(buttonChoix1,0,j+4,2,1)
        self.grid.attach(buttonChoix2,2,j+4,2,1)

        # A propos
        btnAbout = Gtk.Button(label='A propos')
        btnAbout.connect('clicked', self.on_about)
        self.grid.attach(btnAbout,4,j+4,1,1)



    def traitement_cartes(self, button, value, stage):
        '''
        :param button:
        :param value: La référence de la carte (str dans list)
        :param stage: Le niveau (integer) 1 facile, 2 difficile
        :return:
        '''

        if value not in self.choix_tous_les:
            # Stockage de la variable
            # [0] le nom du premier button
            # [1] Sa valeur
            # [2] le nom du second button
            # [3] sa valeur
            self.choix_cases.append(button)
            self.choix_cases.append(value)

            # 1 clic. On desactive la case
            if len(self.choix_cases) == 2:
                if self.niveau == 1:
                    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="images/R" + value,
                                                                     width=100, height=100,
                                                                     preserve_aspect_ratio=True)
                    img = Gtk.Image.new_from_pixbuf(pixbuf)
                    button.set_image(img)
                else:
                    pass
                    self.p.dprint("Niveau 2")

            # 2 clics. On compare les 2 choix
            if len(self.choix_cases) == 4:
                if self.niveau == 1:
                    if self.choix_cases[1][1:-4] == self.choix_cases[3][1:-4]:
                        # GAGNE
                        self.p.dprint("gagné")
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
                        self.labelScore.set_text("Score : " +  str(self.score) + " sur " + str(self.tour))
                    else:
                        # PERDU
                        self.p.dprint("perdu")
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
                        self.labelScore.set_text("Score : " +  str(self.score) + " sur " + str(self.tour))
                else:
                    pass
                    print("Niveau 2")

                # On réinitialise la zone de stockage
                self.choix_cases.clear()

        # Incrémente le tableau des cartes tirées
        self.choix_tous_les.append(value)


        # La partie est finie
        if self.tour == 10:
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

    def on_button_toggled_choix(self, button, name):
        if button.get_active():
            self.niveau = name
            print(self.niveau)

    def charger_jeu(self, button):

        self.choix_tous_les.clear()
        self.choix_cases.clear()
        self.list_of_random_items.clear()
        self.score = 0
        self.tour = 0

        # DEBUG
        self.p.dprint(self.splitPlage)

        liste = []
        if self.splitPlage not in  [['81', '100'],['61', '80']]:
            for i in range(int(self.splitPlage[0]), int(self.splitPlage[1])+1, 1):
                a = "C"+str(i)+".png"
                b = "L"+str(i)+".png"
                liste.append(a)
                liste.append(b)
            self.list_of_random_items = sample(liste, len(liste))
        else:
            self.p.dprint("plage20")
            for i in range(int(self.splitPlage[0]), int(self.splitPlage[1]) + 1, 2):
                a = "C" + str(i) + ".png"
                b = "L" + str(i) + ".png"
                liste.append(a)
                liste.append(b)
            self.list_of_random_items = sample(liste, len(liste))


        pos  = 0
        for i in range(0,20):
            if self.niveau == 1:
                # On montre les cartes // NIVEAU FACILE
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="images/"+self.list_of_random_items[pos],
                                                                 width=100, height=100,
                                                                 preserve_aspect_ratio=True)
                img = Gtk.Image.new_from_pixbuf(pixbuf)
                self.btn[i].set_image(img)

                if i in self.handles:
                    self.btn[i].disconnect(self.handles[i])
                self.handles[i] = self.btn[i].connect("clicked", self.traitement_cartes, self.list_of_random_items[pos], self.niveau)

            else:
                # On cache les cartes // NIVEAU DIFFICILE
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="images/0.png",
                                                                 width=100, height=100,
                                                                 preserve_aspect_ratio=True)
                img = Gtk.Image.new_from_pixbuf(pixbuf)
                self.btn[i].set_image(img)
                self.btn[i].connect("clicked", self.traitement_cartes, self.list_of_random_items[pos], self.niveau)
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
        d.print(__doc__)
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