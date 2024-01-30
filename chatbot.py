from browser import document, html

# Phrase d'origine
phrase_originale = "C'est quoi python ? Python est un langage de programmation."

# Création de la liste de mots et de caractères avec leurs positions
mots_caracteres = []
position = 0

for mot in phrase_originale.split():
    mots_caracteres.append((mot, position))
    position += 1

    for caractere in mot:
        mots_caracteres.append((caractere, position))
        position += 1

# Fonction de recherche de réponse
def generate_response(user_message):
    user_message = user_message.lower()

    mots_recherches = user_message.split()
    mots_trouves = []
    position_suivante = -1

    for mot_recherche in mots_recherches:
        for mot, position in mots_caracteres:
            if mot_recherche == mot.lower() and position > position_suivante:
                mots_trouves.append(mot)
                position_suivante = position

    positions_mots_trouves = [position + 1 for _, position in mots_caracteres if _ in mots_trouves]
    positions_mots_trouves.sort()

    mots_trouves_final = [mot for mot, position in mots_caracteres if position in positions_mots_trouves]

    return " ".join(mots_trouves_final)

# Affichage des messages dans la boîte de chat
chatbox = document["chatbox"]
user_input = document["user_input"]

def display_message(message, sender):
    message_element = html.DIV(message, Class="message " + sender + "-message")
    chatbox <= message_element
    chatbox.scrollTop = chatbox.scrollHeight

def process_user_input(event):
    if event.keyCode == 13:
        user_message = user_input.value.strip()
        user_input.value = ""
        display_message(user_message, "user")
        answer = generate_response(user_message)
        display_message(answer, "chatbot")

user_input.bind("keydown", process_user_input)