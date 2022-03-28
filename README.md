# DnD-project
Mapping project for Dungeons and Dragons Tabletop game.
#
Opis projekta: pride kasneje+
#
Začetek projekta: **12. marec 22**
- Ustvaril osnovni repozitorij, datoteke in pomožne datoteke,
- program, ki nariše mrežo,
- naučil sem se importanja v druge/nove datoteke, uporaba metod
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
\n
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

**dodatno pojasnilo za h:**
Število kvadratkov v smeri y (h) je lahko večje od števila kvadratkov, ki jih program še lahko nariše v okno, pri čemer je velikost kvadratov odvisna od širine mreže, ki je zaenkrat konstantna, in l. Pri generiranju je lahko ta številka večja (do 50)
in lahko kvadratki segajo čez okno. V ta namen se po definicija h-ja ponovno izračuna h, ki mu rečemo "maksimalni dovoljeni h"; t.j. največje število kvadratkov v y smeri, ki jih program še spravi v okno v celoti (upoštevajoč spodnji border).
V ta namen se definira funkcija calculate_max_h(), ki naredi to. 
Ker lahko uporabnik spremeni h, lahko preseže to smiselno količino, in se mora ta h na novo preračunati vsakič, ko gre program skozi loop. 
**Potrebno je spremeniti še, kdaj se h in sq_side ponovno računata. Trenutno se v vsaki iteraciji programa (30x na sekundo), morala pa bi se le, ko uporabnik pritisne refresh.**
#
**23. marec 22**

Delo v parent datoteki:
- Dodal okenca za l,h,z
- Omogočil urejanje okenc in s tem hkrati besedila
- Ugotovil, da sta grid_width in grid_height slabo definirana, saj se pri spreminjanju h in l pokvarita (predvsem h, ampak ima l iste tezave)
- Dodal gumb refresh, ki posodobi okno in mrežo
- popravil okno grid, zdaj deluje pravilno
- počistil kodo, ustvaril novo funkcijo v border.
#več čez vikend
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
#več jutri
#
**27. marec 22**
Delo v parent datoteki:
- testna koda za izrisovanje platform in mostov;
- trenutno ne dela, izriše le platformi (ki bosta kasneje premični) in most med njima
- testna koda za branje navodil ni delovala, trenutno ni v uporabi
#
Delo v seed.py:
- ustvaril funkciji steps() in basic_steps() ki vzameta parameter map in lokacijo začetne in končne platforme v (l,h) kordinatah
- basic_steps() dela zelo preposto, napiše linearna navodila za most in platforme vmes;
- je motivacija/ideja za celo funkcijo steps(), ki iz argumentov napravi list navodil, ki izgledajo kot [slika, (lokacija), rotacija]
- parent datoteka naj bi ta list prebrala in ga izrisala s for loopom
#več čez teden
#
