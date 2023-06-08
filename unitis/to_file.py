import json


def toFile(func):
    def warrap(*args, **kwargs):
        msg = func()(*args, **kwargs)
        with open("data/"+func().__name__+".json", "x") as f:
            f.write(json.dumps(msg, indent=4))
    return warrap
