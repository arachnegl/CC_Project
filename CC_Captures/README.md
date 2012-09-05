This folder contains:

*     capture_watts.py - script for capturing watt readings from smart meter
*     cc_file_tidy_utils.py - script for sanitizing and homogenizing data produced by various capture_watts.py versions
*     rawCCdata folder contains the result of various iterations of capture_watts.py
*     cleanCCdata folder contains result of cc_file_tidy_utils.py as applied to rawCCdata

The capture script happily ran on Ubuntu 12.04 running in a virtual machine on my macbook pro. My implementation uses regular expressions to parse the message from the serial port.

To run simply type:

            $ python capture_watts.py

The script creates a file and then begins to poll a usb serial port buffer for messages every few seconds.

The message received is this format:

      <msg>  
         <src>CC128-v0.11</src>        source & software version
         <dsb>00089</dsb>              days since birth 
         <time>13:02:39</time>         Time reading - needs user config so I use computer timestamp
         <tmpr>18.7</tmpr>       
         <sensor>1</sensor>            Appliance Number as displayed
         <id>01234</id>                radio ID received from the sensor
         <type>1</type>                sensor Type, "1" = electricity
         <ch1>                         sensor channel
            <watts>00345</watts>       data and units
         </ch1>
      </msg>    

(See [official current cost xml specification](www.currentcost.com/cc128/xml.htm) for the general case and more information.)

The script parses the message using regular expressions and extracts a watt reading. It then takes the local timestamp from the users computer and records both into a csv file.

Sample output:

      2012-08-09T10:28:06,84
      2012-08-09T10:28:12,37
      2012-08-09T10:28:18,36
      2012-08-09T10:28:30,33
      2012-08-09T10:28:36,33






Also see [another version](https://github.com/JackKelly/currentCostCosmTX) that uses xml parsing and offers the option of recording data to cosm website.