"""Módulo para avaliar o modelo"""
from sklearn.metrics import accuracy_score
from model.preditor import Preditor

# pylint: disable=R0903:too-few-public-methods
class Avaliador:
    """Classe para avaliar o modelo"""
    def avaliar(self, preditor:Preditor, x_test, y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predicoes = preditor.predizer(x_test)

        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return accuracy_score(y_test, predicoes)
