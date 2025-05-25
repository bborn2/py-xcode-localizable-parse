import json


def main():
    
    trans = {}
    
    with open("ru.txt", "r", encoding="utf-8") as f:
        data2 = json.load(f)
        
        trans = data2["strings"]

        for key, entry in trans.items():
            value = entry.get("value")
            if value:
                print(f"Key: {key}")
                print(f"Value: {value}\n")
                
    print(trans.keys())

    with open("Localizable.xcstrings", "r", encoding="utf-8") as f:
        data = json.load(f)

    chinese_langs = ["zh-Hans"]
        
    for key, val in data["strings"].items():
        localizations = val.get("localizations", {})
        for lang in chinese_langs:
            if lang in localizations:
                value = localizations[lang]["stringUnit"]["value"]
                # print(f"Key: {repr(key)}")
                # print(f"  [{lang}] = {value}\n")
                
                print("--", value)
                if value in trans.keys():
                    print("in")

                    data["strings"][key]["localizations"]["vi"] = {
                            "stringUnit": {
                                    "state": "translated",
                                    "value": trans[value]["value"]
                                }
                            }
    
                    
    with open("Localizable.xcstrings", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
                
                



if __name__ == "__main__":
    main()
