import json
import re

from app_interface import Komunikaty


class Users:
    def __init__(self):
        self.USERS_FILE = 'users.txt'
        self.officials_str = ''
        self.vip_users_str = ''
        self.vip_users: list = []
        self.officials: list = []
        self.read_users()

    def read_users(self):
        try:
            with open('users.txt', 'r') as plik:
                off = 0
                vip = 0
                for line in plik:
                    if re.match('officials', line) is not None:
                        off = 1
                        vip = 0
                    if off:
                        self.officials_str += line.replace('\n', '')
                    if ']' in line:
                        off = 0

                    if re.match('vip_users', line) is not None:
                        off = 0
                        vip = 1
                    if vip:
                        self.vip_users_str += line.replace('\n', '')
                    if ']' in line:
                        vip = 0

            self.officials = json.loads('[' + self.officials_str.split('[')[1])
            self.vip_users = json.loads('[' + self.vip_users_str.split('[')[1])

        except:
            print(Komunikaty.config_file_error(self.USERS_FILE))

    def write_users(self):
        """Funkcja dodatkowa do tworzenia pliku 'users.txt'."""
        with open('users.txt', 'w') as file:
            file.write('officials = ')
            json.dump(self.officials, file, indent=4)
            file.write('\n\nvip_users = ')
            json.dump(self.vip_users, file, indent=4)
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
