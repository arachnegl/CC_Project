My installation only has one channel.This folder contains:

_the capture script
_the raw data
_data that has been sanitized

You can find all the scripts that did the actual work in utilities

The data transmitted from a current cost meter has this format:

      <msg>  

         <src>CC128-v0.11</src>        source & software version
   
         <dsb>00089</dsb>              days since birth
      
         <time>13:02:39</time>         Time reading needs user configuring for this reason I use computer timestamp
      
         <tmpr>18.7</tmpr>       
      
         <sensor>1</sensor>            Appliance Number as displayed
      
         <id>01234</id>                radio ID received from the sensor
      
         <type>1</type>                sensor Type, "1" = electricity
      
         <ch1>                         sensor channel
      
            <watts>00345</watts>       data and units
   
         </ch1>
   
      </msg>    

(Taken from www.currentcost.com/cc128/xml.htm)

My installation only has one channel.

