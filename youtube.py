import requests
import re
import sys

def canal_input():
    nombre_canal = input("Nombre del canal: ")
    canal = "https://www.youtube.com/@" + nombre_canal
    html = requests.get(canal + "/videos").text
    info = re.search('(?<={"label":").*?(?="})',html).group()
    url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")',html).group()

    print(info)
    print(url)

def canal_args(nombre):
    canal = "https://www.youtube.com/@" + nombre
    html = requests.get(canal + "/videos").text
    info = re.search('(?<={"label":").*?(?="})',html).group()
    url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")',html).group()

    print(info)
    print(url)


def main():
    eleccion = sys.argv[1]
    if eleccion == "1":
        canal_input()
    elif eleccion == "2":
        nombre_canal = sys.argv[2]
        canal_args(nombre_canal)
    else:
        print("Introduce la info.")

main()
