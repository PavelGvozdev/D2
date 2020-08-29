import json
import random

beginnings = [
    "Коллеги,",
    "В то же время,",
    "Однако,",
    "Тем не менее,",
    "Следовательно,",
    "Соответственно,",
    "Вместе с тем,",
    "С другой стороны,",
]

subjects = [
    "парадигма цифровой экономики",
    "контекст цифровой трансформации",
    "диджитализация бизнес-процессов",
    "прагматичный подход к цифровым платформам",
    "совокупность сквозных технологий ",
    "программа прорывных исследований",
    "ускорение блокчейн-транзакций ",
    "экспоненциальный рост Big Data",
]

verbs = [
    "открывает новые возможности для",
    "выдвигает новые требования ",
    "несет в себе риски ",
    "расширяет горизонты",
    "заставляет искать варианты",
    "не оставляет шанса для",
    "повышает вероятность",
    "обостряет проблему",
]

actions = [
    "дальнейшего углубления",
    "бюджетного финансирования"
    "синергетического эффекта",
    "компрометации конфиденциальных",
    "универсальной коммодизации",
    "несанкционированной кастомизации",
    "нормативного регулирования",
    "практического применения",
]

ends = [
    "знаний и компетенций.",
    "непроверенных гипотез.",
    "волатильных активов.",
    "опасных экспериментов.",
    "государственно-частных партнёрств.",
    "цифровых следов граждан.",
    "нежелательных последствий.",
    "внезапных открытий.",
]

def makeStatement(*args):
    if len(args) == 0:
        statementString = "{} {} {} {} {}".format(random.choice(beginnings), random.choice(subjects), random.choice(verbs), random.choice(actions), random.choice(ends))
        statementString = json.dumps({"message" : statementString}, ensure_ascii=False)
        return statementString
    else:
        tempArr = []
        for _ in range(args[0]):
            tempArr.append("{} {} {} {} {}".format(random.choice(beginnings), random.choice(subjects), random.choice(verbs), random.choice(actions), random.choice(ends)))
        statementString = json.dumps({"messages" : tempArr}, ensure_ascii=False)
        return statementString