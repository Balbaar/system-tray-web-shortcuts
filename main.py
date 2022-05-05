import pystray
import PIL.Image
import webbrowser

image = PIL.Image.open("logo.png")

google_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

#Matte
math_urls = {1: "https://konto.nok.se/login/nokflex",
             2: "https://nokflex-cdn.nok.se/public/content/formelblad/pdf/Formelblad_matematik_4_2021.pdf"}

#Physics
physics_urls = {1: "https://www.liber.se/plus/E471262201.pdf"}

#Swedish
swedish_urls = {1: "https://classroom.google.com/u/3/c/Mzc4MDUzNjM1MTA0",
                2: "https://drive.google.com/drive/u/3/my-drive"}

#English
english_urls = {1: "https://classroom.google.com/u/3/c/Mzc4MDQwMDA0Nzg3"}

#History
history_urls = {1: "https://classroom.google.com/u/3/c/NDMyMTgwMjU5Nzk3",
                2: "https://docs.google.com/document/d/12u8Sm0bqaV7q0vPWeca3Jch3qPrCp3b2iGoonqRL2Vs/edit",
                3: "https://drive.google.com/drive/u/3/my-drive"}

#Technic
technic_urls = {

}


def clicked(icon, item):
    if str(item) == "Matte":
        for page in math_urls:
            print(f"Trying {math_urls[page]}")
            try:
                webbrowser.get(google_location).open(math_urls[page])
                print(f"Successful {math_urls[page]}")

            except:
                print(f"Failed {math_urls[page]}")

    elif str(item) == "Fysik":
        for page in physics_urls:
            webbrowser.get(google_location).open(physics_urls[page])
            print(f"Successful {math_urls[page]}")

    elif str(item) == "Svenska":
        for page in swedish_urls:
            webbrowser.get(google_location).open(swedish_urls[page])
            print(f"Successful {math_urls[page]}")

    elif str(item) == "Engelska":
        for page in english_urls:
            webbrowser.get(google_location).open(english_urls[page])
            print(f"Successful {math_urls[page]}")

    elif str(item) == "Historia":
        for page in history_urls:
            webbrowser.get(google_location).open(history_urls[page])
            print(f"Successful {math_urls[page]}")

    elif str(item) == "Stäng":
        icon.stop()


icon = pystray.Icon("SchoolCuts", image, menu=pystray.Menu(
    pystray.MenuItem("Matte", clicked),
    pystray.MenuItem("Fysik", clicked),
    pystray.MenuItem("Svenska", clicked),
    pystray.MenuItem("Engelska", clicked),
    pystray.MenuItem("Historia", clicked),
    pystray.MenuItem("Teknik", clicked),
    pystray.MenuItem("Stäng", clicked)
))

icon.run()
