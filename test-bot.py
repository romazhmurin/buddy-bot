from aiogram import types, executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.misc import TgKeys


storage = MemoryStorage()
bot = Bot(token = TgKeys.TOKEN)
dp = Dispatcher(bot,
                storage=storage)


class ProfileStatesGroup(StatesGroup):

    photo = State()
    name = State()
    age = State()
    themes1 = State()
    themes2 = State()
    themes3 = State()
    themes4 = State()
    themes5 = State()
    description = State()



markup = types.ReplyKeyboardRemove()





def get_themes1() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Искусство'))
    kb.add(KeyboardButton('Видеосъемка'))
    kb.add(KeyboardButton('Фотография'))
    kb.add(KeyboardButton('Музыка'))
    kb.add(KeyboardButton('Танцы'))
    kb.add(KeyboardButton('Рисование'))
    kb.add(KeyboardButton('Программирование'))
    kb.add(KeyboardButton('Кулинария'))
    kb.add(KeyboardButton('Литература'))
    kb.add(KeyboardButton('Политика'))
    kb.add(KeyboardButton('Журналистика'))
    kb.add(KeyboardButton('Кинокультура'))
    kb.add(KeyboardButton('Наука'))
    kb.add(KeyboardButton('Экзамены'))
    kb.add(KeyboardButton('Олимпиады'))
    kb.add(KeyboardButton('Прохождение онлайн курсов'))
    kb.add(KeyboardButton('Что угодно'))
    kb.add(KeyboardButton('Продолжить'))

    return kb

def get_themes2() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Видеосъемка'))
    kb.add(KeyboardButton('Фотография'))
    kb.add(KeyboardButton('Музыка'))
    kb.add(KeyboardButton('Танцы'))
    kb.add(KeyboardButton('Рисование'))
    kb.add(KeyboardButton('Программирование'))
    kb.add(KeyboardButton('Кулинария'))
    kb.add(KeyboardButton('Литература'))
    kb.add(KeyboardButton('Политика'))
    kb.add(KeyboardButton('Журналистика'))
    kb.add(KeyboardButton('Кинокультура'))
    kb.add(KeyboardButton('Наука'))
    kb.add(KeyboardButton('Экзамены'))
    kb.add(KeyboardButton('Олимпиады'))
    kb.add(KeyboardButton('Прохождение онлайн курсов'))
    kb.add(KeyboardButton('Что угодно'))
    kb.add(KeyboardButton('Продолжить'))

    return kb

def get_themes3() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('333а'))
    return kb

def kanye() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Продолжить'))
    kb.add(KeyboardButton('Выбрать ещё четыре темы'))
    return kb

def get_themes4() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('444а'))
    return kb


def get_themes5() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('555а'))
    return kb

def anketa() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Продолжить'))
    return kb

def onerrotwo_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Очно'))
    kb.add(KeyboardButton('Онлайн'))
    return kb



def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Создать анкету'))

    return kb


def get_cancel_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/cancel'))

    return kb


def choose_themes_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('choose themes'))

    return kb



@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await message.answer('Вы прервали создание анкеты!',
                        reply_markup=get_kb())


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Добро пожаловать! Чтобы начать поиск партнера необходимо создать анкету.',
                         reply_markup=get_kb())


@dp.message_handler(commands=['create'])
async def cmd_create(message: types.Message) -> None:
    await message.answer("Отправь фотографию, которая будет отображаться в анкете",
                        reply_markup=get_cancel_kb())
    await ProfileStatesGroup.photo.set()


@dp.message_handler(content_types=['text'])
async def func(message):
    if message.text == 'Создать анкету':
        pass
        await message.answer("Отправь фотографию, которая будет отображаться в анкете.",
                        reply_markup=get_cancel_kb())
        await ProfileStatesGroup.photo.set()


@dp.message_handler(lambda message: not message.photo, state=ProfileStatesGroup.photo)
async def check_photo(message: types.Message):
    await message.answer('Это не фотография!')


@dp.message_handler(content_types=['photo'], state=ProfileStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await message.answer('Как вас зовут?')
    await ProfileStatesGroup.next()


@dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) > 100,
                    state=ProfileStatesGroup.age)
async def check_age(message: types.Message):
    await message.answer('Введите реальный возраст!')


@dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) < 10,
                    state=ProfileStatesGroup.age)
async def check_age(message: types.Message):
    await message.answer('Введите реальный возраст!')




@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer('Сколько тебе лет?')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['age'] = message.text

    await message.answer('что хочешь изучать?', reply_markup=get_themes1())
    await ProfileStatesGroup.next()

@dp.message_handler(content_types=['text'], state='*')
async def load_themes1(message: types.Message, state: FSMContext):
    if message.text == 'Искусство':
        async with state.proxy() as data:
            data['themes1'] = message.text
            await ProfileStatesGroup.next()
            await message.reply("Вы выбрали 1/5 тем. Вы можете продолжить или выбрать ещё четыре темы.",reply_markup=kanye())

    elif message.text == 'Танцы':
        async with state.proxy() as data:
            data['themes1'] = message.text
            await ProfileStatesGroup.next()
            await message.reply("Вы выбрали 1/5 тем. Вы можете продолжить или выбрать ещё четыре темы.", reply_markup=kanye())

    elif message.text == 'Политика':
        async with state.proxy() as data:
            data['themes1'] = message.text
            await ProfileStatesGroup.next()
            await message.reply("Вы выбрали 1/5 тем. Вы можете продолжить или выбрать ещё четыре темы.", reply_markup=kanye())

    elif message.text == 'Продолжить':
        async with state.proxy() as data:
            data['themes2'] = 'v'

            await state.finish()
            await bot.send_photo(chat_id=message.from_user.id,
                                                 photo=data['photo'],
                                                 caption=f"{data['name']}, {data['age']}\n\n{data['themes1']}",
                                                 reply_markup=onerrotwo_kb())
            await message.answer('Вот ваша анкета.\nКак вы хотите заниматься?')


    else:
        await message.reply("sieg heil")


@dp.message_handler(state=ProfileStatesGroup.themes2)
async def load_themes2(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['themes2'] = message.text

    await message.answer('Вы выбрали 2/5 тем. Вы можете продолжить или выбрать ещё четыре темы.', reply_markup=get_themes3())
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.themes3)
async def load_themes3(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['themes3'] = message.text

    await message.answer('Вы выбрали 3/5 тем. Вы можете продолжить или выбрать ещё две темы.', reply_markup=get_themes4())
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.themes4)
async def load_themes4(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['themes4'] = message.text

    await message.answer('Вы выбрали 4/5 тем. Вы можете продолжить или выбрать ещё одну тему.', reply_markup=get_themes5())
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.themes5)
async def load_themes5(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['themes5'] = message.text

    await message.answer('Вы выбрали максимум тем.', reply_markup=markup)
    await message.answer('Расскажите немного о себе или нажмите продолжить', reply_markup=anketa())
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.description)
async def load_desc(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Продолжить':
        async with state.proxy() as data:
            data['description'] = '⁠'
            await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=f"{data['name']}, {data['age']} {data['description']}\n\n{data['themes1']}, {data['themes2']}"
                                     f"{data['themes3']}, {data['themes4']}, {data['themes5']}", reply_markup=onerrotwo_kb())

        await message.answer('Ваша анкета успешно создана! ')
        await state.finish()

    async with state.proxy() as data:
        data['description'] = message.text
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=f"{data['name']}, {data['age']}\n\n{data['description']}\n\n{data['themes1']}, {data['themes2']}"
                                     f"{data['themes3']}, {data['themes4']}, {data['themes5']}", reply_markup=onerrotwo_kb())

        await state.finish()







if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)