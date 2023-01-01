# spam bot for telegram 
# this program can help us prank our friends


import time
import pyautogui


def main(file_name, person):
    spam_f = open(file_name, 'r')
    for line in spam_f:
        pyautogui.typewrite(line)
        pyautogui.press('enter')
        time.sleep(0.2)

    # telegram serach person 
    pyautogui.hotkey('ctrl', 'j')
    time.sleep(1)
    pyautogui.typewrite(person)
    time.sleep(5)
    pyautogui.press('enter')


if __name__ == '__main__':
    persons_count = int(input('count: '))
    persons = [input('person: ') for _ in range(persons_count)]
    file_name = input('span file name: ')
    s_min = input('spam time: ')

    time.sleep(10)
    time_z = time.localtime()
    start = time_z.tm_min()
    count = 0

    while end - start != s_min:
        main(file_name, persons[count])
        count += 1
        if count > (persons_count-1):
            count = 0
        end = time_z.tm_min()
