IPE833-001 (renaming to IPE833 from 2025 R1)
IPE833-001 is the new logger in the RT family supported from 2023 R2.1 on.

IPE833

Power-Supply: 9-36V
Operation temperature range: -40-70°C
Protection class: IP67

CPU: ARM64 bit quadcore 1.6 GHz -> please note, that so´s (UserOperation, SeedAndKey,...) need to be re-compiled against ARM64 due to the
different architecture

4GB RAM

16GB eMMC

SD card for RT obligatory (>= 8GB)

4 LEDs (Green PWR, Red ERR, Orange MEA, Yellow - RADIO): Green LED needs several seconds before coming up

4 CAN / CAN FD (up to 5MBd) including termination (via cabeling) and WakeOnCAN (global wakeup) but no Quickstart/NML with all known

components like IPE-CAN/CANdb/CCP/XCP/UDS/J1939

WakeOnRemote (DIO-0) (Please note: if logger is connected to CL30 but not CL15, the IPE833 will boot and then shutdown after having

detected, that no WakeUpReason is active).

WakeOnRTC

GPS up to 10 Hz

4 AIN (0-30V)

4 DIN (DIO-10, DIO-4, DIO-5, DIO-7)

2 DOUT (DIO-8, DIO-9)

USB 3.0 (inside) for USB-Video/Audio/iMICusb

5 GHz WiFi 802.11 ac supporting infrastructure and AP in parallel (antenna internal), no 2.4 GHz
LTE modem

1 ETH (100 MBit) for RT.UI only -> >= 2024 R1: the ETHERNET can also be used as measurement input (eg. for X devices, IP camera,...)

Interface licensing with factor 2 (identical to µCROS SL)

Internal signals for supply voltage and internal temperature (>= 2023 R3)

Gyro (angular rate, acceleration) with 100 Hz (>= 2023 R3)

Images >= 2024 R1 support CL15 natively as Owasys extended the IPE833 firmware due to our specification (CL15 level triggering was
implemented in software before).

IPE833-002 (renaming to IPE833 100 BASE-T1 from 2025 R1)
IPE833-002 is the new variant supported from 2024 R2 on.

The difference is that the ETH interface is an Automotive ETHERNET supporting master and slave mode (default is slave mode).

Being an Automotive ETHERNET, the IPE833-002 can not be connected to the PC via ETHERNET for usage with RT.UI (an adapter as ETAS

CBEB100.1 would be required in between).

The ETHERNET can be used for traffic recording, WWH-OBD, DLT, UDS, PDU, SOME/IP and XCP.

Battery mode

From 2024 R2 the batteries for IPE833 which are available from manufacturer side are supported.

They can be used to work in CAPS mode known from other loggers (Power Bad and Emergency Shutdown) or in MEA mode to continue the
measurement without CL-30 connected for up to 12 hours.

The runtime is by default using the value for the follow up time.

As soon as the value is set to a different value it will not follow this value anymore.

The signal 'Power status' has been added in order to show, in which mode (Power good, Charging, Charging suspended, Battery) the logger is
currently running.

Please note that it will take a longer time until this signal can display a valid value.

IPE833 always offers the signal 'Caps voltage' where the battery voltage can be measured.

As soon as this value fails below a limit (default 3600mV), the logger will shutdown.


