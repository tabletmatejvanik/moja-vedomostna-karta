from PyQt5.QtCore import Qt
def play_win():
    for _ in range(3):
        QApplication.beep()

def play_lose():
    QApplication.beep()
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QGroupBox, QGridLayout, QLabel, QPushButton, QVBoxLayout, QMessageBox
from random import shuffle



mode = "answer"
app = QApplication([])
kolikata = 0
score = 0
window = QWidget()
window.resize(600, 300)
window.setWindowTitle("hádanka")
Moznosti = QGroupBox("Možnosti")
otazka = QLabel("Co je značka sodíku?")
result = QLabel("")

listOfQuestions = [
    ["Co je boot.img?", "Obraz jádra a ramdisku",
     ["Obraz jádra a ramdisku", "Záloha fotek", "Oddíl pro hudbu", "Typ aplikace"]],
    ["Co je hlavní účel Play Integrity?", "Kontrola integrity zařízení",
     ["Zrychlení systému", "Záloha aplikací", "Kontrola integrity zařízení", "Root přístup"]],
    ["Co znamená systemless root?", "Root bez úprav /system",
     ["Root přes Bluetooth", "Root jen pro hry", "Root bez bootloaderu", "Root bez úprav /system"]],
    ["Co je Magisk DenyList?", "Skrytí rootu před aplikacemi",
     ["Skrytí rootu před aplikacemi", "Firewall", "Záloha systému", "Seznam modulů"]],
    ["K čemu slouží partition vbmeta?", "Ověřování Verified Boot",
     ["Cache aplikací", "Oddíl pro SIM", "Ukládání fotek", "Ověřování Verified Boot"]],
    ["Co je EDL mód?", "Nouzový flash režim Qualcomm",
     ["Wi-Fi debug", "Nouzový flash režim Qualcomm", "Herní režim", "Magisk plugin"]],
    ["Co se stane při wipe data?", "Smazání uživatelských dat",
     ["Oprava Knox", "Smazání uživatelských dat", "Zapnutí rootu", "Zrychlení CPU"]],
    ["Co nejčastěji způsobí bootloop po modulu?", "Konflikt při startu systému",
     ["Špatná SIM karta", "Nízká baterie", "Plná galerie", "Konflikt při startu systému"]],
    ["Co dělá fastboot flash?", "Nahraje image do oddílu",
     ["Zapne root", "Vymaže RAM", "Nahraje image do oddílu", "Spustí Android"]],
    ["Jaký je rozdíl mezi ADB a Fastboot?", "ADB běží v systému, Fastboot v bootloaderu",
     ["Fastboot je jen pro Samsung", "ADB je jen pro recovery", "ADB běží v systému, Fastboot v bootloaderu", "Žádný rozdíl"]],
]

listOfQuestions2 = [
    ["Co je dm-verity?", "Ochrana proti změně systémových oddílů",
     ["Antivir pro APK", "Ochrana proti změně systémových oddílů", "Režim fastboot", "Správce SIM"]],
    ["Co znamená Verified Boot?", "Kontrola integrity systému při startu",
     ["Zrychlení bootu", "Kontrola integrity systému při startu", "Root mód", "Režim recovery"]],
    ["Co je Zygisk v Magisku?", "Root injekce přes Zygote proces",
     ["Kernel driver", "Root injekce přes Zygote proces", "Bootloader unlock", "ADB příkaz"]],
    ["Co je rozdíl mezi MagiskHide a DenyList?", "DenyList je moderní náhrada MagiskHide",
     ["Žádný rozdíl", "DenyList je moderní náhrada MagiskHide", "MagiskHide je novější", "DenyList je antivir"]],
    ["Co je AVB (Android Verified Boot)?", "Mechanismus ověřování boot řetězce",
     ["Typ ROM", "Mechanismus ověřování boot řetězce", "Cache systému", "Správce aplikací"]],
    ["Co znamená A/B partition systém?", "Umožňuje bezvýpadkové OTA aktualizace",
     ["Zrychluje RAM", "Umožňuje bezvýpadkové OTA aktualizace", "Vypíná Knox", "Zvětšuje baterii"]],
    ["Co je vbmeta partition?", "Metadata pro Verified Boot kontrolu",
     ["Oddíl pro fotky", "Metadata pro Verified Boot kontrolu", "Oddíl pro aplikace", "Soubor Magisku"]],
    ["Co je initramfs?", "Dočasný souborový systém při bootu",
     ["Typ ROM", "Dočasný souborový systém při bootu", "Antivir modul", "Oddíl /data"]],
    ["Co je rozdíl mezi ext4 a F2FS?", "F2FS je optimalizovaný pro flash úložiště",
     ["ext4 je jen pro PC", "F2FS je optimalizovaný pro flash úložiště", "F2FS je antivir", "ext4 je cloud"]],
    ["Co znamená šifrování /data?", "Uživatelská data jsou chráněná klíčem",
     ["Data jsou veřejná", "Uživatelská data jsou chráněná klíčem", "Zrychlení systému", "Vypnutí Knox"]],
    ["Co je EroFS?", "Read-only souborový systém pro systémové oddíly",
     ["Typ procesoru", "Read-only souborový systém pro systémové oddíly", "Root aplikace", "Wi-Fi protokol"]],
    ["Co je kernel panic?", "Kritický pád jádra systému",
     ["Restart aplikace", "Kritický pád jádra systému", "Vymazání cache", "Změna DPI"]],
    ["Co je TrustZone (TEE)?", "Bezpečné oddělené prostředí procesoru",
     ["Custom ROM", "Bezpečné oddělené prostředí procesoru", "ADB režim", "Magisk modul"]],
    ["Co je Android Keystore?", "Bezpečné úložiště kryptografických klíčů",
     ["Cloud pro fotky", "Bezpečné úložiště kryptografických klíčů", "Oddíl system", "Záloha recovery"]],
    ["Co znamená rollback protection?", "Ochrana proti návratu na starší firmware",
     ["Zrychlení update", "Ochrana proti návratu na starší firmware", "Vypnutí šifrování", "Záloha dat"]],
]

currentQuestions = listOfQuestions
shuffle(currentQuestions)
amount = len(currentQuestions)
result.setAlignment(Qt.AlignCenter)

def load_question():
    global kolikata
    q_text, correct, options = currentQuestions[kolikata]
    options = options.copy()
    shuffle(options)
    otazka.setText(q_text)
    anw1.setText(options[0])
    anw2.setText(options[1])
    anw3.setText(options[2])
    anw4.setText(options[3])
    window.correct_answer = correct

def get_grade(score, total):
    percent = (score / total) * 100
    if percent >= 90:
        return 1
    elif percent >= 75:
        return 2
    elif percent >= 50:
        return 3
    elif percent >= 30:
        return 4
    else:
        return 5

def check_answer():
    global score
    selected = None
    for btn in [anw1, anw2, anw3, anw4]:
        if btn.isChecked():
            selected = btn.text()
    if selected is None:
        result.setText("⚠️ Vyber odpověď!")
        return False
    Moznosti.setEnabled(False)
    if selected == window.correct_answer:
        result.setText("✅ Správně!")
        score += 1
        play_win()
    else:
        result.setText("❌ Špatně!")
        play_lose()
    return True

done = QPushButton("Submit")

def button_click():
    global mode
    if mode == "answer":
        ok = check_answer()
        if ok:
            mode = "next"
            done.setText("Next question")
    else:
        next_question()
        mode = "answer"
        done.setText("Submit")

done.clicked.connect(button_click)

def next_question():
    global kolikata, currentQuestions, amount, score, mode
    kolikata += 1
    if kolikata >= len(currentQuestions):
        percent = (score / amount) * 100
        if percent >= 80 and currentQuestions == listOfQuestions:
            QMessageBox.information(
                window,
                "Level Up!",
                "🔥 Skvělé! Máš víc než 80 %!\nPostupuješ do těžšího levelu!"
            )
            currentQuestions = listOfQuestions2
            shuffle(currentQuestions)
            kolikata = 0
            score = 0
            amount = len(currentQuestions)
            Moznosti.show()
            done.show()
            result.setText("")
            mode = "answer"
            done.setText("Submit")
            load_question()
            return

        grade = get_grade(score, amount)

        if score == amount:
            play_win()
        elif score == 0:
            play_lose()

        percent = round((score / amount) * 100, 1)

        otazka.setText(
            f"Konec!\n"
            f"Skóre: {score}/{amount}\n"
            f"Procenta: {percent}%\n"
            f"Známka: {grade}"
        )

        Moznosti.hide()
        done.hide()
        return

    result.setText("")
    Moznosti.setEnabled(True)
    new()
    load_question()

anw1 = QRadioButton("So")
anw2 = QRadioButton("Na")
anw3 = QRadioButton("k")
anw4 = QRadioButton("P")

group_layout = QGridLayout()
group_layout.addWidget(anw1, 0, 0)
group_layout.addWidget(anw2, 0, 1)
group_layout.addWidget(anw3, 1, 0)
group_layout.addWidget(anw4, 1, 1)
Moznosti.setLayout(group_layout)

def new():
    anw1.setChecked(False)
    anw2.setChecked(False)
    anw3.setChecked(False)
    anw4.setChecked(False)

main_layout = QVBoxLayout()
otazka.setAlignment(Qt.AlignCenter)
main_layout.addWidget(otazka)
main_layout.addWidget(Moznosti)
main_layout.addWidget(done)
main_layout.addWidget(result)

window.setLayout(main_layout)
load_question()
window.show()
app.exec()
