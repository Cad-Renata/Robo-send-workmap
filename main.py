from controllers.email import Email
from controllers.config import Config


listEMail = ['renata.ferreira@cadmus.com.br']


def start():
    config = Config.get_config()
    e = Email(listEMail, config['email']['remetente'], config['email']['senha'])
    e.enviar_email()
    
if __name__ == '__main__':
    start()





