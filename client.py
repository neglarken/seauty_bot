from aiogram import types
from aiogram.types import Message, ContentType, InputFile
from aiogram.dispatcher import FSMContext
from config import dp, channel_id
from states import GettingAnswers
from resources import texts
from resources import keyboards as kb

@dp.message_handler(commands=['start'])
async def start_handler(msg: Message): 
    await msg.answer(texts.hello, reply_markup=kb.inline_markup_start)

@dp.callback_query_handler(lambda c: c.data == 'start', state=[GettingAnswers.get_feedback, GettingAnswers.get_article, GettingAnswers.get_problem])
async def process_callback_start_in_state(callback_query: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await callback_query.message.answer(texts.hello, reply_markup=kb.inline_markup_start)

@dp.callback_query_handler(lambda c: c.data == 'start')
async def process_callback_start(callback_query: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await callback_query.message.answer(texts.hello, reply_markup=kb.inline_markup_start)

@dp.callback_query_handler(lambda c: c.data == 'bonus')
async def process_callback_bonus(callback_query: types.CallbackQuery):
    await callback_query.message.answer(texts.bonus, reply_markup=kb.inline_markup_bonus)

@dp.callback_query_handler(lambda c: c.data == 'ok')
async def process_callback_bonus_ok(callback_query: types.CallbackQuery):
    photo = InputFile('resources/bonus.jpg')
    await callback_query.message.answer(texts.ok, reply_markup=kb.inline_markup_restart)
    await callback_query.message.answer_photo(photo=photo)
    await GettingAnswers.get_feedback.set()

@dp.message_handler(state=GettingAnswers.get_feedback, content_types=[ContentType.PHOTO])
async def get_feedback_handler(msg: Message, state: FSMContext):
    await msg.forward(channel_id)
    await msg.answer(texts.ok_article, reply_markup=kb.inline_markup_restart)
    await state.set_state(GettingAnswers.get_article)

@dp.message_handler(state=GettingAnswers.get_article, content_types=[ContentType.PHOTO])
async def get_article_handler(msg: Message, state: FSMContext):
    await msg.forward(channel_id)
    await msg.answer(texts.ok_finish, reply_markup=kb.inline_markup_restart)
    await state.reset_state()

@dp.message_handler(state=GettingAnswers.get_feedback, content_types=[ContentType.TEXT])
async def get_feedback_text_handler(msg: Message, state: FSMContext):
    await msg.answer(texts.try_again, reply_markup=kb.inline_markup_restart)

@dp.message_handler(state=GettingAnswers.get_article, content_types=[ContentType.TEXT])
async def get_article_text_handler(msg: Message, state: FSMContext):
    await msg.answer(texts.try_again, reply_markup=kb.inline_markup_restart)

@dp.callback_query_handler(lambda c: c.data == 'not_ok')
async def process_callback_bonus_not_ok(callback_query: types.CallbackQuery):
    photo = InputFile('resources/bonus.jpg')
    await callback_query.message.answer(texts.not_ok, reply_markup=kb.inline_markup_restart)
    await callback_query.message.answer_photo(photo=photo)
    await GettingAnswers.get_feedback.set()

@dp.callback_query_handler(lambda c: c.data == 'guide')
async def process_callback_guide(callback_query: types.CallbackQuery):
    await callback_query.message.answer(texts.guide, reply_markup=kb.inline_markup_guide)

@dp.callback_query_handler(lambda c: c.data == 'problem')
async def process_callback_problem(callback_query: types.CallbackQuery):
    await callback_query.message.answer(texts.problem, reply_markup=kb.inline_markup_restart)
    await GettingAnswers.get_problem.set()

@dp.message_handler(state=GettingAnswers.get_problem, content_types=[
    ContentType.PHOTO,
    ContentType.TEXT,
    ContentType.DOCUMENT,
    ContentType.AUDIO,
    ContentType.VOICE,
    ContentType.VIDEO
    ])
async def get_article_handler(msg: Message, state: FSMContext):
    await msg.forward(channel_id)
    await msg.answer(texts.problem_finish, reply_markup=kb.inline_markup_restart)
    await state.reset_state()

@dp.callback_query_handler(lambda c: c.data == 'test')
async def process_callback_test(callback_query: types.CallbackQuery):
    callback_query.message.answer(texts.test, reply_markup=kb.inline_markup_start_test)
        