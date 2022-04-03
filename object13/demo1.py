class Instrument():
    def make_sound(self):
        pass


class Erhu(Instrument):
    def make_sound(self):
        print('二胡在演奏')


class Pinao(Instrument):
    def make_sound(self):
        print('钢琴在演奏')


class Violin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')


class Bird():
    def make_sound(self):
        print('小鸟在叫')


# 演奏的函数
def play(instrument):
    instrument.make_sound()


if __name__ == '__main__':
    play(Erhu())
    play(Pinao())
    play(Violin())
    play(Bird())