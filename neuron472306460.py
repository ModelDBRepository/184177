'''
Defines a class, Neuron472306460, of neurons from Allen Brain Institute's model 472306460

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472306460:
    def __init__(self, name="Neuron472306460", x=0, y=0, z=0):
        '''Instantiate Neuron472306460.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472306460_instance is used instead
        '''
                
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Scnn1a-Tg2-Cre_Ai14_IVSCC_-176962.05.01.01_471001149_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon

        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472306460_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 49.12
            sec.e_pas = -85.860168457
        for sec in self.apic:
            sec.cm = 2.37
            sec.g_pas = 1.0987792532e-07
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000559249473293
        for sec in self.dend:
            sec.cm = 2.37
            sec.g_pas = 2.8222289133e-06
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.000318712
            sec.gbar_Ih = 0.00182646
            sec.gbar_NaTs = 0.718963
            sec.gbar_Nap = 0.000457459
            sec.gbar_K_P = 0.0791887
            sec.gbar_K_T = 0.0108478
            sec.gbar_SK = 0.134814
            sec.gbar_Kv3_1 = 0.215825
            sec.gbar_Ca_HVA = 9.80404e-06
            sec.gbar_Ca_LVA = 3.7419e-05
            sec.gamma_CaDynamics = 0.0141411
            sec.decay_CaDynamics = 398.433
            sec.g_pas = 0.000106921
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

