from app_interface import Komunikaty as k
from officeQueue import OfficeQueue
from users import Users

queues = {
    'A': OfficeQueue(),
    'B': OfficeQueue(),
    'C': OfficeQueue()
}

user = Users()

if __name__ == "__main__":
    while True:
        user_choice: list = k.get_letter_or_password().split()
        if len(user_choice) == 0:
            k.print_wrong_queue_name()
            continue
        if user_choice[0].upper() in queues.keys():
            q = queues[user_choice[0].upper()]
            new_number = q.push()
            k.print_new_number(user_choice[0], new_number)
        elif user.is_official(user_choice[0]):
            queue_letter_official = k.official_get_queue_name().upper()
            if queue_letter_official in queues.keys():
                q = queues[queue_letter_official]
                number = q.pop()
                if number is not None:
                    official_name = user.get_official_username(user_choice[0])
                    k.official_print_handled_number(queue_letter_official, number, official_name)
                else:
                    k.print_empty_queue_info()
            else:
                k.print_wrong_queue_name()
        elif user.is_vip(user_choice[0]):
            vip_level = user.get_vip_level(user_choice[0])
            if len(user_choice) > 1:
                queue_letter_vip = user_choice[1].upper()  # Drugi element listy to numer wybranej kolejki.
                if queue_letter_vip in queues.keys():
                    q = queues[queue_letter_vip]
                    new_number = q.push(vip_level)
                    k.print_new_number(queue_letter_vip, new_number, "VIP")
            else:
                k.print_wrong_queue_name()
        else:
            k.print_wrong_queue_name()
