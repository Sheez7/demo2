import pywhatkit


def send_message_inst():
    mobile = input('Insert number of recipient: ')
    message = input('Insert the message: ')

    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)

# def send_message():
#     mobile = input('Insert number of recipient: ')
#     message = input('Insert the message: ')
#     hour = int(input('Choose the hour: '))
#     minutes - int(input('Choose the minute: '))

    pywhatkit.sendwhatmsg(phone_no=mobile, message=message, time_hour=hour, time_min=minutes)

def main():
    send_message_inst()
    # send_message()
if __name__ == '__main__':
    main()