# comment
# %%
import rivtcalc.rc_lib as rc

rc.doc("pdf", "default", "Carport Seismic Model", "37")

rc.I("""[01]  Seismic Demands for Carport Braces and Beam Connections

    || image | elements.jpg | 70
    Column and Brace Numbers [f]_

    || image | beams2.jpg | 50
    Beam Numbers [f]_
        
    || image | pins.jpg | 90
    Element Pin Connections [f]_

    || image | forceA.jpg | 90
    Axial Forces - Transverse Seismic [f]_

    || image | forceB.jpg | 90
    Axial Forces - Longitudinal Seismic [f]_

    || image | deltA.jpg | 90
    Deformations - Transverse Seismic (visually amplified) [f]_

    || image | deltB.jpg | 90
    Deformations - Longitudinal Seismic (visually amplified) [f]_

    || text | cp_echo.txt | literal

    || text | cp_str.txt | literal

    || text | cp_eig.txt | literal

    || text | cp_str.txt | literal

    """)
rc.V("""[02]  Seismic Capacities and D-C Ratios for Braces
    
    Woodworks 11.2 is used for connection capacities. The software does not
    allow a single bolt row so a two bolt configuration is analyzed and
    capacities are reduced by a factor of 2.

    || image | brace1.jpg | 65
    Brace plate reinforcement (two-bolt rows shown - one row analyzed) [f]_

    || text | braces.txt | literal

    """)
rc.V("""[03]  Seismic Capacities and D-C Ratios for Beam Connections 

    Beam to beam angle connections provide a load path for drag forces and loss of 
    bearing if columns shift in an earthquake.

    || image | bmcon.jpg | 50

    || text | bmcon.txt | literal

    Top of column connections provide a shear load path to the foundation.

    || image | colcon.jpg | 50

    || text | colcon.txt | literal

    """)
# %%
