from random import randrange

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton


personal_token = 'vk1.a.RQ0L9ImzVUBLnJ0jvDsnMgW1EjZlyBGHghvBXiBKpXtkYctv4X_UJBTnvasVrDGrsl1lPQrIAP-budDn4RsPYS2XhvrHwp8pgtoDmCxIizRHVuaXeEf-UoImbAwBr3mlMl_z5JkjPdvruCUyFO51GK8dU2KPvUKA0CQ16cppnhvA3Lvo7nJ_rX0V12cJ8j224LOiUJT1NoMmoha7ommtWA'

def filter_friends(partners_list):
    if not partners_list['is_friend'] and not partners_list['is_closed']:
        return True
    else:
        return False

personal_vk = vk_api.VkApi(token=personal_token)
token = 'vk1.a.tJsBcxT5vZEq8eIh-VMmuhJDeWdEoUm5Ziz8Mg524f-0CSIW7Bi4xXkHQLUeBdhXuv6n8A19umgV3onwGodtHrxnGt6mrvhjQQOPWPUSBrbbC0mgL9IKPmYJHsD1CS8B_7NRW9d5qabSxG3AAsHEbdj7iRGFFrXEDEQE1gocE2YYj9iLbby8RFI3-Nwflocrd9llPrW1k6EvLW774A-FpA'
# token = input('Token: ')
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)
first_keyboard = VkKeyboard()
active_keyboard = VkKeyboard()


testers = None


class VkBot:
    def __init__(self, personal_vk_token, vk_token):
        self.vk = vk_api.VkApi(token=vk_token)
        self.testers = []
        self.personal_vk = personal_vk_token
        self.hometown = ''
        self.partner_age = 0

    def next_partner(self):
        if self.testers is None or not self.testers:
            self.testers = \
            self.personal_vk.method('users.search',
                                    values={'count': 100, 'sex': 1, 'has_photo': 1,'hometown': self.hometown,'age_from': self.partner_age-1,'age_to': self.partner_age+1, 'fields': ['is_friend']})['items']
        self.testers = list(filter(filter_friends,self.testers))
        all_photos = []
        for image in self.personal_vk.method('photos.get',
                                   {'owner_id': self.testers[0]['id'],
                                    'album_id': "profile", "extended": "1"})['items']:
            all_photos.append([image["likes"]["count"], image["id"]])
        all_photos.sort()
        all_photos.reverse()
        best_images = []
        for image in all_photos[:3]:
            best_images.append(f"photo{self.testers[0]['id']}_{image[1]}")
        self.send_photos(event.user_id, attachment=",".join(best_images))
        self.write_msg(event.user_id, f'https://vk.com/id{self.testers[0]["id"]}')
        self.testers.pop(0)

    def send_photos(self, user_id, attachment):
        self.vk.method('messages.send', {'user_id': user_id, 'attachment': attachment, 'random_id': randrange(10 ** 7), })

    def write_msg(self,user_id, message):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), })

    def first_state(self):
        request = event.text
        if request.lower() == "начать":
            send_keyboard(event.user_id, 'Начинаем!', first_keyboard.get_keyboard())
        elif request.lower() == "привет":
            self.write_msg(event.user_id, f"Хай, {event.user_id}")
        elif request.lower() == "пока":
            self.write_msg(event.user_id, "Пока((")
        elif request.lower() == "подобрать":
            send_keyboard(event.user_id, 'Введите город для поиска', first_keyboard.get_empty_keyboard())
            # self.write_msg(event.user_id,'Введите город для поиска')
            id_and_state[str(event.user_id)]+= 1
            # self.next_partner()
        else:
            self.write_msg(event.user_id, "Не поняла вашего ответа...")

    def second_state(self):
        request = event.text
        self.hometown = request
        print(self.hometown)
        self.write_msg(event.user_id, 'Введите возраст партнера')
        id_and_state[str(event.user_id)]+= 1

    def third_state(self):
        request = event.text
        self.partner_age = int(request)
        print(self.partner_age)
        send_keyboard(event.user_id, 'Всё готово, можно начинать', active_keyboard.get_keyboard())
        id_and_state[str(event.user_id)] += 1


    def active_state(self):
        request = event.text
        if request.lower() == 'следующий':
            self.next_partner()
        elif request.lower() == 'выйти':
            id_and_state[str(event.user_id)] = 0
            send_keyboard(event.user_id, 'Начинаем!', first_keyboard.get_keyboard())


vkbot = VkBot(personal_vk,token)


def send_keyboard(user_id, message, keyboard):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),'keyboard': keyboard})

first_keyboard.add_button('Подобрать', VkKeyboardColor.PRIMARY)
first_keyboard.add_button('Автоподбор', VkKeyboardColor.PRIMARY)
first_keyboard.add_line()
first_keyboard.add_button('Показать избранное', VkKeyboardColor.PRIMARY)
first_keyboard.add_button('Показать заблокированных', VkKeyboardColor.PRIMARY)

active_keyboard.add_button('Следующий', VkKeyboardColor.PRIMARY)
active_keyboard.add_button('Выйти', VkKeyboardColor.PRIMARY)
active_keyboard.add_line()
active_keyboard.add_button('В избранное', VkKeyboardColor.PRIMARY)
active_keyboard.add_button('Заблокировать', VkKeyboardColor.PRIMARY)
active_keyboard.add_line()
active_keyboard.add_button('Лайк', VkKeyboardColor.PRIMARY)
active_keyboard.add_button('Дизлайк', VkKeyboardColor.PRIMARY)

id_and_state={
    '282135965': 0,
    '11617682' : 0,
    '512577409': 0
}

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            match id_and_state[str(event.user_id)]:
                case 0:
                    vkbot.first_state()
                case 1:
                    vkbot.second_state()
                case 2:
                    vkbot.third_state()
                case 3:
                    vkbot.active_state()