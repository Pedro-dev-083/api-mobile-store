"""Módulo contendo as funções para predizer"""
import pickle

class Preditor:
    """Classe contendo os métodos para predizer"""
    def __init__(self):
        self.model = None

    def carrega_modelo(self, path):
        """
        Dependendo do final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                self.model = pickle.load(file)
        else:
            raise ValueError('Formato de arquivo não suportado')

    def predizer(self, x_input):
        """
        Realiza a predição de um paciente com base no modelo treinado
        """
        if self.model is None:
            raise RuntimeError('O modelo não foi carregado')

        diagnosis = self.model.predict(x_input)
        return diagnosis
