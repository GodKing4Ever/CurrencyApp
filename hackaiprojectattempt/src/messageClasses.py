from uagents import Model

class hasChanged(Model):
    change: bool

class ValuesFinal(Model):
    valDict: dict
    additional: str
