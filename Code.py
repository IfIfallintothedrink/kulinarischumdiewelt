import streamlit as st
import random
import json
import os

# Datei-Pfade
DATEI_VERBLEIBEND = "verbleibende_laender.json"
DATEI_VERWENDET = "verwendete_laender.json"

# Offizielle Liste von 195 Ländern (UN + Vatikan + Taiwan)
ALLE_LAENDER = [
    "Afghanistan", "Ägypten", "Albanien", "Algerien", "Andorra", "Angola", "Antigua und Barbuda", "Äquatorialguinea",
    "Argentinien", "Armenien", "Aserbaidschan", "Äthiopien", "Australien", "Bahamas", "Bahrain", "Bangladesch",
    "Barbados", "Belgien", "Belize", "Benin", "Bhutan", "Bolivien", "Bosnien und Herzegowina", "Botsuana", "Brasilien",
    "Brunei", "Bulgarien", "Burkina Faso", "Burundi", "Chile", "China", "Costa Rica", "Dänemark", "Demokratische Republik Kongo",
    "Dominica", "Dominikanische Republik", "Dschibuti", "Ecuador", "El Salvador", "Eritrea", "Estland", "Eswatini",
    "Fidschi", "Finnland", "Frankreich", "Gabun", "Gambia", "Georgien", "Ghana", "Grenada", "Griechenland", "Guatemala",
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Indien", "Indonesien", "Irak", "Iran", "Irland", "Island",
    "Israel", "Italien", "Jamaika", "Japan", "Jemen", "Jordanien", "Kambodscha", "Kamerun", "Kanada", "Kap Verde", "Kasachstan",
    "Katar", "Kenia", "Kirgisistan", "Kiribati", "Kolumbien", "Komoren", "Kongo", "Kroatien", "Kuba", "Kuwait", "Laos",
    "Lettland", "Libanon", "Liberia", "Libyen", "Liechtenstein", "Litauen", "Luxemburg", "Madagaskar", "Malawi", "Malaysia",
    "Malediven", "Mali", "Malta", "Marokko", "Marshallinseln", "Mauretanien", "Mauritius", "Mexiko", "Mikronesien", "Moldau",
    "Monaco", "Mongolei", "Montenegro", "Mosambik", "Myanmar", "Namibia", "Nauru", "Nepal", "Neuseeland", "Nicaragua", "Niederlande",
    "Niger", "Nigeria", "Nordkorea", "Nordmazedonien", "Norwegen", "Oman", "Österreich", "Osttimor", "Pakistan", "Palau",
    "Panama", "Papua-Neuguinea", "Paraguay", "Peru", "Philippinen", "Polen", "Portugal", "Ruanda", "Rumänien", "Russland",
    "Salomonen", "Sambia", "Samoa", "San Marino", "São Tomé und Príncipe", "Saudi-Arabien", "Schweden", "Schweiz", "Senegal",
    "Serbien", "Seychellen", "Sierra Leone", "Simbabwe", "Singapur", "Slowakei", "Slowenien", "Somalia", "Spanien", "Sri Lanka",
    "St. Kitts und Nevis", "St. Lucia", "St. Vincent und die Grenadinen", "Sudan", "Südafrika", "Südkorea", "Südsudan", "Suriname",
    "Syrien", "Tadschikistan", "Taiwan", "Tansania", "Thailand", "Togo", "Tonga", "Trinidad und Tobago", "Tschad", "Tschechien",
    "Tunesien", "Türkei", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "Ungarn", "Uruguay", "Usbekistan", "Vanuatu", "Vatikanstadt",
    "Venezuela", "Vereinigte Arabische Emirate", "Vereinigte Staaten", "Vietnam", "Weißrussland", "Zentralafrikanische Republik", "Zypern"
]

# Dateien laden oder initialisieren
def lade_datei(pfad, fallback):
    if os.path.exists(pfad):
        with open(pfad, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return fallback

def speichere_datei(pfad, daten):
    with open(pfad, "w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=2)

verwendet = lade_datei(DATEI_VERWENDET, [])
verbleibend = lade_datei(DATEI_VERBLEIBEND, [l for l in ALLE_LAENDER if l not in verwendet])

# App UI
st.title("🍽️ Länder-Auslosung für die Kochgruppe")

if not verbleibend:
    st.warning("🎉 Ihr habt bereits alle 195 Länder ausprobiert!")
else:
    if st.button("Neues Land auslosen"):
        neues_land = random.choice(verbleibend)
        st.success(f"🎊 Das neue Land ist: **{neues_land}**")

        # aktualisieren
        verwendet.append(neues_land)
        verbleibend.remove(neues_land)
        speichere_datei(DATEI_VERBLEIBEND, verbleibend)
        speichere_datei(DATEI_VERWENDET, verwendet)

# Anzeige
st.subheader("✅ Bereits gekocht:")
st.write(", ".join(sorted(verwendet)))

st.subheader("🌍 Noch übrig:")
st.write(f"{len(verbleibend)} Länder")
