import google.generativeai as genai



# Configuration avec ta clé API
genai.configure(api_key="AIzaSyBbtyZVEvPvMV6flEwFFbUe69syCmoj-y0")


# Création du modèle (doit être multimodal !)
model = genai.GenerativeModel("gemini-2.5-flash")  # ou gemini-1.5-pro
