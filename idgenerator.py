import random
from common import AREA_MAP
from idvalidator import IdValidator


class IdGenerator:

    def __init__(self):
        self._generated_ids = set()
        self._id_validator = IdValidator()

    def generate(self, area_codes=list(AREA_MAP.keys())):
        while True:
            # pick an area code
            area_code = random.choice(area_codes)
            # pick gender code
            gender_code = random.randint(1, 2).__str__()
            codes = [area_code, gender_code]
            for _ in range(8):
                codes.append(random.randint(0, 9).__str__())
            codes = ''.join(codes)
            if self._id_validator.validate(codes) and codes not in self._generated_ids:
                return codes

if __name__ == '__main__':
    generator = IdGenerator()
    print(generator.generate(['L']))