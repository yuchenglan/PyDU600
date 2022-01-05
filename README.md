# PyDU600
Transfer data from DU600 spectrometers to RPi/PC/Mac

## Created and maintained by Yucheng Lan, Chiedozie Ogueri, and Tyrome Fowlkes
### DU spectrophotometers
The Beckman spectrophotometer was the first easy-to-use single instrument containing both the optical and electronic components needed for ultraviolet-absorption spectrophotometry within a single housing.  The Beckman DU UV-vis spectrophotometers, first introduced in 1941, were the first commercial scientific instruments to measure ultraviolet-visible light absorbed by substances.  The last DU spectrophotometer was produced on July 6, 1976.  There were approximately 30,000 DU spectrophotometers manufactured and sold between 1941 and 1976.  Some models can be found in present research labs because of its general "all-purpose machines".  Initial price of DU meters were roughly $700 and used DU ones are sold around $500 on eBay, making DU VIS-vis spectrometers attractiable to research laboratories.

https://en.wikipedia.org/wiki/DU_spectrophotometer
GREGORY SMUTZER, The Scientist, 15(20) (2001)27. Spectrophotometers: An Absorbing Tale

### Instrumentation
The spectrometers possess high resolution and the minimization of stray light in the ultraviolet region. A mechanism was developed to accurately control wavelength selection from a quartz prism in the spectrometers.  The optics and electronics were integrated of the spectrophotometers into a single unit that greatly simplified its use.  Light sources generate either UV or visible light, and can be either a tungsten halogen lamp for emission of visible radiation (380-780 nm), a hydrogen or deuterium discharge lamp for UV radiation (190-350 nm), or a xenon lamp that generates a continuous output of light over the UV and visible spectrum.

### Advantages
It was accurate in both the visible and ultraviolet ranges.  The practical short-wavelength limit for an absorption spectrophotometer is approximately 190 nanometers.  Some commercial UV-visible spectrophotometers extend the measurable range into the near infrared (780-3,000 nm).  For most DU UV-vis spectrometers, the spectral range is 190 - 1100 nanometers.  Their wavelength accuracy is about 0.5 nm at full range and the wavelength repeatability is about 0.2 nm at full range.  The accuracy and repeatablility are comparable to modern spectrophotometers with several even tens of thousand dollars. 

### Disadvantages of DU spectrophotometers
The software of DU meters are outdated.  The graphical user interface (GUI) of DU meters were programmed by Java?.  The data were saved in Lotus 1-2-3, the spreadsheet standard that was hugely popular in the 1980s.  Deadly, the data saved on computers can only outputted through flap disks which have been superseded by USB flash drives, or printers which can not support digital format.  It is hard to transfer data to other computers.  

Possible for update
Luckily, there is one RS232 interface at the rear of computers.  Experimental data can be transferred to other computer through the RS232 port.  For researchers who are not familar with coding, it takes some time to code.  Here we share our coding to help users to update the system.


## versions
1. Version 0.01.?21: Manually save data on RPi/PC/Mac from DU600 spectrometers.
2. Version 0.02.?: Autho save data on RPi/PC/Mac from DU600 spectrometers.
3. Version 0.03: GUI (coming)
