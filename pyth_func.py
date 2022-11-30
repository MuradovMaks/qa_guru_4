# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser Chrome"
# или "Open Browser [Chrome]"
# на ваш выбор.

def funcs(search_arg, *args):
    search_arg = search_arg.__name__.replace("_", " ").upper() + ":"
    print (search_arg, *args)



def open_browser(browser_name):
    funcs(open_browser, browser_name)
def go_to_companyname_homepage(page_url):
    funcs(go_to_companyname_homepage,page_url)
def find_registration_button_on_login_page(page_url, button_text):
    funcs(find_registration_button_on_login_page,page_url,button_text)
open_browser("Chrome")
go_to_companyname_homepage("https:/google.com")
find_registration_button_on_login_page("URL", "Login")