from enum import Enum
from tkinter import ttk, constants, StringVar

class Summa:
    def __init__(self, sovellus, arvo):
        self._sovellus = sovellus
        self._arvo = arvo
    def suorita(self):
        self._sovellus.plus(self._arvo())

class Erotus:
    def __init__(self, sovellus, arvo):
        self._sovellus = sovellus
        self._arvo = arvo
    def suorita(self):
        self._sovellus.miinus(self._arvo())

class Nollaus:
    def __init__(self, sovellus):
        self._sovellus = sovellus
    def suorita(self):
        self._sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus, arvo):
        self._sovellus = sovellus
        self._arvo = arvo
    def suorita(self):
        self._sovellus.aseta_arvo(self._arvo())

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        self._aikaisemmat_arvot = []
        self._syote_kentta = ttk.Entry(master=self._root)
        self._komennot = {
            Komento.SUMMA: Summa(sovellus, self._lue_syote),
            Komento.EROTUS: Erotus(sovellus, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovellus),
            Komento.KUMOA: Kumoa(sovellus, self._saa_aikaisempi_arvo)
        }


    def _lue_syote(self):
        return int(self._syote_kentta.get())

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovellus.arvo())

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        if komento != Komento.KUMOA: 
            self._aikaisemmat_arvot.append(self._sovellus.arvo())
        komento_olio = self._komennot[komento]
        komento_olio.suorita()

        if self._sovellus.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovellus.arvo())
    
    def _saa_aikaisempi_arvo(self):
        if len(self._aikaisemmat_arvot) > 0:
            return self._aikaisemmat_arvot.pop()
        return 0
