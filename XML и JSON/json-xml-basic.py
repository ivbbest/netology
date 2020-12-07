import json
import xml.etree.ElementTree as ET


def top_words(tmp_str, top_key, len_key):
    """
    На вход получаем строку, сколько топовых слов вывести и от какой длины слова делать анализ
    """
    #список с уникальными словами
    list_words = list(tmp_str.split())
    poisk = dict()

    for elem in list_words:
        len_word = len(elem)

        if len_word > len_key:

            if elem in poisk:
                poisk[elem] += 1
            else:
                poisk[elem] = 1

    #сортировка словаря и печать 10 популярных слов
    popular_words = sorted(poisk.items(), key=lambda x: x[1], reverse=True)[:top_key]
    print(popular_words)

def analysis_json(file):
    """
    Программа, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее
    6 символов для файла json.
    """

    with open(file, encoding='utf-8') as f:
        json_data = json.load(f)

    tmp_str = ''
    len_json = len(json_data["rss"]["channel"]["items"])

    #создание большой строки со всеми данными из дескрипшен
    for i in range(len_json):
        my_words = (json_data["rss"]["channel"]["items"][i]["description"]).lower()
        tmp_str += ''.join(my_words)

    top_words(tmp_str, 10, 6)

def analysis_xml(file):
    """
    Программа, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее
    6 символов для файла xml.
    """
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file, parser)
    root = tree.getroot()
    xml_text = ''
    news_xml = root.findall("channel/item")

    for news in news_xml:
        descr = news.find("description")
        xml_text += ''.join(descr.text.lower())

    top_words(xml_text, 10, 6)


file_json = 'newsafr.json'
file_xml = 'newsafr.xml'

analysis_json(file_json)
analysis_xml(file_xml)