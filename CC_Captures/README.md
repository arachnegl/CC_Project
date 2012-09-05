This folder contains:

_the capture script
_the raw data
_data that has been sanitized

You can find all the scripts that did the actual work in utilities

The data transmitted from my current cost meter has this format:

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

See [official current cost xml specification](www.currentcost.com/cc128/xml.htm) for the general case and more information.

The capture script happily ran on Ubuntu 12.04 running in a virtual machine on my macbook pro. My implementation uses regular expressions to parse the message from the serial port.

To run simply type:

            $ python capture_watts.py

Also see [another version](https://github.com/JackKelly/currentCostCosmTX) that uses xml parsing and offers the option of recording data to cosm website.

