[app]
title = AirDesk Native Pro
package.name = airdesknative
package.domain = org.airdesk
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 2.5
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Full Android 15 (API 35) + Modern 64-bit Support + Local Hotspot HTTP Cleartext
android.api = 35
android.minapi = 24
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, ACCESS_WIFI_STATE, ACCESS_NETWORK_STATE, CHANGE_WIFI_MULTICAST_STATE, CAMERA
android.extra_manifest_application_arguments = android:usesCleartextTraffic="true"
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
