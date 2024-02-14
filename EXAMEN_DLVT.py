import ply.lex as lex
import tkinter as tk
from tkinter import scrolledtext

# Define tokens
tokens = (
    'RESERVADA',
    'IDENTIFICADOR',
    'OPERADOR',
    'NUMERO',
    'SIMBOLO'
)

# Reglas para tokens
t_RESERVADA = r'(base|altura|Area)'
t_IDENTIFICADOR = r'(Diana|Laura|fecha)'
t_SIMBOLO = r'[()]'
t_OPERADOR = r'[*/=]'
t_NUMERO = r'\d+(\.\d+)?'

# Ignorar espacios y saltos de línea
t_ignore = ' \n'

# Función para manejar errores
def t_error(t):
    print(f"Carácter no válido: {t.value[0]} en la línea {t.lineno}")
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()

# Función para analizar la entrada
def analizar_codigo(codigo):
    lexer.input(codigo)
    tokens_encontrados = []
    for token in lexer:
        tokens_encontrados.append((token.type, token.value, token.lineno))
    return tokens_encontrados

# Interfaz gráfica
def analizar():
    codigo_fuente = entrada.get("1.0", tk.END)
    tokens = analizar_codigo(codigo_fuente)
    resultado.delete("1.0", tk.END)
    
    # Organizar tokens en secciones
    reservadas = []
    identificadores = []
    operadores = []
    numeros = []
    simbolos = []
    
    for token in tokens:
        tipo, valor, linea = token
        resultado.insert(tk.END, f"{tipo}        {valor}         {linea}\n")
        
        if tipo == 'RESERVADA':
            reservadas.append(valor)
        elif tipo == 'IDENTIFICADOR':
            identificadores.append(valor)
        elif tipo == 'OPERADOR':
            operadores.append(valor)
        elif tipo == 'NUMERO':
            numeros.append(valor)
        elif tipo == 'SIMBOLO':
            simbolos.append(valor)

# Crear ventana
ventana = tk.Tk()
ventana.title("Analizador Léxico")

# Entrada de texto
entrada = scrolledtext.ScrolledText(ventana, width=40, height=10)
entrada.pack()

# Etiqueta para la tabla de tokens  
Tabla = tk.Label(ventana, text="TOKEN                    TIPO                   LINEA")
Tabla.pack()

# Resultado
resultado = scrolledtext.ScrolledText(ventana, width=40, height=20)
resultado.pack()

# Botón para analizar
boton_analizar = tk.Button(ventana, text="Analizar", command=analizar)
boton_analizar.pack()

ventana.mainloop()
