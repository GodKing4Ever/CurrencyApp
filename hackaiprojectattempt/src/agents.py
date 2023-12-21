from uagents import Agent, Context, Bureau
from messageClasses import *
from apiCall import getVals, readVals
# import json
Val1 = None
Val2 = None
tick = 0
infoVal={}
KEY="72c6fe965374d00afaae3000"
changeTracker = Agent(name="changeTracker")
coreAgent = Agent(name="core")
displayUpdater = Agent(name = "displayUpdater")
UpdateChecker = Agent(name = "updater")

@UpdateChecker.on_interval(period=900)
async def changeTick(ctx: Context):
    global tick
    tick = 1

@changeTracker.on_event('startup')
async def initialise(ctx: Context):
    ctx.storage.set(key="V1", value= Val1)
    ctx.storage.set(key="V2", value= Val2)
    # ctx.storage.set(key="tick", value= 0)

@changeTracker.on_interval(period=0.5)
async def check(ctx: Context):
    global Val2
    global Val1
    if((Val1!=ctx.storage.get(key="V1")) or (Val2!=ctx.storage.get(key="V2")) or tick==1):
        ctx.storage.set(key="V1", value= Val1)
        ctx.storage.set(key="V2", value= Val2)
        tick=2
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
    tick=3
    # await ctx.send(displayUpdater.address, ValuesFinal(valDict=infoVal, additional=addInfo))


AllAgents=  Bureau()
AllAgents.add(UpdateChecker)
AllAgents.add(changeTracker)
AllAgents.add(coreAgent)

if __name__=='__main__':
    # print(len({}))
    coreAgent.run()


    





