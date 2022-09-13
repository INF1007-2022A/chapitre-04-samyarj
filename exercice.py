#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if len(string) % 2 == 0:
        return True
    else:
        return False
    #pass


def remove_third_char(string: str) -> str:
    # return (string[:2] + string[3:])
    new_str = ''
    for car in string:
        if car != string[2]:
            new_str+= car
    return new_str # probleme est que ca va enlever tous les cars de 3 ex. bonbon


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_str = str()
    for car in string:
        if car != old_char:
            new_str += car
        elif car == old_char:
            new_str += new_char
    return new_str


def get_number_of_char(string: str, char: str) -> int:
    pass


def get_number_of_words(sentence: str, word: str) -> int:
    pass


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
