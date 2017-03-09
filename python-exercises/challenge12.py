########################################
#   Python Game based on POINTLESS BBC #
########################################
import time
import json
import random
import os.path
TEAMS={"teams":[],"scores":[]}
SAVED_GAME_JSON="saved_game.json"
BATCH_STACK=[
                ["Questions about the US", "Questions about Spain", "Questions about world statics"],
                ["Questions about Football", "Questions about Films/TV", "Questions about Chemistry"],
                ["Questions about physics", "Questions about words", "Questions about history"]
            ]
QUESTION_STACK= [
                    [
                        ["US cities beginning with A", "US cities within 2000 miles from San Diego", "Year with less pollution in NY ever."],
                        ["Metropolitan area with the least pop.", "Words ending in ino"],
                        ["Countries that have won the miss world", "AUSTRALIAN OSCAR-WINNING ACTORS"]
                    ],
                    [
                        ["GOALKEEPERS WHO HAVE PLAYER FOR ENGLAND","TOP-FLIGHT WINNING FOOTBALL MANAGER","CITIES THAT HAVE HEALD THE FIFA WORLD CUP FINAL","ENGLAND WORLD CUP GOAL SCORERS"],
                        ["HOSTS OF AN AUDIENCE WITH","US TV SHOWS AND THEIR CITIES","FILM VILLIANS AND THEIR FILMS","TV GLADIATORS","ACTORS WHO APPEARED IN BOTH BRIDGET JONES FILMS"],
                        ["GASES WITH A SINGLE-LETTER CHEMICAL SYMBOL","GEM STONES"]
                    ],
                    [
                        ["NATURALLY OCCURRING OBJECTS AND PHENOMENA IN SPACE","FIRST 20 ELEMENTS OF THE PERIODIC TABLE"],
                        ["WORDS ENDING IN ...EEK","WORDS ENDING IN OGY"],
                        ["FAMOUS STEPHENS","EUROPEAN COUNTRIES WITH A MONARCH"]
                    ],
                ]
ANSWER_STACK=[
                
                    [
                        ["Arkansas","Alamo","Abington","Albany","Arlington"],
                        ["Los Angeles","Seattle","Las Vegas","Denver","Phoenix","Hermosillo"],
                        ["2009"]
                    ],
                    [
                        ["Toledo"],
                        ["abanino", "abietino", "acerino", "adamantino", "adeliño", "adivino", "adulterino", "afino", "agatino", "agustino", "ajicomino", "ajotrino", "alabastrino", "alavecino", "alavencino", "albarino", "albellanino", "albino", "alcaladino", "alcalaino", "alcalino", "alcantarino", "alcino", "aldino", "alejandrino", "alfonsino", "algonquino", "alicantino", "aliño", "almandino", "almecino", "alpino", "alvino", "amaracino", "ambarino", "amberino", "anacardino", "anadino", "andaniño", "andantino", "andino", "andrino", "andrògino", "angevino", "añino", "anodino", "ansarino", "antequino", "antonino", "aquilino", "arandino", "architriclino", "aretino", "argelino", "argentino", "arietino", "aristino", "armiño", "asbestino", "asesino", "asinino", "asnino", "astifino", "atino", "austrino", "avilesino", "azulino", "bagarino", "baldaquino", "barbastrino", "barbilampiño", "barcino", "barquino", "becoquino", "beduino", "beguino", "benedictino", "benino", "bilbaìno", "bipontino", "bizantino", "blanquecino", "bombardino", "boquino", "botrino", "bovino", "brigantino", "brinquiño", "brocino", "buccino", "bufalino", "buitrino", "butrino", "cabalino", "cairino", "calabacino", "calepino", "camino", "campesino", "camposino", "canino", "cansino", "capitalino", "capitolino", "caprino", "capuchino", "caquino", "carilampiño", "cariño", "carolino", "carriño", "casino", "caspolino", "catarrino", "catavino", "catino", "catirrino", "caudino", "cebollino", "cedrino", "celestino", "celtolatino", "censorino", "cenzalino", "cerrotino", "cervantino", "cervino", "cesarino", "cetrino", "chino", "ciclamino", "cigoñino", "cincomesino", "cinquino", "cipolino", "cipresino", "ciprino", "circunvecino", "cisalpino", "cisandino", "citrino", "clandestino", "cochino", "cofino", "coinquilino", "colino", "collarino", "colombino", "columbino", "comino", "concertino", "concino", "condòmino", "contèrmino", "contino", "convecino", "copino", "coquino", "coralino", "corcino", "corderino", "corpiño", "correntino", "corvino", "costino", "cremesino", "crepusculino", "cretino", "cristalino", "cristino", "crocino", "cuino", "cupresino", "cupulino", "damasquino", "dañino", "demostino", "desaliño", "desatino", "descamino", "descariño", "desiño", "destino", "devino", "diamantino", "diclino", "diezmesino", "difumino", "dino", "disfumino", "divino", "docemesino", "doctrino", "dominò", "dragontino", "drino", "dulzaino", "duomesino", "efesino", "elefantino", "eleusino", "empino", "encarnadino", "encino", "endino", "endocrino", "endrino", "entrefino", "entreliño", "equino", "escobino", "escolarino", "escriño", "escudriño", "esforrocino", "esfumino", "esmeraldino", "espino", "estornino", "estudiantino", "falcino", "fariño", "felino", "femenino", "ferino", "fernandino", "ferrocino", "fescenino", "figulino", "filipino", "fino", "florentino", "focino", "fornacino", "fornecino", "forrocino", "francolino", "frontino", "fueguino", "gallino", "gamusino", "garbino", "gèmino", "genuino", "gibelino", "gigantino", "ginebrino", "girino", "girondino", "golondrino", "gongorino", "gorrino", "gosipino", "granadino", "grecolatino", "guaiño", "guiño", "gurrumino", "hacino", "hedentino", "herculino", "hermandino", "heterodino", "hialino", "hocino", "hornecino", "igualadino", "inconcino", "indino", "indochino", "infantino", "inquilino", "interandino", "interino", "intestino", "isabelino", "jabino", "jacarandino", "jacerino", "jacintino", "jacobino", "jamaiquino", "jazarino", "jorgolino", "josefino", "juncino", "jupiterino", "ladino", "lampiño", "langostino", "laricino", "latino", "laurino", "lazarino", "lechino", "lechuguino", "leonino", "leporino", "leptorrino", "levantino", "libertino", "ligurino", "ligustrino", "lino", "lorquino", "losino", "luciferino", "lupino", "lupulino", "macuquino", "maguntino", "malino", "manuelino", "maravetino", "marcelino", "marino", "marrasquino", "masculino", "masticino", "matino", "matutino", "mayorino", "mediastino", "melino", "mendocino", "menino", "merculino", "merino", "mesquino", "metalino", "mezquino", "michino", "minino", "mino", "mirandino", "mirrino", "mirtino", "misògino", "mohìno", "mojino", "molino", "mollino", "monfortino", "montenegrino", "montesino", "morabetino", "mortecino", "mosquino", "mùrrino", "nacarino", "najerino", "nardino", "nectarino", "negrestino", "neogranadino", "neolatino", "neoyorquino", "nervino", "neuquino", "neutrino", "nicerobino", "niño", "nocturnino", "nòmino", "nortino", "numantino", "ojizaino", "olivino", "onfacino", "opalino", "oreoselino", "ormino", "ovino", "padrino", "paladino", "palatino", "palentino", "palestino", "palomino", "pampino", "pamporcino", "papalino", "partiquino", "patavino", "paulatino", "pechardino", "pedernalino", "peino", "pejino", "pelegrino", "pepino", "peregrino", "pergamino", "perlino", "perusino", "pestiño", "pingu$ino", "pino", "placentino", "platino", "platirrino", "plautino", "poìno", "pollino", "ponentino", "porcino", "porrino", "precolombino", "prestiño", "prìstino", "pueblerino", "purpurino", "quimerino", "quino", "rabino", "raposino", "rascalino", "ratino", "reatino", "rebociño", "rechino", "redolino", "refino", "reino", "remolino", "repentino", "resobrino", "revesino", "ricino", "rionegrino", "rocino", "rosarino", "rosmarino", "sabatino", "sabino", "sacarino", "sacramentino", "sagallino", "saguntino", "saìno", "salamandrino", "salamanquino", "salentino", "salino", "salmantino", "salvajino", "sandalino", "sanguino", "sanjuanino", "santafecino", "santafesino", "santanderino", "santiaguino", "sapino", "saturnino", "segorbino", "seguntino", "selvajino", "sementino", "semitrino", "serapino", "seròtino", "serpentino", "serragatino", "serrino", "sibilino", "sietemesino", "sino", "sobrino", "solferino", "sordino", "submarino", "subreino", "succino", "sucotrino", "superfino", "superheterodino", "supino", "tagarino", "taino", "tamborino", "tangerino", "tanino", "tapacamino", "tarentino", "taurino", "teatino", "tensino", "tèrmino", "terrino", "tiberino", "tiburtino", "tino", "tobosino", "tocino", "tojino", "tondino", "topino", "torbellino", "tortosino", "tragavino", "trajino", "transalpino", "transandino", "transmarino", "transtiberino", "trasalpino", "trasandino", "trasmarino", "trastiberino", "trecemesino", "tremesino", "tresmesino", "tridentino", "triestino", "trino", "tripolino", "tunecino", "turbino", "turquino", "ulaguiño", "ultramarino", "uterino", "valentino", "vecino", "vellocino", "venino", "venusino", "verdino", "vespertino", "vicentino", "vino", "viperino", "virreino", "visontino", "visorreino", "vizcaìno", "vulpino", "zafirino", "zaino", "zangolotino", "zucarino"],
                    ],
                    [
                        ["US","USA","United States", "United States of America", "Argentina", "Nigeria", "Veneswala", "Brazil", "Austria", "Greece", "Poland", "Turkey", "United Kingdom"],
                        ["Nicole Kidman", "Peter Finch", "Heath Ledger", "Cate Blanchett", "Gefforey Rush", "Russell Crowe"]
                    ],

                    [
                        ["Peter Bennete", "Paul Robinson", "Ray Clements", "Robert Green", "David James", "Richard Wright", "Jimmy Rimmer", "Nigerl Spink", "Peter Shilton", "David Semen"],
                        ["Alex Ferguson", "Jose Marinio", "Howard Kendell", "Joe Fagan", "Ron Saunders", "Bob Paisely", "Howard Wilkinson", "George Graham", "Howard Kendall", "Carlo Ancellotti", "Kenny Dalglish", "Arsene Wenger"],
                        ["Montedivao", "Johanasburg", "London", "Yokohama", "Solna", "Santiago", "Passadena", "Bern", "Buenos Aires", "Rio de Janeiro", "Mexico City", "Berlin", "Munich", "Madrid", "Rome", "Paris"],
                        ["Paul Scoles", "Emile Heskey"]
                    ],
                    [
                        ["Michael Buble", "Take That"]
                    ]
             ]
if not os.path.isfile(SAVED_GAME_JSON):
    print("Game config not found. Creating new game.")
    with open(SAVED_GAME_JSON, "wt") as fe:

        teams=int(input("How many teams will be playing: "))
        for i in range(teams):
            if int(teams) - i == 1:
                comma=""
            print("Team " + str(i+1))
            TEAMS["teams"].append(input("Enter teamname: "))

        print(TEAMS)
        json.dump(TEAMS, fe)
        fe.close()
with open(SAVED_GAME_JSON, "r") as f:
    print("Welcome to Pointless")
    print("Where obvious answers mean nothing\nAnd obscure answers mean everything\nThe less points, the more you win.\nGood luck!")
    print("We will play with the teams from last time:")
    jsonTeams=json.load(f)
    print(jsonTeams["teams"])
    TEAMS=jsonTeams
    randomstack=random.randint(0,2)
    for i in range(len(TEAMS)):
        print("Welcome, team " + TEAMS["teams"][i])
        print("\nDecide: ")
        count=0
        randomstack=random.randint(0,2)
        for i in BATCH_STACK[randomstack]:
        	print(" - "+str(count+1) + " - " + str(BATCH_STACK[randomstack][count]))
        	count += 1
        choice=int(input("Batch: "))
        count=0
        for i in QUESTION_STACK[randomstack][choice-1]:
            count+=1
            print(" Question " + str(count) + " - " + i)
        q_choice=int(input("Enter question: "))
        ans=input("Enter answer to q " + str(q_choice) + ": ")
        if ans in ANSWER_STACK[choice-1][q_choice-1]:
            print("That is correct! This answer is x points!")
        else:
            print("Wrong - Next team!")
