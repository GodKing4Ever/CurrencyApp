from uagents import Agent, Context, Bureau
from messageClasses import *
from apiCall import getVals, readVals
# from interface import changeClock
# import json
Val1 = None
Val2 = None
tick = 0
clock = 0
infoVal={}
start =1
KEY="72c6fe965374d00afaae3000"
changeTracker = Agent(name="changeTracker")
coreAgent = Agent(name="core")
displayUpdater = Agent(name = "displayUpdater")
UpdateChecker = Agent(name = "updater")

def changeVar(a, b):
    global Val2, Val1
    Val1=a
    Val2=b

def setClock(a):
    global clock
    clock = a

def getClock():
    global clock
    v=clock
    clock=0
    return v

def getInfoVal():
    global infoVal
    return infoVal


@UpdateChecker.on_interval(period=900)
async def changeTick(ctx: Context):
    global tick, start
    if start:
        start = 0
    else:
        tick = 1

@changeTracker.on_event('startup')
async def initialise(ctx: Context):
    ctx.storage.set(key="V1", value= Val1)
    ctx.storage.set(key="V2", value= Val2)
    # ctx.storage.set(key="tick", value= 0)

@changeTracker.on_interval(period=1)
async def check(ctx: Context):
    # print("changeTracker is running")
    
    global Val2
    global Val1
    global tick
    # print(f"Agent Val1:{Val1} Val2:{Val2}")
    if((Val1!=ctx.storage.get(key="V1")) or (Val2!=ctx.storage.get(key="V2")) or tick==1):
        ctx.logger.info("Change detected")
        ctx.storage.set(key="V1", value= Val1)
        ctx.storage.set(key="V2", value= Val2)
        tick=2
        print("Tick is:", tick)
        await ctx.send(coreAgent.address, hasChanged(change=True))



# @coreAgent.on_event('startup')
# async def getData(ctx: Context):
#     try:
#         values = getVals(API_KEY=KEY, Currency='INR')
#         with open("hackaiprojectattempt/src/CurrencyValues.txt", "w") as f:
#             f.write(json.dumps(values))
#             ctx.logger.info("Written data to file succesfully")
#     except Exception as e:
#         print(f"There is a/an {e} at coreAgent startup")

@coreAgent.on_message(hasChanged)
async def updateVals(ctx:Context, __ : str, _ : hasChanged):
    # addInfo = 'NONE'
    global infoVal, tick
    ctx.logger.info("CoreAgent recieving message")
    if Val1 != None and Val2 == None:
        infoVal = getVals(API_KEY=KEY, Currency=Val1)
    elif Val1 == None and Val2 != None:
        infoVal = getVals(API_KEY=KEY, Currency=Val2)
    elif Val1 != None and Val2 != None:
        infoVal = getVals(API_KEY=KEY, Currency=Val1)[Val2]
    elif Val1 == None and Val2 == None:
        infoVal = {}
        # addInfo = 'RESET'
    else:
        ctx.logger.error(f"Some unforneen case has occurerd. Val1: {Val1}, Val2: {Val2}, infoVal: {infoVal}")
        raise ValueError
    setClock(1)
    tick=0
    ctx.logger.info("CoreAgent execution Complete")
    # await ctx.send(displayUpdater.address, ValuesFinal(valDict=infoVal, additional=addInfo))


AllAgents=  Bureau()
AllAgents.add(UpdateChecker)
AllAgents.add(changeTracker)
AllAgents.add(coreAgent)

if __name__=='__main__':
    # print(len({}))
    # coreAgent.run()
    pass


    





