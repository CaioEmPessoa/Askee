from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QMessageBox, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from windows.telaposts import Ui_MainWindow
from modules.post import post
from modules.criarpost import criarpost
import os, sys

# Importa as classes de comunicação com as APIs do módulo AskeeRequests
from AskeeRequests import PostRequests, UsersRequests

class telaposts(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaposts, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # 1. Inicializa as instâncias das APIs de Posts e Utilizadores
        self.api_posts = PostRequests()
        self.api_users = UsersRequests()
        
        # 2. Cache local em memória para evitar requisições repetidas ao mesmo ID de utilizador
        self.user_cache = {}
        
        # 3. Configura dinamicamente o container onde a lista de posts será exibida
        self.posts_layout = None
        self.configurar_layout_posts()
        
        # 4. Conexões originais dos botões da tua janela principal
        self.ui.main_butt_post.clicked.connect(self.post)
        self.ui.main_butt_criarpost.clicked.connect(self.tela_criar_post)
        
        # 5. Efetua o carregamento automático dos posts ao abrir a tela
        self.carregar_feed()

    def configurar_layout_posts(self):
        """Define o local de renderização dos posts. Cria uma ScrollArea dinâmica caso 

        a interface original contenha apenas os mockups estáticos do Designer.
        """
        if hasattr(self.ui, 'verticalLayout'):
            self.posts_layout = self.ui.verticalLayout
            self.posts_layout.setAlignment(QtCore.Qt.AlignTop)
        else:
            # Caso a UI use posicionamento absoluto ou não exponha o verticalLayout,
            # criamos uma área de rolagem acoplada à aba principal ('main_tab')
            target_widget = getattr(self.ui, 'main_tab', self.ui.centralwidget)
            
            self.scroll_area = QScrollArea(target_widget)
            self.scroll_area.setWidgetResizable(True)
            self.scroll_area.setStyleSheet("background-color: #000000; border: none;")
            
            self.scroll_widget = QWidget()
            self.scroll_widget.setStyleSheet("background-color: #000000;")
            self.posts_layout = QVBoxLayout(self.scroll_widget)
            self.posts_layout.setAlignment(QtCore.Qt.AlignTop)
            self.scroll_area.setWidget(self.scroll_widget)
            
            # Oculta os elementos estáticos de exemplo desenhados no Qt Designer para não sobrepor
            componentes_antigos = ['main_label_icon', 'main_label_user', 'main_label_post', 'main_butt_post']
            for comp in componentes_antigos:
                if hasattr(self.ui, comp):
                    getattr(self.ui, comp).hide()
            
            # Ajusta o posicionamento da lista dinâmica dentro do ecrã
            if target_widget.layout():
                target_widget.layout().addWidget(self.scroll_area)
            else:
                # Margem segura abaixo dos botões de busca/criação superiores
                self.scroll_area.setGeometry(20, 140, 860, 520)

    def post(self):
        self.window = post()
        self.window.show()

    def tela_criar_post(self):
        add = criarpost()
        if add.exec_():
            self.carregar_feed() # Recarrega a lista se um post novo for criado

    def carregar_feed(self):
        """Solicita os posts ao backend usando a tua classe base de requisições"""
        try:
            resposta = self.api_posts.get_all()
            
            # Validação e extração do array de posts dependendo do envelope do JSON
            if resposta and isinstance(resposta, dict) and "data" in resposta:
                lista_de_posts = resposta["data"]
            elif isinstance(resposta, list):
                lista_de_posts = resposta
            else:
                lista_de_posts = []
                
            if lista_de_posts:
                self.popular_interface_com_posts(lista_de_posts)
            else:
                print("Aviso: A API de posts retornou um feed vazio.")
        except Exception as e:
            print(f"Erro crítico ao conectar à API de Posts: {e}")

    def popular_interface_com_posts(self, posts):
        """Limpa o container e renderiza os novos cards do feed do mais recente ao antigo"""
        if self.posts_layout is None:
            return

        # Limpeza absoluta de qualquer widget remanescente no layout
        while self.posts_layout.count():
            item = self.posts_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        
        # Percorre o feed de trás para a frente (mais recentes primeiro)
        for p in reversed(posts):
            user_id = p.get('userId') or p.get('user_id') or p.get('authorId') or p.get('author_id')
            
            # Valores de contingência recolhidos do próprio corpo do post
            usuario_nome = p.get('username') or p.get('author') or p.get('user') or "Anônimo"
            icone = p.get('userIcon') or p.get('icon') or ":)"
            
            if user_id:
                # Verifica cache para poupar processamento e rede
                if user_id in self.user_cache:
                    user_info = self.user_cache[user_id]
                    usuario_nome = user_info.get('username') or user_info.get('name') or usuario_nome
                    icone = user_info.get('icon') or icone
                else:
                    try:
                        res = self.api_users.get_request(path=str(user_id))
                        dados_user = res.jsonResponse
                        
                        user_info = dados_user.get('data') if isinstance(dados_user, dict) and 'data' in dados_user else dados_user
                        if user_info and isinstance(user_info, dict):
                            self.user_cache[user_id] = user_info
                            usuario_nome = user_info.get('username') or user_info.get('name') or usuario_nome
                            icone = user_info.get('icon') or icone
                    except Exception:
                        # Em caso de falha na requisição HTTP/JSON do utilizador, 
                        # o programa ignora silenciosamente mantendo os dados de contingência locais.
                        pass
            
            titulo = p.get('title', 'Sem título')
            
            # Instancia o card de post estilizado
            frame_post = self.criar_widget_de_post(icone, usuario_nome, titulo)
            self.posts_layout.addWidget(frame_post)

    def criar_widget_de_post(self, icon, user, title):
        """Gera em runtime os frames visuais baseados na paleta do terminal (Preto/Verde)"""
        frame = QFrame()
        frame.setMinimumSize(QtCore.QSize(300, 110))
        frame.setMaximumSize(QtCore.QSize(16777215, 141))
        frame.setStyleSheet("border: 1px solid #00ff00; background-color: #000000; font: 10pt \"Consolas\";")
        layout = QHBoxLayout(frame)
        
        # --- Bloco Lateral do Ícone ---
        frame_icon = QFrame()
        frame_icon.setMaximumSize(QtCore.QSize(60, 100))
        frame_icon.setStyleSheet("border: none;")
        layout_icon = QVBoxLayout(frame_icon)
        layout_icon.setContentsMargins(0, 0, 0, 0)
        
        label_icon = QLabel(str(icon))
        label_icon.setMinimumSize(QtCore.QSize(50, 50))
        label_icon.setMaximumSize(QtCore.QSize(50, 50))
        label_icon.setStyleSheet("border: 1px solid #00ff00; color: #00ff00; font: 14pt \"Consolas\";")
        label_icon.setAlignment(QtCore.Qt.AlignCenter)
        layout_icon.addWidget(label_icon)
        layout.addWidget(frame_icon)
        
        # --- Bloco Central de Informação (Autor e Conteúdo) ---
        frame_text = QFrame()
        frame_text.setStyleSheet("border: none;")
        layout_text = QVBoxLayout(frame_text)
        layout_text.setContentsMargins(5, 0, 5, 0)
        
        label_user = QLabel(str(user))
        label_user.setStyleSheet("color: #00ff00; font: bold 11pt \"Consolas\"; border: none;")
        layout_text.addWidget(label_user)
        
        label_title = QLabel(str(title))
        label_title.setStyleSheet("font: 13pt \"Consolas\"; text-decoration: underline; color: #00ff00; border: none;")
        label_title.setWordWrap(True)
        layout_text.addWidget(label_title)
        layout.addWidget(frame_text)
        
        # --- Botão de Transição (">") ---
        btn_go = QPushButton(">")
        btn_go.setMinimumSize(QtCore.QSize(35, 50))
        btn_go.setMaximumSize(QtCore.QSize(50, 60))
        btn_go.setStyleSheet("border: 1px solid #00ff00; font: 24pt \"Consolas\"; color: #00ff00; background-color: #000000;")
        btn_go.clicked.connect(self.post)
        layout.addWidget(btn_go)
        
        return frame