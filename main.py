try:
    class Human:
        def __init__(self, name, age, weight, height):
            name = 'mike'
            age = 21
            weight = 72
            height = 185

    class Worker(Human):
        def __init__(self):
            super().__init__()
            self.progress = 0
            self.gladness = 50
            self.alive = True

        def to_study(self):
            print('Time to study')
            self.progress += 2
            self.gladness -= 2

        def to_work(self):
            print('Time to work')
            self.progress += 1
            self.gladness -= 1

        def to_sleep(self):
            print('Time to sleep')
            self.gladness += 5

        def to_chill(self):
            print('Time to chill')
            self.gladness += 5
            self.progress -= 1

        def is_alive(self):
            if self.progress < -0.5:
                self.alive = False

            elif self.gladness <= 0:
                print('Depression')
                self.alive + False

        def end_of_day(self):
            print(f'Gladness = {self.gladness}')
            print(f'Progress = {self.progress}')

except:
    ('Something is wrong!')