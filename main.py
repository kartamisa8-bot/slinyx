import asyncio
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging
import pytz
from handlers import user_commands,ip_func
from handlers.norma import *
from callbacks import callbacks, adduser, link_gtables, stats, neaktiv, promotions, p_transfer, extra_work

scheduler = AsyncIOScheduler()
moscow_tz = pytz.timezone('Europe/Moscow')

#  logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s')


def handle_norma():
    asyncio.run(check_norma())


async def main():
    bot = Bot("vk1.a.njf0QE6ohEMojLlj6Q-obHutdN2puoEAFz1ClGT9t1EnmfFgsESubBSJ-FdW-zStHJ4eruhHgx1I2VovazLf8xl1_goMtKX_pwS8CwfFKaw8MU_WzpbkjUToHMKVA3iW-XjW3XmmvYhsypvPThgiu-WycZpP7FFds9b0E_lIsdU1EsHlshBt17cCwh2pJpV-e8jYhuMP3Y94okghWlAJ-A", parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        callbacks.router,
        adduser.router,
        link_gtables.router,
        neaktiv.router,
        stats.router,
        promotions.router,
        p_transfer.router,
        extra_work.router,
        ip_func.router,

    )

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.send_message(716255074, "✅ Бот был успешно запущен!")
    scheduler.add_job(handle_norma, 'cron', hour=11, minute=28, timezone=moscow_tz)
    #  scheduler.add_job(job2, 'interval', seconds=2)
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

