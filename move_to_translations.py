import os
import json

transalations_root = '/Users/denissamohvalov/Documents/development/OmniCoin2----Translations'
locales_root = '/Users/denissamohvalov/Documents/development/OmniCoin2--Language/locales'
locales = ['en', 'es', 'fr', 'it', 'ru']

def walk():
    obj = {}
    for root, dirs, files in os.walk(locales_root):
        path = root.split(os.sep)
        for file in files:
            try:
                path = os.path.join(root, file)
                with open(path) as json_data:
                    data = json.loads(json_data.read())
                    for el in data:
                        obj[el['id']] = el['defaultMessage']
            except Exception as e:
                print(str(e) + " " + path)
    for locale in locales:
        with open(os.path.join(transalations_root, '%s.json' % locale), 'w') as out:
            out.write(json.dumps(obj, indent=4))

if __name__ == '__main__':
    walk()


