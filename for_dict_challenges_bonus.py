"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def collect_tasks():
    find_user_id_with_max_messages()
    find_user_id_with_max_replies()
    most_watched_ids()


def find_user_id_with_max_messages():
    max_count_messages = 0
    user_id_with_max_messages = ""
    user_id_list = []
    for message in generate_chat_history():
        user_id_list.append(message.get("sent_by"))
    for user in user_id_list:
        if user_id_list.count(user) > max_count_messages:
            max_count_messages = user_id_list.count(user)
            user_id_with_max_messages = user
    print(
        f"айди пользователя, который написал больше всех сообщений: {user_id_with_max_messages}, количество сообщений: {max_count_messages}")


def find_user_id_with_max_replies():
    max_count_id = 0
    replies_id = ""
    replies_id_list = []
    messages = generate_chat_history()
    user_id_with_max_replies = ""

    for message in messages:
        if message.get("reply_for") is not None:
            replies_id_list.append(str(message.get("reply_for")))
    # print(replies_id_list)
    for message_id in replies_id_list:
        if replies_id_list.count(message_id) > max_count_id:
            max_count_id = replies_id_list.count(message_id)
            replies_id = message_id
    for m in messages:
        if str(m.get("id")) == replies_id:
            user_id_with_max_replies = m.get("sent_by")
    print(f"айди пользователя, на сообщения которого больше всего отвечали: {user_id_with_max_replies}")


def most_watched_ids():
    max_id_size = 0
    max_id_list = []
    user_id_list = []
    messages = generate_chat_history()
    for message in messages:
        if len(message.get("seen_by")) > max_id_size:
            max_id_size = len(message.get("seen_by"))
            max_id_list.clear()
            max_id_list = message.get("seen_by")
    print(
        f"айди пользователей, сообщения которых видело больше всего уникальных пользователей: {', '.join(str(uid) for uid in max_id_list)}")


if __name__ == "__main__":
    collect_tasks()
