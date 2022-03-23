# DnD-project
#Mapping project for Dungeons and Dragons Tabletop game.
#
#--------------------------------------------------------
#Opis projekta: pride kasneje+
#
#--------------------------------------------------------
#Začetek projekta: 12. 3. 22
#- Ustvaril osnovni repozitorij, datoteke in pomožne datoteke,
#- program, ki nariše mrežo,
#- naučil sem se importanja v druge/nvoe datoteke, uporaba metod
#
#--------------------------------------------------------
#13. 3. 22
#Ustvaril parent program in se igral z velikostjo oken in parametri
#
#--------------------------------------------------------
#19. 3. 22
#Delo v parent datoteki:
#- Pretvoril grid.py v interno kodo znotraj map_randomizer.py
#- Dobil sem testne assete, ustvaril mapo Assets, zahvala @cainos_chen na twt; https://cainos.itch.io/pixel-art-top-down-basic
#- Dodal testno okno za besedilni input, iz katerega bom pobiral informacije
#- Program je po implementirani kodi začel delovati počasi, nekje se počasi začne izvajati
#- Odpravil počasno delovanje in glitchanje
#več v torek
#
#--------------------------------------------------------
#22. 3. 22
#Nova datoteka: Seed.py
#- Pomožna koda za branje, generiranje in shranjevanje seeda
#- Seed je unikatna številka asociirana z vsako mapo; sestavljena iz 10 števk: prva in druga dve sta število kvadratkov v x smeri;
#- tretja in četrta sta število kvadratkov v y smeri (o tem več v naslednjem razdelku), peta je z vrednost, preostalih 5 pa je rezerviranih za risanje mape same.
#- Generate() in read() zgenerirate in prebereta/ pretvorita seed v koordinate za uporabo v parent datoteki
#
#Delo v parent datoteki:
#- Dodal seed
#- Napisal pravilno (bolj efektivno) računanje maksimalnega h za izrisovanje grida
#- Okno za izpisovanje seeda
#- Pravilna velikost okna grid, na katerega se bodo kasneje izrisovale slike
#- Počistil kodo (Hvala Eva)
#več jutri
#
#-------------------------------------------------------
#23. 3. 22
#Delo v parent datoteki
#- Dodal okenca za l,h,z
#- Omogočil urejanje okenc in s tem hkrati besedila
#- Ugotovil, da sta grid_width in grid_height slabo definirana, saj se pri spreminjanju h in l pokvarita (predvsem h, ampak ima l iste tezave)
#- Dodal gumb refresh, ki posodobi okno in mrežo
#- popravil okno grid, zdaj deluje pravilno
#- počistil kodo, ustvaril novo funkcijo v border.
#več čez vikend
