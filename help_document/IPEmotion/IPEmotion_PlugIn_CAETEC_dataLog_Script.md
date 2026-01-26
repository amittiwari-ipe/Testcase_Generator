Manual

ARCOS
ETHOS
μCROS

Script Environment Guide

Date of issue: March 22, 2022

© Copyright 2007 - 2022 by:

IPETRONIK GmbH, Niederlassung Bergkirchen
Kreuzackerstrasse 4a
85232 Bergkirchen
Germany

All rights reserved. Any reprinting, photocopying or translation of this manual, in whole or
in part, requires advance written approval of IPETRONIK.

Pictures and sketches are for illustration purposes only and are not to be used as design
drawings nor to serve as offer or assembly drawings.

All specifications are based on the technical status of March 22, 2022. We reserve the right
to make any changes required to technically improve the equipment.

This manual has been produced with all due diligence.

IPETRONIK shall not be held liable for any damage resulting from the use of this manual,
providing it is not due to gross negligence on our own part or the part of our legal rep-
resentative or vicarious agent, and to the extent that the damage does not stem from
personal injury, bodily harm or damage to health.

All related registered brands and trademarks are the property of the respective owners.

Changesanderrorsexcepted.

1

CONTENTS

Contents

1 Using this Manual

1.1
1.2
1.3

Content . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Syntax Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2 General Script Statements

2.1

2.2

2.4

Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.1 Integers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.2 Floating-point numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.3 Strings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.4 Truth Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.5 Signal references
2.1.6 Arrays
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Persistence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.1 P_DATASET
2.2.2 P_CONFIG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.3 P_EVER . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3 Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.1 Arithmetic Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.2 Relational Operators
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.3 Logical Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.4 Binary Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Arrays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4.1 Array Expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4.2 Length . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4.3 Accessing Elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4.4 Arrays in Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.1 if
2.5.2 while / do-while . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.3 for
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.4 foreach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
User-defined Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.6.1 Declaration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.6.2 Return Value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.6.3 Calling Functions
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
System Functions
2.7.1 Writing to the Log File or File in Dataset
. . . . . . . . . . . . . . . . . .
2.7.2 System time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.8 Moving minimum and maximum . . . . . . . . . . . . . . . . . . . . . . . . . .
2.9 Mathematical Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Special Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10
2.10.1 Sending Bus Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.2 Checking Busses for Lapsed Time . . . . . . . . . . . . . . . . . . . . . .
2.10.3 User-defined Events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.4 ASCII Conversion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2.5 Conditions and Loops

2.6

2.7

Changesanderrorsexcepted.

5
5
5
5

6
6
6
6
6
7
7
8
9
9
9
9
10
10
10
10
11
11
11
12
12
12
13
13
13
13
14
14
14
15
15
16
16
16
16
17
18
18
18
18
18

2

CONTENTS

2.10.5 Char Conversion (decimal) . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.6 Char Conversion (hexadecimal) (from scriptEngine 1.6.3) . . . . . . .
2.10.7 Conversion from string to integer . . . . . . . . . . . . . . . . . . . . . .
2.10.8 Shutting Down the System . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.9 Preventing Shutdown . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.10Switching Power Out [supported only by the CAN PM interface] . . .
2.10.11Checking Signal Names . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.12Checking Method Names . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.13Checking Datafile Names . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.14Regulate Backlight
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.15Show Display Limitwarning . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.16Special Tags
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.17Dataset comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.10.18Number of CCP/XCP Station . . . . . . . . . . . . . . . . . . . . . . . .
2.10.19Number of CCP/XCP Daq Lists
. . . . . . . . . . . . . . . . . . . . . . .
2.10.20Adding Text Attachments to Datafiles . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . .
2.10.21Adding Data Attachments to Datafiles
2.11 Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3 Sending on Busses

3.1
3.2
3.3
3.4
3.5

Bus Messages
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Sending on a CAN Bus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Sending on FlexRay/LIN Bus . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Sending of ASCII-Texts or Numeric Values (CAN-Bus only) . . . . . . . . . . .
Sending of TECMP/PLP events . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4 Signals
4.1
4.2
4.3

Accessing Signal Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Script Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Digital Output Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

5 Triggers

5.1
5.2 Multi-Level
5.3
5.4 Groups
5.5
5.6

Single-Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Levels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Accessing States
Persistence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

6 Methods and datafiles
Accessing States

6.1

7 Signal engines

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

7.1

Accessing States

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

8 Storage Targets

8.1

Accessing States

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

9 OpenABK Mailboxes

9.1
9.2

Declaration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Accessing mailboxes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Changesanderrorsexcepted.

19
19
19
19
20
20
20
20
21
21
21
22
22
23
23
23
24
24

25
25
25
26
26
27

28
28
28
30

31
31
31
32
32
33
33

34
34

34
34

35
35

35
35
36

3

CONTENTS

10 Gateway

Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.1
10.2 Source with ID Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.2.1 General Format
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.2.2 Filter rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.3 Target . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.4 Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

11 Events

11.1 Cyclically Occurring Events . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Free Script Event . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.2
State Change . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.3
Received Events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.4
TECMP/PLP events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.5
11.6
Timeout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.7 Automatic Timer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.8 Manual Timer
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.9
Trigger Event . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.10 Value Change . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.11 System Events
11.12 OpenABK Key Events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.13 OpenABK Mailbox Events

12 Actions

13 Alive Counters

13.1 Declaration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13.2 CheckAlive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

14 CAN display protocol

14.1
14.2

Frame composition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Script Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14.2.1 Create CAN display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14.2.2 Configure CAN display . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14.2.3 Signal groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14.2.4 Display signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14.2.5 Send information for a signal
. . . . . . . . . . . . . . . . . . . . . . . .
14.2.6 Send information for a signalgroup . . . . . . . . . . . . . . . . . . . . .

15 Application Example

16 Appendix

16.1
Embedding in the Configuration File . . . . . . . . . . . . . . . . . . . . . . . .
16.2 Reserved Words . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Changesanderrorsexcepted.

36
36
36
37
37
37
37

39
39
39
39
39
40
41
42
42
42
42
43
43
44

45

46
46
47

48
48
48
48
49
49
50
50
51

52

53
53
53

4

1.1 CONTENT

1 Using this Manual

1.1 Content

This guide explains how scripts can be applied to control the measurement procedures of
the ARCOS and μCROS dataLog, and how they are integrated into existing configuration
files. It also provides a compact reference list of the required commands.

1.2 Scope

This document does not explain the general structure of the dataLog configuration file
(see the separate document).

1.3 Syntax Definition

In the various syntax examples, angle brackets, ’< >’, enclose placeholders, i.e. words
that are to be replaced by the user. If the placeholder must be a specific data type, this
specification is enclosed in square brackets, ’[ ]’, within the angle brackets.
Optional specifications are enclosed in double square brackets, ’[[ ]]’.

Changesanderrorsexcepted.

5

2.1 VARIABLES

2 General Script Statements

It is possible to create any number of script statements, with user-defined functions and
variables.

2.1 Variables

Variable names must begin with a letter, but otherwise may be composed of numbers
and letters. The maximum length is 40 characters.

2.1.1 Integers

Integer variables are always internally stored in signed 64-bit form. So the possible values
range from -9223372036854775808 to 9223372036854775807. As variable types, ’int’ and
’long’ can be used equivalently. Hexadecimal values are specified with a preceding
’0x’, binary values with a preceding ’0b’.

Syntax:

Examples:

int <variable name > [[= <script
expression>]];
long <variable name > [[= <script
expression>]];

int threehundred = 0x12C;
long twohundred = 0b11001000;

2.1.2 Floating-point numbers

Floating-point numbers are always internally stored in signed 64-bit form. Possible values
thus range from ±4.941*10-324 to ±1.798*10308; a point ’.’ is used as a decimal separator.
As variable types, float’ and ’double’ can be used equivalently. Variables can be reset
by using ’NaN’.

float <variable name > [[= <expression>]];
double <variable name > [[= <expression>]];

float pi = 3.1416;
double pi = 3.1416;

Syntax:

Example:

2.1.3 Strings

Strings are specified by means of the variable type ’string’, enclosed in double quotation
marks. The length of a string is theoretically infinite. The addition operator, ’+’, can be

Changesanderrorsexcepted.

6

2.1 VARIABLES

used to combine several strings. Length of a string can be returned by using its attribute
’length’. An interval [x:y] as a suffix for a string variable will return a sub-string from char-
acter x to character y (zero-based).
Escape sequences can be used within strings:
\n Newline
Tab
\t
\\ Backslash
\’
\“ Double quote

Single quote

Syntax:

Example:

string <variable name> [[= <expression>]] ;
<variable name>.length
<variable name>[<Pos 1 [int]>:<Pos 2
[int]>]

string version = "v0.3.1-beta";
int stringlength = version.length;
11
string substring = version[1:5];
„0.3.1“
string str = “line1 \n line2“;

// =

// =

2.1.4 Truth Values

A Boolean variable requires the variable type ’bool’ and can have the values ’true’ or
’false’.

Syntax:

Example:

bool <variable name > [[= <expression>]];

bool isValid = true;

2.1.5 Signal references

The variable type ’Signal’ contains a reference to a signal. All properties of the signal can
be requested from the reference. The reference variable can be passed to a user-defined
function as an argument.

Syntax:

Example:

Signal <variable name> [[= <signal name>]];

Signal sig = 'cpuload'

Changesanderrorsexcepted.

7

2.1 VARIABLES

2.1.6 Arrays

An array variable contains multiple elements of the same type. The elements can later
be read or written by using an index. Arrays can also contain other arrays as elements.
An array variable without any initializer contains no elements.

Syntax:

Example:

<element type>[] <variable name> [[=
<expression>]];

int[] array1 = [1, 2, 3, 4];
int[][] array2 = [[1, 2, 3], [4, 5]];

Changesanderrorsexcepted.

8

2.2 PERSISTENCE

2.2 Persistence

In the script, variables can be marked as persistent. When the logger is ended, their values
are stored and then imported during the next start-up. There are four optional modes for
the duration of the persistence:

2.2.1 P_DATASET

Stored data is deleted at the end of the dataset (max. FW 1.5).

Syntax:

Example:

P_DATASET <variable type> <variable name>;

P_DATASET int persistCounter;

2.2.2 P_CONFIG

Stored data is kept until a new configuration file is imported.

Syntax:

Example:

P_CONFIG <variable type> <variable name>;

P_CONFIG int persistCounter;

2.2.3 P_EVER

Stored data is never deleted.

Syntax:

Example:

P_EVER <variable type> <variable name>;

P_EVER int persistCounter;

Changesanderrorsexcepted.

9

2.3 OPERATORS

2.3 Operators

2.3.1 Arithmetic Operators

Addition, ’+’, is defined for all data types. Two integer values yield an integer result. If at
least one of the two summands is a floating-point number, then the sum is, as well. The
Boolean values ’true’ and ’false’ are interpreted numerically, as 1 and 0, respectively. The
addition operator can also be used to combine strings. If the right summand is numeric
or Boolean, then its character representation is used.

The subtraction operator, ’-’, is defined for numeric and Boolean data types. If minuend
and subtrahend are both integers, then this is also true of the result of the subtraction. In
any other case, the result is a floating-point number. The Boolean values ’true’ and ’false’
are interpreted numerically, as 1 and 0, respectively.

The multiplication operator, ’*’, is defined for numeric and Boolean data types.
If both
In any other
factors are integers, then this is also true of the result of the multiplication.
case, the result is a floating-point number. The Boolean values ’true’ and ’false’ are inter-
preted numerically, as 1 and 0, respectively.

The division operator, ’/’, is defined for numeric and Boolean data types. If dividend and
divisor are both integers, then this is also true of the result of the division. In any other case,
the result is a floating-point number. The Boolean values ’true’ and ’false’ are interpreted
numerically, as 1 and 0, respectively. Division by zero is not defined.
Example:
Both operands are integers: 1 / 2 = 0, Result is also a integer.
One or both operands are from datatype double or float: 1.0 / 2 = 0.5 Result is also a dou-
ble or float.

The modulo operator, ’%’, finds the remainder of an integer division and is only defined for
integer operands.

2.3.2 Relational Operators

The operators equal to, ’==’; and not equal to, ’!=’, are defined for two Boolean values,
two strings and two numeric values. These three types cannot be combined.

The operators, less than, ’<’; less than or equal to, ’<=’; greater than, ’>’; and greater than
or equal to, ’>=’, are defined for numeric values.

2.3.3 Logical Operators

The AND relation, ’AND’ / ’&&’; the OR relation, ’OR’ / ’||’; the exclusive OR relation,
’XOR’; and the negation, ’NOT’ / ’!’, are defined for Boolean values.

Changesanderrorsexcepted.

10

2.4 ARRAYS

2.3.4 Binary Operators

The bit-wise AND relation, ’&’; the bit-wise OR relation, ’|’; the bit-wise exclusive OR rela-
tion, ’^’; and the bit-wise negation, ’~’, are defined for integer values.

2.4 Arrays

2.4.1 Array Expressions

An array literal can be used to create an array with explicitly specified elements:

Syntax:

Example:

[ <elements> ]

[1, 2, 3, 4]
[[1, 2, 3], [10, 20]]

Alternatively the array function can be used to create an array filled with a specified num-
ber of copies of an initial value:

Syntax:

Example:

array(<number of elements>, <initializer>)

array(5, 42)

These expressions can be used at any point, where an array is accepted. They can also
be nested.

Example:

int[] a = [1, 2, 3, 4];

int[][] a = [[1, 2, 3], [10, 20]];

// set a to [42, 42, 42, 42, 42]
int[] a = array(5, 42);

// set a to [[10, 10], [10, 10], [10, 10]]
int[][] a = array(3, array(2, 10));

// set a to [[100, 100, 100], [10, 20]]
int[][] a = [array(3,100), [10, 20]];

Changesanderrorsexcepted.

11

2.4 ARRAYS

2.4.2 Length

The length of an array can be queried with the .length attribute:

Syntax:

Example:

<array>.length

int[] a = [1, 2, 3, 4];
int len = a.length; // set len to 4

2.4.3 Accessing Elements

Individual elements can be read and written by using an index:

Syntax:

Example:

<array>[<index>]

int[] a = [1, 2, 3, 4];
a[1] = 10; // a is now [1, 10, 3, 4]
int i = a[2]; // set i to 3

For nested arrays multiple indices can be used:

Example:

int[] a = [[1, 2], [3, 4]];
a[1][0] = 10; // a is now [[1, 2], [10, 4]]
int i = a[1][1]; // set i to 4

The sub-arrays of nested arrays can also be read and writted directly. Note that assigning
a sub-array to a new variable creates a copy.

Example:

int[] a = [[1, 2], [3, 4]];
a[0] = [10, 20, 30]; // a is now [[10, 20,
30], [10, 4]]
int[] sub = a[1]; // sub is now [3, 4]

2.4.4 Arrays in Functions

Arrays can be passed to and returned from functions just like other values. Note however
this this involves copying the array.

Changesanderrorsexcepted.

12

2.5 CONDITIONSANDLOOPS

Example:

int[] f(int[] arg) { arg[0] = 10; return
arg; }
int[] a = f([1, 2, 3]); // a is now [10, 2,
3]

2.5 Conditions and Loops

The script statement used in the following section consists of either a single expression with
a trailing semicolon, or a number of expressions in curly brackets.

2.5.1 if

Specification of ’else’ statements is optional.

Syntax:

if (<condition [bool]>) <statement>; [[else
<statement>;]]

Example:

if (isValid == true) num = 4; else num = 3;

2.5.2 while / do-while

’While’ means the condition is evaluated before the body of the loop is executed; ’do-
while’ means it is evaluated afterward.

while (<condition [bool]>) <statement>
do <statement> while (<condition [bool]>);

do x++; y = x * 2;
while (y <= 10) {y++;}

while (y <= 10);

Syntax:

Example:

2.5.3 for

For a ’for’ loop, three parameters are specified. The first, an expression executed once at
the beginning – usually – initializes a counter variable. The second, a condition checked
before each loop iteration, stops the execution of the loop as soon as its result is ’untrue’.
The third parameter, again an expression, is executed after each loop iteration and –
generally – increments the counter.

Changesanderrorsexcepted.

13

2.6 USER-DEFINEDFUNCTIONS

Syntax:

for (<expression>; <condition [bool]>;
<expression>)<statement>;

Example:

for (int i = 0; i < 10; i++) x = x * i;

2.5.4 foreach

A ’foreach’ is used to iterate over the lements of an array.

Syntax:

Example:

foreach (<element type> <variable name> :
<array expression>) <statement>;

int[] a = [1, 2, 3, 4];
foreach (int i : a) x += i;

Die ’foreach’ kann benutzt werden, um über die Elemente eines Arrays zu iterieren:

Syntax:

Beispiel:

foreach (<ElementTyp> <VariablenName> :
<ArrayAusdruck>) <Anweisung>;

int[] a = [1, 2, 3, 4];
foreach (int i : a) x += i;

2.6 User-defined Functions

For function names, the same conventions apply as for variables.

2.6.1 Declaration

Before each function can be used, it must first be declared in the script. Zero or any
number of parameters can be passed in a list. The data type must be defined for the
return value.
If the function is not meant to return a value, the specification should be
’void’.

Syntax:

Example:

<return data type> <function name>
(<parameter1>, <parameter2>, ...,
<parameterN>) <statement>
void AddtoValue (double d) { value = value
+ d; }

Changesanderrorsexcepted.

14

2.6 USER-DEFINEDFUNCTIONS

2.6.2 Return Value

Each function can have a return value, whose type need not be declared. The key word
’return’ may occur exactly once in the body of the function. Execution is stopped at this
point.

Syntax:

Example:

return <expression>;

int multi (int x, int y) { return x * y; }

2.6.3 Calling Functions

Once declared, a function can be used at any subsequent place in the script. All pa-
rameters must be passed as previously defined. If the given function has a return value, it
can be processed.

Example:

if (multi(5,3) != 15) error = true;

Changesanderrorsexcepted.

15

2.7 SYSTEMFUNCTIONS

2.7 System Functions

2.7.1 Writing to the Log File or File in Dataset

The command ’printf’ prints to the log file. Furthermore it is possible to write into a datafile
of type ’raw’ (since v2017.02) or a filewriter method (only v2016.10).
The first parameter is the target of the operation and can be either LOGFILE or the name
of the target file.

Syntax:

Example:

return <expression>;

printf (LOGFILE, "Variable x has the value
" + x + ".");
printf('myFile', "string1\n string2");

2.7.2 System time

The command ’system time’ returns the current system time and stores it in an integer vari-
able. Defined methods can then extract from this time stamp such discrete information as
milliseconds, minute, day or year. Microsecond (usec), millisecond (msec), second (sec),
minute (min), hour (hour), day (day), month (month) and year (year) can be accessed.
The command ’systemtimeString’ returns the system time as string.
The current measurement time (measdelay corrected system time) can be requested with
the commands ’meastime’ and ’meastimeString’.

Syntax:

Example:

int <variable name> = systemtime ();
<variable name>.<unit of time>
int time = systemtime(); int currentHour =
time.hour;

2.8 Moving minimum and maximum

The ’movingmin’ and ’movingmax’ functions return the minmum or maximum value of its
first argument during a number of previous calls. The number of stored values is given in
the second parameter, which has to be a positive integer literal.
These functions use separate value buffers for each lexical occurence in the script, mean-
ing that calls at different positions do not affect each other.

Syntax:

Example:

movingmin(<value [float]>, <num samples
[int]>)
movingmax(<value [float]>, <num samples
[int]>)
movingmin('test_sig', 100)
movingmax(x + 10, 50)

Changesanderrorsexcepted.

16

2.9 MATHEMATICALFUNCTIONS

2.9 Mathematical Functions

The following functions are available for mathematical computations. The data type of
the return value of each function is specified in square brackets.

Trigonometric functions [float]:
Trigonometric inverse functions
[float]:
Hyperbola functions [float]:
Exponential functions and
logarithms [float]:
Powers and square roots [float]:
Rounding up and down [int]:
Absolute values [float]:

cos ( a ), sin ( a ), tan ( a )
acos ( a ), asin ( a ), atan ( a )

cosh ( a ), sinh ( a ), tanh ( a )
exp ( a ), log ( a ), ln ( a )

pow ( a, b ), sqrt ( a )
ceil ( a ), floor ( a )
abs ( a )

Changesanderrorsexcepted.

17

2.10 SPECIALFUNCTIONS

2.10 Special Functions

2.10.1 Sending Bus Messages

The function ’send’ sends messages on a particular bus (see 3.2).

2.10.2 Checking Busses for Lapsed Time

The function ’check_bus’ checks whether, within a specific past time interval, messages
Instead of a single bus, it also possible to list several
have arrived on a particular bus.
busses, separated by commas. The return is a ’bool’ type value and specifies whether
traffic occurred on the bus within the specified time (in ms).

Syntax:

Example:

check_bus (<time [int]>, <bus type>,
<channel number>); check_bus (<time [int]>,
<bus alias>);
bool alive = check_bus (1000, 'PT-CAN',
CAN, 2, 'FR1');

2.10.3 User-defined Events

Specified anywhere in the script, the function ’userevent’ stores user-defined pairs, con-
sisting of a name and a pertinent value, in an internal data structure. These entries can
be processed, as required, by custom dataLog extensions and written to separate out-
put files. The first parameter must be a ’string’ type, the second can be any data type.
Sources of the latter can be variables, constants or even signal values.

Syntax:

Example:

userevent (<name [string]>, <value>);

userevent("Level of TestTrigger",
TestTrigger.level);

2.10.4 ASCII Conversion

The function ’toChar’ converts the ASCII values of printable characters into the equivalent
characters. The first parameter must be a type ’int’ and represent the ASCII value of a
printable character. The return type is ’string’.

Syntax:

Example:

toChar(<ASCII value [int]>);

string A = toChar(0x41);

Changesanderrorsexcepted.

18

2.10 SPECIALFUNCTIONS

2.10.5 Char Conversion (decimal)

With the ’toASCII’ function numeric variables can be converted into a formatted string.
For integers, the number of digits is specified in floating point numbers, the total width and
the amount of decimal places contained therein.

Syntax:

Example:

toASCII (<number/variable [int]>, <output
width [int]>);
toASCII (< number/variable [float]>,
< output width [int]>, <decimal places
[int]>);
string A = toASCII(intVar, 4);
string B = toASCII(floatVar, 8, 2);

2.10.6 Char Conversion (hexadecimal) (from scriptEngine 1.6.3)

With the ’toHexFull’ function integer variables can be converted into a hexadecimal for-
matted string. The optional secend parameters can contain the minimum width.

Syntax:

toHexFull(<number/variable [int]>,
[[<output width [int]>]]);

Example:

string A = toHexFull(intVar, 8);

2.10.7 Conversion from string to integer

With the ’toInteger’ function a string can be converted into an integer containing the
ASCII values of the string characters, e.g. ’toInteger(“ABCD”)’ returns 0x44434241. At most
the first eight characters of the string are converted.

Syntax:

Example:

toInteger (<text/variable [string]>);

int A = toInteger("ABCD");

2.10.8 Shutting Down the System

The function ’shutdown_system’ shuts down the data logger. Any normally performed
data transmissions are omitted.

Syntax:

shutdown_system ();

Changesanderrorsexcepted.

19

2.10 SPECIALFUNCTIONS

2.10.9 Preventing Shutdown

The function ’preventShutdownForSeconds’ disables the shutdown of the logger due to
a missing wake condition (KL15 or busses) for a specified amount of time (in seconds).
Manual shutdown from the webinterface or the script is not affected. The allowed time is
limited to 30 seconds.

Syntax:

Example:

preventShutdownForSeconds (<number/variable
[int]>);
preventShutdownForSeconds(10);

2.10.10 Switching Power Out [supported only by the CAN PM interface]

The function ’set_bus_power’ switches the separate power supply of a particular CAN
channel. This function is only supported by the ARCOS CAN PM (Power Management)
slide-in module.

Syntax:

Example:

set_bus_power (<bus type>, <channel
number>, <status [bool]>);
set_bus_power (<bus alias>, <status
[bool]>);
set_bus_power (CAN, 12, true);
set_bus_power ('PT_CAN', true);

2.10.11 Checking Signal Names

The function ’isValidSignal’ checks whether a signal with a given name exists. This indicates
whether an external configuration is loaded, for example. The return type is ’bool’.

Syntax:

Example:

isValidSignal<signal name [string]>);

bool extSignalPresent =
isValidSignal("extSignal");

2.10.12 Checking Method Names

The function ’isValidMethod’ checks whether a method with a given name exists. This
indicates whether an external configuration is loaded, for example. The return type is
’bool’.

Changesanderrorsexcepted.

20

2.10 SPECIALFUNCTIONS

Syntax:

Example:

isValidMethod(<method name [string]>);

bool extMethodPresent =
isValidMethod("extMethod");

2.10.13 Checking Datafile Names

The function ’isValidDatafile’ checks whether a datafile with a given name exists. This
indicates whether an external configuration is loaded, for example. The return type is
’bool’.

Syntax:

Example:

isValidDatafile(<datafile name [string]>);

bool extDatafilePresent =
isValidDatafile("extDatafile");

2.10.14 Regulate Backlight

With the ’hid_SetBacklight’ function, the backlight of an attached ABK screen can be
controlled.

Syntax:

void hid_SetBacklight (<brightness (in %)
[float]>)

Example:

hid_SetBacklight (50);

2.10.15 Show Display Limitwarning

With the ’hid_limitwarning’ function, a warning can be displayed on an attached ABK
screen. The parameters ”triggering signal” and ”limit value” are not evaluated, but simply
passed to the screen.

Changesanderrorsexcepted.

21

2.10 SPECIALFUNCTIONS

Syntax:

void hid_limitwarning (<priority (0-255)
[int]>, <class name [string]>, <triggering
signal>, <limit value [float]>, <additional
parameters (arbitrary number)>)

Syntax additional parameters: (<key [string]>, <value [string]>)

Example:

hid_limitwarning(1, "", 'cpu_temp',
80, "instruction_1", "WARNING",
"instruction_2", "CPU temperature is too
high");

2.10.16 Special Tags

With the ’specialtagvalue’ function it is possible to access tags that obtain special values
at runtime. For some dataset related tags an additional parameter containing the dataset
name is required. The following tags are available:

• fn: Frontnumber of the logger

• vin: Value of the signal with special role ”vin” (special=vin)

• odo: Value of the signal with special role ”odo” (speical=odo)

• since v2017.10: datasetglobalid: Global unique index of the dataset (requires a dataset

name as second parameter)

• since v2017.10: datasetlocalid: Local unique index of the dataset (requires a dataset

name as second parameter)

The return value of all tags is of type string.

Syntax:

Example:

string specialtagvalue(<tag [string]>[[,
<dataset name [string]>]])
string frontnumber = specialtagvalue("fn");
send (string globalid =
specialtagvalue("datasetglobalid",
"myDataset");

2.10.17 Dataset comments

Since v2017.10 configured dataset comments can be accessed with the function ’dataset-
comment’. The first parameter of this function is the key of the desired comment. As the
comments can be nested the key has to be given in namespace notation, though all
components of the key are required. The second parameter is the name of the dataset
that contains the comment.

Changesanderrorsexcepted.

22

2.10 SPECIALFUNCTIONS

Syntax:

Example:

string datasetcomment(<comment key
[string>]>, <dataset name [string]>)
string vehicletype =
datasetcomment("vehicledata::type",
"myDataset");

2.10.18 Number of CCP/XCP Station

Returns the number of CCP or XCP stations. The first argument is either ”ccp” or ”xcp”. The
second argument indicates which stations are counted and can be ”all”, ”connected”
or ”versionCheckSuccessful”. If the second argument is ommited, ”all” is used.

Syntax:

Example:

int numStations(<type [string]>[, <filter
[string]>])
int numConnectedStations =
numStations("xcp", "connected");

2.10.19 Number of CCP/XCP Daq Lists

Returns the number of CCP or XCP daq lists. The first argument is either ”ccp” or ”xcp”.
The second argument indicates which daq lists are counted and can be ”all” or ”started”.
If the second argument is ommited, ”all” is used.

Syntax:

Example:

int numDaqLists(<type [string]>[, <filter
[string]>])
int numRunningDaqLists = numDaqLists("xcp",
"started");

2.10.20 Adding Text Attachments to Datafiles

Adds a text attachment to an existing datafile. The text is stored in a separate text file,
which is then associated to the datafile in the feger header. The datafile is specified by its
configured name and the timestamp, at which the specific instance of this file was active.

Syntax:

Example:

void addTextAttachmentToDataFile(<datafile
name [string]>, <datafile timestamp
[string]>, <text [string]>)
addTextAttachmentToDataFile("parent_datafile",
meastime(), "test text");

Changesanderrorsexcepted.

23

2.11 COMMENTS

2.10.21 Adding Data Attachments to Datafiles

Associates an existing datafile as a data attachment to another existing datafile in the
feger header. Both datafiles are specified by their configured name and the timestamp,
at which the specific instance of this file was active.

Syntax:

Example:

void addDataAttachmentToDataFile(<base
datafile name [string]>, <base datafile
timestamp [string]>, <attachment datafile
name [string]>, <attachment datafile
timestamp [string]>)
addDataAttachmentToDataFile("base_datafile",
meastime(), "attachment_datafile",
meastime());

2.11 Comments

A comment in the script begins with the character combination slash - asterisk, ’/*’, and
ends with asterisk - slash, ’*/’. Alternatively, a single-line comment begins with a pair of
slashes, ’//’, and ends automatically at the next line break.

Changesanderrorsexcepted.

24

3.1 BUSMESSAGES

3 Sending on Busses

3.1 Bus Messages

Bus messages are first declared, then subsequently sent. The exact ’value’ of a bus mes-
sage is calculated at the time it is sent.

Sources can be Boolean or numeric variables, constants or the raw values of signals.
If
not all the bits of a value are to be used, an interval can be specified, enclosed in square
brackets, [<highest bit>:<lowest bit>]. The bits are always counted from 0 (the least signif-
icant bit). Boolean variables are sent as a single bit. Floating-point values are sent as a
32-bit float – followed by the specification ’float’ enclosed in square brackets – or, without
this specification, as a 64-bit double.
If no data length is specified, it is computed from the used sources.
Warning: Numeric constants and variables have an internal bit length of 64. This means,
if no interval is specified, they fill a complete CAN message!

Syntax:

Example:

MESSAGE <message name> ([[<data length in
bytes [int]>]]) { <sources > }
MESSAGE testMsg (8) { longY[23:0],
doubleX[float], 1[7:0] }

3.2 Sending on a CAN Bus

The system function ’send’ can be used to send data (bus message or integer variable)
on the CAN bus. The byte data length defined in the bus message is converted to the
appropriate DLC, which differs from the length for CAN-FD messages with more than eight
bytes. If the message is too short it is filled with zeros. The parameter ’ext. ID’ can have
the values 0 and 1 and specifies whether the following ID is from the extended range. The
optional parameters ’FDF’ (FD Frame) and ’BRS’ (Bit Rate Switch), available since v2018.06,
specify if the message schould be sent as FD frame and if the higher bit rate should be
used.

Syntax:

Example:

send (<bus message >, <CAN bus alias>,
<ext. ID>, <ID> [[, <FDF (bool)>, <BRS
(bool)>]]);
send (<data [int]>, CAN, <channel number>,
<ext. ID>, <ID> [[, <FDF (bool)>, <BRS
(bool)>]]);
send (testMsg, CAN, 8, 0, 264);
send (intVar, 'FA-CAN', 1, 4301, true,
false);

Changesanderrorsexcepted.

25

3.3 SENDINGONFLEXRAY/LINBUS

3.3 Sending on FlexRay/LIN Bus

The system function ’send’ can be used to send data (bus message or integer variable) on
the FlexRay and (since v2017.10) LIN bus. The DLC contained in the bus message is applied
when sending. If the parameter ’oneshot’ is left out or set to true, the message is sent only
once. Otherwise it is repeated until another message is sent on the same ID.

Syntax:

Example:

send (send (<bus message>, <FlexRay/LIN bus
alias >, <ID> [[, <oneshot (bool)>]] );
send (<data [int]>, FLEXRAY/LIN, <channel
number>, <ID> [[, <oneshot (bool)>]] );

send (testMsg, LIN,1, 0x100);
send (intVar, 'FR1', 1392, false);

3.4 Sending of ASCII-Texts or Numeric Values (CAN-Bus only)

The system functions ’send_text_to_can’ and ’send_number_to_can’ can be used to send
data (ASCII-texts, integer variables or bus messages) on a CAN bus.

Unique to these functions is that it is possible to specify a delay parameter (in ms). With
this the system ensures to respect a send pause between two consecutive transmissions
of the specified delay value. This is to make sure that i.E. receiver with limited processing
power won’t miss any message.

ASCII-Texts get Sent with multiple messages of up to 8 byte. Once the remaining rest of the
text to be sent is less than 8 bytes, the last messege will be transmitted with a DLC exactly
matching the remaining number of bytes to be sent.
Numeric variables always get sent with a DLC of 8 as all interger script variables have a
64-bit representation internally.
If ’send_number_to_can’ is used with a previously defined message insted of an integer
variable, it will respect the DLC defined with the definition of the bus message.

The parameter ’ext. ID’ can have the values 0 and 1 and specifies whether the following
ID is from the extended range. The optional parameters ’FDF’ (FD Frame) and ’BRS’ (Bit
Rate Switch), available since v2018.06, specify if the message schould be sent as FD frame
and if the higher bit rate should be used.

Changesanderrorsexcepted.

26

3.5 SENDINGOFTECMP/PLPEVENTS

Syntax:

Example:

send_text_to_can (<string>, <CAN bus
alias>, <ext. ID>, <ID>, <delay> [[, <FDF
(bool)>, <BRS (bool)>]]);
send_text_to_can (<string>, CAN, <channel
number>, <ext. ID>, <ID>, <delay> [[, <FDF
(bool)>, <BRS (bool)>]]);
send_number_to_can (<bus message>, <CAN bus
alias>, <ext. ID>, <ID>, <delay> [[, <FDF
(bool)>, <BRS (bool)>]]);
send_number_to_can (<data [int]>, CAN,
<channel number>, <ext. ID>, <ID>, <delay>
[[, <FDF (bool)>, <BRS (bool)>]]);
send_text_to_can ("Hello World", CAN, 8, 0,
264, 10);
send_number_to_can (intVar, 'FA-CAN', 1,
4301, 10, true, false);

3.5 Sending of TECMP/PLP events

The functions ’send_tecmp_controlmessage’, ’send_plp_userevent’ and ’send_plp_genericevent’
can be used to send TECMP/PLP events on an ethernet channel.

All functions take either the number or the alias of the ethernet channel as first argument.
For the first two functions, the second argument is the message or event ID of the event
to send. The last functions takes a MESSAGE as second arguemnt.

Syntax:

Example:

send_tecmp_controlmessage (<ETH channel
number>, <message ID>);
send_tecmp_controlmessage (<ETH channel
alias>, <message ID>);
send_plp_userevent (<ETH channel number>,
<event ID>);
send_plp_userevent (<ETH channel alias>,
<event ID>);
send_plp_genericevent (<ETH channel
number>, <message>);
send_plp_genericevent (<ETH channel alias>,
<message>);

send_tecmp_controlmessage (2, 23);
send_plp_userevent ('Test-Eth', 42);
send_plp_genericevent ('Test-Eth',
testMsg);

Changesanderrorsexcepted.

27

4.1 ACCESSINGSIGNALPROPERTIES

4 Signals

4.1 Accessing Signal Properties

Signal proerties can be accessed using the syntax <Signal>.<Property>. <Signal> is either
the name of the signal or a signal reference variable.

<Signal>.value
<Signal>.stringvalue

<Signal>.unit
<Signal>.raw

value of the signal [float/string]
string representation of the signal (e.g.
used with vtabs) [string]
unit [string]
raw value of the signal [int]

<Signal>.name
<Signal>.scale
<Signal>.offset

signal name [string]
factor of the comput. method [float]
offset of the comput. method [float]

Example:

int sigraw = 'Signal1'.raw;

4.2 Script Signals

Aside from ’real’ signals from bus sources, computed signals can be generated from parts
of the script. Using the specified sample rate (in Hz), the script expression is computed and
made available as a signal value. This signal can then be recorded by a measurement
method or presented in the display. Additionally an optional argument can be used to
mark the signal as having a special meaning. Currently the roles “vin”, ”odo”, “gps_lat”,
“gps_lon” and “gps_ele” are predefined and serve an extra purpose in dataLog.

New syntax used since dataLog 2019.10:

Changesanderrorsexcepted.

28

4.2 SCRIPTSIGNALS

Syntax:

Example:

SIGNAL <signal name> {
TERM = (<expression>);
SAMPLERATE = <sample rate [int]>;
[[ UNIT = <unit [string]>; ]]
[[ SPECIALROLE = <role [string]>; ]]
[[ COMPUMETHOD = <compumethod>; ]]
[[ DECIMALPLACES = <decimal places [int]>;
]]
}

SIGNAL odosig {
TERM = (intVarX);
SAMPLERATE = 1;
UNIT = "km";
SPECIALROLE = "odo";
COMPUMETHOD = compOdo;
DECIMALPLACES = 3;
}

Old syntax used up to dataLog 2019.06:

Syntax:

Examples:

SIGNAL <signal name> (<sample rate [int]>,
<expression>, [[<special_role [string]>]]);
SIGNAL <signal name> (<unit [string]>,
<sample rate [int]>, <expression>,
[[<special_role [string]>]]);

SIGNAL varX (100, intVarX);
SIGNAL speedMph ("mph", 1, speed);
SIGNAL odosig ("odosignal", 1, intVarX,
"odo");

Changesanderrorsexcepted.

29

4.3 DIGITALOUTPUTSIGNALS

4.3 Digital Output Signals

The script can also be used to control the digital output channels of the logger. The script
expression is processed at the specified sample rate (in Hz). If the expression returns ’true’,
the output channel specified by ’channel number’ is switched.

Syntax:

Example:

DIGITAL_OUT <signal name> (<channel number
[int]>, <sample rate [int]>, <expression>
);
DIGITAL_OUT DigOut2 (2, 10, digOut ==
true);

Changesanderrorsexcepted.

30

5.1 SINGLE-LEVEL

5 Triggers

Triggers can be defined as single-level triggers, with an optional continuity specification,
or as multi-level, finite state machines. Triggers have a duration – they remain active for as
long as the triggering condition is met.
All times must be specified in ms. Passive triggers aren’t processed. Timeouts, pre or post-
times, as well as trigger group specifications are optional. Any trigger groups that have
not been previously declared are automatically created. The individual elements must
be specified in the prescribed order.

5.1 Single-Level

In the case of single-level triggers, the continuity option specifies that the trigger is only
activated if the trigger condition remains met for the specified duration.

Syntax:

Example:

TRIGGER <trigger name> (<active [bool]>) {
TERM = (<expression [bool]>);
[[ CONTINUITY = <time [int]>; ]]
[[ TIMEOUT = <time [int]>; ]]
[[ PRETIME = <time [int]>; ]]
[[ POSTTIME = <time [int]>; ]]
[[ GROUPS (<trigger groups>); ]]
}

TRIGGER test1 (true) {
TERM = (x > 10);
CONTINUITY = 5000;
PRETIME = 10000;
POSTTIME = 500;
GROUPS (DEFAULT, 'SpecialGroup_A');
}

5.2 Multi-Level

Multi-level triggers can theoretically comprise an infinite list of levels. The starting level is
always 0; only one level can be active at any given time. Both the set condition of the
next higher and the reset condition of the current level are checked. If necessary, a level
change takes place.

Changesanderrorsexcepted.

31

5.3 LEVELS

Syntax:

Example:

TRIGGER <trigger name> (<active [bool]>) {
[[ TIMEOUT = <time [int]>; ]]
[[ PRETIME = <time [int]>; ]]
[[ POSTTIME = <time [int]>; ]]
[[ GROUPS (<trigger groups>); ]]
<level list>
}

TRIGGER test2 (true) {
PRETIME = 10000;
POSTTIME = 500;
GROUPS (DEFAULT)
LEVEL (1)
LEVEL (2)
LEVEL (3)
}

SET (x == 2); RESET (x <= 1);
(x > 2); TIMEOUT = 500;
SET (x > 10); RESET (true);

5.3 Levels

The specifications timeout, name and reset condition are optional. Levels needn’t be
consecutively numbered and are – if necessary – sorted in ascending order.
If the set
condition is defined without specifying ’SET’, the negation of the expression acts as the
reset condition. If ’true’ is specified as reset condition, the level resets as soon as it becomes
active.

LEVEL (<level number [int]> [[, <level
name>]] ){
SET (<expression [bool]>);
[[ RESET (<expression [bool]>); ]]
[[ TIMEOUT = <time [int]>; ]]
}
LEVEL (<level number [int]> [[, <level
name>]] ) {
<expression [bool]>;
[[ TIMEOUT = <time [int]>; ]]
}
See Section 5.2.

Syntax:

Example:

5.4 Groups

Trigger groups are logical relations between several individual triggers. Default is an OR
relation. To specify an AND relation, the group must be explicitly declared. Permitted
values for the mode are ’and’ and ’or’.

Changesanderrorsexcepted.

32

5.5 ACCESSINGSTATES

Syntax:

Example:

TRIGGER_GROUP (<group name>, <mode>);

TRIGGER_GROUP ('TEST_GRP3', and);

5.5 Accessing States

From the outside, it is possible to access the trigger and its states in the following ways:

<trigger name>
<trigger name>.level
<trigger name>.pre
<trigger name>.post
<trigger name>.count

trigger active [bool]
active level [int]
pre-trigger time [int]
post-trigger time [int]
trigger event counter [int]

It is possible to modify the trigger event counter from the script
environment:

Syntax:

<trigger name>.count = <trigger event
counter [int]>;

Example:

'Trig_Speed'.count = 5;

5.6 Persistence

The event counter for a trigger can be assigned a multi-level persistence – if not otherwise
specified, it persists for the duration of a data set.
The desired persistence level P_XXX (cf. Section 2.2) precedes the key word TRIGGER.

Example:

P_CONFIG TRIGGER trigger name (true) {
TERM = (isValid);}

Changesanderrorsexcepted.

33

6.1 ACCESSINGSTATES

6 Methods and datafiles

6.1 Accessing States

From the script it is possible to access the states of a method or datafile in the following
ways:

<method name>
<method name>.pre
<method name>.post
<method/datafile name>.datafiles

<method/datafile name>.datasize

recording active [bool]
pre-trigger time [int]
post-trigger time [int]
number of files in the current
dataset [int]
size of the current file in bytes [int]

For methods or datafiles using snapshot mode (Snapshot – see
the dataLog manual), the following additional parameters are
available:

<method/datafile name>.snapshots
<method/datafile name>.snapshotfiles
<method/datafile name>.snapshotsize

number of markers [int]
number of marked files [int]
total size of marked files [int]

7 Signal engines

7.1 Accessing States

From the script it is possible to access the states of signal engine stations and their DAQ
lists in the following ways:

Changesanderrorsexcepted.

34

8.1 ACCESSINGSTATES

<station name>.connected

connection state
(0: disconnected, 1: connected,
NULL: uninitialized) [double]

For CCP and XCP stations, the following additional parameters are
available:

<station name>.versioncheck_result

<station name>.versioncheck_version

<station name>.<DAQ list
name>.configured
<station name>.<DAQ list
name>.started

result of the versioncheck
(0: failed, 1: successful,
NULL: not yet checked) [double]
current version string
(only set if versioncheck was
successful) [string]
true when the DAQ list was
successfully configured [bool]
true when the DAQ list was
successfully started [bool]

8 Storage Targets

8.1 Accessing States

It is possible to access size information about connected storage media from within a
script. In order to be able to do so, the requested partition must have been given a unique
name or label beforehand. The following information is then provided:

<label>.total
<label>.used_mb

<label>.used

total size of partition in MB [double]
currently used size of partition in MB
[double]
currently used size of partition in %
[double]

Note that this information is only available while the partition is actually used.

9 OpenABK Mailboxes

openABK mailboxes can be defined in the script. The values of these mailboxes can then
be read or set from a connected openABK display.

9.1 Declaration

Mailboxes are defined with the ABKMAILBOX keyword. The name has to be identical to
the name used in the display layout.
If it contains spaces or special chars it has to be
enclosed in single quotation marks. Supported types are double, string and bool.

Changesanderrorsexcepted.

35

9.2 ACCESSINGMAILBOXES

Syntax:
Example:

ABKMAILBOX <type> <name>;
ABKMAILBOX double MyMailbox;
ABKMAILBOX string 'My String Mailbox';

9.2 Accessing mailboxes

Mailboxes can be read and written like normal variables.

Example:

MyMailbox = 10;
printf(LOGFILE, 'My String Mailbox');

10 Gateway

A gateway relays all the messages from one or more source busses to one or more target
busses. By using an ID filter and the appropriate number of filter rules, it is possible to include
or exclude individual IDs or entire ranges of IDs.
Warning: Only CAN busses are currently supported as sources or targets.

Syntax:

GATEWAY <name> { <source(s)> <target(s)> }

10.1 Source

One or more busses can be specified as a source for a gateway. Busses are addressed
either by using the combination of bus type and channel number, or by means of the
respective alias. If no ID filter is specified, all messages are relayed.

Syntax:

SOURCE (<bus>);
SOURCE (<bus>, <channelnum>);

10.2 Source with ID Filter

A source bus can be combined with a filter to restrict the IDs that are sent on. Permitted
values for the filter action are ’include’ and ’exclude’. The standard action is performed
on all IDs to which none of the specified rules apply.

Changesanderrorsexcepted.

36

10.3 TARGET

10.2.1 General Format

Syntax:

SOURCE (<bus>) {
<filter rules>
DEFAULT = <action>;}

SOURCE (<bus>, <channelnum>) {
<filter rules>
DEFAULT = <action>;}

10.2.2 Filter rules

Filter rules are applied in the order they are defined in the script. The first pertinent rule is
applied . ’Ext. ID’ can have the values ’0’ or ’1’, and specifies whether the following IDs
are from the extended range.

Syntax:

FILTERRULE (<action>, <ext. ID>, <ID>);
FILTERRULE (<action>, <ext. ID>, <StartID>,
<EndID>);

10.3 Target

One or more busses can be specified as a target for a gateway. The busses can be ad-
dressed using either the combination bus type and channel number, or by means of the
respective alias. An ID filter is not supported.

Syntax:

TARGET (<bus>);
TARGET (<bus>, <channelnum>);

10.4 Example

The following example generates a gateway for relaying messages from CAN 1 to the
FA-CAN. The IDs 0x64 bis 0xc7 – except for 105 – are to be filtered out.

Changesanderrorsexcepted.

37

10.4 EXAMPLE

Code:

GATEWAY testGW_CAN1_FACAN {
SOURCE (CAN, 1) {
FILTERRULE (include, 0, 105);
FILTERRULE (exclude, 0, 0x64, 0xc7);
DEFAULT = include;
}
TARGET ('FA-CAN');
}

Changesanderrorsexcepted.

38

11.1 CYCLICALLYOCCURRINGEVENTS

11 Events

All times are specified in ms. It is always possible to use a bus type / channel number tuple,
instead of a bus alias. Unless otherwise specified, events always occur synchronized to the
rate of measurement (1kHz).

11.1 Cyclically Occurring Events

Syntax:

Example:

EVENT <event name> CYCLE (<time [int]>);

EVENT cycle_3s CYCLE (3000);

11.2 Free Script Event

A free script event occurs if the Boolean expression yields ’true’.

Syntax:

EVENT <event name> FREE (<expression
[bool]>);

Example:

EVENT free_isValid FREE (isValid);

11.3 State Change

The events SET and RESET are comparable in their behavior to free events, except that
they only activate once, when the expression yields true (for SET) or untrue (for RESET).

Syntax:

Example:

EVENT <event name> SET (<expression
[bool]>);
EVENT <event name> RESET (<expression
[bool]>);

EVENT free_becomeValid SET (isValid);
EVENT free_becomeInvalid RESET (isValid);

11.4 Received Events

Asynchronous events occur when a signal is received – either an unspecified message on
a specific bus type, an unspecified message on a specific bus, or a specific message on
a specific bus. Aside from specifying a concrete ID, it is also possible to specify the upper
and lower limits of a range of IDs.

Changesanderrorsexcepted.

39

11.5 TECMP/PLPEVENTS

In all frame-based receive events the current frame id can be accessed via the integer
variable _ID, which is useful when receiving events on ID ranges or all busses. Additionally
_IDEXT is available for CAN and _CYCLE for FlexRay messages.
The message content is stored as an array of bytes in the variable _PAYLOAD and addi-
tionally as an integer in the variable _MESSAGE for CAN and LIN.
How to get the signal value in an signal-based receive event see subsection 4.1 Accessing
Signal Properties.

Syntax:

Example:

EVENT <event name> RECEIVE (<signal name>);
EVENT <event name> RECEIVE (<bus type>);
EVENT <event name> RECEIVE (<bus alias>);
EVENT <event name> RECEIVE (<CAN bus
alias>, <ext. ID>, <ID>);
EVENT <event name> RECEIVE (<CAN bus
alias>, <ext. ID>, <ID1>, <ID2>);
EVENT <event name> RECEIVE (<LIN bus
alias>, <ID>);
EVENT <event name> RECEIVE (<LIN bus
alias>, <ID1>, <ID2>);
EVENT <event name> RECEIVE (<FlexRay bus
alias>, <ID>, <CycleDiv>, <CycleMod>);
EVENT <event name> RECEIVE (<FlexRay
bus alias>, <ID1>, <ID2>, <CycleDiv>,
<CycleMod>);

EVENT recvTemp1 RECEIVE ('temp1sig');
EVENT recvCAN RECEIVE (CAN);
EVENT recvFR1 RECEIVE (FlexRay, 1);
EVENT recvTempMsg RECEIVE ('PT-CAN', 0,
101);
EVENT recvCAN3_100_199 RECEIVE (CAN, 3, 0,
0x64, 0xc7);

11.5 TECMP/PLP events

These events occur when either a TECMP or PLP event is received on an ethernet chan-
nel configured for TECMP or PLP. An ethernet channel number or alias can be specified
optionally.

For TECMP control message the module ID can be accessed via the integer variable
_MODULEID. The message ID is stored in the integer variable _MESSAGEID.

The probe ID of PLP event is available via the integer variable _PROBEID. For PLP user events
the event ID can be accessed via the integer variable _EVENTID. For PLP generic events
the payload is stored in the variable _PAYLOAD as an array of bytes.

Changesanderrorsexcepted.

40

11.6 TIMEOUT

Syntax:

Example:

11.6 Timeout

EVENT <event name> TECMP_CONTROLMESSAGE ();
EVENT <event name> TECMP_CONTROLMESSAGE
(<ETH channel number>);
EVENT <event name> TECMP_CONTROLMESSAGE
(<ETH channel alias>);
EVENT <event name> PLP_USEREVENT ();
EVENT <event name> PLP_USEREVENT (<ETH
channel number>);
EVENT <event name> PLP_USEREVENT (<ETH
channel alias>);
EVENT <event name> PLP_GENERICEVENT ();
EVENT <event name> PLP_GENERICEVENT (<ETH
channel number>);
EVENT <event name> PLP_GENERICEVENT (<ETH
channel alias>);

EVENT tecmpCtrl TECMP_CONTROLMESSAGE ();
EVENT plpUser PLP_USEREVENT (2);
EVENT plpGeneric PLP_GENERICEVENT
('myEth');

This event occurs when, for a specified time period, messages are not received – either any
messages on a specific bus type, any messages on a specific bus, or a specific message
on a specific bus.
The event also occurs if the specified message has never been received. Once it has
occurred, the event remains inactive until the message is received again.

Syntax:

Example:

EVENT <event name> TIMEOUT (<time [int]>,
<bus type>);
EVENT <event name> TIMEOUT (<time [int]>,
<bus alias>);
EVENT <event name> TIMEOUT (<time [int]>,
<CAN bus alias>, <ext. ID>, <ID>);
EVENT <event name> TIMEOUT (<time [int]>,
<LIN bus alias>, <ID>);
EVENT <event name> TIMEOUT (<time [int]>,
<FlexRay bus alias>, <ID>, <CycleDiv>,
<CycleMod>);

EVENT toCAN TIMEOUT (1000, CAN);
EVENT toFR1 TIMEOUT (1000, FlexRay, 1);
EVENT toTempMsg TIMEOUT (1000, 'PT-CAN', 0,
101);

Changesanderrorsexcepted.

41

11.7 AUTOMATICTIMER

11.7 Automatic Timer

The timer is automatically activated once (!) when the specified condition remains met
for the specified period of time. The name of the timer can be used to query its state; for
example, in order to use it in a trigger condition.

Syntax:

Example:

EVENT <event name> TIMER (<expression
[bool]>, <time [int]>);
TIMER <event name> (<expression [bool]>,
<time [int]>);
EVENT timer_xOddFor2sec TIMER ((x % 2 !=
0), 2000);
TIMER timer_xEvenFor2sec ((x % 2 == 0),
2000);

11.8 Manual Timer

The manual timer must be started; once the period of time expires, it activates once (!).
Stopping it resets the time to 0.

Syntax:

Example:

EVENT <event name> TIMER (<time [int]>);
<event name>.start
<event name>.stop

EVENT timer_2sec TIMER (2000);
timer_2sec.start;
timer_2sec.stop;

11.9 Trigger Event

The event occurs once (!) when the corresponding trigger is activated.

Syntax:

EVENT <event name> TRIGGER (<trigger
name>);

Example:

EVENT trig1_started TRIGGER ('trig1');

11.10 Value Change

This asynchronous event occurs when the value of a specific signal or of a specific mes-
sage on a specific bus changes.

Changesanderrorsexcepted.

42

11.11 SYSTEMEVENTS

Syntax:

Example:

EVENT <event name> UPDATE (<signal name>);
EVENT <event name> UPDATE (<CAN bus alias>,
<ext. ID>, <ID>);
EVENT <event name> UPDATE (<LIN bus alias>,
<ID>);
EVENT <event name> UPDATE (<FlexRay bus
alias>, <ID>, <CycleDiv>, <CycleMod>);

EVENT updTemp1 UPDATE ('temp1sig');
EVENT updTempMsg UPDATE ('PT-CAN', 0, 101);

11.11 System Events

System events occur on starting up and shutting down the system, on starting and ending
a measurement and on changes in the connected USB mass storage devices. A dataset
name can be added to events of type RECORDINGBEGIN and RECORDINGEND. In this
case they only occur when the recording of the specified dataset begins or ends. Other-
wise they occur when any recording begins or ends.

Syntax:

EVENT <event name> SYSTEM (STARTUP);
EVENT <event name> SYSTEM (SHUTDOWN);
EVENT <event name> SYSTEM (MEASBEGIN);
EVENT <event name> SYSTEM (MEASEND);

EVENT <event name> SYSTEM (RECORDINGBEGIN[[,
<dataset name [string]>]]);
EVENT <event name> SYSTEM (RECORDINGEND[[,
<dataset name [string]>]]);

EVENT <event name> SYSTEM (USBPLUGGED);
EVENT <event name> SYSTEM (USBUNPLUGGED);

11.12 OpenABK Key Events

For the combination of keys on the openABK input device with actions following events
If no device ID is specified, the assignment is valid for each connected
are available.
input device.

Changesanderrorsexcepted.

43

11.13 OPENABKMAILBOXEVENTS

Syntax:

Key Codes:

Key Events:

EVENT <event name> HID_KEY (<device-ID
[int]>, <key code>, <key event>, <time
[int]> );
EVENT <event name> HID_KEY (<key code>,
<key event>, <time [int]> );

HID_KEY_ROTATE_LEFT
HID_KEY_ROTATE_RIGHT
HID_KEY_ROTATE_PUSH
HID_KEY_PAGE_LEFT
HID_KEY_PAGE_RIGHT
HID_KEY_PAGE_UP
HID_KEY_PAGE_DOWN
HID_KEY_MENU
HID_KEY_BACK
HID_KEY_F1
HID_KEY_F2
HID_KEY_TRIGGER

HID_KEY_EVENT_PRESS
HID_KEY_EVENT_HOLD
HID_KEY_EVENT_RELEASE

11.13 OpenABK Mailbox Events

ABKMAILBOX events occur when an openABK mailbox updates.
caused either by a display or by the script itself.

This update can be

Syntax:

Example:

EVENT <event name> ABKMAILBOX (<mailbox
name>);

ABKMAILBOX double MyMailbox;
EVENT mailbox_event ABKMAILBOX (MyMailbox);

Changesanderrorsexcepted.

44

11.13 OPENABKMAILBOXEVENTS

12 Actions

For any event, the script can specify any number of associated actions that are executed
when the event occurs.
The following script statement consists of either a single expression, with a trailing semi-
colon; or a series of expressions, in curly brackets.
If event and action are directly combined, then there is no need to specify an event
name.

Syntax:

ON <event name> <statement>
ON EVENT <event name> <event type> (<event
parameter>) <statement>
ON EVENT <event type> (<event parameter>)
<statement>

ON outside_hot warnDriver();
ON upd_indoor_temp {
doSomething();
printf (LOGFILE, "Temp = " +
indoor_temp.value);}
ON EVENT trig1_started TRIGGER ('trig1') x
= 3.124325;
ON EVENT CYCLE (2000) { doSomethingElse();
}

Changesanderrorsexcepted.

45

13.1 DECLARATION

13 Alive Counters

Alive counters sent by control units can be monitored and their states checked whenever
required.

13.1 Declaration

In addition to the source message specification, the start and end values of the expected
range, an error value, and a timeout (in milliseconds) are specified.
Instead of ”bus type, channel number”, a bus alias can be used.
Instead of defining a new signal source, an existing signal can also be specified.
signal has its own timeout, a new specification of a timeout is optional.
However, if a timeout different from signal-specific one is to be applied, or if the signal
is to have no timeout, specifying a different value creates a copy of the signal with the
pertinent timeout.

If the

Syntax:

Example:

CHECKALIVE <name> (CAN, <channel number>,
<ext. ID>, <ID [int]>, <offset [float]>,
<scale [float]>, <bit offset [int]>, <bit
length [int]>, <data format>, <CAN format>,
<start value [int]>, <end value [int]>,
<error value [int]>, <timeout [int]>);
CHECKALIVE <name> (LIN, <channel number>,
<ID [int]>, <offset [float]>, <scale
[float]>, <bit offset [int]>, <bit length
[int]>, <data format>, <LIN format>, <start
value [int]>, <end value [int]>, <error
value [int]>, <timeout [int]>);
CHECKALIVE <name> (FlexRay, <channel num>,
<ID [int]>, <CycleDiv [int]>, <CycleMod
[int]>, <offset [float]>, <scale [float]>,
<bit offset [int]>, <bit length [int]>,
<data format>, <FlexRay format>, <start
value [int]>, <end value [int]>, <error
value [int]>, <timeout [int]>);
CHECKALIVE <name> (<signal name>, <start
value [int]>, <end value [int]>, <error
value [int]> [[, <timeout [int]> ]] );

CHECKALIVE chk_alv_test1 (CAN, 1, 0, 100,
-65.0, 0.2, 32, 16, unsigned, intel, 1,
254, 255, 1000);
CHECKALIVE chk_alv_test2
('alv_counter_sig', 1, 14, 15, 500);

Changesanderrorsexcepted.

46

13.2 CHECKALIVE

13.2 CheckAlive

Whenever required, the name of the CheckAlive object can be used to check the validity
of the last value. The name can be used analogously to a Boolean variable.

Example:

CHECKALIVE chk_alv_test (...);
if (chk_alv_test == false)
anErrorFunction();

Changesanderrorsexcepted.

47

14.1 FRAMECOMPOSITION

14 CAN display protocol

This protocol was developed in cooperation with BMW EG-7 to transmit signal values to a
CAN-based display.

14.1 Frame composition

Composition of a CAN frame:

Byte

0

1

Content VarNum Command

2 3 4 5 6 7
Data

Composition of command byte:

Byte

0 1 2 3 4

Content Attributes

Available attributes are:

5

6
Reserved Deleted Commit

7

• 0x0 -> current value

• 0x1 -> minimum value

• 0x2 -> maximum value

• 0x8 -> signal name

• 0x9 -> display name

• 0xA -> unit

• 0xB -> description

14.2 Script Commands

IDs have to be unique and >0.

14.2.1 Create CAN display

Creates CAN display with DisplayID. The optional parameters ’FDF’ (FD Frame) and ’BRS’
(Bit Rate Switch), available since v2018.06, specify if the outgoing messages schould be
sent as FD frames and if the higher bit rate should be used. This doesn’t affect messages
sent by the display.

Changesanderrorsexcepted.

48

14.2 SCRIPTCOMMANDS

Syntax:

Example:

createCanDisplay(<DisplayID>,
<DisplayName>, <BusAlias>, <ExtID>, <CANID>
[[, <FDF (bool)>, <BRS (bool)>]])
createCanDisplay(<DisplayID>,
<DisplayName>, CAN, <BusChannelNum>,
<ExtID>, <CANID> [[, <FDF (bool)>, <BRS
(bool)>]])

createCanDisplay(0x01, ''MKT View II'',
'RemoteCAN', 0, 0x14);
createCanDisplay(0x01, ''MKT View II'',
CAN, 8, 0, 0x14, true, false);

14.2.2 Configure CAN display

Sets up parameter for minimum send cycle, decimal symbol and fill characters for NaN
values.

Syntax:

setCanDisplayProperty(<DisplayID>,
<PropertyName>, <PropertyValue>)
setCanDisplayProperty(<DisplayName>,
<PropertyName>, <PropertyValue>)

PropertyName = ''min_send_cycle'' | ''decimal_symbol'' |
''no_value_fill_character''

Example:

Note:

setCanDisplayProperty(0x01,
''min_send_cycle'', ''1'');
setCanDisplayProperty(''MKT View II'',
''min_send_cycle'', ''1'');

Parameter ’PropertyValue’ will always be stated as string
in double exclamation marks.

14.2.3 Signal groups

Creates a group for signals with unified update rate.

Syntax:

Example:

createDisplaySignalGroup(<DisplayID>,
<GroupID>, <GroupName>)
createDisplaySignalGroup(<DisplayName>,
<GroupID>, <GroupName>)
createDisplaySignalGroup(0x01, 0x01, ''1
Hz'');
createDisplaySignalGroup(''MKT View II'',
0x01, ''1 Hz'');

Changesanderrorsexcepted.

49

14.2 SCRIPTCOMMANDS

14.2.4 Display signals

Creates a display signal and sets up display signal name, value width, decimal places,
display unit and display factor.

Syntax:

Example:

createDisplaySignal(<GroupID>, <SignalID>,
<SignalName>, <DisplayedSignalName>,
<ValueWidth>, <DecimalPlaces>)
createDisplaySignal(<GroupName>,
<SignalID>, <SignalName>,
<DisplayedSignalName>, <ValueWidth>,
<DecimalPlaces>)
createDisplaySignal(<GroupID>, <SignalID>,
<SignalName>, <DisplayedSignalName>,
<DisplayedUnit>, <Factor>, <ValueWidth>,
<DecimalPlaces>)
createDisplaySignal(<GroupName>,
<SignalID>, <SignalName>,
<DisplayedSignalName>, <DisplayedUnit>,
<Factor>, <ValueWidth>, <DecimalPlaces>)

createDisplaySignal(''1 Hz'', 0x01,
'measdelay', ''Measurement delay'', 8,
2);
createDisplaySignal(0x01, 0x01,
'measdelay', ''Measurement delay'', ''s'',
0.001, 8, 5);

14.2.5 Send information for a signal

Sends chosen attribute for a single signal. Available attributes are current value, min/max
values, signal name, display name, unit and description.

Syntax:

sendDisplaySignal(<DisplayID>, <SignalID>,
<AttributeName>)
sendDisplaySignal(<DisplayName>,
<SignalID>, <AttributeName>)

AttributeName = ''current'' | ''min'' | ''max'' | ''signalname'' |
''displayname'' | ''unit'' | ''description''

Example:

sendDisplaySignal(0x01, 0x04, ''current'');
sendDisplaySignal(''MKT View II'', 0x04,
''current'');

Changesanderrorsexcepted.

50

14.2 SCRIPTCOMMANDS

14.2.6 Send information for a signalgroup

Sends chosen attribute for all signals in a group. Available attributes are current value,
min/max values, signal name, display name, unit and description.

Syntax:

sendDisplaySignalGroup(<DisplayID>,
<GroupID>, <AttributeName>)
sendDisplaySignalGroup(<DisplayName>,
<GroupName>, <AttributeName>)

AttributeName = ''current'' | ''min'' | ''max'' | ''signalname'' |
''displayname'' | ''unit'' | ''description''

Example:

ssendDisplaySignalGroup(0x01, ''1 Hz'',
''displayname'');
sendDisplaySignalGroup(''MKT View II'',
0x01, ''displayname''

Changesanderrorsexcepted.

51

14.2 SCRIPTCOMMANDS

15 Application Example

The following section demonstrates the application of a simple CAN gateway, used to
manipulate the data. There are three options for relaying a message: upon receipt of the
source data; only when the signal value has changed; or at fixed, variant frequency.

This example specifies relaying the message immediately upon receipt:

ON EVENT gw1 RECEIVE (CAN, 3, 0, 100) {
send (_MESSAGE, CAN, 5, 0, 273);}

In the following example, the message is relayed upon receipt only if the value has changed:

ON EVENT gw2 UPDATE (CAN, 3, 0, 101) {
send (_MESSAGE, CAN, 5, 0, 272); }

And here, the currently valid value is sent cyclically:

long gw3_tmp_message;

ON EVENT gw3_recv RECEIVE (CAN, 1, 0, 752) {
gw3_tmp_message = _MESSAGE; }

ON EVENT gw3_cycl CYCLE (250) {
send (gw2_tmp_message, CAN, 3, 0, 43); }

Changesanderrorsexcepted.

52

16.1 EMBEDDINGINTHECONFIGURATIONFILE

16 Appendix

16.1 Embedding in the Configuration File

Scripts are embedded in the configuration file ’datalog.cfg’ in the following manner. The-
oretically, any number of scripts can be thus embedded, one after another.

<datalog_cfg>

<settings>

...

</settings>
<signals>
...

</signals>
<triggers>

...

</triggers>
<scripts>

<script>

name=scriptname
<scriptbody>

scriptcode

</scriptbody>

</script>
...

</scripts>
<methods>
...

</methods>

</datalog_cfg>

16.2 Reserved Words

The following terms (in alphabetical order) are reserved and must never be used, either
as identifiers for variables or functions, or as any other type of name:

abs, acos, AND, asin, atan, bool, BUS, can, Can, CAN, ceil, CHECKALIVE, cos, cosh, CY-
CLE, DEFAULT, do, double, else, EVENT, exp, false, FILTERRULE, flexray, Flexray, FlexRay, float,
floor, for, FREE, GATEWAY, GROUPS, HID_KEY, if, int, isValidMethod, isValidSignal, LEVEL, lin,
Lin, LIN, ln, log, LOGFILE, long, MESSAGE, ON, OR, POSTTIME, pow, PRETIME, print, printf,
P_CONFIG, P_DATASET, P_EVER, P_TRANSFER, RECEIVE, RESET, return, send, SET, set_bus_power,
shutdown_system, Signal, SIGNAL, sin, sinh, SOURCE, sqrt, string, SYSTEM, TARGET, TIMEOUT,
TIMER, toAscii, toChar, toInteger, TRACE, TRIGGER, TRIGGER_GROUP, true, UPDATE, VOID,
while, XOR

Changesanderrorsexcepted.

53


