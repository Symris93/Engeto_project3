# Engeto_project3

## Popis

Tento projekt slouží ke scrappování dat z Českých parlamentních voleb z roku 2017. Specificky z [této stránky](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

## Instalace knihoven

Všechny potřebné knihovny jsou v souboru `requirements.txt`.

Pro instalaci doporučuji používát virtuální prostředí.

```
pip install -r requirements.txt
```

## Spuštění projektu

Projekt zpustíte navigací do složky ve VSC a vložení následujcího kódu do terminálu:

```
python Election_Scrapper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "votes_summary_Benesov.csv"
```
kde první parametr je **URL vybrané obce** a druhý je **název CSV** kam se výsledky uloží.

## Ukázka

### Výsledky hlasování pro okres Benešov

  1. argument: `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101`
  2. argument: `votes_summary_Benesov.csv`

### Spuštění programu
```
python Election_Scrapper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "votes_summary_Benesov.csv"
```

### Průběh stahovaní
```
Stahuji data z URL "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"
Vytvářím CSV "votes_summary_Benesov.csv"
Ukončuji election scrapper
```

### Částečný výstup
```
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
529303,Benešov,13 104,8 485,8 437,1 052,10,2,624,3,802,597,109,35,112,6,11,948,3,6,414,2 577,3,21,314,5,58,17,16,682,10
532568,Bernartice,191,148,148,4,0,0,17,0,6,7,1,4,0,0,0,7,0,0,3,39,0,0,37,0,3,0,0,20,0
530743,Bílkovice,170,121,118,7,0,0,15,0,8,18,0,2,0,0,0,3,0,0,2,47,1,0,6,0,0,0,0,9,0
532380,Blažejovice,96,80,77,6,0,0,5,0,3,11,0,0,3,0,0,5,1,0,0,29,0,0,6,0,0,0,0,8,0
532096,Borovnice,73,54,53,2,0,0,2,0,4,4,1,0,1,0,0,3,0,0,1,29,0,0,5,0,0,0,0,1,0
```





