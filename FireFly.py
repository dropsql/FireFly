API_KEY = 'e3ee9044e4527decd1f483bdcafc878b'
API_URL = 'http://apilayer.net/api/validate?access_key={}&number={}&country_code=&format=1'

import requests
import sys

from rich.console import Console

BANNER = '''[magenta]
   __ _          __ _      
  / _(_)_ _ ___ / _| |_  _ 
 |  _| | '_/ -_)  _| | || | [green]A fork of https://github.com/Lexxrt/FireFly[/green]
 |_| |_|_| \___|_| |_|\_, | [green]by https://github.com/dropsql[/green]
                      |__/ 
[/magenta]
'''

console = Console()

console.print(BANNER)

if len(sys.argv) == 1:
	console.print(f'py {sys.argv[0]} <number 1> <number 2> (etc.)')
	sys.exit(-1)

numbers = [x.strip() for x in sys.argv[1:]]

for number in numbers:
	console.rule(f'results for number: \'{number}\'')
	r = requests.get(API_URL.format(API_KEY, number))
	
	if 'You have not supplied a valid API Access Key' in r.text:
		console.print('[red][-][/red] your API key seems invalid :/')
		sys.exit()

	json_data = r.json()
	if json_data['valid'] == True:
		for key, value in json_data.items():
			if value:
				key = key.replace('_', ' ')

				if ' ' in key:
					x = key.split(' ')
					out = ''
					for y in x:
						out += y[0].upper() + y[1:] + ' '
					key = out
				else:
					key = key[0].upper() + key[1:]

				console.print(f'[green][+][/green] {key}: {value}')
	else:
		console.print('[red][-][/red] the phone number seems invalid :/')
