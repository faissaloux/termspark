import termspark.termspark

class PrinterArgException(Exception):
    def __init__(self, position):
        self.position = position

    def __str__(self):
        message = termspark.TermSpark().spark_left([f" print_{self.position}() ", 'white', 'red'], [f" doesn't accept lists, maybe you wanna use ", 'red'], [f" spark_{self.position}() ", 'white', 'blue'])
        return str(message)