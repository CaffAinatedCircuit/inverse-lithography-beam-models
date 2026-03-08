# Results.md

## asap7sc7p5t_28_L_220121a Analysis

### Layer 1

![Layer 1 - 4 beams](images/asap7sc7p5t_28_L_220121a_1_4_comparison.png) ![Layer 1 - 8 beams](images/asap7sc7p5t_28_L_220121a_1_8_comparison.png)
![Layer 1 - 16 beams](images/asap7sc7p5t_28_L_220121a_1_16_comparison.png) ![Layer 1 - 64 beams](images/asap7sc7p5t_28_L_220121a_1_64_comparison.png)

**Figure 1**: Localized Gaussian clearly outperforms Ewald at 4 beams (clear spot vs two spheres). 8 beams shows vertical fringes for both. 16 beams optimal; 64 beams overfits with unwanted fringes.

### Layer 2 - Periodic Stripes Vertical

![Layer 2 - 4 beams](images/asap7sc7p5t_28_L_220121a_2_4_comparison.png) ![Layer 2 - 8 beams](images/asap7sc7p5t_28_L_220121a_2_8_comparison.png)
![Layer 2 - 16 beams](images/asap7sc7p5t_28_L_220121a_2_16_comparison.png) ![Layer 2 - 64 beams](images/asap7sc7p5t_28_L_220121a_2_64_comparison.png)

**Figure 2**: 4 beams shows no structure. Ewald forms single stripe at 8 beams. Clear fringes by 16 beams. Gaussian catches up at 64 beams.

### Layer 10 - Symmetric Squares Layout

![Layer 10 - 4 beams](images/asap7sc7p5t_28_L_220121a_10_4_comparison.png) ![Layer 10 - 8 beams](images/asap7sc7p5t_28_L_220121a_10_8_comparison.png)
![Layer 10 - 16 beams](images/asap7sc7p5t_28_L_220121a_10_16_comparison.png) ![Layer 10 - 64 beams](images/asap7sc7p5t_28_L_220121a_10_64_comparison.png)

**Figure 3**: Gaussian generates nearly complete pattern by 16 beams. Ewald consistently one generation behind.

### Layer 17 - Asymmetric Horizontal Stripes

![Layer 17 - 4 beams](images/asap7sc7p5t_28_L_220121a_17_4_comparison.png) ![Layer 17 - 8 beams](images/asap7sc7p5t_28_L_220121a_17_8_comparison.png)
![Layer 17 - 16 beams](images/asap7sc7p5t_28_L_220121a_17_16_comparison.png) ![Layer 17 - 64 beams](images/asap7sc7p5t_28_L_220121a_17_64_comparison.png)

**Figure 4**: Ewald rough pattern by 16 beams; Gaussian cleaner at 64. Ewald constrained by symmetric fringes.

### Layer 18 - TSV-like Metal Via Layer

![Layer 18 - 4 beams](images/asap7sc7p5t_28_L_220121a_18_4_comparison.png) ![Layer 18 - 8 beams](images/asap7sc7p5t_28_L_220121a_18_8_comparison.png)
![Layer 18 - 16 beams](images/asap7sc7p5t_28_L_220121a_18_16_comparison.png) ![Layer 18 - 64 beams](images/asap7sc7p5t_28_L_220121a_18_64_comparison.png)

**Figure 5**: Both require 64 beams. Gaussian approximates dotted lines as single lines; Ewald shows symmetric fringes.

### Layer 19 - Maze Pattern

![Layer 19 - 4 beams](images/asap7sc7p5t_28_L_220121a_19_4_comparison.png) ![Layer 19 - 8 beams](images/asap7sc7p5t_28_L_220121a_19_8_comparison.png)
![Layer 19 - 16 beams](images/asap7sc7p5t_28_L_220121a_19_16_comparison.png) ![Layer 19 - 64 beams](images/asap7sc7p5t_28_L_220121a_19_64_comparison.png)

**Figure 6**: Only 64 beams produce results. Gaussian struggles with close features; Ewald generates excessive fringes.

## PicoRV32a

### Layer 68 - Complex Design Hallucinations

![PicoRV32a Layer 68 - 4 beams](images/picorv32a_68_4_comparison.png) ![PicoRV32a Layer 68 - 8 beams](images/picorv32a_68_8_comparison.png)
![PicoRV32a Layer 68 - 16 beams](images/picorv32a_68_16_comparison.png) ![PicoRV32a Layer 68 - 64 beams](images/picorv32a_68_64_comparison.png)

**Figure 7**: All configurations show hallucinations. Requires higher epochs or significantly more beams.

## Conclusion

This is not practical for most applications due to fundamental limitations. However, symmetric TSV generation represents a niche where these methods could outperform classical approaches.

**Key Limitations:**
- Closed spaces cause reflections/refractive distortions
- Asymmetric patterns suffer from symmetric fringe artifacts  
- 64+ beams typically required

This method must complement traditional lithography rather than replace it.

**Future Work**: Multi-wavelength synthesis, partial coherence models, volumetric 3D patterning.
