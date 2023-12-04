KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.joukko = [0] * self.kapasiteetti
        self.alkioiden_maara = 0

    def kuuluu(self, alkio):
        if alkio in self.joukko:
            return True
        return False

    def lisaa(self, alkio):
        if self.alkioiden_maara == len(self.joukko):
            self.kopioi_taulukko(
                self.joukko,
                [0] * (self.alkioiden_maara + self.kasvatuskoko)
            )

        if not self.kuuluu(alkio):
            self.joukko[self.alkioiden_maara] = alkio
            self.alkioiden_maara += 1

    def poista(self, alkio):
        if alkio in self.joukko:
            self.alkioiden_maara -= 1
            self.joukko.remove(alkio)

    def kopioi_taulukko(self, vanha_taulukko, uusi_taulukko):
        for i in range(0, len(vanha_taulukko)):
            uusi_taulukko[i] = vanha_taulukko[i]
        self.joukko = uusi_taulukko

    def mahtavuus(self):
        return self.alkioiden_maara

    def to_int_list(self):
        taulu = [0] * self.alkioiden_maara

        for i in range(0, len(taulu)):
            taulu[i] = self.joukko[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_maara == 0:
            return "{}"
        elif self.alkioiden_maara == 1:
            return "{" + str(self.joukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_maara - 1):
                tuotos = tuotos + str(self.joukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.joukko[self.alkioiden_maara - 1])
            tuotos = tuotos + "}"
            return tuotos
