"""Módulo contendo as informações de um celular"""
from typing import Union
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Float, Boolean

from model import Base

# pylint: disable=R0902:too-many-instance-attributes
# pylint: disable=R0903:too-few-public-methods
class Mobile(Base):
    """Classe representando o modelo de um Celular para salvar no banco"""
    __tablename__ = 'mobiles'

    id = Column(Integer, primary_key=True)
    battery_power = Column("Battery_power", Integer)
    blue = Column("Blue", Boolean)
    clock_speed = Column("Clock_speed", Float)
    date_insert = Column(DateTime, default=datetime.now())
    dual_sim = Column("Dual_sim", Boolean)
    fc = Column("Fc", Integer)
    four_g = Column("Four_g", Boolean)
    int_memory = Column("Int_memory", Integer)
    m_dep = Column("M_dep", Float)
    manufacturer = Column("Manufacturer", String(50))
    mobile_wt = Column("Mobile_wt", Integer)
    model= Column("Model", String(50))
    n_cores = Column("N_cores", Integer)
    pc = Column("Pc", Integer)
    price_range_predicted = Column("Price_range_predicted", Integer, nullable=True)
    price_final = Column("Price_final", Float, nullable=True)
    px_height = Column("Px_height", Integer)
    px_width = Column("Px_width", Integer)
    ram = Column("Ram", Integer)
    sc_h = Column("Sc_h", Integer)
    sc_w = Column("Sc_w", Integer)
    talk_time = Column("Talk_time", Integer)
    three_g = Column("Three_g", Boolean)
    touch_screen = Column("Touch_screen", Boolean)
    wifi = Column("Wifi", Boolean)

    # pylint: disable=R0913:too-many-arguments
    # pylint: disable=R0914:too-many-locals
    def __init__(self, battery_power:int, blue:bool, clock_speed:float, dual_sim:bool,
                 fc:int, four_g:bool, int_memory:int,
                 m_dep:float, manufacturer:str, mobile_wt:int,
                 model:str, n_cores:int, pc:int,
                 price_range_predicted:int, price_final:float, px_height:int,
                 px_width:int, ram:int, sc_h:int, sc_w:int,
                 talk_time:int, three_g:bool, touch_screen:bool, wifi:bool,
                 date_insert:Union[DateTime, None] = None):
        """
        Cria um Celular

        Arguments:
        battery_power: Total de energia da bateria em mAh.
        blue: Se possui bluetooth.
        clock_speed: Velocidade do microprocessador do celular em GHz.
        date_insert: Data de quando o celular foi inserido à base.
        dual_sim: Se o celular suporta dois sims (Chips).
        fc: Mega pixels da câmera frontal.
        four_g: Se possui 4G.
        int_memory: Memória interna em GB (Gigabytes).
        m_dep: Profundidade do Celular em cm (centímetros).
        manufacturer: Fabricante do celular (Ex: Samsung, Motorola).
        mobile_wt: Peso do celular em gramas.
        model: Modelo do celular (Ex: Galaxy A11, Moto G5).
        n_cores: Números de núcleos do processador.
        pc: Mega pixels da câmera principal.
        price_range_predicted: Alcance de preço predito. 
        (0 - Baixo Custo, 1 - Médio Custo, 2 - Alto Custo, 3 - Muito Alto Custo).
        price_final: Preço final decidido pelo varejista.
        px_height: Altura da resolução em pixels.
        px_width: Largura da resolução em pixels.
        ram: Memória RAM em MB (Megabytes).
        sc_h: Altura da tela do celular em cm (centímetros).
        sc_w: Largura da tela do celular em cm (centímetros);
        talk_time: Maior tempo que uma única carga de bateria irá durar durante uma ligação.
        three_g: Se possui 3G.
        touch_screen: Se possui tela sensível a toque.
        wifi: Se possui Wi-fi.
        """

        self.battery_power = battery_power
        self.blue = blue
        self.clock_speed = clock_speed
        self.date_insert = date_insert
        self.dual_sim = dual_sim
        self.fc = fc
        self.four_g = four_g
        self.int_memory = int_memory
        self.m_dep = m_dep
        self.manufacturer = manufacturer
        self.mobile_wt = mobile_wt
        self.model = model
        self.n_cores = n_cores
        self.pc = pc
        self.price_range_predicted = price_range_predicted
        self.price_final = price_final
        self.px_height = px_height
        self.px_width = px_width
        self.ram = ram
        self.sc_h = sc_h
        self.sc_w = sc_w
        self.talk_time = talk_time
        self.three_g = three_g
        self.touch_screen = touch_screen
        self.wifi = wifi

        # se não for informada, será o data exata da inserção no banco
        if date_insert:
            self.date_insert = date_insert
