choose = input("Möchtest du ver- oder entschlüsseln? (ver/ent)\n")

if choose == "ver":

    buchstaben = "abcdefghijklmnopqrstuvwxyz"

    input_message = input("Zu verschlüsselnden Text eingeben:\n")

    verschlüsselung = int(input("Verschiebung eingeben:\n"))

    output_message = ""

    input = len(input_message)

    for i in range(input):
        character = input_message[i]
        locate = buchstaben.find(character)
        relocate = (locate + verschlüsselung) % 26
        output_message += buchstaben[relocate]
        #print(charater, locate, relocate)
    print("Die Verschlüsselung von " + input_message + " mit einer Verschiebung von " + str(verschlüsselung) + " lautet: " + output_message)

if choose == "ent":
    
    buchstaben = "abcdefghijklmnopqrstuvwxyz"

    input_message = input("Zu entschlüsselnden Text eingeben:\n")

    verschlüsselung = int(input("Verschiebung eingeben:\n"))

    output_message = ""

    input = len(input_message)

    for i in range(input):
        character = input_message[i]
        locate = buchstaben.find(character)
        relocate = (locate - verschlüsselung) % 26
        output_message += buchstaben[relocate]
        #print(character, locate, relocate)
    print("Die Entschlüsselung von " + input_message + " mit einer Verschiebung von " + str(verschlüsselung) + " lautet: " + output_message)
