import json
import os

app_root = "/Users/denissamohvalov/Documents/development/omnibazaar-ui/app"
locales_root = "/Users/denissamohvalov/Documents/development/OmniCoin2--Language/locales"


def replace(el, path):

    for root, dirs, files in os.walk(app_root + path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as data:
                content = data.read()
                start_id = content.find(el['id'])
                if start_id == -1:
                    continue
                start_message = content.find('defaultMessage:', start_id)
                if start_message == -1:
                    continue
                end = content.find(' }', start_message)
                message = el['defaultMessage'].replace("'", "\\'")
                with open(file_path, 'w') as out:
                    out.write(
                        "%s '%s'\n %s" % (
                            content[:start_message + len('defaultMessage:')],
                            message,
                            content[end:]
                        )
                    )


def walk():
    for root, dirs, files in os.walk(locales_root):
        path = root.split(os.sep)
        for file in files:
            try:
                path = os.path.join(root, file)
                with open(path) as json_data:
                    data = json.loads(json_data.read())
                    for el in data:
                        replace(el, root.replace(locales_root, ''))

            except Exception as e:
                print(str(e) + " " + path)


if __name__ == '__main__':
    walk()
