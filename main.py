from ui.user_interface import UserInterface
from models.output_handler import OutputHandler

if __name__ == "__main__":
    UserInterface.greeting()
    output_handler = OutputHandler()
    while True:
        input_command = str(input("Введите команду: "))
        if input_command not in output_handler.COMMANDS:
            UserInterface.wrong_command()
        else:
            output_handler.current_action = input_command
            output_handler.command_handler()



