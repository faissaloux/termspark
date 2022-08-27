import termspark.termspark

class PrinterArgException(Exception):
    def __init__(self, position):
        self.position = position

    def __str__(self):
        termspark.TermSpark().line().spark()
        message = termspark.TermSpark().spark_left([f" print_{self.position}() ", 'white', 'red'], [f" doesn't accept lists, maybe you wanna use ", 'red'], [f" spark_{self.position}() ", 'white', 'blue'])
        message.spark()
        termspark.TermSpark().line().spark()
        return str(message)