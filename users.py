import json

from app_interface import Komunikaty


class Users:
    def __init__(self):
        self.USERS_FILE = 'users.json'
        self.vip_users: list = []
        self.officials: list = []
        self.read_users()

    def read_users(self):
        try:
            with open(self.USERS_FILE, 'r') as plik:
                users_dict = json.loads(plik.read())
            self.officials = users_dict['officials']
            self.vip_users = users_dict['vip_users']
        except:
            print(Komunikaty.config_file_error(self.USERS_FILE))

    def write_users(self):
        """Funkcja dodatkowa do tworzenia pliku 'users.json'."""
        with open(self.USERS_FILE, 'w') as file:
            users_dict = {
                'officials': self.officials,
                'vip_users': self.vip_users
            }
            json.dump(users_dict, file, indent=2)
        print('Zapisano plik użytkowników.')

    def is_vip(self, password: str) -> bool:
        for vip in self.vip_users:
            if vip.get('password') == password:
                return True
        return False

    def is_official(self, password: str) -> bool:
        for official in self.officials:
            if official.get('password') == password:
                return True
        return False

    def get_vip_level(self, password) -> int:
        for vip in self.vip_users:
            if vip.get('password') == password:
                return vip.get('vip_level', 1)
        return 0

    def get_official_username(self, password) -> str:
        for official in self.officials:
            if official['password'] == password:
                return official.get('username', '???')
        return ''


if __name__ == '__main__':
    users = Users()
    print('Test weryfikacji odczytanych użytkowników:\n')
    for i in users.officials:
        print(users.is_official(i['password']), i)
    for i in users.vip_users:
        print(users.is_vip(i['password']), i)
