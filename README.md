# DnD-project
Mapping project for Dungeons and Dragons Tabletop game.
#
Opis projekta: pride kasneje+
#
Začetek projekta: **12. marec 22**
- Ustvaril osnovni repozitorij, datoteke in pomožne datoteke,
- program, ki nariše mrežo,
- naučil sem se importanja v druge/nvoe datoteke, uporaba metod
#
**13. marec 22**

Ustvaril parent program in se igral z velikostjo oken in parametri
#
**19. marec 22**

Delo v parent datoteki:
- Pretvoril grid.py v interno kodo znotraj map_randomizer.py
- Dobil sem testne assete, ustvaril mapo Assets, zahvala @cainos_chen na twt; https://cainos.itch.io/pixel-art-top-down-basic
- Dodal testno okno za besedilni input, iz katerega bom pobiral informacije
- Program je po implementirani kodi začel delovati počasi, nekje se počasi začne izvajati
- Odpravil počasno delovanje in glitchanje
več v torek
#
**22. marec 22**

Nova datoteka: Seed.py
- Pomožna koda za branje, generiranje in shranjevanje seeda
- Seed je unikatna številka asociirana z vsako mapo; sestavljena iz 10 števk: prva in druga dve sta število kvadratkov v x smeri;
- tretja in četrta sta število kvadratkov v y smeri (o tem več v naslednjem razdelku), peta je z vrednost, preostalih 5 pa je rezerviranih za risanje mape same.
- Generate() in read() zgenerirate in prebereta/ pretvorita seed v koordinate za uporabo v parent datoteki
#
Delo v parent datoteki:
- Dodal seed
- Napisal pravilno (bolj efektivno) računanje maksimalnega h za izrisovanje grida
- Okno za izpisovanje seeda
- Pravilna velikost okna grid, na katerega se bodo kasneje izrisovale slike
- Počistil kodo (Hvala Eva)
več jutri
#
**23. marec 22**

Delo v parent datoteki:
- Dodal okenca za l,h,z
- Omogočil urejanje okenc in s tem hkrati besedila
- Ugotovil, da sta grid_width in grid_height slabo definirana, saj se pri spreminjanju h in l pokvarita (predvsem h, ampak ima l iste tezave)
- Dodal gumb refresh, ki posodobi okno in mrežo
- popravil okno grid, zdaj deluje pravilno
- počistil kodo, ustvaril novo funkcijo v border.
več čez vikend
#
**26. marec 22**

Ran into some problems; namely:
Projektna naloga zahteva spletno stran / spletni vmesnik; izkaže pa se, da pygame knjižnica ne deluje z nobenim od api-jev, ki so na voljo za importiranje
kode v html.
Trenutne možnosti so tri: nadaljuj projektno as-is, le da končna koda samo izvozi "sliko" mape in jo vrže na spletno stran (lahko bi bilo problematično s časom);
koda ostane/se spremeni v podobno, a celotno risanje se izvaja direktno v hmtl (to reši večino težav, a nevem kako točno bi bilo to z uvažanjem/izvažanjem slik);
poišče se nov library in začne na novo(kar pa tudi ni idealno)
Ta koda bo ostala, saj bo iz nje nastala vsaj prototipna aplikacija za generiranje map, in izkušnja v programiranju in novo znanje pythona.
Dodatno: počisti se readme:
#
Delo v parent datoteki:
- Odpravil buge v risanju mreže
  - Redefiniral l in h v primeru, da uporabnik spremeni katero od vrednosti
  - zaenkrat velikost mreže v x smeri ostane konstantna
  - maksimalni h se ponovno preračuna
- odpravil buge pri displayanju seeda; dodal error, ki neha risati mapo v primeri da seed string ni ustrezen
- napravil osnovno displayanje slik
#
Novo v border:
- calculate_max_h() ki vzame parametre in izračuna max h, malo očisti kodo znotraj glavne datoteke
več jutri (mogoče)
#
