import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# KAREN
def dibujar_nombre_karen():
    plt.text(0.0, 0.5, 'K', fontsize=100, color='blue')
    plt.text(0.1, 0.5, 'A', fontsize=100, color='blue')
    plt.text(0.2, 0.5, 'R', fontsize=100, color='blue')
    plt.text(0.3, 0.5, 'E', fontsize=100, color='blue')
    plt.text(0.4, 0.5, 'N', fontsize=100, color='blue')

# DIANA
def dibujar_nombre_diana():
    plt.text(0.55, 0.5, '&', fontsize=100, color='magenta')
    plt.text(0.7, 0.5, 'D', fontsize=100, color='green')
    plt.text(0.82, 0.5, 'I', fontsize=100, color='green')
    plt.text(0.86, 0.5, 'A', fontsize=100, color='green')
    plt.text(0.97, 0.5, 'N', fontsize=100, color='green') 
    plt.text(1.1, 0.5, 'A', fontsize=100, color='green')

# plot
plt.figure(figsize=(10, 4))
plt.axis('off')  # Ocultar los ejes

# Dibujar
dibujar_nombre_karen()
dibujar_nombre_diana()

# Mostrar el plot
plt.show()