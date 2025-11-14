import google.generativeai as genai



# Configuration avec ta clé API
genai.configure(api_key="AIzaSyDeylBoI5wpK-gyK_enfd1T8-L_doG_5hg")


# Création du modèle (doit être multimodal !)
model = genai.GenerativeModel("gemini-2.5-flash")  # ou gemini-1.5-pro
