from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Command

inline_btn_bonus = InlineKeyboardButton('Бонус 150 RUB', callback_data='bonus')
inline_btn_guide = InlineKeyboardButton('Гайд', callback_data='guide')
inline_btn_test = InlineKeyboardButton('Тест', callback_data='test')
inline_btn_problem = InlineKeyboardButton('Вопрос/Проблема', callback_data='problem')
inline_markup_start = InlineKeyboardMarkup().add(inline_btn_bonus,inline_btn_guide,inline_btn_test,inline_btn_problem)

inline_btn_ok = InlineKeyboardButton('Уже оставил(-a) отзыв', callback_data='ok')
inline_btn_not_ok = InlineKeyboardButton('Не оставил(-а) отзыв', callback_data='not_ok')
inline_btn_restart = InlineKeyboardButton('Начать сначала', callback_data='start')
inline_markup_bonus = InlineKeyboardMarkup().add(inline_btn_ok, inline_btn_not_ok, inline_btn_problem, inline_btn_restart)

inline_markup_restart = InlineKeyboardMarkup().add(inline_btn_restart)

inline_btn_guide_url = InlineKeyboardButton('Твоя идеальная кожа', url='https://mssg.su/tb/BZt7ZArZ')
inline_markup_guide = InlineKeyboardMarkup().add(inline_btn_guide_url, inline_btn_restart)

inline_btn_start_test = InlineKeyboardButton('Пройти тест!', callback_data='start_test')
inline_markup_start_test = InlineKeyboardMarkup().add(inline_btn_restart, inline_btn_start_test)