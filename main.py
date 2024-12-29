
# main.py
import process_requests, actions, os, config

def main():
    var = 'Tú: ' if config.idiom == 'es' else 'You: '
    input_user = input(var)
    # process user input and return the virtual assistant's response
    actions.va_response(process_requests.get_response(input_user))

if __name__ == '__main__':
    os.system('cls')  # clear the terminal screen (for Windows)
    intro = actions.introduce_myself()
    actions.va_response(intro)
    while True:
        main()
