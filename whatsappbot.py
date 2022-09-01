from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = " Bom dia pessoal, veja o video que acabou de sair https://www.youtube.com"
        # Altere o nome dos grupos aqui
        self.grupos = ["nome_do_grupo"]
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "this is a test"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["nome_do_grupo"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        #<span dir="auto" title="Família" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Família</span>
        #<div tabindex="-1" class="p3_M1">
        #<span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(5)
            grupo.click()
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(5)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(5)
            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()