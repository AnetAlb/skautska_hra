from random import randint
'''
Úkolem je vytvořit známou skautskou hru „Kdo? S kým? Co dělali?“.
Hra se hráče zeptá postupně na různé otázky, například
„Kdo?“, „S kým?“, „Co dělali?“, „Kde?“, „Kdy?“, a nakonec „Proč?“,
s tím, že mu umožní na jednu otázku odpovědět vícekrát a všechny odpovědi si uloží.
Na závěr pak hra z každé sady odpovědí vybere náhodně jednu odpověď a z takto
vybraných odpovědí složí větu, kterou vypíše uživateli. Seznam otázek by mělo
být možné změnit na jednom místě bez zásahu do logiky programu.
'''
def skauti():
    otazky = ['Kdo?', 'S kým?', 'Co dělali?', 'Kde?', 'Kdy?','Proč?']
    list_odpovedi = {}
    delka_odpovedi = {}

    #vytvareni prazdnych slovniku
    for jednotlive_otazky in otazky:
        list_odpovedi[jednotlive_otazky] = []
        delka_odpovedi[jednotlive_otazky] = []


    for pocet_otazek in range(8):
        cislo_klice=randint(0,5)
        print(otazky[cislo_klice])
        konkretni_otazka = otazky[cislo_klice]
        konkretni_odpoved = input('Odpovez: ')
        # vytvori slovnik se vsemi odpovedmi na otazku
        list_odpovedi[konkretni_otazka].append(konkretni_odpoved)


    pribeh=[]
    #vybere random odpoved na otazku
    for question in otazky:
        delka_odpovedi[question] = len(list_odpovedi[question])
        if len(list_odpovedi[question]) <= 1:
            cislo_odpovedi = 0
        else:
            cislo_odpovedi = randint(0,len(list_odpovedi[question])-1)

        try:
            pribeh.append(list_odpovedi[question][cislo_odpovedi])
        except IndexError:
            pass

    print (' '.join(pribeh))


skauti()
