import time

from botcity.web import Browser, By, WebBot
from uteis.tratamento_log.logger import loggin


class BotWeb:

    def __init__(self):
        self.bot = WebBot()
        self.logger = loggin()


    def config_navegador(self):

        browser = Browser.UNDETECTED_CHROME
        self.bot.browser = browser
        self.bot.headless = False


    def abrir_navegador(self):
        try:
            navegador = self.bot.start_browser()
            self.bot.wait(4000)

            self.logger.info("Navegador foi aberto!!")
            return navegador

        except ConnectionError as erro:
            self.logger.exception(f"Houve um erro de conexão!!: {erro}")
            raise

        except Exception as erro:
            self.logger.exception(f"Aconteceu um erro inesperado ao tentar abrir o navegador!!: {erro}")
            raise

class ClickCoockie(BotWeb):
    def __init__(self):
        super().__init__()


    def abertura_site(self):
        try:
            self.bot.wait(4000)
            site_jogo = self.bot.navigate_to("https://orteil.dashnet.org/cookieclicker/")
            self.bot.maximize_window()
            return site_jogo
            

        except ConnectionError:
            self.logger.error("Houve um erro de conexão na abertura do site")

        except Exception as erro:
            self.logger.exception(f"Houve um erro inesperado ao tentar abrir o site: {erro}")
            raise


    def selecao_idioma(self):
        try:
            self.bot.wait(3000)
            idioma = self.bot.find_element(
                selector="langSelect-PT-BR",
                by=By.ID
            )

            if not idioma:
                self.logger.error("Elemento de idioma não encontrado")
                return

            self.bot.wait_for_element_visibility(idioma)
            idioma.click()
            self.logger.info('Idioma PT-BR selecionado!!')
            return

        except ConnectionError:
                    self.logger.error("Houve um erro de conexão na abertura do site")
        
        except Exception as erro:
            self.logger.exception(f"Houve um erro inesperado ao tentar abrir o site: {erro}")
            raise


    def cliques(self):
        
        try:

            big_cockie = self.bot.find_element(
                selector="bigCookie",
                by=By.ID
            )

            if not big_cockie:
                self.logger.error("Não foi possivel achar o elemento")
                return

            self.bot.wait_for_element_visibility(big_cockie)
            self.logger.info("O robô começou a clicar")

            while True:
                big_cockie.click()
                time.sleep(0.2)

        except ConnectionError:
            self.logger.exception("Houve um erro de internet. O robô parou")
            return

        except Exception as erro:
            self.logger.exception(f"Houve um erro inesperado na clicagem do big cockie: {erro}")
            raise





site = BotWeb()
jogo = ClickCoockie()

jogo.config_navegador()
jogo.abrir_navegador()
jogo.abertura_site()
jogo.selecao_idioma()
jogo.cliques()


