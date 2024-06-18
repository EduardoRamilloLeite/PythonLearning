#o log (ou registro) é usado para registrar informações importantes durante a execução de um programa.
#  Isso é particularmente útil para diagnóstico, monitoramento, depuração e rastreamento de eventos.
#  Os logs permitem aos desenvolvedores entender o comportamento do programa em diferentes cenários, identificar problemas e otimizar o desempenho.

#abstração
#log
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def log(self, msg): #assinatura do metodo
        raise NotImplementedError('Implemente o metodo log') 
    
    def log_error(self, msg):
        return self._log(f'Error:, {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):   #mixin é pra falar pra outros desenvolvedores para usarem essa herança
        def _log(self, msg):
            msg_formatada = f'{msg} ({self.__class__.__name__})'
            print('salvando no log:', msg_formatada)
            with open (LOG_FILE, 'a') as arquivo:
                arquivo.write(msg_formatada)
                arquivo.write('\n')
            

    
class LogPrintMixin(Log):   
        def _log(self, msg): #prescisa definir o metodo log
            print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('Que legal')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')
    
