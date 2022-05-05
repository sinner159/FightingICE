rem batファイルサンプル

setlocal ENABLEDELAYEDEXPANSION

rem 実行したいAIの数-1
set FIGHT_AI_NUM=1


rem 使用キャラクター
set CHARACTER=ZEN
java -cp FightingICE.jar;./lib/lwjgl/*;./lib/natives/windows/*;./lib/*;  Main --limithp 400 400 --grey-bg --inverted-player 1  --blind-player 0 --py4j

rem TIMEOUT /T -1
endlocal

exit