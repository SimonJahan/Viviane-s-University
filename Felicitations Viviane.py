import streamlit as st
from datetime import datetime

# Titre principal
st.title("💪 Encouragements pour Viviane !")

# Accueil chaleureux
st.header("Bienvenue Viviane ! 🌟")
st.write("""
Les rattrapages approchent en septembre, mais tu as tout pour réussir !  
Garde confiance en toi, tout le monde croit en toi ! Voici quelques mots et citations pour te donner de la force.
""")

# Citations motivantes
st.subheader("🌈 Citations motivantes")
citations = [
    "Le succès, c’est se promener d’échecs en échecs tout en restant motivé. – Winston Churchill",
    "Ta seule limite, c’est toi-même.",
    "Vous ne devez jamais abandonner. – Marie Curie",
    "Crois en toi, tous les jours, un peu plus."
]
st.write(f"**{citations[datetime.now().day % len(citations)]}**")

# Zone pour laisser un message d'encouragement
st.subheader("🎉 Laisse un message à Viviane")
message = st.text_area("Écris ici un mot d'encouragement pour Viviane :")
if st.button("Envoyer"):
    st.success("Merci pour ton message envoyé à Viviane ! 💌")

# Footer positif
st.markdown("<hr>", unsafe_allow_html=True)
st.write("Toute l’équipe est derrière toi, Viviane ! Tu vas briller en septembre ✨")
