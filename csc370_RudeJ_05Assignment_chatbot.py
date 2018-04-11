# -*- coding: utf-8 -*-
#
#########################
#       ChatBot v 1.0   #
#       CSC370          #
#       By: Jordon Rude #
#########################
#
# This is a basic chat bot using the chatterbot API
#

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Frank
chatbot = ChatBot('Frank',
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        logic_adapters=[
                "chatterbot.logic.BestMatch"
    ],
        input_adapter="chatterbot.input.TerminalAdapter",
        output_adapter="chatterbot.output.TerminalAdapter",
        database="../database.db"
)

#this line sets the trainer to use the follow lines
chatbot.set_trainer(ListTrainer)

#each line is an acceptable answer to the previous line


chatbot.train([
        "Hi!",
        "Hello!",
        "Hey there!",
        "Oh hi!",
])

chatbot.train([
        "How are you?",
        "I am fine.",
        "That is good",
        "I am glad",
])

#initiates code and asks for user input
print("Type something to begin...")


# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        chatbot_input = chatbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


#####
# more testing is needed and a better UI for seeing which 
# is chatting, the bot or the user
#
#####

