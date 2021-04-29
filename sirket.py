class Sirket():
    def __init__(self, ad):
        self.ad = ad
        self.biznes = True

    def proqram(self):
        secim = self.menuSecim()
        if secim == 1:
            self.isciElaveEt()
        if secim == 2:
            self.isciCixart()
        if secim == 3:
            self.verilecekMaawiGoster()
        if secim == 4:
            self.maaslariVer()
        if secim == 5:
            self.rasxodYaz()
        if secim == 6:
            self.gelirYaz()

    def menuSecim(self):
        secim = int(input(
            "*** {} wirketine xow geldiniz***\n\n1-Isci Elave Et\n2-Isci Cixart\n3-Verilecek Maawlari Goster\n4-Maawlari ver\n5-Rasxod Yaz\n6-Geliri Yaz\n-Seciminizi Yazin:".format(
                self.ad)))
        while secim < 1 or  secim > 6:
            secim = int(input("Zehmet olmasa, 1 ile 6 arasinda olan secimlerden birini secin:"))
        return secim

    def isciElaveEt(self):
        id = 1
        ad = input("Iwcinin adini yazin:")
        soyad = input("Iwcinin soyadini yazin:")
        yaw = input("Iwcinin yawini yazin:")
        cinsiyyet = input("Iwcinin cinsiyyetini yazin:")
        maaw = input("Iwcinin maawini yazin:")

        with open ("isciler.txt", "r") as dosya:
            iscisiyahisi = dosya.readlines()

            if len(iscisiyahisi) == 0:
                id = 1
            else:
                with open("isciler.txt", "r") as dosya:
                    id = int(dosya.readlines()[-1].split(")")[0]) + 1

        with open("isciler.txt", "a+") as dosya:
            dosya.write("{}){} {} {} {} {}\n".format(id, ad, soyad, yaw, cinsiyyet, maaw))

        print(iscisiyahisi)

    def isciCixart(self):
        with open("isciler.txt", "r") as dosya:
            isciler = dosya.readlines()

        for isci in isciler:
            print(isci)

        secim = int(input("Zehmet olmasa, cixartmaq istediyiniz iscinin sira nomresini secin(1-{}:".format(len(isciler))))

        while secim < 1 or secim > len(isciler):
            secim = int(input("Zehmet olmasa, cixartmaq istediyiniz iscinin sira nomresini secin(1-{}:".format(len(isciler))))

        isciler.pop(secim - 1)

        saygac = 1

        dIsciler = []

        for isci in isciler:
            dIsciler.append(str(saygac)+")"+isci.split(")")[1])
            saygac +=1

        with open("isciler.txt", "w") as dosya:
            dosya.writelines(dIsciler)

    def verilecekMaawiGoster(self, hesab="a"):
        """ hesab: a ayliq, i ise illik hesab"""
        with open("isciler.txt", "r") as dosya:
            isciler = dosya.readlines()

        maaslar = []

        for isci in isciler:
            maaslar.append(int(isci.split("-")[-1]))

        print("Bu ay umumi verilecek olan maas: {}".format(sum(maaslar)))

    def maaslariVer(self):
        with open("isciler.txt", "r") as dosya:
            isciler = dosya.readlines()


        maaslar = []

        for isci in isciler:
            maaslar.append(int(isci.split("-")[-1]))


        toplamMaas = sum(maaslar)

        ### budceden maasi alma ###

        with open("budce.txt", "r") as dosya:

            tbudce = int(dosya.readlines()[0])

        tbudce = tbudce - toplamMaas

        with open("budce.txt", "w") as dosya:
            dosya.write(str(tbudce))

    def rasxodYaz(self):


    def gelirYaz(self):
        pass


sirket = Sirket ("Nail SocialMedia Group")


while sirket.biznes:
    sirket.proqram()

