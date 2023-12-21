import json
def getVals(API_KEY, Currency):
    import requests
    
    URL= f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{Currency}"
    req = requests.get(URL)
    # print(req)
    # print("\n\n\n\n")
    req_final= req.json()['conversion_rates']
    return req_final

def readVals():
    with open('/home/samanth/Code/HackAIProjectAttempt/hackaiprojectattempt/src/CurrencyValues.txt') as f:
        req = f.readlines()
# print(req[0])
        req = json.loads(req[0])
        return req

# print(readVals())