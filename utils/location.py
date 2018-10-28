# encoding: utf-8
import json
def get():
    locations = []
    with open("utils/areas.json") as file:
        data = json.load(file)
        for province in data:
            locations.append({"code": province["value"], "name": province["label"]})
            # 判断省下面是否有市
            if province.get("children"):
                # 遍历市
                for city in province.get("children"):
                    locations.append({"code": city["value"], "name": city["label"], "provinceCode": province["value"]})
                    # 判断市下面是否有区
                    if city.get("children"):
                        for area in city.get("children"):
                            locations.append({"code": area["value"], "name": area["label"], "provinceCode": province["value"], "cityCode": city["value"]})
    return locations