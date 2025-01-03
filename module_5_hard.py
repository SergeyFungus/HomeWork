import time


class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return f'{self.nickname}'


class Video:

    def __init__(self, title: str, duration: int, adult_mode=bool(False)):
        super().__init__()
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return f'{self.title}'

    def dur(self):
        return self.duration


class UrTube:

    def __init__(self):

        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: int):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i
                return self.current_user

    def register(self, nickname: str, password: int, age: int):
        Nuser = User(nickname, password, age)
        if Nuser not in self.users:
            self.users.append(Nuser)
            self.log_out()
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)
            else:
                print(f'Видео с названием {i.title} уже существует')

    def get_videos(self, text):
        listOfVideos = []
        for i in self.videos:
            if text.lower() in i.title.lower():
                listOfVideos.append(str(i))
        return listOfVideos

    def watch_video(self, video):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for i in self.videos:
                if video in i.title:
                    dur = Video.dur(i)
                    for k in range(1, dur + 1):
                        print(k, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Какой язык программирования выбрать для разработчика', 200)
    v2 = Video('Для чего нужны программы?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('выбрать'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего нужны программы?')
    ur.register('ivanov_ivan', 'kipr5723link', 13)
    ur.watch_video('Для чего нужны программы?')
    ur.register('Genna', 'lkasdlFGkjsdhe4rfdrde5', 25)
    ur.watch_video('Для чего нужны программы?')

    # Проверка входа в другой аккаунт
    ur.register('ivanov_ivan', 'Gdfgs34ASEG45zsgds5z', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Какой язык программирования выбрать для разработчика????')