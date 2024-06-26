from contextlib import contextmanager
import sys
@contextmanager
def reversed_print():
    save_stdout = sys.stdout.write
    sys.stdout.write = lambda x: save_stdout(x[::-1])
    yield
    sys.stdout.write = save_stdout

# TEST_4:
with reversed_print():
    print('Я кашлянул в звенящей тишине,')
    print('И от шального эха стало жутко…')
    print('Расскажет ли утятам обо мне')
    print('под утро мной испуганная утка?')

# TEST_5:
names = ['Творимир Матвеев', 'Светлана Жданова', 'Агап Голубев', 'Макар Дьячков', 'Евпраксия Григорьева',
         'Доброслав Михайлов', 'Зинаида Турова', 'Лариса Сафонова', 'Раиса Моисеева', 'Фадей Герасимов',
         'Синклитикия Сергеева', 'Павел Чернов', 'Синклитикия Меркушева', 'Ксения Исакова', 'Зоя Богданова',
         'Александра Васильева', 'Макар Капустин', 'Антонин Терентьев', 'Марина Мамонтова', 'Станимир Калашников',
         'Фёкла Комарова', 'Милий Соколов', 'Кира Белозерова', 'Вениамин Фомичев', 'Максим Жуков', 'Симон Кудрявцев',
         'Вера Носова', 'Иванна Князева', 'Ювеналий Капустин', 'Юрий Кулаков', 'Татьяна Владимирова', 'Ия Дмитриева',
         'Спиридон Зыков', 'Майя Савина', 'Феврония Моисеева', 'Любовь Игнатьева', 'Кузьма Дорофеев',
         'Поликарп Панфилов', 'Парамон Силин', 'Платон Жуков']

with reversed_print():
    print(*names, sep=' зпт ', end=' тчк')

# TEST_6:
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''

with reversed_print():
    print(text)