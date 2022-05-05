setlocal ENABLEDELAYEDEXPANSION

set FIGHT_AI_NUM=1
set CHARACTER=ZEN
start java -cp FightingICE.jar;./lib/lwjgl/*;./lib/natives/windows/*;./lib/*;  Main --limithp 400 400 --grey-bg --blind-player 0 --py4j
