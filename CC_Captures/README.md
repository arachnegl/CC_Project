
This folder contains:

_the capture script
_the raw data
_data that has been sanitized

You can find all the scripts that did the actual work in utilities

The data transmitted from a current cost meter has this format:

<msg>                            start of message
   <src>CC128-v0.11</src>        source & software version
   <dsb>00089</dsb>              days since birth, ie days run
   <time>13:02:39</time>         24 hour clock time as displayed
   <tmpr>18.7</tmpr>             temperature as displayed
   <sensor>1</sensor>            Appliance Number as displayed
   <id>01234</id>                radio ID received from the sensor
   <type>1</type>                sensor Type, "1" = electricity
   <ch1>                         sensor channel
      <watts>00345</watts>       data and units
   </ch1>
   <ch2>
      <watts>02151</watts>
   </ch2>
   <ch3>
      <watts>00000</watts>
   </ch3>
</msg>                           end of message

(Taken from www.currentcost.com/cc128/xml.htm)

My installation only has one channel.
