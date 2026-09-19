# Importa o módulo responsável por trabalhar com threads.
import threading


# Define a metaclasse responsável por transformar uma classe em um Singleton.
class SingletonMeta(type):

    # Dicionário que armazenará as instâncias das classes (variável global).
    _instancias = {}

    # Lock utilizado para proteger a criação das instâncias.
    _lock = threading.Lock()

    # O método __call__ é executado quando fazemos: MinhaClasse()
    def __call__(cls, *args, **kwargs):

        # Adquire o Lock antes de verificar/criar a instância.
        with cls._lock:

            # Verifica se a classe ainda não possui uma instância.
            if cls not in cls._instancias:

                # Cria a instância utilizando o comportamento normal da metaclasse.
                cls._instancias[cls] = super().__call__(*args, **kwargs)

            # Retorna a instância armazenada.
            return cls._instancias[cls]