J1939

IPEmotionPC with Protocols-PlugIn and IPEmotionRT support J1939 concerning signal measurement as well as

diagnostics messages.

For signal measurement IPEmotion includes a J1939 database containing  more than 4000 signals

For diagnostic messages the followind message types are supported

DM1

DM2

DM3

DM4

DM6

DM11

DM12

DM19

DM23

DM24

DM25

DM27

DM28

DM29

DM31

DM35

DM41

DM42

DM43

DM44

DM45

DM46

DM47

DM48

DM49

DM50

DM51

DM52

DM1 contains the identifier which sent the message, the lamp status, the flash status and a list of trouble codes in terms

of 4 byte DTC values (if no trouble codes exist, there might be only the identifier, map status and flash status.

As there is no common definition for storing an DM1 message, IPEmotion uses an own defined byte array using the

following structure:

typedef struct

{

    UINT32        ulIdentifier;

    UINT8        ucLampStatus;

    UINT8        ucFlashStatus;

    UINT32*        pulDtcs;

} ST_Dm1Message;

The 4 bytes of a DTC include:
FMI: byte{2] & 0x1F

OC:  byte[3] & 0x7F

SPN:(byte[0] << 0) | (byte[1] << 8) | ((byte[2] >> 5) << 16)

J1939 on CAN FD (J1939-22)

The most significant difference of J1939 on CAN FD is the usage of the newly defined Multi-PG.

This was introduced in order to be able to use the larger frame size of CAN FD by still supporting the existing PGs which

are designed for 8 byte CAN frames.

The CAN ID of a Multi-PG is set up in the style of existing PGs (Parameter Group Number, Destination Address, Source
Address, Priority).

Multi-PGs have the newly defined PGN 9472.

The payload of a Multi-PG contains a sequence of PGs including a 4 byte header including the PGN.

Data field: C-PG 1 | C-PG 2 | C-PG 3

C-PG header:

Byte 1: Bit876: TOS (Type of service)|Bit543: TF(Trailer format)|Bit2:EDP|Bit1:DP

Byte 2: PF

Byte 3: GE

Byte 4: Payload length

PGN: EDP(Extended data page)|DP(Data page)|PF(PDU format)|GE(Group extension)

40 F0 90 08 34 25 A4 1E E0 30 88 7C 40 F0 91 08 1D B5 F5 0C D8 0C FF FF 40 F0 94 08 80 BB FC 93 1D B5 1D B5

-> PGN F090 -> PGN F091 -> PGN F094


