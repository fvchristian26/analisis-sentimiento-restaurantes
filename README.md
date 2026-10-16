# Proyecto de Análisis de Sentimiento en Opiniones de Restaurantes

> **Clasificación automatizada de opiniones de comensales mediante modelos preentrenados de Hugging Face y aceleración por GPU.**

---

## 📌 Descripción del Proyecto
Este proyecto desarrolla un prototipo funcional de Inteligencia Artificial enfocado en el Procesamiento del Lenguaje Natural (PLN) para la industria gastronómica. Utilizando modelos basados en la arquitectura **Transformers**, se automatiza la clasificación de opiniones de clientes (provenientes de Google Reviews, Facebook y encuestas internas) en tres categorías de sentimiento:
* **`POS`**: Positivo
* **`NEU`**: Neutral
* **`NEG`**: Negativo

El objetivo técnico es comparar el desempeño de tres modelos preentrenados en español sobre un entorno acelerado en **Google Colab con GPU T4**, evaluando el equilibrio entre precisión técnica (*Accuracy*, *F1-score*) y eficiencia operativa (latencia de inferencia).

---

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.10+
* **Ecosistema de IA:** Hugging Face (`transformers`, `datasets`, `evaluate`, `huggingface_hub`)
* **Procesamiento de Datos:** Pandas, Scikit-learn
* **Entorno de Ejecución:** Google Colab (GPU NVIDIA T4)
* **Control de Versiones:** Git y GitHub

---

## 📁 Estructura del Repositorio
```text
analisis-sentimiento-restaurantes/
│
├── data/
│   └── dataset_restaurante.csv          # Dataset con las 30 opiniones clasificadas
│
├── notebooks/
│   └── prototipo_evaluacion_modelos.ipynb # Cuaderno interactivo con el flujo completo
│
├── results/
│   └── metricas_comparativas.csv         # Métricas generadas tras la evaluación
│
├── src/
│   └── preprocessing.py                 # Script ejecutable para reproducir el dataset
│
├── requirements.txt                      # Dependencias del entorno
└── README.md                             # Documentación técnica principal