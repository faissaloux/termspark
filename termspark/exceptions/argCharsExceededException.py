import termspark.termspark

class ArgCharsExceededException(Exception):
    def __init__(self, arg, max):
        self.arg = arg
        self.max = max

    def __str__(self):
        termspark.TermSpark().line().spark()
        message = termspark.TermSpark().print_left(f"Sorry, {self.arg} can contain only {self.max} character", 'red')
        message.spark()
        termspark.TermSpark().line().spark()
        return str(message)