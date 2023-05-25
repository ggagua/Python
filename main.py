import requests
import json
import sqlite3
#მოცემული კოდს არ ესაჭიროება უნივერსალური API Key, რადგან კონკრეტული API არ ითხოვს მას, SWAPI აბრუნებს პერსონაჟებს, პლანეტებს,
#კოსმოსურ ხომალდებს, მომხმარებლის შეყვანილი ინფორმაციის მიხედვით
number = int(input("შეიყვანე რიცხვი: "))
response = requests.get(f'https://swapi.dev/api/people/{number}/')
if response.status_code == requests.codes.ok:
    print("სტატუს კოდი არის -", response.status_code)
    print("ფაილის ფორმატი არის", response.headers['Content-Type'])
    result = response.json()
    #პრინიტ ამოვაკომენტარე, რადგან ასევე იქმნება json ფაილიც ცალკე და არ არის საჭიროება კონსოლში გამოტანის.
    # print(json.dumps(result, indent=3))
else:
    print("Error:", response.status_code, response.text)

#ვქმნით JSON ფაილს.
with open('sw.json', 'w') as file:
    json.dump(result, file, indent=3)

#მოგვაქვს საინტერესო ინფორმაცია
print(f'პერსონაჟი {result["name"]} დაიბადა {result["birth_year"]} წელს, მისი სიმაღლეა {result["height"]}, მასა კი {result["mass"]}, '
      f'მასზე ფილმების ყურება შესაძლებელია მოცემულ ლინკებზე - {result["films"]}')

#ვქმნით ბაზას,
conn = sqlite3.connect('star_wars.db')
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE characters
#                   (id INTEGER PRIMARY KEY,
#                   name TEXT,
#                   height TEXT,
#                   gender TEXT,
#                   year TEXT)''')
# conn.commit()

#შეგვაქვს მონაცემები ბაზაში, სახელი, სიმაღლე, სქესი და დაბადების წელი, ვაკითხავთ ჯსონ-ს და მოგვაქვს ინფორმაცია.
name = result['name']
height = result['height']
gender = result['gender']
year = result['birth_year']

cursor.execute("INSERT INTO characters(name, height, gender, year) VALUES(?, ?, ?, ?)",
               (name, height, gender, year))


conn.commit()





