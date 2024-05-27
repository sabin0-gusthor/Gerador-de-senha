import string
import tkinter as tk
from tkinter import ttk
import random
import pyperclip  # Certifique-se de ter o pacote pyperclip instalado para instaçar use o pip intall pyperclip

print("Script iniciado") 

class GeradorDeSenha:
    def __init__(self, root):
        try:
            print("Iniciando a classe GeradorDeSenha")  
            self.root = root
            self.root.title("Gerador de Senha")
            
            # Configurar a interface do usuário
            self.create_widgets()
            print("Widgets criados")  
        except Exception as e:
            print(f"Erro na inicialização: {e}")

    def create_widgets(self):
        try:
            print("Criando widgets")  
            # Frame principal
            main_frame = ttk.Frame(self.root, padding="10")
            main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
            
            # Configurar expansão do frame principal
            self.root.columnconfigure(0, weight=1)
            self.root.rowconfigure(0, weight=1)
            main_frame.columnconfigure(0, weight=1)
            main_frame.columnconfigure(1, weight=1)
            
            # Título
            ttk.Label(main_frame, text="Gerador de Senha", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=10)
            
            # Label para comprimento da senha
            ttk.Label(main_frame, text="Tamanho da Senha:").grid(row=1, column=0, sticky=tk.W)
            
            # Combobox para comprimento da senha
            self.length_var = tk.StringVar(value='14')
            self.length_combobox = ttk.Combobox(main_frame, textvariable=self.length_var, values=['10', '12', '14', '16', '18', '20'])
            self.length_combobox.grid(row=1, column=1, sticky=(tk.W, tk.E))
            
            # Checkbox para usar caracteres especiais
            self.use_special_chars_var = tk.BooleanVar(value=True)
            self.special_chars_checkbutton = ttk.Checkbutton(main_frame, text="Usar caracteres especiais", variable=self.use_special_chars_var)
            self.special_chars_checkbutton.grid(row=2, column=0, columnspan=2, pady=5)
            
            # Botão para gerar senha
            generate_button = ttk.Button(main_frame, text="Gerar Senha", command=self.generate_password)
            generate_button.grid(row=3, column=0, columnspan=2, pady=5)
            
            # Campo para exibir a senha gerada
            self.result_var = tk.StringVar()
            self.result_entry = ttk.Entry(main_frame, textvariable=self.result_var, state='readonly', font=("Helvetica", 12))
            self.result_entry.grid(row=4, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
            
            # Botão para copiar senha
            copy_button = ttk.Button(main_frame, text="Copiar Senha", command=self.copy_password)
            copy_button.grid(row=5, column=0, columnspan=2, pady=5)
            print("Widgets criados com sucesso")  
        except Exception as e:
            print(f"Erro ao criar widgets: {e}")

    def generate_password(self):
        try:
            print("Gerando senha")  
            length = int(self.length_var.get())
            use_special_chars = self.use_special_chars_var.get()
            
            special_chars = '$&@!?%#' if use_special_chars else ''
            all_chars = string.ascii_letters + string.digits + special_chars
            password = ''.join(random.choice(all_chars) for _ in range(length))
            
            self.result_var.set(password)
            print(f"Senha gerada: {password}")  
        except Exception as e:
            print(f"Erro ao gerar senha: {e}")
    
    def copy_password(self):
        try:
            print("Copiando senha") 
            pyperclip.copy(self.result_var.get())
            print("Senha copiada")  
        except Exception as e:
            print(f"Erro ao copiar senha: {e}")

if __name__ == "__main__":
    try:
        print("Inicializando o Tkinter")  
        root = tk.Tk()
        app = GeradorDeSenha(root)
        print("Iniciando o loop principal")  
        root.mainloop()
    except Exception as e:
        print(f"Erro no loop principal: {e}")