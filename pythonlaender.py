import streamlit as st
import random
import json
import os

DATEI = "länder.json"

ALLE_LÄNDER = [
    "Afghanistan", "Albanien", "Algerien", "Andorra", "Angola", "Argentinien", "Armenien", "Australien",
    "Bahamas", "Bangladesch", "Belgien", "Benin", "Bhutan", "Bolivien", "Bosnien und Herzegowina", "Botsuana",
    "Brasilien", "Bulgarien", "Chile", "China", "Dänemark", "Deutschland", "Dominikanische Republik", "Ecuador",
    "Ägypten", "Estland", "Finnland", "Frankreich", "Georgien", "Ghana", "Griechenland", "Großbritannien",
    "Guatemala", "Honduras", "Indien", "Indonesien", "Irland", "Iran", "Irak", "Italien", "Jamaika", "Jordanien",
    "Kambodscha", "Kanada", "Katar", "Kasachstan", "Kroatien", "Kuba", "Laos", "Lettland", "Libanon", "Litauen",
    "Luxemburg", "Malaysia", "Malta", "Marokko", "Mexiko", "Mongolei", "Mosambik", "Namibia", "Nepal", "Neuseeland",
    "Niederlande", "Niger", "Nigeria", "Norwegen", "Österreich", "Pakistan", "Panama", "Paraguay", "Philippinen",
    "Polen", "Portugal", "Rumänien", "Russland", "Saudi-Arabien", "Schweden", "Schweiz", "Senegal", "Serbien",
    "Singapur", "Slowakei", "Slowenien", "Spanien", "Sri Lanka", "Südafrika", "Südkorea", "Syrien", "Tansania",
    "Thailand", "Tschechien", "Tunesien", "Türkei", "Uganda", "Ukraine", "Ungarn", "Uruguay", "USA", "Venezuela",
    "Weißrussland", "Zypern"
]

BEREITS_GEKOCHT = ["Island", "Peru", "Japan", "Tibet", "Vietnam", "Madagaskar", "Kenya"]

def lade_liste():
    if os.path.exists(DATEI):
        with open(DATEI, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return [land for land in ALLE_LÄNDER if land not in BEREITS_GEKOCHT]

def speichere_liste(liste):
    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(liste, f, ensure_ascii=False)

st.title("🌍 Länder-Auslosung für die Kochgruppe")

länder = lade_liste()

if not länder:
    st.warning("Alle Länder wurden bereits verwendet!")
else:
    if st.button("Neues Land ziehen"):
        land = random.choice(länder)
        st.success(f"Euer neues Land ist: **{land}**")
        länder.remove(land)
        speichere_liste(länder)

    st.info(f"Übrige Länder: **{len(länder)}**")
