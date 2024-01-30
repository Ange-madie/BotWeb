from browser import document, html, bind, window

chat = document["chatbox"]
user = document["demande_utilisateur"]
data = {
    "Bonjour": [('Bonjour',), 'Bonjour'],
    "Salut": [('Salut',), 'Salut'],
    "Comment vas-tu ?": [('Comment', 'vas', 'tu'), 'Je vais bien, merci.'],
    "Qui es-tu ?": [('Qui', 'es', 'tu'), 'Je suis le ChatBot Nora GV 1'],
    "D'ou vien tu ?": [("D'ou", 'vien', 'tu'), "Je vien d'un PC qui se trouve à un endroit dans le monde."],
    "Que peut-tu me dire à propos de python ?": [("Que", "peut", "tu", "me", "dire", "à", "propos", "de", "python"), "Python est un langage de programmation."],
    "Comment t'appelles-tu ?": [("Comment", "t'appelles", "tu"), "Je m'appelle Nora GV."],
    "Quel est ton nom ?": [("Quel", "est", "ton", "nom"), "Mon nom est Nora GV."],
    "Qui est ton créateur": [("Qui", "est", "ton", "créateur"), "Mes créateurs se nomment Asolan1200 et Arcel Bika."],
    "Java, c'est quoi ?": [("Java", "c'est", "quoi"), "Java est un lanagage de programmation comme python"]
}
mots = []
peu_point = ["Qui", "est", "C'est", "quoi", "es"]
synonyme = {}


for value in data.values():
    for g in value[0]:
        if not g in mots:
            mots.append(g)
          
            
def test_in_tab(tab1: list | tuple, tab2: list | tuple):
    for value in tab1:
        if value in tab2:
            return True

    return False


def all_test_in_tab(tab1: list | tuple, tab2: list | tuple):
    for value in tab1:
        if value not in tab2:
            return False

    return True

def separateur_mot(phrase: str):
    """Fonction pour diviser une phrase en mots."""
    mot = []
    ignorer = ["?", "-", ".", "!", "_", " ", ","]
    l = []
    for letter in phrase:
        if letter not in ignorer:
            l.append(letter)
        else:
            if l:
                mot.append(''.join(l))
            l = []
    if l:
        mot.append(''.join(l))

    return tuple(mot)

def generate_reponse(message):
    cpt = 0
    select = 0
    choisie = ""
    # self.save_mot(self.reponse)
    tab_reponse = separateur_mot(message)
    print(tab_reponse)
    for cle, valeur in data.items():
        for w in valeur[0]:
            if cle.lower() == message:
                print(cle)
                cpt += 5
            elif w.lower() in tab_reponse:
                if w in peu_point:
                    cpt += 0.2
                else:
                    cpt += 1
            else:
                if w in synonyme.keys():
                    if synonyme[w].lower() in tab_reponse:
                        cpt += 1
        data[cle].append(cpt)
        print(cpt)
        cpt = 0
    for cle, valeur in data.items():
        if valeur[2] > 0:
            if valeur[2] > select:
                select = valeur[2]
    for cle in data.keys():
        if data[cle][2] == select:
            choisie = data[cle][1]
    for cle in data.keys():
        data[cle].pop()
    return choisie

def display_message(message, emetteur):
    smessage = html.DIV(f"{emetteur}: "+message, Class=f"message {emetteur}-message")
    chat <= smessage
    chat.scrollTop = chat.scrollHeight

def process(event):
    if event.code == "Enter":
        mes = user.value
        display_message(mes, "User")
        rep_bot = generate_reponse(mes.lower())
        display_message(rep_bot, "Nora")
        user.value = ""

user.bind("keydown", process)