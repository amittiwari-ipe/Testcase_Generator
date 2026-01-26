OBD-II

OBD-II (On Board Diagnostics) is a standardized protocol which shell allow anyone to access diagnostic vehicle data.

It is a request and response protcol where a tester initiates a communication and one or more ECUs respond.

At OBDonCAN the tester is using the fixed CAN-ID 0x7DF for 11-bit-Identifier and 0x18DB33F1 for 29-bit-Identifier.

The vehicles ECUs use the IDs 0x7E8 – 0x7EF for 11-bit-Identiiers and 0x18DA1xx for 29-bit-Identifiers to respond.

For OBDonCAN ISO-TP is used for the data exchange where the beginning of the payload is used to define the length of

the OBD-II specific data.

OBD-II defines various services for handling modes like

Service 0x01 -> Current data

Service 0x03 -> Diagnostic trouble codes

Service 0x09 -> Information data like VIN and versions
...

The service is defined by the first byte of the OBD-II payload in the request.

The following bytes define the service specific data.

18DB33F1x Tx d 8 02 01 0D 7F 00 00 83 30

                          -> 02 is the length of the ODB-II data

                                -> 01 is service 0x01 for current data

                                     -> 0D is the service 1 PID 0x0D for the vehicle speed

18DAF105x Rx d 8 03 41 0D 00 AA AA AA AA

                          -> 03 is the length of the ODB-II response data of ECU 0x05

                                -> 41 is the postive answer to service 0x01

                                     -> 0D shows that the answer belongs to PID 0x0D

                                          -> 00 is the current value for the vehicle speed ( 0 km/h)

18DB33F1x Tx d 8 02 09 02 7F 00 00 83 30

                          -> 02 is the length of the ODB-II data
                                -> 09 is service 0x09 for vehicle information data

                                     -> 02 is the id for requesting the VIN
18DAF101x Rx d 8 10 14 49 02 01 57 56 47

                           -> 10 defines that the length is sent in the next byte

                                -> 14 is the length of the ODB-II data (0x14 ->  20 byte)

                                     -> 49 is the positive response to service 0x09

                                                    -> 57 56 47 are the first 3 bytes of the VIN

18DA01F1x Tx d 8 30 00 00 7F 00 00 83 30 is the flow control frame to make the ECU sent the rest of the data

18DAF101x Rx d 8 21 5A 5A 5A 45 32 34 52

18DAF101x Rx d 8 22 45 30 32 30 32 37 34 -> these 2 frames complete the answer to the VIN 57 56 47 5A 5A 5A 45 32

34 52 45 30 32 30 32 37 34  (0x57 -> 87 -> W, 0x56 -> 86 -> V,...) -> WVGZZZE24RE020274


