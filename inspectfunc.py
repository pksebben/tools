import inspect
import logging
logging.basicConfig()
logger = logging.getLogger()


def unravel():
    for i in inspect.stack():
        print(f"{i.filename}::{i.function}:{i.lineno}")

def print_caller():
    frame = inspect.stack()[1]
    caller = f"{frame.filename}::{frame.function}:{frame.lineno}"
    print(caller)



if __name__ == "__main__":
    def layerone():
        layertwo()

    def layertwo():
        layerthree()

    def layerthree():
        unravel()

    layerone()
