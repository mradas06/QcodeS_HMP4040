import pytest 

from qcodes_contrib_drivers.drivers.RohdeSchwarz.HMP4040 import RohdeSchwarzHMP4040
import qcodes.instrument.sims as sims
visalib = sims.__file__.replace('__init__.py', 'RSHMP4040.yaml@sim')

@pytest.fixture(scope='module')

def HMP4040():
    hmp4040 = RohdeSchwarzHMP4040('hmp4040',
                                   address='GPIB::1::INSTR',
                                   num_channels=4,
                                   visalib=visalib,
                                   terminator='\n')

    yield hmp4040

    hmp4040.close()

def test_init(HMP4040):

    for hmp in [HMP4040]:

        idn_dict = hmp.IDN()
        
        assert idn_dict['vendor'] == 'QCoDeS'


