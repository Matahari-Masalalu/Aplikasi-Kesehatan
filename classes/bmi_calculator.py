class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        height_m = self.height / 100
        return self.weight / (height_m ** 2)

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Kekurangan berat badan"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Kelebihan berat badan"
        else:
            return "Obesitas"