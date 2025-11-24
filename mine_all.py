import minescript
import time

# --- Nastavení ---
RADIUS = 2          # jak daleko těžit bloky okolo
ATTACK_RADIUS = 3   # dosah útoku na zvířata
DELAY = 0.15        # krátká pauza mezi cykly

def crouch():
    minescript.key("shift", True)   # držet shift
    time.sleep(0.1)

def break_block(x, y, z):
    minescript.lookat(x, y, z)
    minescript.attack()             # držení levého tlačítka nejde, Minescript spamuje attack()

def kill_animals(px, py, pz):
    mobs = minescript.getmobs()
    for m in mobs:
        name = m["name"]
        x, y, z = m["x"], m["y"], m["z"]

        if abs(x - px) <= ATTACK_RADIUS and abs(y - py) <= ATTACK_RADIUS and abs(z - pz) <= ATTACK_RADIUS:
            if any(animal in name for animal in ["cow", "pig", "sheep", "chicken"]):
                minescript.lookat(x, y, z)
                minescript.attack()

def destroy_blocks_around(px, py, pz):
    for dx in range(-RADIUS, RADIUS+1):
        for dy in range(-RADIUS, RADIUS+1):
            for dz in range(-RADIUS, RADIUS+1):

                bx, by, bz = px + dx, py + dy, pz + dz
                block = minescript.getblock(bx, by, bz)

                if block != "minecraft:air":
                    break_block(bx, by, bz)

def autominer():
    minescript.echo("[INFO] AutoMine zapnut.")

    crouch()

    while True:
        px, py, pz = minescript.player_position()
        px, py, pz = int(px), int(py), int(pz)

        crouch()                          # pořád drží shift
        destroy_blocks_around(px, py, pz) # těží
        kill_animals(px, py, pz)          # zabíjí moby

        time.sleep(DELAY)


# --- Spuštění ---
autominer()