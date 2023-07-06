from aiogram.dispatcher.filters.state import StatesGroup, State

class GettingAnswers(StatesGroup):
    get_feedback = State()
    get_article = State()
    get_problem = State()