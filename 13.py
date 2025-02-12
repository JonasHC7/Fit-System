import tkinter as tk
from tkinter import ttk, messagebox

def calcular_dieta():
    if not nome_texto.get() or not idade_texto.get() or not peso_texto.get() or not altura_texto.get():
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return
    
    nome = str(nome_texto.get())
    idade = int(idade_texto.get())
    peso = float(peso_texto.get())
    altura = float(altura_texto.get())
    doenca = int(doenca_var.get())

    if 20 <= idade <= 30 and 50 <= peso <= 70 and 150 <= altura <= 180:
        if doenca == 1:
            dieta = """Dieta para Diabetes (Dieta A): 
            Café da Manhã:
- 2 ovos mexidos com vegetais (espinafre, tomate, cebola)
- 1 fatia de pão integral
- 1/2 abacate
- 1 xícara de chá verde sem açúcar

Lanche da Manhã:
- 1 maçã pequena
- 10 amêndoas

Almoço:
- 100g de peito de frango grelhado
- 1/2 xícara de quinoa cozida
- Salada de folhas verdes (alface, rúcula, agrião) com tomate, pepino e azeite de oliva

Lanche da Tarde:
- 1 iogurte natural desnatado
- 1/4 xícara de mirtilos

Jantar:
- 100g de salmão assado com limão e ervas
- 1/2 xícara de arroz integral
- Brócolis no vapor
- Salada de cenoura ralada com vinagrete

Ceia:
- 1 taça de gelatina diet"""
        elif doenca == 2:
            dieta = """Dieta para Colesterol (Dieta B): 
            Café da Manhã:
- 1 omelete de claras com espinafre
- 1 fatia de pão integral
- 1/2 abacate
- 1 copo de suco de laranja natural

Lanche da Manhã:
- 1 pera
- 10 nozes

Almoço:
- 100g de salmão grelhado
- 1/2 xícara de arroz integral
- Brócolis no vapor
- Salada de folhas verdes com azeite de oliva

Lanche da Tarde:
- 1 iogurte natural desnatado
- 1 colher de sopa de sementes de chia

Jantar:
- 100g de peito de frango grelhado
- 1 batata-doce assada
- Aspargos grelhados

Ceia:
- 1 xícara de chá de camomila"""
        elif doenca == 3:
            dieta = """Dieta para Pressão Alta (Dieta C): 
            Café da Manhã:
- Mingau de aveia com leite desnatado e banana
- 1 fatia de melancia
- 1 xícara de chá de hortelã

Lanche da Manhã:
- 1 iogurte natural desnatado
- 1/4 xícara de morangos

Almoço:
- 100g de peixe grelhado
- 1/2 xícara de quinoa cozida
- Salada de pepino, tomate e alface com azeite de oliva
- 1 laranja

Lanche da Tarde:
- 1 pera
- 1 punhado de amêndoas

Jantar:
- 100g de filé mignon grelhado
- 1 batata-doce cozida
- Couve refogada
- Salada de cenoura ralada

Ceia:
- 1 maçã"""
        else:
            dieta = """Dieta Padrão: 
            Café da Manhã:
- 2 fatias de pão integral com queijo branco
- 1 copo de suco de laranja natural
- 1 banana

Lanche da Manhã:
- 1 iogurte natural desnatado
- 1 punhado de castanhas

Almoço:
- 100g de peito de frango grelhado
- 1/2 xícara de arroz integral
- Salada de folhas verdes com tomate e cenoura ralada
- 1 maçã

Lanche da Tarde:
- 1 pera
- 1 barra de cereal integral

Jantar:
- 100g de salmão assado
- 1 batata assada com alecrim
- Brócolis cozidos
- Salada de beterraba e rúcula

Ceia:
- 1 taça de gelatina diet"""
    else:
        dieta = """Dieta Padrão: 
        Café da Manhã:
- 2 fatias de pão integral com queijo branco
- 1 copo de suco de laranja natural
- 1 banana

Lanche da Manhã:
- 1 iogurte natural desnatado
- 1 punhado de castanhas

Almoço:
- 100g de peito de frango grelhado
- 1/2 xícara de arroz integral
- Salada de folhas verdes com tomate e cenoura ralada
- 1 maçã

Lanche da Tarde:
- 1 pera
- 1 barra de cereal integral

Jantar:
- 100g de salmão assado
- 1 batata assada com alecrim
- Brócolis cozidos
- Salada de beterraba e rúcula

Ceia:
- 1 taça de gelatina diet"""
    
    messagebox.showinfo("Dieta Recomendada", dieta)

def calcular_imc():
    if not peso_texto.get() or not altura_texto.get():
        messagebox.showerror("Erro", "Por favor, preencha os campos de peso e altura.")
        return
    
    peso = float(peso_texto.get())
    altura = float(altura_texto.get()) / 100  # Convertendo altura de CM para metros
    imc = peso / (altura ** 2)
    messagebox.showinfo("IMC", "Seu IMC é {:.2f}".format(imc))

def finalizar_app():
    messagebox.showinfo("Finalizar", "Finalizando o aplicativo...")
    janela.destroy()

# Interface gráfica
janela = tk.Tk()
janela.title("Fit System")


# Labels e entradas
tk.Label(janela, text="Seja bem vindo a sua mudança de vida ").pack()

tk.Label(janela, text="Digite seu nome:").pack()
nome_texto = tk.Entry(janela)
nome_texto.pack()

tk.Label(janela, text="Digite sua idade:").pack()
idade_texto = tk.Entry(janela)
idade_texto.pack()

tk.Label(janela, text="Digite seu peso:").pack()
peso_texto = tk.Entry(janela)
peso_texto.pack()

tk.Label(janela, text="Digite sua altura em CM:").pack()
altura_texto = tk.Entry(janela)
altura_texto.pack()

# Botão de cálculo de IMC
button_calcular_imc = ttk.Button(janela, text="Calcular IMC", style='TButton', command=calcular_imc)
button_calcular_imc.pack(pady=5)  # Adiciona um pequeno espaço vertical entre o botão e a entrada de altura

tk.Label(janela, text="Você possui algum destes problemas de saúde?").pack()
doenca_var = tk.IntVar()
tk.Radiobutton(janela, text="Diabetes", variable=doenca_var, value=1).pack()
tk.Radiobutton(janela, text="Colesterol", variable=doenca_var, value=2).pack()
tk.Radiobutton(janela, text="Pressão Alta", variable=doenca_var, value=3).pack()
tk.Radiobutton(janela, text="N/A", variable=doenca_var, value=4).pack()

# Botão de cálculo de dieta e finalizar app
tk.Button(janela, text="Calcular Dieta", command=calcular_dieta).pack()
tk.Button(janela, text="Finalizar APP", command=finalizar_app).pack()

janela.mainloop()