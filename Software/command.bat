adb shell su -c 'chmod 777 /data'
adb shell su -c './data/mem_heap 23628 sdcard/23628.mem'
adb pull sdcard/23628.mem D:\thesis\getmem_gui - 副本\bin\Debug
adb shell su -c 'rm sdcard/23628.mem'
exit
