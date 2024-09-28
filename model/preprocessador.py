"""Módulo focado no pré-processamento dos dados"""
import numpy as np
from sklearn.model_selection import train_test_split

class PreProcessador:
    """
    Classe para realizar o pré-processamento dos 
    dados, vindo do front, antes de utilizá-los para 
    poder predizer.
    """

    def separa_teste_treino(self, dataset, percentual_teste, seed=7):
        """ Cuida de todo o pré-processamento. """
        # limpeza dos dados e eliminação de outliers

        # feature selection

        # divisão em treino e teste
        x_train, x_test, y_train, y_test = self.__preparar_holdout(dataset,
                                                                  percentual_teste,
                                                                  seed)
        # normalização/padronização

        return (x_train, x_test, y_train, y_test)

    def __preparar_holdout(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o método holdout.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """
        dados = dataset.values
        x = dados[:, 0:-1]
        y = dados[:, -1]
        return train_test_split(x, y, test_size=percentual_teste, random_state=seed)

    def preparar_form(self, form):
        """ Prepara os dados recebidos do front para serem usados no modelo. """
        x_input = np.array([
            form.battery_power,
            form.blue,
            form.clock_speed,
            form.dual_sim,
            form.fc,
            form.four_g,
            form.int_memory,
            form.m_dep,
            form.mobile_wt,
            form.n_cores,
            form.pc,
            form.px_height,
            form.px_width,
            form.ram,
            form.sc_h,
            form.sc_w,
            form.talk_time,
            form.three_g,
            form.touch_screen,
            form.wifi,
        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        x_input = x_input.reshape(1, -1)
        return x_input
