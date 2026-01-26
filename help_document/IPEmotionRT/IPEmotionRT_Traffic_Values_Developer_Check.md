How to Collect Required Traffic Values for Developer
Check (NoValue from A2L Measuring)

Short Description:

Sometimes a user may report that the RT Logger shows NoValue from a connected ECU during an XCP protocol
measurement. This typically indicates that the connection between the ECU and the RT Logger was not established as

expected.

In such cases, recording traffic with transmit frames can help developers understand why the connection failed or was

not as expected.

Steps to Create the Required RT Configuration:

1.  Load the customer’s RT configuration in IPEmotionRT.UI.

2.  Select the CAN connector where the A2L file was imported (the one with the measuring issue).

3.  Activate XXX Protocol Trigger and Protocol Status.

4.  Go to XXX Protocol Trigger → Tab Output and set Start Value = 0.

5.  Right-click on the CAN → Components → Add Traffic → Add Status.

6.  Select Traffic → Traffic Settings → enable Transmit frames (Tx).

7.  Go to Acquisition → add the Traffic channel and the Status to a new Storage Group.

8.  Set Mode = Triggered Data Storage → Post Trigger = 10 s → Start Trigger = XXX Protocol Trigger ≥ 0.5.

9.  In Formulas, add: Time(1) ≥ 10.

10.  In Tab Output, select XXX Protocol Trigger as the output channel.

11.  Start measuring for a while and collect several different ZIPRT and LOG files.

Expected Results:

The saved Traffic channel should show transmit frames (Tx). These logs will help the developer analyze the initial

communication attempts between the RT Logger and the ECU, and may reveal the root cause for why values are not

being displayed.


