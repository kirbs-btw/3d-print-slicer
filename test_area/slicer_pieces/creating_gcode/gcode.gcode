; Bastian Lipka
M140 S60
M105
M190 S60
M104 S195
M105
M109 S195
M82 ;absolute extrusion mode
G21 ;metric values
G90 ;absolute positioning
M82 ;set extruder to absolute mode
M107 ;start with the fan off
G28 X0 Y0 ;move X/Y to min endstops
G28 Z0 ;move Z to min endstops
G1 Z15.0 F100 ;move the platform down 15mm
G92 E0 ;zero the extruded length
G1 F200 E3 ;extrude 3mm of feed stock
G92 E0 ;zero the extruded length again
G1 F100
M117 Printing...
G5
G92 E0
G1 F2400 E-6
;LAYER_COUNT:2
;LAYER:0
M106 S255 ;set fan speed
M204 S3000
M205 X10 Y10
G0 Z0
G1 X50.0 Y50.0 E0.125
G1 X50.0 Y50.25 E0.125
G1 X50.0 Y50.25 E5.0
G1 X50.0 Y60.0 E5.0
G1 X50.0 Y60.0 E5.375
G1 X50.75 Y60.0 E5.375
G1 X50.75 Y60.0 E20.0
G1 X80.0 Y60.0 E20.0
G1 X80.0 Y60.0 E20.125
G1 X80.0 Y59.75 E20.125
G1 X80.0 Y59.75 E25.0
G1 X80.0 Y50.0 E25.0
G1 X80.0 Y50.0 E25.375
G1 X79.25 Y50.0 E25.375
G1 X79.25 Y50.0 E40.0
G1 X50.0 Y50.0 E40.0
G0 Z1.2500000000000036
;LAYER:1
G1 X50.0 Y50.0 E40.25
G1 X50.0 Y50.5 E40.25
G1 X50.0 Y50.5 E45.0
G1 X50.0 Y60.0 E45.0
G1 X50.0 Y60.0 E45.75
G1 X51.5 Y60.0 E45.75
G1 X51.5 Y60.0 E60.0
G1 X80.0 Y60.0 E60.0
G1 X80.0 Y60.0 E60.25
G1 X80.0 Y59.5 E60.25
G1 X80.0 Y59.5 E65.0
G1 X80.0 Y50.0 E65.0
G1 X80.0 Y50.0 E65.75
G1 X78.5 Y50.0 E65.75
G1 X78.5 Y50.0 E80.0
G1 X50.0 Y50.0 E80.0
G0 Z2.4999999999999964
;LAYER:2
G1 X50.0 Y50.0 E80.375
G1 X50.0 Y50.75 E80.375
G1 X50.0 Y50.75 E85.0
G1 X50.0 Y60.0 E85.0
G1 X50.0 Y60.0 E86.125
G1 X52.25 Y60.0 E86.125
G1 X52.25 Y60.0 E100.0
G1 X80.0 Y60.0 E100.0
G1 X80.0 Y60.0 E100.375
G1 X80.0 Y59.25 E100.375
G1 X80.0 Y59.25 E105.0
G1 X80.0 Y50.0 E105.0
G1 X80.0 Y50.0 E106.125
G1 X77.75 Y50.0 E106.125
G1 X77.75 Y50.0 E120.0
G1 X50.0 Y50.0 E120.0
G0 Z3.75
;LAYER:3
G1 X50.0 Y50.0 E120.5
G1 X50.0 Y51.0 E120.5
G1 X50.0 Y51.0 E125.0
G1 X50.0 Y60.0 E125.0
G1 X50.0 Y60.0 E126.5
G1 X53.0 Y60.0 E126.5
G1 X53.0 Y60.0 E140.0
G1 X80.0 Y60.0 E140.0
G1 X80.0 Y60.0 E140.5
G1 X80.0 Y59.0 E140.5
G1 X80.0 Y59.0 E145.0
G1 X80.0 Y50.0 E145.0
G1 X80.0 Y50.0 E146.5
G1 X77.0 Y50.0 E146.5
G1 X77.0 Y50.0 E160.0
G1 X50.0 Y50.0 E160.0
G0 Z5.0
;LAYER:4
G1 X50.0 Y50.0 E160.625
G1 X50.0 Y51.25 E160.625
G1 X50.0 Y51.25 E165.0
G1 X50.0 Y60.0 E165.0
G1 X50.0 Y60.0 E166.875
G1 X53.75 Y60.0 E166.875
G1 X53.75 Y60.0 E180.0
G1 X80.0 Y60.0 E180.0
G1 X80.0 Y60.0 E180.625
G1 X80.0 Y58.75 E180.625
G1 X80.0 Y58.75 E185.0
G1 X80.0 Y50.0 E185.0
G1 X80.0 Y50.0 E186.875
G1 X76.25 Y50.0 E186.875
G1 X76.25 Y50.0 E200.0
G1 X50.0 Y50.0 E200.0
G0 Z6.25
;LAYER:5
G1 X50.0 Y50.0 E200.75
G1 X50.0 Y51.5 E200.75
G1 X50.0 Y51.5 E205.0
G1 X50.0 Y60.0 E205.0
G1 X50.0 Y60.0 E207.25
G1 X54.5 Y60.0 E207.25
G1 X54.5 Y60.0 E220.0
G1 X80.0 Y60.0 E220.0
G1 X80.0 Y60.0 E220.75
G1 X80.0 Y58.5 E220.75
G1 X80.0 Y58.5 E225.0
G1 X80.0 Y50.0 E225.0
G1 X80.0 Y50.0 E227.25
G1 X75.5 Y50.0 E227.25
G1 X75.5 Y50.0 E240.0
G1 X50.0 Y50.0 E240.0
G0 Z7.5000000000000036
;LAYER:6
G1 X50.0 Y50.0 E240.875
G1 X50.0 Y51.75 E240.875
G1 X50.0 Y51.75 E245.0
G1 X50.0 Y60.0 E245.0
G1 X50.0 Y60.0 E247.625
G1 X55.25 Y60.0 E247.625
G1 X55.25 Y60.0 E260.0
G1 X80.0 Y60.0 E260.0
G1 X80.0 Y60.0 E260.875
G1 X80.0 Y58.25 E260.875
G1 X80.0 Y58.25 E265.0
G1 X80.0 Y50.0 E265.0
G1 X80.0 Y50.0 E267.625
G1 X74.75 Y50.0 E267.625
G1 X74.75 Y50.0 E280.0
G1 X50.0 Y50.0 E280.0
G0 Z8.749999999999998
;LAYER:7
G1 X50.0 Y50.0 E281.0
G1 X50.0 Y52.0 E281.0
G1 X50.0 Y52.0 E285.0
G1 X50.0 Y60.0 E285.0
G1 X50.0 Y60.0 E288.0
G1 X56.0 Y60.0 E288.0
G1 X56.0 Y60.0 E300.0
G1 X80.0 Y60.0 E300.0
G1 X80.0 Y60.0 E301.0
G1 X80.0 Y58.0 E301.0
G1 X80.0 Y58.0 E305.0
G1 X80.0 Y50.0 E305.0
G1 X80.0 Y50.0 E308.0
G1 X74.0 Y50.0 E308.0
G1 X74.0 Y50.0 E320.0
G1 X50.0 Y50.0 E320.0
G0 Z9.999999999999998
;LAYER:8
G1 X50.0 Y50.0 E321.125
G1 X50.0 Y52.25 E321.125
G1 X50.0 Y52.25 E325.0
G1 X50.0 Y60.0 E325.0
G1 X50.0 Y60.0 E328.375
G1 X56.75 Y60.0 E328.375
G1 X56.75 Y60.0 E340.0
G1 X80.0 Y60.0 E340.0
G1 X80.0 Y60.0 E341.125
G1 X80.0 Y57.75 E341.125
G1 X80.0 Y57.75 E345.0
G1 X80.0 Y50.0 E345.0
G1 X80.0 Y50.0 E348.375
G1 X73.25 Y50.0 E348.375
G1 X73.25 Y50.0 E360.0
G1 X50.0 Y50.0 E360.0
G0 Z11.25
;LAYER:9
G1 X50.0 Y50.0 E361.25
G1 X50.0 Y52.5 E361.25
G1 X50.0 Y52.5 E365.0
G1 X50.0 Y60.0 E365.0
G1 X50.0 Y60.0 E368.75
G1 X57.5 Y60.0 E368.75
G1 X57.5 Y60.0 E380.0
G1 X80.0 Y60.0 E380.0
G1 X80.0 Y60.0 E381.25
G1 X80.0 Y57.5 E381.25
G1 X80.0 Y57.5 E385.0
G1 X80.0 Y50.0 E385.0
G1 X80.0 Y50.0 E388.75
G1 X72.5 Y50.0 E388.75
G1 X72.5 Y50.0 E400.0
G1 X50.0 Y50.0 E400.0
G0 Z12.500000000000002
;LAYER:10
G1 X50.0 Y50.0 E401.375
G1 X50.0 Y52.75 E401.375
G1 X50.0 Y52.75 E405.0
G1 X50.0 Y60.0 E405.0
G1 X50.0 Y60.0 E409.125
G1 X58.25 Y60.0 E409.125
G1 X58.25 Y60.0 E420.0
G1 X80.0 Y60.0 E420.0
G1 X80.0 Y60.0 E421.375
G1 X80.0 Y57.25 E421.375
G1 X80.0 Y57.25 E425.0
G1 X80.0 Y50.0 E425.0
G1 X80.0 Y50.0 E429.125
G1 X71.75 Y50.0 E429.125
G1 X71.75 Y50.0 E440.0
G1 X50.0 Y50.0 E440.0
G0 Z13.750000000000002
;LAYER:11
G1 X50.0 Y50.0 E441.5
G1 X50.0 Y53.0 E441.5
G1 X50.0 Y53.0 E445.0
G1 X50.0 Y60.0 E445.0
G1 X50.0 Y60.0 E449.5
G1 X59.0 Y60.0 E449.5
G1 X59.0 Y60.0 E460.0
G1 X80.0 Y60.0 E460.0
G1 X80.0 Y60.0 E461.5
G1 X80.0 Y57.0 E461.5
G1 X80.0 Y57.0 E465.0
G1 X80.0 Y50.0 E465.0
G1 X80.0 Y50.0 E469.5
G1 X71.0 Y50.0 E469.5
G1 X71.0 Y50.0 E480.0
G1 X50.0 Y50.0 E480.0
G0 Z14.999999999999998
;LAYER:12
G1 X50.0 Y50.0 E481.625
G1 X50.0 Y53.25 E481.625
G1 X50.0 Y53.25 E485.0
G1 X50.0 Y60.0 E485.0
G1 X50.0 Y60.0 E489.875
G1 X59.75 Y60.0 E489.875
G1 X59.75 Y60.0 E500.0
G1 X80.0 Y60.0 E500.0
G1 X80.0 Y60.0 E501.625
G1 X80.0 Y56.75 E501.625
G1 X80.0 Y56.75 E505.0
G1 X80.0 Y50.0 E505.0
G1 X80.0 Y50.0 E509.875
G1 X70.25 Y50.0 E509.875
G1 X70.25 Y50.0 E520.0
G1 X50.0 Y50.0 E520.0
G0 Z16.25
;LAYER:13
G1 X50.0 Y50.0 E521.75
G1 X50.0 Y53.5 E521.75
G1 X50.0 Y53.5 E525.0
G1 X50.0 Y60.0 E525.0
G1 X50.0 Y60.0 E530.25
G1 X60.5 Y60.0 E530.25
G1 X60.5 Y60.0 E540.0
G1 X80.0 Y60.0 E540.0
G1 X80.0 Y60.0 E541.75
G1 X80.0 Y56.5 E541.75
G1 X80.0 Y56.5 E545.0
G1 X80.0 Y50.0 E545.0
G1 X80.0 Y50.0 E550.25
G1 X69.5 Y50.0 E550.25
G1 X69.5 Y50.0 E560.0
G1 X50.0 Y50.0 E560.0
G0 Z17.5
;LAYER:14
G1 X50.0 Y50.0 E561.875
G1 X50.0 Y53.75 E561.875
G1 X50.0 Y53.75 E565.0
G1 X50.0 Y60.0 E565.0
G1 X50.0 Y60.0 E570.625
G1 X61.25 Y60.0 E570.625
G1 X61.25 Y60.0 E580.0
G1 X80.0 Y60.0 E580.0
G1 X80.0 Y60.0 E581.875
G1 X80.0 Y56.25 E581.875
G1 X80.0 Y56.25 E585.0
G1 X80.0 Y50.0 E585.0
G1 X80.0 Y50.0 E590.625
G1 X68.75 Y50.0 E590.625
G1 X68.75 Y50.0 E600.0
G1 X50.0 Y50.0 E600.0
G0 Z18.75
;LAYER:15
G1 X50.0 Y50.0 E602.0
G1 X50.0 Y54.0 E602.0
G1 X50.0 Y54.0 E605.0
G1 X50.0 Y60.0 E605.0
G1 X50.0 Y60.0 E611.0
G1 X62.0 Y60.0 E611.0
G1 X62.0 Y60.0 E620.0
G1 X80.0 Y60.0 E620.0
G1 X80.0 Y60.0 E622.0
G1 X80.0 Y56.0 E622.0
G1 X80.0 Y56.0 E625.0
G1 X80.0 Y50.0 E625.0
G1 X80.0 Y50.0 E631.0
G1 X68.0 Y50.0 E631.0
G1 X68.0 Y50.0 E640.0
G1 X50.0 Y50.0 E640.0
G0 Z20.000000000000004
;LAYER:16
G1 X50.0 Y50.0 E642.125
G1 X50.0 Y54.25 E642.125
G1 X50.0 Y54.25 E645.0
G1 X50.0 Y60.0 E645.0
G1 X50.0 Y60.0 E651.375
G1 X62.75 Y60.0 E651.375
G1 X62.75 Y60.0 E660.0
G1 X80.0 Y60.0 E660.0
G1 X80.0 Y60.0 E662.125
G1 X80.0 Y55.75 E662.125
G1 X80.0 Y55.75 E665.0
G1 X80.0 Y50.0 E665.0
G1 X80.0 Y50.0 E671.375
G1 X67.25 Y50.0 E671.375
G1 X67.25 Y50.0 E680.0
G1 X50.0 Y50.0 E680.0
G0 Z21.249999999999996
;LAYER:17
G1 X50.0 Y50.0 E682.25
G1 X50.0 Y54.5 E682.25
G1 X50.0 Y54.5 E685.0
G1 X50.0 Y60.0 E685.0
G1 X50.0 Y60.0 E691.75
G1 X63.5 Y60.0 E691.75
G1 X63.5 Y60.0 E700.0
G1 X80.0 Y60.0 E700.0
G1 X80.0 Y60.0 E702.25
G1 X80.0 Y55.5 E702.25
G1 X80.0 Y55.5 E705.0
G1 X80.0 Y50.0 E705.0
G1 X80.0 Y50.0 E711.75
G1 X66.5 Y50.0 E711.75
G1 X66.5 Y50.0 E720.0
G1 X50.0 Y50.0 E720.0
G0 Z22.5
;LAYER:18
G1 X50.0 Y50.0 E722.375
G1 X50.0 Y54.75 E722.375
G1 X50.0 Y54.75 E725.0
G1 X50.0 Y60.0 E725.0
G1 X50.0 Y60.0 E732.125
G1 X64.25 Y60.0 E732.125
G1 X64.25 Y60.0 E740.0
G1 X80.0 Y60.0 E740.0
G1 X80.0 Y60.0 E742.375
G1 X80.0 Y55.25 E742.375
G1 X80.0 Y55.25 E745.0
G1 X80.0 Y50.0 E745.0
G1 X80.0 Y50.0 E752.125
G1 X65.75 Y50.0 E752.125
G1 X65.75 Y50.0 E760.0
G1 X50.0 Y50.0 E760.0
G0 Z23.75
;LAYER:19
G1 X50.0 Y50.0 E762.5
G1 X50.0 Y55.0 E762.5
G1 X50.0 Y55.0 E765.0
G1 X50.0 Y60.0 E765.0
G1 X50.0 Y60.0 E772.5
G1 X65.0 Y60.0 E772.5
G1 X65.0 Y60.0 E780.0
G1 X80.0 Y60.0 E780.0
G1 X80.0 Y60.0 E782.5
G1 X80.0 Y55.0 E782.5
G1 X80.0 Y55.0 E785.0
G1 X80.0 Y50.0 E785.0
G1 X80.0 Y50.0 E792.5
G1 X65.0 Y50.0 E792.5
G1 X65.0 Y50.0 E800.0
G1 X50.0 Y50.0 E800.0
G0 Z25.0
;LAYER:20
G1 X50.0 Y50.0 E802.625
G1 X50.0 Y55.25 E802.625
G1 X50.0 Y55.25 E805.0
G1 X50.0 Y60.0 E805.0
G1 X50.0 Y60.0 E812.875
G1 X65.75 Y60.0 E812.875
G1 X65.75 Y60.0 E820.0
G1 X80.0 Y60.0 E820.0
G1 X80.0 Y60.0 E822.625
G1 X80.0 Y54.75 E822.625
G1 X80.0 Y54.75 E825.0
G1 X80.0 Y50.0 E825.0
G1 X80.0 Y50.0 E832.875
G1 X64.25 Y50.0 E832.875
G1 X64.25 Y50.0 E840.0
G1 X50.0 Y50.0 E840.0
G0 Z26.250000000000004
;LAYER:21
G1 X50.0 Y50.0 E842.75
G1 X50.0 Y55.5 E842.75
G1 X50.0 Y55.5 E845.0
G1 X50.0 Y60.0 E845.0
G1 X50.0 Y60.0 E853.25
G1 X66.5 Y60.0 E853.25
G1 X66.5 Y60.0 E860.0
G1 X80.0 Y60.0 E860.0
G1 X80.0 Y60.0 E862.75
G1 X80.0 Y54.5 E862.75
G1 X80.0 Y54.5 E865.0
G1 X80.0 Y50.0 E865.0
G1 X80.0 Y50.0 E873.25
G1 X63.5 Y50.0 E873.25
G1 X63.5 Y50.0 E880.0
G1 X50.0 Y50.0 E880.0
G0 Z27.499999999999996
;LAYER:22
G1 X50.0 Y50.0 E882.875
G1 X50.0 Y55.75 E882.875
G1 X50.0 Y55.75 E885.0
G1 X50.0 Y60.0 E885.0
G1 X50.0 Y60.0 E893.625
G1 X67.25 Y60.0 E893.625
G1 X67.25 Y60.0 E900.0
G1 X80.0 Y60.0 E900.0
G1 X80.0 Y60.0 E902.875
G1 X80.0 Y54.25 E902.875
G1 X80.0 Y54.25 E905.0
G1 X80.0 Y50.0 E905.0
G1 X80.0 Y50.0 E913.625
G1 X62.75 Y50.0 E913.625
G1 X62.75 Y50.0 E920.0
G1 X50.0 Y50.0 E920.0
G0 Z28.75
;LAYER:23
G1 X50.0 Y50.0 E923.0
G1 X50.0 Y56.0 E923.0
G1 X50.0 Y56.0 E925.0
G1 X50.0 Y60.0 E925.0
G1 X50.0 Y60.0 E934.0
G1 X68.0 Y60.0 E934.0
G1 X68.0 Y60.0 E940.0
G1 X80.0 Y60.0 E940.0
G1 X80.0 Y60.0 E943.0
G1 X80.0 Y54.0 E943.0
G1 X80.0 Y54.0 E945.0
G1 X80.0 Y50.0 E945.0
G1 X80.0 Y50.0 E954.0
G1 X62.0 Y50.0 E954.0
G1 X62.0 Y50.0 E960.0
G1 X50.0 Y50.0 E960.0
G0 Z30.0
;LAYER:24
G1 X50.0 Y50.0 E963.125
G1 X50.0 Y56.25 E963.125
G1 X50.0 Y56.25 E965.0
G1 X50.0 Y60.0 E965.0
G1 X50.0 Y60.0 E974.375
G1 X68.75 Y60.0 E974.375
G1 X68.75 Y60.0 E980.0
G1 X80.0 Y60.0 E980.0
G1 X80.0 Y60.0 E983.125
G1 X80.0 Y53.75 E983.125
G1 X80.0 Y53.75 E985.0
G1 X80.0 Y50.0 E985.0
G1 X80.0 Y50.0 E994.375
G1 X61.25 Y50.0 E994.375
G1 X61.25 Y50.0 E1000.0
G1 X50.0 Y50.0 E1000.0
G0 Z31.25
;LAYER:25
G1 X50.0 Y50.0 E1003.25
G1 X50.0 Y56.5 E1003.25
G1 X50.0 Y56.5 E1005.0
G1 X50.0 Y60.0 E1005.0
G1 X50.0 Y60.0 E1014.75
G1 X69.5 Y60.0 E1014.75
G1 X69.5 Y60.0 E1020.0
G1 X80.0 Y60.0 E1020.0
G1 X80.0 Y60.0 E1023.25
G1 X80.0 Y53.5 E1023.25
G1 X80.0 Y53.5 E1025.0
G1 X80.0 Y50.0 E1025.0
G1 X80.0 Y50.0 E1034.75
G1 X60.5 Y50.0 E1034.75
G1 X60.5 Y50.0 E1040.0
G1 X50.0 Y50.0 E1040.0
G0 Z32.5
;LAYER:26
G1 X50.0 Y50.0 E1043.375
G1 X50.0 Y56.75 E1043.375
G1 X50.0 Y56.75 E1045.0
G1 X50.0 Y60.0 E1045.0
G1 X50.0 Y60.0 E1055.125
G1 X70.25 Y60.0 E1055.125
G1 X70.25 Y60.0 E1060.0
G1 X80.0 Y60.0 E1060.0
G1 X80.0 Y60.0 E1063.375
G1 X80.0 Y53.25 E1063.375
G1 X80.0 Y53.25 E1065.0
G1 X80.0 Y50.0 E1065.0
G1 X80.0 Y50.0 E1075.125
G1 X59.75 Y50.0 E1075.125
G1 X59.75 Y50.0 E1080.0
G1 X50.0 Y50.0 E1080.0
G0 Z33.75
;LAYER:27
G1 X50.0 Y50.0 E1083.5
G1 X50.0 Y57.0 E1083.5
G1 X50.0 Y57.0 E1085.0
G1 X50.0 Y60.0 E1085.0
G1 X50.0 Y60.0 E1095.5
G1 X71.0 Y60.0 E1095.5
G1 X71.0 Y60.0 E1100.0
G1 X80.0 Y60.0 E1100.0
G1 X80.0 Y60.0 E1103.5
G1 X80.0 Y53.0 E1103.5
G1 X80.0 Y53.0 E1105.0
G1 X80.0 Y50.0 E1105.0
G1 X80.0 Y50.0 E1115.5
G1 X59.0 Y50.0 E1115.5
G1 X59.0 Y50.0 E1120.0
G1 X50.0 Y50.0 E1120.0
G0 Z35.0
;LAYER:28
G1 X50.0 Y50.0 E1123.625
G1 X50.0 Y57.25 E1123.625
G1 X50.0 Y57.25 E1125.0
G1 X50.0 Y60.0 E1125.0
G1 X50.0 Y60.0 E1135.875
G1 X71.75 Y60.0 E1135.875
G1 X71.75 Y60.0 E1140.0
G1 X80.0 Y60.0 E1140.0
G1 X80.0 Y60.0 E1143.625
G1 X80.0 Y52.75 E1143.625
G1 X80.0 Y52.75 E1145.0
G1 X80.0 Y50.0 E1145.0
G1 X80.0 Y50.0 E1155.875
G1 X58.25 Y50.0 E1155.875
G1 X58.25 Y50.0 E1160.0
G1 X50.0 Y50.0 E1160.0
G0 Z36.25
;LAYER:29
G1 X50.0 Y50.0 E1163.75
G1 X50.0 Y57.5 E1163.75
G1 X50.0 Y57.5 E1165.0
G1 X50.0 Y60.0 E1165.0
G1 X50.0 Y60.0 E1176.25
G1 X72.5 Y60.0 E1176.25
G1 X72.5 Y60.0 E1180.0
G1 X80.0 Y60.0 E1180.0
G1 X80.0 Y60.0 E1183.75
G1 X80.0 Y52.5 E1183.75
G1 X80.0 Y52.5 E1185.0
G1 X80.0 Y50.0 E1185.0
G1 X80.0 Y50.0 E1196.25
G1 X57.5 Y50.0 E1196.25
G1 X57.5 Y50.0 E1200.0
G1 X50.0 Y50.0 E1200.0
G0 Z37.5
;LAYER:30
G1 X50.0 Y50.0 E1203.875
G1 X50.0 Y57.75 E1203.875
G1 X50.0 Y57.75 E1205.0
G1 X50.0 Y60.0 E1205.0
G1 X50.0 Y60.0 E1216.625
G1 X73.25 Y60.0 E1216.625
G1 X73.25 Y60.0 E1220.0
G1 X80.0 Y60.0 E1220.0
G1 X80.0 Y60.0 E1223.875
G1 X80.0 Y52.25 E1223.875
G1 X80.0 Y52.25 E1225.0
G1 X80.0 Y50.0 E1225.0
G1 X80.0 Y50.0 E1236.625
G1 X56.75 Y50.0 E1236.625
G1 X56.75 Y50.0 E1240.0
G1 X50.0 Y50.0 E1240.0
G0 Z38.75
;LAYER:31
G1 X50.0 Y50.0 E1244.0
G1 X50.0 Y58.0 E1244.0
G1 X50.0 Y58.0 E1245.0
G1 X50.0 Y60.0 E1245.0
G1 X50.0 Y60.0 E1257.0
G1 X74.0 Y60.0 E1257.0
G1 X74.0 Y60.0 E1260.0
G1 X80.0 Y60.0 E1260.0
G1 X80.0 Y60.0 E1264.0
G1 X80.0 Y52.0 E1264.0
G1 X80.0 Y52.0 E1265.0
G1 X80.0 Y50.0 E1265.0
G1 X80.0 Y50.0 E1277.0
G1 X56.0 Y50.0 E1277.0
G1 X56.0 Y50.0 E1280.0
G1 X50.0 Y50.0 E1280.0
G0 Z40.0
;LAYER:32
G1 X50.0 Y50.0 E1284.125
G1 X50.0 Y58.25 E1284.125
G1 X50.0 Y58.25 E1285.0
G1 X50.0 Y60.0 E1285.0
G1 X50.0 Y60.0 E1297.375
G1 X74.75 Y60.0 E1297.375
G1 X74.75 Y60.0 E1300.0
G1 X80.0 Y60.0 E1300.0
G1 X80.0 Y60.0 E1304.125
G1 X80.0 Y51.75 E1304.125
G1 X80.0 Y51.75 E1305.0
G1 X80.0 Y50.0 E1305.0
G1 X80.0 Y50.0 E1317.375
G1 X55.25 Y50.0 E1317.375
G1 X55.25 Y50.0 E1320.0
G1 X50.0 Y50.0 E1320.0
G0 Z41.25
;LAYER:33
G1 X50.0 Y50.0 E1324.25
G1 X50.0 Y58.5 E1324.25
G1 X50.0 Y58.5 E1325.0
G1 X50.0 Y60.0 E1325.0
G1 X50.0 Y60.0 E1337.75
G1 X75.5 Y60.0 E1337.75
G1 X75.5 Y60.0 E1340.0
G1 X80.0 Y60.0 E1340.0
G1 X80.0 Y60.0 E1344.25
G1 X80.0 Y51.5 E1344.25
G1 X80.0 Y51.5 E1345.0
G1 X80.0 Y50.0 E1345.0
G1 X80.0 Y50.0 E1357.75
G1 X54.5 Y50.0 E1357.75
G1 X54.5 Y50.0 E1360.0
G1 X50.0 Y50.0 E1360.0
G0 Z42.5
;LAYER:34
G1 X50.0 Y50.0 E1364.375
G1 X50.0 Y58.75 E1364.375
G1 X50.0 Y58.75 E1365.0
G1 X50.0 Y60.0 E1365.0
G1 X50.0 Y60.0 E1378.125
G1 X76.25 Y60.0 E1378.125
G1 X76.25 Y60.0 E1380.0
G1 X80.0 Y60.0 E1380.0
G1 X80.0 Y60.0 E1384.375
G1 X80.0 Y51.25 E1384.375
G1 X80.0 Y51.25 E1385.0
G1 X80.0 Y50.0 E1385.0
G1 X80.0 Y50.0 E1398.125
G1 X53.75 Y50.0 E1398.125
G1 X53.75 Y50.0 E1400.0
G1 X50.0 Y50.0 E1400.0
G0 Z43.75
;LAYER:35
G1 X50.0 Y50.0 E1404.5
G1 X50.0 Y59.0 E1404.5
G1 X50.0 Y59.0 E1405.0
G1 X50.0 Y60.0 E1405.0
G1 X50.0 Y60.0 E1418.5
G1 X77.0 Y60.0 E1418.5
G1 X77.0 Y60.0 E1420.0
G1 X80.0 Y60.0 E1420.0
G1 X80.0 Y60.0 E1424.5
G1 X80.0 Y51.0 E1424.5
G1 X80.0 Y51.0 E1425.0
G1 X80.0 Y50.0 E1425.0
G1 X80.0 Y50.0 E1438.5
G1 X53.0 Y50.0 E1438.5
G1 X53.0 Y50.0 E1440.0
G1 X50.0 Y50.0 E1440.0
G0 Z45.0
;LAYER:36
G1 X50.0 Y50.0 E1444.625
G1 X50.0 Y59.25 E1444.625
G1 X50.0 Y59.25 E1445.0
G1 X50.0 Y60.0 E1445.0
G1 X50.0 Y60.0 E1458.875
G1 X77.75 Y60.0 E1458.875
G1 X77.75 Y60.0 E1460.0
G1 X80.0 Y60.0 E1460.0
G1 X80.0 Y60.0 E1464.625
G1 X80.0 Y50.75 E1464.625
G1 X80.0 Y50.75 E1465.0
G1 X80.0 Y50.0 E1465.0
G1 X80.0 Y50.0 E1478.875
G1 X52.25 Y50.0 E1478.875
G1 X52.25 Y50.0 E1480.0
G1 X50.0 Y50.0 E1480.0
G0 Z46.25
;LAYER:37
G1 X50.0 Y50.0 E1484.75
G1 X50.0 Y59.5 E1484.75
G1 X50.0 Y59.5 E1485.0
G1 X50.0 Y60.0 E1485.0
G1 X50.0 Y60.0 E1499.25
G1 X78.5 Y60.0 E1499.25
G1 X78.5 Y60.0 E1500.0
G1 X80.0 Y60.0 E1500.0
G1 X80.0 Y60.0 E1504.75
G1 X80.0 Y50.5 E1504.75
G1 X80.0 Y50.5 E1505.0
G1 X80.0 Y50.0 E1505.0
G1 X80.0 Y50.0 E1519.25
G1 X51.5 Y50.0 E1519.25
G1 X51.5 Y50.0 E1520.0
G1 X50.0 Y50.0 E1520.0
G1 X50.0 Y50.0 E1524.875
G1 X50.0 Y59.75 E1524.875
G1 X50.0 Y59.75 E1525.0
G1 X50.0 Y60.0 E1525.0
G1 X50.0 Y60.0 E1539.625
G1 X79.25 Y60.0 E1539.625
G1 X79.25 Y60.0 E1540.0
G1 X80.0 Y60.0 E1540.0
G1 X80.0 Y60.0 E1544.875
G1 X80.0 Y50.25 E1544.875
G1 X80.0 Y50.25 E1545.0
G1 X80.0 Y50.0 E1545.0
G1 X80.0 Y50.0 E1559.625
G1 X50.75 Y50.0 E1559.625
G1 X50.75 Y50.0 E1560.0
G1 X50.0 Y50.0 E1560.0;end of print
;moves after print
G1 F2400 E2.34871
M140 S0
M204 S4000
M205 X20 Y20
M107
M104 S0 ; turn off extruder
M140 S0 ; turn off bed
M84 ; disable motors
M107
G91 ;relative positioning
G1 E-1 F300 ;retract the filament a bit before lifting the nozzle
to release some of the pressure
G1 Z+0.5 E-5 ;X-20 Y-20 F100 ;move Z up a bit and retract filament even more
G28 X0 ;Y0 ;move X/Y to min endstops
so the head is out of the way
G1 Y180 F2000
M84 ;steppers off
G90
M300 P300 S4000
M82 ;absolute extrusion mode
M104 S0
;End of Gcode