class CalorieCalculator:
    def __init__(self, user):
        self.user = user

    def calculate_bmr(self):
        if self.user.gender == "Laki-laki":
            return 10 * self.user.weight + 6.25 * self.user.height - 5 * self.user.age + 5
        else:
            return 10 * self.user.weight + 6.25 * self.user.height - 5 * self.user.age - 161

    def calculate_daily_calories(self):
        bmr = self.calculate_bmr()
        activity_multiplier = {
            "Sedentari (tidak aktif)": 1.2,
            "Ringan (olahraga ringan 1-3 hari/minggu)": 1.375,
            "Sedang (olahraga sedang 3-5 hari/minggu)":  1.55,
            "Tinggi (olahraga berat 6-7 hari/minggu)": 1.725,
        }
        return bmr * activity_multiplier[self.user.activity_level]