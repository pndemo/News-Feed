import os, sys
import json
import urllib.request

class Color:
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

width = os.get_terminal_size()

def get_news_feed():
    url = 'https://jsonplaceholder.typicode.com/posts'
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    for x in data:
        print (Color.RED + '*'.center(width.columns, '*') + Color.END + '\n')
        print (Color.BOLD + 'Post ' + str(x['id']) + ': ' + str(x['title']) + Color.END + '\n')
        print (str(x['body']) + '\n')
        print (Color.GREEN + 'Posted by User: ' + str(x['userId']) + Color.END + '\n')

def main_menu(error_msg):
    """
    lists all functionality of the site
    """
    #clear existing screen
    os.system('clear')
    menu_choices = [1,2,3,99]
    star_divider = '*' * 35
    line_divider = '-' * 35

    #check for error messages
    if not error_msg:
        #introduce the app
        print(star_divider)
        print ('* Welcome to Primitive Social!    *')
        print ('%s \n\n' % star_divider)
    else:
        #give user the error message
        print (star_divider)
        print(error_msg)
        print (star_divider)
        #clear error message
        error_msg = None

    #show other options
    print('Select an action from the menu below:\n')
    print('1. View News Feed\n')
    print('2. Create a New Post\n')
    print('3. Comment on a Post\n')
    print('%s \n' % line_divider)
    print('99. ****Quit appication****\n')
    print('%s \n' % line_divider)
    choice = int(input('choice >>'))

    #validate choice
    if choice not in menu_choices:
        error_msg = 'Invalid choice! Please enter a number from the actions list!'
        main_menu(error_msg)

    if choice == 1:
        get_news_feed()

    if choice == 2:
        pass
        #create new Post

    if choice == 3:
        pass
        #comment

    if choice == 99:
        print ('\n%s \n' % star_divider)
        print ('Application will exit now!\n\n')
        sys.exit()

if __name__ == '__main__':
    main_menu(error_msg=None)
    
