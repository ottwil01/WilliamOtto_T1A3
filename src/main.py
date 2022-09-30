import datetime as dt
from datetime import date
import requests
from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
import functions
import colorama
from colorama import Fore
colorama.init(autoreset=True)

base_url = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = 'f820095e8faeb3eb39572008bae7a59c'
city = input('Which city in Australia are you flying out of? ')
url = base_url + '&appid=' + api_key + '&q=' + city + '&units=imperial'
response = requests.get(url).json()

if response['cod'] == '404':
    city = input('That is not a city, please try again: ')
    url = base_url + '&appid=' + api_key + '&q=' + city + '&units=imperial'
    response = requests.get(url).json()

ground_temp = functions.f_to_c(response['main']['temp'])
weather_description = response['weather'][0]['description']
current_humidity = response['main']['humidity']
cloud_cover_percent = (response['clouds']['all'])
dew_point = ground_temp - ((100 - current_humidity) / 5)
cloud_base = ((ground_temp - dew_point) / 2.5) * 1000
cloud_base_temp = (-0.00984 * cloud_base) + ground_temp
alt_clear = "{:.2f}".format((10 + ground_temp) / 0.00984)
alt_mixed = "{:.2f}".format((15 + ground_temp) / 0.00984)
alt_rime = "{:.2f}".format((20 + ground_temp) / 0.00984)

if weather_description != "clear sky":
    ice_present = 'Yes'
    safe_zone = f'Safe to fly below {cloud_base}, or above {alt_rime}'
else:
    ice_present = 'No'
    safe_zone = 'There is no potential for icing!'

print(ground_temp, cloud_base_temp, cloud_base, alt_clear, alt_mixed, alt_rime)


x = PrettyTable()
x.field_names = ['City Name', 'Weather Description', 'Cloud Cover (%)', 'Cloud Base (ft)', 'Ice Present', 'Ice-free Flying Altitude']
x.add_row([city, weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
print(x)

if ice_present == 'No':
    print('Here is a visual output of the potential icing zones higlighted in red:')
    print('-----------------------------------------------------------------------')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░No ice at any flying altitude!░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
else:
    print('Here is a visual output of the potential icing zones higlighted in red:')
    print('-----------------------------------------------------------------------')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░Low Risk of icing░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED} █░░░░░░░░░░Rime Ice at max {alt_rime} feet░░░░░░░░█-20C')
    print(f'{Fore.RED} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}A█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}L█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}T█░░░░░░░░░░░Mixed Ice at max {alt_mixed} feet░░░░░░░░░█-15C')
    print(f'{Fore.RED}I█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}T█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}U█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}D█░░░░░░░░░Clear Ice at max {alt_clear} feet░░░░░░░░░█-10C')
    print(f'{Fore.RED}U█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}E█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED} █░░░░░░░░░Cloud base at {cloud_base} feet░░░░░░░░█ 0C')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░No risk of icing░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')

def menu():
    options = ['Information on Icing', 'Try another City', 'Exit']
    submenu_options = ['Clear Ice', 'Mixed Ice', 'Rime Ice']
    main_menu = TerminalMenu(options)
    quitting = False
while quitting == False:
    menu_entry_index = main_menu.show()
    selection = options(main_entry_index)
    if selection == 'Exit':
        quitting = True
    if selection == 'Information on Icing':
        print("Clear Ice:")
        print('Clear ice is formed by supercooled large water droplets that mostly occur in the temperature range from 0 C to -10 C. The ice itself freezes slowly upon impact forming a smooth sheet of transparent ice.')
        print('Because the droplets are large, as they freeze, they spread over the surface, combining with other droplets, forming a solid surface. There are no air bubbles to weaken the structure of the ice layer.')
        print('As more ice accumulates, it developes ridges which pose a large risk of causing issues to aerodynamic and instrument performance with up to a 500% increase in drag. It\'s thickness also makes it more difficult to remove using de-icing equipment.')
        print('Rime Ice:')
        print('Rime ice is a type of ice that occurs in the coldest conditions, usually below -15C. Rime ice is opaque or milky/white ice that occurs commonly in stratiform clouds. The supercooled water droplets ')
        print('that form with rime ice are much smaller than that of clear ice. This means the droplets maintain the sperical shapes as they freeze without much spreading.')
        print('Mixed Ice:')
        print('Mixed ice is the most common type of ice that may occur due to the varying nature of droplet sizes within a cloud. This type of ice is most commonly found in temperatures ranging from -10C to -15C.')
        print('')
        break
    if selection == 'Try another City':
        break