M-Gateway3

M-Gateway3 is a device that can be used in 2 modes:
In interface mode it is a PC interface with 2 CAN / CAN FD interfaces which can be connected via USB/LAN/WiFi.

For the same device only one connection will be used with the order UBS/LAN/WiFi.

In logger mode it is a RT logger with 2 CAN / CAN FD interfaces, an X-LINK interface, a ETH interface and and WiFi interfaces

(Infrastructure/AP) .

As it is not possible to use both modes in parallel, the PC mode is always prior.

As soon as a connection from a PC is setup, the M-Gateway3 will switch into PC interface mode (status LED changes from yellow to green).

One of the 2 CAN / CAN FD interfaces is supporting the M3 pogo pin connection.

Both CAN / CAN FD interfaces can be used with the D-SUB9 connector.

Both CAN / CAN FD interfaces support a termination which can be de-/activated by software.

CAN FD supports up to 8MBd.

By default the id is set to 'Gateway_xxxxx' instead of 'Logger_xxxxx' (e.g. as WiFi AP SSID) .

As a PC device the M-Gateway3 is supported in X-PlugIn, Protocols-PlugIn,... (via CAN-Server) where it can be detected and the CANs can be
configured and used.

Transmitting data of several X-devices (and/or M-devices and or other signals) with one A2L can done done by using the XCP slaves which can
be configured on the Acquisition tab.

XCP slaves can be used via LAN (ETH) and/or WiFi.

As IPEmotionRT 2025 R1 will support XCP master via WiFi, this will also enable the gateway mode for routing signals from one device to
another via WiFi.

Routing via LAN/WiFi can also be done via CMP which allows receiving traffic and/or signals.

The configuration of the logger takes place in RT.UI:

Summary:

ARM64 CPU (same as IPE833)

2 CAN, CAN FD for M devices, Traffic, Status and Protocols.

FEATURE ETH as feature connector for X devices, Traffic, Status and Protocols.

ETH for RT.UI connection and XCP slave streaming

WLAN supporting infrastructure and AP in parallel

Interface mode
If the M-Gateway3 USB driver is installed and the M-Gateway3 is connected via USB, the Windows device manager will show the M-Gateway3
as USB device:

Logger mode
Also in logger mode the M-Gateway3 can be used via RT.UI via USB.
If the USB driver for RT (IPEmotion RT Data Logger USB-Driver) is installed, the device manager will also display the M-Gateway3 as

'IPEmotion RT Data Logger'


