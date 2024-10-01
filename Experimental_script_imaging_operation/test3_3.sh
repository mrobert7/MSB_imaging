#!/bin/bash
#for red and orange long pass/blue
libcamera-still --width 2312 --height 1736 --datetime -n -o /media/raspberry4/Raspi_USB/slotimaging/well3/Data3 --contrast 1.0 --brightness 0.1 --shutter 30000 --denoise off --awbgains 1.5,2.0
# -n not showing preview 
# -t preview time -t 5000
# --contrast default1.0
#--brightness -1~1 default 0 ?
#--saturation default 1
#--ev exposure compensation -10~10 default 0
#--shutter shutter speed in ms
#--gain	 akarusa?
#--awbgains 1.5,2.0   white balance
#--roi
#Set region of interest (digital zoom) e.g. 0.25,0.25,0.5,0.5
#-dt, --datetime : Replace output pattern (%d) with DateTime (MonthDayHourMinSec)
#--denoise 
#auto - default mode, use standard spatial denoising, if it is video, it will use fast color noise reduction and use high-quality color noise reduction when taking still pictures. The preview image will not use any color denoising.
#off - turn off spatial denoising and color denoising
#cdn_off - turn off color denoising
#cdn_fast - use fast color denoising
#cdn_hq - use high-quality color denoising, not suitable for video recording.
