from common import AREA_MAP

class IdValidator:
    """Identify personal id

    The first code of id must be an alphabet.
    The second code must be 1 or 2.
    """

    MULTIPLE_NUM = (1, 1, 1, 2, 0, 8, 6, 3, 1, 5, 8)

    def validate(self, personal_id):
        if len(personal_id) != 10:
            return False
        if not personal_id[0].isalpha():
            return False
        if not personal_id[1:].isdigit():
            return False
        if personal_id[1] != '1' and personal_id[1] != '2':
            return False
        # generate multiple codes
        multiple_codes = []
        multiple_codes.extend(AREA_MAP.get(personal_id[0]))
        for code in personal_id[1:]:
            multiple_codes.append(int(code))
        multiple_sum = 0
        for multiple_code, code in zip(multiple_codes, self.MULTIPLE_NUM):
            multiple_sum += multiple_sum * code
        return multiple_sum % 10 == 0

if __name__ == '__main__':
    test_id = 'B120863158'
    validator = IdValidator()
    print(validator.validate(test_id))