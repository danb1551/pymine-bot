import minescript # type: ignore
import time
import sys

MOB = False

def getBlockName():
    try:
        return minescript.player_get_targeted_block().type
    except Exception as e:
        return f"Error: {e}"
    
def canMineThisPickaxe(block, pickaxe):
    pick_level = None
    block_level = None
    if "wooden_pickaxe" in pickaxe:
        pick_level = 1
    elif "stone_pickaxe" in pickaxe or "gold_pickaxe" in pickaxe:
        pick_level = 2
    else:
        pick_level = 3
    levelOne = ["stone", "diorite", "coal"]
    levelTwo = ["iron"]
    levelThree = ["gold", "diamond"]
    for item in levelThree:
        if block in item:
            block_level = 3
    for item in levelTwo:
        if block in item:
            block_level = 2
    for item in levelOne:
        if block in item:
            block_level = 1
    if block_level == None:
        block_level = 3
    if pick_level == None:
        pick_level = 3
    return bool(block_level <= pick_level)

def hasWorstPlace(old_pick, new_pick):
    old_pick_level = None
    if "wooden_pickaxe" in old_pick:
        old_pick_level = 1
    elif "stone_pickaxe" in old_pick or "gold_pickaxe" in old_pick:
        old_pick_level = 2
    else:
        old_pick_level = 3
    new_pick_level = None
    if "wooden_pickaxe" in new_pick:
        new_pick_level = 1
    elif "stone_pickaxe" in new_pick or "gold_pickaxe" in new_pick:
        new_pick_level = 2
    else:
        new_pick_level = 3
        return bool(old_pick_level > new_pick_level)

def getAdequatePickaxe():
    block = getBlockName()
    inv = minescript.player_inventory()
    old_pick = ""
    for i in range(0, 9):
        if "pickaxe" in inv[i].item: 
            if canMineThisPickaxe(block, inv[i].item):
                if old_pick == "":
                    old_pick = inv[i].item
                    slot = inv[i].slot
                    continue
                new_pick = inv[i].item
                if hasWorstPlace(old_pick, new_pick):
                    slot = inv[i].slot
                    old_pick = new_pick
    return slot

def getBestTool():
    block = getBlockName()
    pickaxe = ["stone", "ore", "diamond_block", "gold_block", "iron_block", "coal", "coal_block", "copper_block"]
    axe = ["oak_log", "log", "chest", "minecraft:oak_log"]
    shovel = ["dirt", "grass_block", "gravel", "sand"]
    sword = ["web"]
    if minescript.player_get_targeted_entity() != None and MOB == True:
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
    for _ in sword:
        if _ in block:
            return "sword"
    minescript.echo("[INFO] nic nenalezeno")
    minescript.echo("[INFO] Vybírání výchozího materiálu")
    return "pickaxe"

def getToolIndex(tool):
    if "pickaxe" in tool:
        return getAdequatePickaxe()
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
    sleep = 0.25

for i in range(iterations):
    if minescript.player_get_targeted_entity() != None and MOB == False:
        break
    setBestTool()
    time.sleep(sleep)
