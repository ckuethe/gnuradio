#!/usr/bin/env python
#
# Copyright 2004 Free Software Foundation, Inc.
# 
# This file is part of GNU Radio
# 
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
# 
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
import math

class test_sig_source (gr_unittest.TestCase):

    def setUp (self):
        self.fg = gr.flow_graph()

    def tearDown (self):
        self.fg = None

    def test_pll_carriertracking (self):
        expected_result = ((1.00000238419+6.47922693275e-09j),
                           (0.998399555683+0.0565364062786j),
                           (0.994261980057+0.10695001483j),
                           (0.98843306303+0.151648163795j),
                           (0.981579363346+0.191063538194j),
                           (0.974212288857+0.225630432367j),
                           (0.966734290123+0.255773901939j),
                           (0.959442555904+0.281897842884j),
                           (0.952551782131+0.304379671812j),
                           (0.946205317974+0.323566257954j),
                           (0.940503358841+0.339778244495j),
                           (0.935505151749+0.353307723999j),
                           (0.931235432625+0.364419162273j),
                           (0.927616357803+0.373535633087j),
                           (0.924710214138+0.380666583776j),
                           (0.922494113445+0.386005342007j),
                           (0.92093116045+0.389725029469j),
                           (0.919974088669+0.391981720924j),
                           (0.919572234154+0.392916500568j),
                           (0.919680893421+0.392660915852j),
                           (0.920248389244+0.39133310318j),
                           (0.921222627163+0.389039844275j),
                           (0.922548472881+0.385877460241j),
                           (0.924184799194+0.381939411163j),
                           (0.926086127758+0.377309292555j),
                           (0.928135097027+0.37224984169j),
                           (0.930293083191+0.366814315319j),
                           (0.932614028454+0.360868781805j),
                           (0.935064375401+0.354473829269j),
                           (0.937613248825+0.347684770823j),
                           (0.940225422382+0.340550601482j),
                           (0.942881464958+0.33312189579j),
                           (0.945559620857+0.325443327427j),
                           (0.948240220547+0.31755694747j),
                           (0.950899422169+0.309499144554j),
                           (0.953524827957+0.301307469606j),
                           (0.956105649471+0.293015599251j),
                           (0.958630502224+0.284654557705j),
                           (0.96103054285+0.276443749666j),
                           (0.963361799717+0.26819768548j),
                           (0.965623259544+0.259936869144j),
                           (0.967810571194+0.251679092646j),
                           (0.969916880131+0.243440493941j),
                           (0.971936583519+0.235235646367j),
                           (0.97387367487+0.227080151439j),
                           (0.975726902485+0.218987599015j),
                           (0.977494239807+0.210969462991j),
                           (0.979169845581+0.203035995364j),
                           (0.980761289597+0.195199295878j),
                           (0.982269346714+0.187469303608j),
                           (0.983659446239+0.180052131414j),
                           (0.984931468964+0.1729388237j),
                           (0.986136198044+0.165923252702j),
                           (0.987275123596+0.159012272954j),
                           (0.988349795341+0.15221118927j),
                           (0.989354014397+0.145524248481j),
                           (0.990296065807+0.138957872987j),
                           (0.991178870201+0.132516458631j),
                           (0.992005050182+0.126204773784j),
                           (0.992770493031+0.120025672019j),
                           (0.993480443954+0.113984130323j),
                           (0.994139909744+0.108083210886j),
                           (0.994751393795+0.102326385677j),
                           (0.995293080807+0.0969148278236j),
                           (0.995791256428+0.091630294919j),
                           (0.996252119541+0.0864710733294j),
                           (0.996678769588+0.0814334899187j),
                           (0.997069239616+0.0765165910125j),
                           (0.997423350811+0.071716658771j),
                           (0.997748315334+0.0670333206654j),
                           (0.998046517372+0.0624645166099j),
                           (0.998317599297+0.058009263128j),
                           (0.998557567596+0.053665690124j),
                           (0.998775064945+0.0494344644248j),
                           (0.998971700668+0.0453144386411j),
                           (0.999140620232+0.0415064357221j),
                           (0.99927687645+0.0379924885929j),
                           (0.999400436878+0.0345549099147j),
                           (0.999511957169+0.0311931278557j),
                           (0.99961233139+0.0279070306569j),
                           (0.999694347382+0.0246965941042j),
                           (0.999765276909+0.0215622838587j),
                           (0.999826848507+0.0185046810657j),
                           (0.999880313873+0.0155246723443j),
                           (0.999920129776+0.0126227736473j),
                           (0.999949812889+0.00980060640723j),
                           (0.99997317791+0.00705910893157j),
                           (0.999990820885+0.00439921114594j),
                           (0.999998450279+0.00202245195396j),
                           (0.999998092651-0.00029227725463j),
                           (0.999994516373-0.00254815118387j),
                           (0.999988794327-0.00474932929501j),
                           (0.999977111816-0.00689708162099j),
                           (0.999957799911-0.00899503659457j),
                           (0.999936699867-0.0110441967845j),
                           (0.999914228916-0.0130464555696j),
                           (0.999889075756-0.0150024276227j),
                           (0.999855577946-0.0169130507857j),
                           (0.999821305275-0.0187777336687j),
                           (0.999786794186-0.0205969288945j))

        sampling_freq = 10e3
        freq = sampling_freq / 100

        alpha = 0.1
        beta = alpha * alpha / 4.0
        maxf = 1
        minf = -1

        src = gr.sig_source_c (sampling_freq, gr.GR_COS_WAVE, freq, 1.0)
        pll = gr.pll_carriertracking_cc(alpha, beta, maxf, minf)
        head = gr.head (gr.sizeof_gr_complex, int (freq))
        dst = gr.vector_sink_c ()

        self.fg.connect (src, pll, head)
        self.fg.connect (head, dst)

        self.fg.run ()
        dst_data = dst.data ()

        self.assertComplexTuplesAlmostEqual (expected_result, dst_data, 5)

if __name__ == '__main__':
    gr_unittest.main ()
