import os
from time import sleep


def cls():  # Czyszczenie okna terminala.
    os.system('cls' if os.name == 'nt' else 'clear')


class Komunikaty:
    @staticmethod
    def config_file_error(file_name: str = ""):
        return ("\n.U.W.A.G.A.!!!"
                f"\nProgram nie wykrył prawidłowego pliku konfiguracyjnego"
                f"{' ' + file_name if len(file_name) else file_name}!"
                "\nBrak mozliwości zalogowania się jako urzędnik lub VIP!")

    @staticmethod
    def get_letter_or_password(user: str = ""):
        return input(f"\nWitaj{' ' + user if len(user) else ''}, wybierz literę kolejki:\n"
                     "A: Rejestracja pojazdów\n"
                     "B: Prawa Jazdy\n"
                     "C: Dowody Osobiste\n")

    @staticmethod
    def print_new_number(queue: str, number: int, vip_name: str = ""):
        print(f"Twoj numerek{' VIP' if len(vip_name) else ''} to {queue.upper()}.{number}")
        sleep(1)  # Czekaj x sekund
        cls()  # Wyczyść okno. (Nie działa w PyCharm!)

    @staticmethod
    def print_wrong_queue_name():
        print("Nieprawidlowa nazwa kolejki!")

    @staticmethod
    def print_empty_queue_info():
        print("Kolejka jest pusta. Możesz iść na kawę :)")

    @staticmethod
    def official_print_handled_number(queue: str, number: int, user: str = ""):
        print(f"Urzedniku{' ' + user if len(user) else ''}, obslugujesz teraz {queue}.{number}")
        sleep(1)  # Czekaj x sekund
        cls()  # Wyczyść okno. (Nie działa w PyCharm!)

    @staticmethod
    def official_get_queue_name():
        return input("\nWybierz kolejkę, którą chcesz obsłużyć: ").upper()


if __name__ == "__main__":
    print("Te funkcje odpowiadają za wuświetlanie użytkownikowi komunikatów.")
