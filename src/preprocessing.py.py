import os
import pandas as pd

def generar_dataset_restaurante():
    """
    Script reproducible para generar y estructurar el conjunto de datos
    de opiniones de comensales para el análisis de sentimientos.
    Exporta el dataset a la carpeta 'data/dataset_restaurante.csv'.
    """
    # 1. Definición del corpus estructurado de 30 opiniones
    data = {
        "comentario": [
            "El restaurante es excelente, la comida tiene un sazón increíble y el servicio fue rápido.",
            "La experiencia fue terrible, la comida llegó fría y el mesero fue grosero. No volvería jamás.",
            "El ambiente del lugar es agradable y tranquilo, aunque los platillos son algo costosos para lo que ofrecen.",
            "Un lugar excepcional para cenar en pareja, los postres son deliciosos y la atención sobresaliente.",
            "Pésima organización, tardaron más de una hora en darnos una mesa y la comida no tenía sabor.",
            "El servicio estuvo bien, nada extraordinario, pero cumple para una comida rápida.",
            "Me encantó la presentación de los platos y la amabilidad del personal. ¡Muy recomendable!",
            "La relación calidad-precio es muy mala, porciones pequeñas y precios exagerados.",
            "Un espacio muy acogedor, limpio y con una carta de vinos excelente.",
            "No me gustó para nada, la música estaba muy alta y la comida me cayó pesada.",
            "La comida estuvo deliciosa y el tiempo de espera fue mínimo. Volveremos pronto.",
            "Pedimos varios platillos y todos estaban fríos. La atención de la recepcionista dejó mucho que desear.",
            "El menú es variado y los precios son aceptables. El café podría ser mejor.",
            "Excelente lugar para desayunar en familia, las porciones son generosas y el sazón es buenísimo.",
            "Muy mala higiene en el baño y las mesas estaban pegajosas. No lo recomiendo.",
            "La sazón es impecable, de las mejores cortes de carne que he probado en la ciudad.",
            "La atención del personal es muy atenta, aunque el parqueo es muy reducido y complicado.",
            "Llegamos a la hora de la reserva y nuestra mesa no estaba lista. Esperamos 40 minutos extra.",
            "Los tacos y las salsas tienen un sabor espectacular. El precio vale totalmente la pena.",
            "Normal, la comida no destaca pero el lugar es cómodo para platicar un rato.",
            "Definitivamente uno de mis lugares favoritos. La pasta alfredo es exquisita.",
            "Se equivocaron dos veces con nuestra orden y el mesero se mostró molesto cuando se lo señalamos.",
            "Tienen buenas opciones vegetarianas y el jugo natural estaba muy fresco.",
            "Un restaurante promedio, ideal si buscas algo rápido para almorzar sin grandes expectativas.",
            "La ambientación con música en vivo le da un toque fantástico a la velada. 10/10.",
            "Los precios aumentaron considerablemente y la calidad de los ingredientes bajó.",
            "Servicio cordial, platillos bien presentados y un ambiente muy familiar.",
            "Tardaron demasiado en traer la cuenta y la terminal bancaria falló varias veces.",
            "La sopa del día estaba increíblemente sabrosa y recién hecha.",
            "Las bebidas estaban bastante bien, aunque el platillo principal carecía de sal."
        ],
        "sentimiento": [
            "POS", "NEG", "NEU", "POS", "NEG", 
            "NEU", "POS", "NEG", "POS", "NEG", 
            "POS", "NEG", "NEU", "POS", "NEG", 
            "POS", "NEU", "NEG", "POS", "NEU", 
            "POS", "NEG", "POS", "NEU", "POS", 
            "NEG", "POS", "NEG", "POS", "NEU"
        ]
    }
    
    # 2. Creación del DataFrame
    df = pd.DataFrame(data)
    
    # 3. Creación del directorio 'data' si no existe
    os.makedirs('data', exist_ok=True)
    
    # 4. Exportación a CSV
    file_path = os.path.join('data', 'dataset_restaurante.csv')
    df.to_csv(file_path, index=False, encoding='utf-8')
    print(f"Dataset generado exitosamente en: {file_path}")

def normalizar_etiqueta(pred_label):
    """
    Función auxiliar para normalizar las etiquetas de salida de diferentes
    modelos de Hugging Face a la convención corporativa (POS, NEU, NEG).
    """
    label_upper = str(pred_label).upper()
    if 'NEG' in label_upper or 'NEGATIVE' in label_upper or '1' in label_upper:
        return 'NEG'
    elif 'NEU' in label_upper or 'NEUTRAL' in label_upper or '2' in label_upper:
        return 'NEU'
    else:
        return 'POS'

if __name__ == "__main__":
    generar_dataset_restaurante()