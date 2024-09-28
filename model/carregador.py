"""Módulo para carregar um Dataframe"""
import pandas as pd

# pylint: disable=R0903:too-few-public-methods
class Carregador:
    """Classe para carregar um Dataframe"""

    def carregar_dados(self, url: str, atributos: list):
        """ Carrega e retorna um DataFrame. Há diversos parâmetros 
        no read_csv que poderiam ser utilizados para dar opções 
        adicionais.
        """

        return pd.read_csv(url, names=atributos, header=0,
                           skiprows=0, delimiter=',')
