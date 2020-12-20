import ijson
import json
import requests
from io import StringIO
import mock


def main():
    # with open("sample.json") as fp:
    #     objects = ijson.items(fp, 'item')
    #     print(len(list(objects)))
    with open("Check.json") as fp:
    # fp = StringIO()
    # fp.write(
    #     '[{ "name": "Paris", "type": "city" },{ "name": "Paris", "type": "city" }]'
    # )
        objects = list(ijson.items(fp, 'item',use_float=True))
        print(objects[0].__str__())
        # print(len(objects))
        # print("".join([str(obj) for obj in objects]))


    # fp.write("[")
    # for _ in range(0,100000):
    #     fp.write('{ "name": "Paris", "type": "city" },')
    # fp.write("]")
if __name__ == "__main__":
    main()
