ETHERNET protocols

ECU communication on ETHERNET can be PDU or SOME/IP.

Independent of the protocol the communication ften uses a VLAN.

Additionally for security reasons the data may be encapsulated in MACsec.

MACsec (Media Access Control Security) is defined by the IEEE 802.1AE standard and allows secure communication on
Ethernet.

The MACsec header contains:

Tag Control Information (TCI/AN):    1 byte

Short Length (SL):                            1 byte (Used only for Ethernet frames shorter than 48 bytes)

Packet Number (PN):                       4 bytes (A 32-bit monotonically increasing counter to detect replay attacks)

Secure Channel Identifier (SCI):      8 bytes (Optional. Identifies the sender’s secure channel uniquely using MAC address +
port identifier. Required if the SC bit in TCI is set.).

Tag Control Information is a bit field containing:

Bit Name Description

7 C

6 E

5 SC

4 SCB

Confidentiality Enabled (1 = encryption enabled)

End Station (1 = intended for end station)
Secure Channel Identifier Present (1 = SCI field is present)
SCI Base (reserved in some cases)

3 ReservedReserved

2–0AN

Association Number (3-bit field, values 0–7)

If bit 7 (0x80) is set, the payload is encrypted, which is actually not supported.

If bit 5 (0x20) is set, SCI uis present (-> 16 byte header) other SCI is not present (-> 8 byte

header).


