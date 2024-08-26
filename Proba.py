import random
from math import trunc
from random import Random


def prikazTrenutnogStanja(sektor,energijaStita,brojRaketa):
    print (f"------ sektor {sektor}/5-------\n")
    print(f"Energija stita je: {energijaStita}\n")
    print(f"Broj raketa: {brojRaketa} ")


def napraviSlucajBroj(min, max):
    return random.randint(min,max)


def raketniNapad(brRakte):
    if brRakte>0:
        print("Raketa je lansirana")
        brRakte-=1
        if napraviSlucajBroj(1,100)<=90:
            steta=napraviSlucajBroj(30,40)
            print ("Pogodak")
            print(f"Nanesena steta neprijateljskom brodu je {steta}")
            return steta, brRakte

        else:
            print("Raketa je promasila neprijateljski brod")
            return 0, brRakte
    else:
        print("Nemate raketa ")
        return 0,brRakte


def uspesanBeg():
    if napraviSlucajBroj(1,100)<=50:
        return True
    else:
        return False


def napadNeprijatelja():
    steta =napraviSlucajBroj(10,15)
    print(f"Pogodak steta je:  {steta} ")

    return steta



def borbaSaNeprijateljem(energijaStita,brRaktea):
    HPNeprijatelja=50
    while(HPNeprijatelja>0 and energijaStita>0):

        print(f"HP Neprijatelja {HPNeprijatelja}")
        print("izaberi jedan od tri nacina odbrane")
        print("1) Laserski napad")
        print("2) napad rakteom ako imate na raspolaganju rakte")
        print("3) pokusaj bekstva")
        odabir = input("Unesite broj isped zelenog nacina odbrane")

        if odabir =="1":
            if napraviSlucajBroj(1,100)<=80:
                print("Napad je uspeo pogodak")
                steta =napraviSlucajBroj(10,20)
                HPNeprijatelja-=steta
            else:
                print("Napad nije uspeo promasili ste neprijatelja")
        elif odabir == "2":
            steta, brRaktea=raketniNapad(brRaktea)
            HPNeprijatelja-=steta
        elif odabir == "3":
            if(uspesanBeg()):
                print("Uspesno ste pobegli")

                return energijaStita,brRaktea,False
        else:
            print("propusten potez")
            print("Neprijatelj uzvraca udarac")

        if(HPNeprijatelja<=0):
            print("Neprijateljski brod je unisten")
            return energijaStita,brRaktea,True

        else:
            if(napraviSlucajBroj(1,100)<=70):
                energijaStita -= napadNeprijatelja()
                print(f"Preostala energija stita je: {energijaStita}")
            else:
                print("Neprijatelj vas je promasio")
    return energijaStita,brRaktea,HPNeprijatelja<=0












def svemirskiOkrsaj():
    energija_stita=100
    broj_raketa =3
    br_unistenih_neprijatelja=0

    for sektor in range(1,6):
        prikazTrenutnogStanja(sektor, energija_stita, broj_raketa)
        sansa=napraviSlucajBroj(1,100)

        if sansa<=80:
            print("\nNeprijateljski brod se pojavio")
            energija_stita, broj_raketa,pobeda = borbaSaNeprijateljem(energija_stita, broj_raketa)
            if pobeda:
                br_unistenih_neprijatelja+=1


        else:
             print("Prosli ste uspesno kroz ovaj sektor")
        if(energija_stita<=0):
            print("Vas stit je unisten igra je zavrsena")
            break

    if energija_stita>0:
        print("Cestitmo pobedili ste ")
        print(f"Broj unistenih neprijateljskih brodova je {br_unistenih_neprijatelja}")









if __name__=="__main__":
     svemirskiOkrsaj()
