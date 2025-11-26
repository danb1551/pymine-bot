import minescript # type: ignore
import time
import sys

def getBlockName():
    try:
        return minescript.player_get_targeted_block().type
    except Exception as e:
        return f"Error: {e}"

def getBestTool():
    block = getBlockName()
    pickaxe = ["stone", "ore", "diamond_block", "gold_block", "iron_block", "coal", "coal_block", "copper_block"]
    axe = ["oak_log", "log", "chest", "minecraft:oak_log"]
    shovel = ["dirt", "grass_block", "gravel", "sand"]
    if minescript.player_get_targeted_entity() != None:
        return "_axe"
    for _ in pickaxe:
        if _ in block:
            return "pickaxe"
    for _ in axe:
        if _ in block:
            return "_axe"
    for _ in shovel:
        if _ in block:
            return "shovel"
    minescript.echo("[INFO] nic nenalezeno")
    minescript.echo("[INFO] Vybírání výchozího materiálu")
    return "pickaxe"

def getToolIndex(tool):
    inv = minescript.player_inventory()
    for item in inv:
        if tool in item.item:
            return item.slot

def setBestTool():
    index = getToolIndex(getBestTool())
    minescript.player_inventory_select_slot(index)


try:
    iterations = int(sys.argv[1])
except Exception as e:
    iterations = 100
try:
    sleep = int(sys.argv[2])
except Exception as e:
    sleep = 0.1

for i in range(iterations):
    setBestTool()
    time.sleep(sleep)
