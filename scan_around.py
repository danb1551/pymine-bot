import minescript

def scan_3d(radius=3):
    px, py, pz = minescript.player_position()
    px, py, pz = int(px), int(py), int(pz)

    world = []

    for dy in range(-radius, radius + 1):
        layer_y = py + dy
        layer = []

        for dz in range(-radius, radius + 1):
            row = []
            for dx in range(-radius, radius + 1):
                block = minescript.getblock(px + dx, layer_y, pz + dz)
                row.append(block)
            layer.append(row)

        world.append((layer_y, layer))

    return world



# --- Použití: ---
scan = scan_3d(radius=2)


def zpracujOkoli(world):
    for layer_y, layer in world:
        minescript.echo(f"[INFO] Zpracovávám vrstvu Y={layer_y}")

        for row in layer:
            processed_row = []

            for block in row:
                typ = block.split(":")[1]

                if "grass_block" in typ:
                    processed_row.append("dirt")
                elif "short_grass" in typ or "long_grass" in typ:
                    processed_row.append("grass")
                else:
                    processed_row.append(typ)

            minescript.echo(" ".join(processed_row))

zpracujOkoli(scan)