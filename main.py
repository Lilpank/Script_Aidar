import os

import vk_api
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
VK_SESSION = vk_api.VkApi(token=ACCESS_TOKEN)
long_poll = VkLongPoll(VK_SESSION)

users = {142036975: "Глеб", }  # TODO: Дописать жертв.

abusive = ", ты ...!"  # TODO: Дописать самим ругательства.


def run_long_poll():
    """
    Запуск бота
    """
    for event in long_poll.listen():
        # если пришло новое сообщение - происходит проверка текста сообщения
        if event.type == VkEventType.MESSAGE_NEW:
            print(event.chat_id)  # нужно для прослушивания канала.
            # У меня чат Коэффициенты Стьюдента id: 33
            if event.chat_id == 33 and event.from_chat:
                if event.user_id in users:
                    VK_SESSION.method('messages.send',
                                      {'chat_id': 33, 'message': users[event.user_id] + abusive, 'random_id': 0})


if __name__ == '__main__':
    run_long_poll()
