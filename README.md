# PyMine bot

Implementation of minescript mod.

I use minecraft java edition with version 1.21.10 and installed [fabric](https://fabricmc.net/use/installer/),
[fabric API](https://www.curseforge.com/minecraft/mc-mods/fabric-api) and most importantli [minescript](https://minescript.net/)

## Choose-best

This script choose the best tool for what you are looking at. If you don't have pickaxe, axe or shovel and looking at somethink that is for this tool, it get exception and ende with error. That is what you can end running the script. If you don't have pickaxe it won't start because pickaxe is default tool.

### How to run

Params.:

```minecraft-chat
\choose-best [iterations] [sleep]
```

where iterations is number of trying to choose the best tool and sleep is time between these iterations. Default is 100 for iterations and 0.1 for sleep
