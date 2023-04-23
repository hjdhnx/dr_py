# 需要cmder
adb connect 192.168.10.192
adb devices -l
adb logcat -c
adb logcat | grep -i QuickJS