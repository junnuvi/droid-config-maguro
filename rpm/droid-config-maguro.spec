# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device maguro
%define vendor samsung
%define vendor_pretty Samsung
%define device_pretty Galaxy Nexus
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 2.0
# We assume most devices will
%define have_modem 1
%include droid-configs-device/droid-configs.inc
