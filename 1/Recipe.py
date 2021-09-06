def recept(antal):
    ägg = int(3/4 * antal)
    strösocker = 3/4 * antal
    vaniljsocker = 2/4 * antal
    bakpulver = 2/4 * antal
    vetemjöl = 3/4 * antal
    smör = 75/4 * antal
    vatten = 1/4 * antal

    smörForm = 10/4 * antal
    ströbröd = 0.75/4 * antal

    print(f"""
    Recept för {antal} personer;
    * {ägg} Ägg
    * {strösocker} dl strösocker
    * {vaniljsocker} tsk vaniljsocker
    * {bakpulver} tsk bakpulver
    * {vetemjöl} dl vetemjöl
    * {smör} g smör
    * {vatten} dl vatten
    
    För Formen;
    * {smörForm} g smör
    * {ströbröd} dl ströbröd
    """)