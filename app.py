import tkinter as tk
from tkinter import ttk

class MonitorClima:
    def __init__(self, localizacao):
        self.__localizacao = localizacao

    def medir(self):
        raise NotImplementedError("Método medir deve ser implementado nas subclasses.")

    def exibir_resultados(self):
        raise NotImplementedError("Método exibir_resultados deve ser implementado nas subclasses.")

    def get_localizacao(self):
        return self.__localizacao

class MonitorTemperatura(MonitorClima):
    def __init__(self, estado, uf, temperatura):
        localizacao = f"{estado} ({uf})"
        super().__init__(localizacao)
        self.__temperatura = temperatura

    def medir(self):
        print(f"Medindo a temperatura no clima em {self.get_localizacao()}.")

    def exibir_resultados(self):
        print(f"Resultados do monitoramento de temperatura em {self.get_localizacao()}:")
        print(f"- Temperatura: {self.__temperatura}°C")

    def get_temperatura(self):
        return self.__temperatura

class MonitorUmidade(MonitorClima):
    def __init__(self, estado, uf, umidade):
        localizacao = f"{estado} ({uf})"
        super().__init__(localizacao)
        self.__umidade = umidade

    def medir(self):
        print(f"Medindo a umidade no clima em {self.get_localizacao()}.")

    def exibir_resultados(self):
        print(f"Resultados do monitoramento de umidade em {self.get_localizacao()}:")
        print(f"- Umidade: {self.__umidade}%")

    def get_umidade(self):
        return self.__umidade

dados_estados_2020 = {
   "Acre": {"uf": "AC", "temperatura": 25, "umidade": 75},
    "Alagoas": {"uf": "AL", "temperatura": 28, "umidade": 80},
    "Amapá": {"uf": "AP", "temperatura": 26, "umidade": 78},
    "Amazonas": {"uf": "AM", "temperatura": 30, "umidade": 85},
    "Bahia": {"uf": "BA", "temperatura": 29, "umidade": 75},
    "Ceará": {"uf": "CE", "temperatura": 31, "umidade": 82},
    "Distrito Federal": {"uf": "DF", "temperatura": 27, "umidade": 70},
    "Espírito Santo": {"uf": "ES", "temperatura": 28, "umidade": 75},
    "Goiás": {"uf": "GO", "temperatura": 30, "umidade": 72},
    "Maranhão": {"uf": "MA", "temperatura": 32, "umidade": 79},
    "Mato Grosso": {"uf": "MT", "temperatura": 29, "umidade": 73},
    "Mato Grosso do Sul": {"uf": "MS", "temperatura": 28, "umidade": 74},
    "Minas Gerais": {"uf": "MG", "temperatura": 26, "umidade": 68},
    "Pará": {"uf": "PA", "temperatura": 27, "umidade": 77},
    "Paraíba": {"uf": "PB", "temperatura": 29, "umidade": 80},
    "Paraná": {"uf": "PR", "temperatura": 23, "umidade": 65},
    "Pernambuco": {"uf": "PE", "temperatura": 31, "umidade": 78},
    "Piauí": {"uf": "PI", "temperatura": 30, "umidade": 77},
    "Rio de Janeiro": {"uf": "RJ", "temperatura": 28, "umidade": 74},
    "Rio Grande do Norte": {"uf": "RN", "temperatura": 30, "umidade": 81},
    "Rio Grande do Sul": {"uf": "RS", "temperatura": 22, "umidade": 68},
    "Rondônia": {"uf": "RO", "temperatura": 26, "umidade": 76},
    "Roraima": {"uf": "RR", "temperatura": 27, "umidade": 79},
    "Santa Catarina": {"uf": "SC", "temperatura": 24, "umidade": 70},
    "São Paulo": {"uf": "SP", "temperatura": 26, "umidade": 68},
    "Sergipe": {"uf": "SE", "temperatura": 29, "umidade": 76},
    "Tocantins": {"uf": "TO", "temperatura": 29, "umidade": 75},
}


def obter_dados_monitoramento(estado):
    dados_estado = dados_estados_2020.get(estado)
    if dados_estado:
        uf = dados_estado.get("uf")
        temperatura = dados_estado.get("temperatura")
        umidade = dados_estado.get("umidade")
        return MonitorTemperatura(estado, uf, temperatura), MonitorUmidade(estado, uf, umidade)
    else:
        print(f"Dados de monitoramento para o estado de {estado} não encontrados.")
        return None, None

class MonitorClimaApp:
    def __init__(self, root):
        self.__root = root
        self.__root.title("Monitor de Clima")

        self.__estado_label = ttk.Label(root, text="Escolha o estado:")
        self.__estado_combobox = ttk.Combobox(root, values=list(dados_estados_2020.keys()))
        self.__obter_dados_button = ttk.Button(root, text="Obter Dados", command=self.exibir_dados)
        self.__resultados_text = tk.Text(root, height=10, width=40)

        self.__imagem_label = ttk.Label(root)
        self.carregar_imagem("mapa-brasil.png")  

        self.__estado_label.pack(pady=10)
        self.__estado_combobox.pack(pady=10)
        self.__obter_dados_button.pack(pady=10)
        self.__resultados_text.pack(pady=10)
        self.__imagem_label.pack(pady=10)

    def exibir_dados(self):
        estado_selecionado = self.__estado_combobox.get()
        monitor_temperatura, monitor_umidade = obter_dados_monitoramento(estado_selecionado)
        
        if monitor_temperatura and monitor_umidade:
            monitor_temperatura.medir()
            monitor_temperatura.exibir_resultados()
            monitor_umidade.medir()
            monitor_umidade.exibir_resultados()

            resultados = f"\nResultados para {estado_selecionado} ({dados_estados_2020[estado_selecionado]['uf']}):"
            resultados += f"\n- Temperatura: {monitor_temperatura.get_temperatura()}°C"
            resultados += f"\n- Umidade: {monitor_umidade.get_umidade()}%"

            self.__resultados_text.delete(1.0, tk.END)
            self.__resultados_text.insert(tk.END, resultados)
        else:
            self.__resultados_text.delete(1.0, tk.END)
            self.__resultados_text.insert(tk.END, f"Dados de monitoramento para o estado de {estado_selecionado} não encontrados.")

    def carregar_imagem(self, nome_imagem):
        caminho = f"{nome_imagem}"
        try:
            imagem = tk.PhotoImage(file=caminho)
            self.__imagem_label.configure(image=imagem)
            self.__imagem_label.image = imagem
        except tk.TclError:
            print(f"Erro ao carregar a imagem: {caminho}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MonitorClimaApp(root)
    root.mainloop()
