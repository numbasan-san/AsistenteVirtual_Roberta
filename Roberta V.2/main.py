
# main.py
import process_requests, actions, os

def main():
    input_user = input('Tú: ')
    # process user input and return the virtual assistant's response
    actions.va_response(process_requests.get_response(input_user))

if __name__ == '__main__':
    os.system('cls')  # clear the terminal screen (for Windows)
    while True:
        main()