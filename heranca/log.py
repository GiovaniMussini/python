from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'success: {msg}')


class LogFiliMixin(Log):
    def _log(self, msg):
        msg_format = (f'{msg} ({self.__class__.__name__})')
        with open(LOG_FILE, 'a+', encoding='utf8') as arquivo:
            arquivo.write(msg_format)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')



if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Erro no log')
    lp.log_success('Log feito com sucesso')
    lf = LogFiliMixin()
    lf.log_error('Erro no log')
    lf.log_success('Log feito com sucesso')
