
import qcodes as qc
import qcodes_contrib_drivers.drivers.RohdeSchwarz.HMP4040 as hmp4040


ps = hmp4040.RohdeSchwarzHMP4040('ps_1', 'ASRL6::INSTR')


ps.ch1.set_voltage.set(0.05)   #channel 1 voltage set 0.05
ps.ch2.set_current.set(0.2)    #channel 2 current set 0.2

print(ps.ch1.set_voltage.get())
print(ps.ch2.set_current.get())


ps.ch1.state('ON')   #output_Ch1 on

ps.state('ON')    #master on


print('V1=', ps.ch1.voltage.get())
print('I1=', ps.ch1.current.get())
print('P1=', ps.ch1.power.get())

ps.ch1.state('OFF')   #outpu_ch1 off

ps.state('OFF')  #master off

