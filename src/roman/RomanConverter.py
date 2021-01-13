class RomanConverter:
    def roman(self, number):
        rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        res = ''

        for i in range(0, len(arab)):
            while number >= arab[i]:
                res += rom[i]
                number -= arab[i]

        return res