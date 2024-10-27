
# main.py
import process_requests, actions, os

def main():
    input_user = input('Tú: ')
    actions.va_response(process_requests.get_response(input_user))

if __name__ == '__main__':
    os.system('cls')
    # intro = actions.introduce_myself()
    # actions.va_response(intro)
    while True:
        main()
