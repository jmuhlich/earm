from pysb import *
# Parameter section
#
# 8/3/2011 
# The parameters for ['kbidCbidMf', 'kbidCbidMr', 'kbidbcl2f', 'kbidbcl2r', 'kc8bidf', 'kc8bidr', 'kc8bidc']
# were optimized using simulated annealing to match the output of tBid in earm_1_5 to the 
# original output of earm_1_0. I used a sigma of 5% (i.e. .05) for the objective function.
#

# Special parameters
v = .07; # mitochondria compartment volume/cell volume

# EARM 1.0 parameters
# Reaction rates
parameter_dict = {
    #--------------------
    # EARM 2.0 bcl2 module parameters
    #--------------------
    # Bid transport to mitochondria
    'BID_trans':  [ Parameter('kbidTbidMf', 0.0612607534149),
                    Parameter('kbidTbidMr', 0.000709215581377)],
    # Bax transport to mitochondria
    'BAX_trans':  [ Parameter('kbaxCbaxMf', 0.00730727274745), 
                    Parameter('kbaxCbaxMr', 0.0107476023245)],
    # Bclxl translocation
    'BCLXL_trans':[ Parameter('kbclxlCbclxlMf', 0.00080830468994),
                    Parameter('kbclxlCbclxlMr', 0.0136380873594)],
    # Bax activation by Bid
    'BIDt_BAX':   [ Parameter('kbidtbaxf', 1.78519244773e-08),
                    Parameter('kbidtbaxr', 0.000127019618397),
                    Parameter('kbidtbaxc', 3.12885090105 )],
    # Bax activation by Bid
    'BIDm_BAX':   [ Parameter('kbidmbaxf', 1.78519244773e-08),
                    Parameter('kbidmbaxr', 0.000127019618397),
                    Parameter('kbidmbaxc', 3.12885090105 )],
    # Bak activation via Bid ***CHECK VALUES
    'BIDt_BAK':   [ Parameter('kbidtbakf', 2.3840120805e-07),
                    Parameter('kbidtbakr', 0.00116686859656),
                    Parameter('kbidtbakc', 0.616100104218)],
    #Bax pore assembly
    'BAX_PORE':   [[Parameter('kbaxdimf', 1.9e-05),
                    Parameter('kbaxdimr', 0.00253168857302)],
                   [Parameter('kbaxtrimf', 0.00012),
                    Parameter('kbaxtrimr', 0.000455745565138)],
                   [Parameter('kbaxtetf', 0.000116),
                    Parameter('kbaxtetr', 0.000902098483308)]],
    #Bak pore assembly
    'BAK_PORE':   [[Parameter('kbakdimf', 1.98972134863e-05),
                    Parameter('kbakdimr', 0.00117910083105)],
                   [Parameter('kbaktrimf', 0.000120932227934 ),
                    Parameter('kbaktrimr', 4.81022463147e-06)],
                   [Parameter('kbaktetf',  0.000116488694321),
                    Parameter('kbaktetr', 0.000743264410286)]],
    # Inhibitions of Bax/Bak by Bcl2/BclxL/Mcl1
    # These are used in the simple_bind_table function which expects
    # row-major order (if you don't know what this means google it)
    'BID_BAX_BAK_inh':[[Parameter('kbidbcl2f', 1.45280010e-06),
                        Parameter('kbidbcl2r', 1.70789566e-03)],
                       [Parameter('kbidbclxlf', 2.53724317374e-06),#
                        Parameter('kbidbclxlr', 0.000777609558706  )]],
    # Sensitizers of Bcl2/BclxL/Mcl1 by Bad/NOXA
    'BCLs_sens':      [[Parameter('kbadbcl2f',  3.77284671141e-06),
                        Parameter('kbadbcl2r',  0.00106766288445 )],
                       [Parameter('kbadbclxlf', 5.02786873341e-05),
                        Parameter('kbadbclxlr', 0.00029689476754 )],
                       [Parameter('knoxabclxlf', 1.46064619002e-05),
                        Parameter('knoxabclxlr', 0.00137190327654 )],
                       [Parameter('knoxamcl1f', 5.97803309472e-06),
                        Parameter('knoxamcl1r', 6.68821754476e-05 )]],
    
    #---------------------------
    # EARM 1.0 legacy parameters
    #---------------------------

    # rec_to_bid module parameters
    'L_R_DISC':   [ Parameter('klrf', 3.16778866964e-07),       
                    Parameter('klrr', 0.00348412289944),
                    Parameter('klrc', 6.25171535745e-06)],
    # C8 activation via DISC,
    'DISC_C8':    [ Parameter('kdiscc8f', 6.24455983646e-06),   
                    Parameter('kdiscc8r', 5.31630214477e-05),
                    Parameter('kdiscc8c', 7.2196057206)],
    # Bid cleavage by C8
    'C8_BID':     [ Parameter('kc8bidf', 4.12889999975e-08),
                    Parameter('kc8bidr', 4.5677553868e-05),
                    Parameter('kc8bidc', 16.0133713052)],
    # DISC inhibition by FLIP
    'DISC_FLIP':  [ Parameter('kflipdiscf', 4.20690082454e-07), 
                    Parameter('kflipdiscr', 7.29146539552e-05)],
    # C8 inhibition by BAR
    'BAR_C8':     [ Parameter('kbarc8f', 3.74374298237e-07), 
                    Parameter('kbarc8r', 0.00154671269112)],

    #---------------------------
    # pore_to_parp module parameters
    #---------------------------
    # CytoC transport by Bax
    'BAX_CYTC':   [[ Parameter('kbaxcytocMCf',  1.07052327914e-05),   #same as Bax-SMAC
                     Parameter('kbaxcytocMCr',  0.00114074765938 ),   #same as Bax-SMAC
                     Parameter('kbaxcytocMCc', 11.1174330138     )]], #same as Bax-SMAC
    # Smac transport by Bax
    'BAX_SMAC':   [[ Parameter('kbaxsmacCAf',   1.07052327914e-05),  #change to MC for consistency (mito to cyto)
                     Parameter('kbaxsmacCAr',   0.00114074765938 ),
                     Parameter('kbaxsmacCAc',  11.1174330138     )]],
    # CytoC transport activation by Bak **
    'BAK_CYTC':   [[ Parameter('kbakcytocMCf',  9.21063577757e-06 ),
                     Parameter('kbakcytocMCr',  0.00234088295981  ),
                     Parameter('kbakcytocMCc', 27.3582352876      )]],
    # Smac transport by Bak  **
    'BAK_SMAC':   [[ Parameter('kbaksmacCAf',  9.21063577757e-06),   #same as Bak-SMAC
                     Parameter('kbaksmacCAr',  0.00234088295981 ),   #same as Bak-SMAC
                     Parameter('kbaksmacCAc', 27.3582352876     )]], #same as Bak-SMAC
    # CytoC activation
    'CYTOC_ACT':  [ Parameter('kcytocCcytoAf', 0.0273684974471),  #same as SMAC_ACT
                    Parameter('kcytocCcytoAr', 0.0136700510202)], #same as SMAC_ACT
    # Smac activation
    'SMAC_ACT':  [ Parameter('ksmacCsmacAf', 0.0273684974471),
                   Parameter('ksmacCsmacAr', 0.0159988303507)],
    # Apaf activation by CytC
    'APAF_CYTC':  [ Parameter('kcytocCapaff', 5e-07),
                    Parameter('kcytocCapafr', 1e-03),
                    Parameter('kcytocCapafc', 1e+00)],
    # Apop formation by Apaf + C9
    'APOP_C9:APAF':[ Parameter('kapafc9f', 5e-08),
                     Parameter('kapafc9r', 1e-03)],
     # C3 activation by Apop
    'APOP_C3':    [ Parameter('kapopc3f', 5e-09),
                    Parameter('kapopc3r', 1e-03),
                    Parameter('kapopc3c', 1e+00)],
    # Apop inhibition by XIAP
    'APOP_XIAP':  [ Parameter('kapopxiapf', 2e-06),
                    Parameter('kapopxiapr', 1e-03)],
    # XIAP inhibition by Smac
    'SMAC_XIAP':  [ Parameter('ksmacxiapf', 3.0000000001e-06),
                    Parameter('ksmacxiapr', 0.00184889755483)],
    # C3 activation by C8
    'C3_C8':      [ Parameter('kc8c3f', 1e-07), 
                    Parameter('kc8c3r', 1e-03),
                    Parameter('kc8c3c', 1e+00)],
    # C6 activation by C3
    'C6_C3':      [ Parameter('kc3c6f', 1e-06), 
                    Parameter('kc3c6r', 1e-03),
                    Parameter('kc3c6c', 1e+00)],
    # C3 ubiquination tag by XIAP
    'C3_XIAP':    [ Parameter('kxiapc3f', 2e-06),
                    Parameter('kxiapc3r', 1e-03),
                    Parameter('kxiapc3c', 1e-01)],
    # PARP cleavage by C3
    'PARP_C3':    [ Parameter('kc3parpf', 1e-06),
                    Parameter('kc3parpr', 1e-02),
                    Parameter('kc3parpc', 1e+00)],
    # C8 activation by C6
    'C8_C6':      [ Parameter('kc6c8f', 3e-08), 
                    Parameter('kc6c8r', 1e-03),
                    Parameter('kc6c8c', 1e+00)],

    #---------------------------------
    # EARM 1.0 HeLa initial conditions
    # Non-zero initial conditions (in molecules per cell):
    #---------------------------------
    'INIT_AMTS':    [ Parameter('L_0'     ,  3000), # Ligand corresponding to 50 ng/ml SuperKiller TRAIL
                      Parameter('R_0'     ,   200),   # TRAIL receptor 
                      Parameter('flip_0'  , 1.0e2),  # Flip
                      Parameter('C8_0'    , 2.0e4),   # procaspase-8 
                      Parameter('BAR_0'   , 1.0e3),  # Bifunctional apoptosis regulator
                      Parameter('Bid_0'   , 4.0e4),  # Bid
                      Parameter('Bax_0'   , 0.8e5), # Bax
                      Parameter('Bak_0'   , 0.2e5), # Bak
                      Parameter('Bcl2_0'  , 2.0e4),   # cytosolic Bcl2
                      Parameter('BclxL_0' , 2.0e4),  # cytosolic BclxL
                      Parameter('Mcl1_0'  , 2.0e4),   # mitochondrial Mcl1  
                      Parameter('Bad_0'   , 1.0e3),  # Bad
                      Parameter('NOXA_0'  , 1.0e3),  # NOXA
                      Parameter('CytoC_0' , 5.0e5),  # cytochrome c
                      Parameter('Smac_0'  , 1.0e5),  # Smac    
                      Parameter('Apaf_0'  , 1.0e5),  # Apaf-1
                      Parameter('C3_0'    , 1.0e4),  # procaspase-3 (pro-C3)
                      Parameter('C6_0'    , 1.0e4),  # procaspase-6 (pro-C6)  
                      Parameter('C9_0'    , 1.0e5),  # procaspase-9 (pro-C9)
                      Parameter('XIAP_0'  , 1.0e5),  # X-linked inhibitor of apoptosis protein  
                      Parameter('PARP_0'  , 1.0e6),  # C3* substrate
                      ]
    }


