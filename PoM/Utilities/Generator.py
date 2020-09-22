import random
import string


class randomGen:

    def __init__(self, charlength: int):
        self.charlen = charlength

    def randomChar(self) -> str:
        return ''.join(random.choice(string.ascii_letters) for _ in range(self.charlen))

    def random_email(self) -> str:
        return self.randomChar()+"@paymark.co.nz"

    def random_password(self):
        return self.randomChar()


print(randomGen(7).random_password())
