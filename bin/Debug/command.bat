adb shell su -c 'chmod 777 /data'
adb shell su -c './data/mem_heap 21447 sdcard/21447.mem'
adb pull sdcard/21447.mem D:\thesis\getmem_gui\bin\Debug
adb shell su -c 'rm sdcard/21447.mem'
exit
