KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.joukko = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, alkio):
        return alkio in self.joukko

    def lisaa(self, alkio):
        if not self.kuuluu(alkio):
            self.joukko[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm += 1
            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == self.kapasiteetti:
                uusi_joukko = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(self.joukko, uusi_joukko)
                self.joukko = uusi_joukko
                self.kapasiteetti += self.kasvatuskoko
            return True
        return False

    def poista(self, alkio):
        if self.kuuluu(alkio):
            for i, kohde_luku in enumerate(self.joukko):
                if kohde_luku == alkio:
                    self.joukko[i] = 0
                    if i+1 != self.kapasiteetti:
                        for j, luku in enumerate(self.joukko[i+1:]):
                            if luku == 0:
                                break
                            self.joukko[j-1] = luku
                    break
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_lista(self, lista_a, lista_b):
        for i in range(len(lista_a)):
            lista_b[i] = lista_a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.joukko[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        joukkojen_yhdiste = IntJoukko()
        joukko_ab = joukko_a.to_int_list() + joukko_b.to_int_list()
        for alkio in joukko_ab:
            joukkojen_yhdiste.lisaa(alkio)
        return joukkojen_yhdiste

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        joukkojen_leikkaus = IntJoukko()
        joukko_a, joukko_b = joukko_a.to_int_list(), joukko_b.to_int_list()
        for alkio in joukko_a:
            if alkio in joukko_b:
                joukkojen_leikkaus.lisaa(alkio)
        return joukkojen_leikkaus

    @staticmethod
    def erotus(joukko_a, joukko_b):
        joukkojen_erotus = IntJoukko()
        joukko_a, joukko_b = joukko_a.to_int_list(), joukko_b.to_int_list()
        for alkio in joukko_a:
            if alkio not in joukko_b:
                joukkojen_erotus.lisaa(alkio)
        return joukkojen_erotus

    def __str__(self):
        return "{" + ", ".join(str(alkio) for alkio in self.joukko[:self.alkioiden_lkm]) + "}"
