import os
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

print("--- INICIANDO PROCESO EN CONTENEDOR ---")

# Si no existe 'model.pkl', lo entrenamos automáticamente aquí mismo
if not os.path.exists("model.pkl"):
    print("No se encontró 'model.pkl'. Entrenando un modelo base de ejemplo...")
    
    textos_entreno = [
        "La comida estuvo excelente y el servicio increíble.",
        "Delicioso todo, muy recomendado.",
        "El peor lugar que he visitado, la comida fría y mal servicio.",
        "Pésimo ambiente y tardaron muchísimo en atender.",
        "Estuvo regular, nada del otro mundo pero aceptable."
    ]
    etiquetas = [1, 1, 0, 0, 1]  # 1 = Positivo, 0 = Negativo
    
    modelo_temp = make_pipeline(CountVectorizer(), MultinomialNB())
    modelo_temp.fit(textos_entreno, etiquetas)
    
    joblib.dump(modelo_temp, "model.pkl")
    print("¡Modelo 'model.pkl' creado y guardado con éxito!")

# Cargar el modelo
model = joblib.load("model.pkl")
print("¡Modelo cargado correctamente en el sistema!")

# Textos de prueba
textos_prueba = [
    "¡Me encantó este restaurante, volveré sin duda!",
    "La comida fue horrible y el mesero grosero.",
    "Un lugar pasable para comer algo rápido."
]

print(f"\nEvaluando {len(textos_prueba)} casos de prueba:")
for i, texto in enumerate(textos_prueba, start=1):
    pred = model.predict([texto])[0]
    proba = model.predict_proba([texto])[0]
    sentimiento = "Positivo (1)" if pred == 1 else "Negativo (0)"
    print(f"\nCaso {i}: \"{texto}\"")
    print(f" -> Resultado: {sentimiento} | Probabilidades: {proba}")

print("\n--- FIN DE LA SIMULACIÓN EXITOSA ---")