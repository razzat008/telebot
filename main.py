# simple telegram bot using telegram api
import telegram.ext
"""importing api tokens"""
with open("token.txt") as token_file:
    token = token_file.read()

"""runs at the start"""


def start(update, context):
    update.message.reply_text(
        f"Hello! and welcome to testbot.\nYou can type /help to list all the available commands")


def help(update, context):
    update.message.reply_text("""
These are currently available commands:
/help
/aboutme
""")

def web(update,context):
    update.message.reply("""
    https://ceaser008.github.io/webpage/
""")

def aboutme(update, context):
    update.message.reply_text("""Just a regular guy with interests in coding.
My socials:
github:https://github.com/razzat008
webpage:https://rajatdahal.com.np
                              """)


def handle_messages(update, context):
    commandlist = ["hi", "h", "?"]
    if (update.message.text == x for x in commandlist):
        update.message.reply_text("""
If you meant /help then:
These are currently available commands:
/help
/aboutme
""")
    else:
        update.message.reply_text(f"{update.message.text} not found")


updater = telegram.ext.Updater(token, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("aboutme", aboutme))
disp.add_handler(telegram.ext.CommandHandler("web", web))

disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.text, handle_messages))

updater.start_polling()
updater.idle()
