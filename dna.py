barva_las = {
    "crna":"CCAGCAATCGC",
    "rjava":"GCCAGTGCCG",
    "korencek":"TTAGCTATCGC"
}
oblika_obraza = {
    "kvadraten":"GCCACGG",
    "okrogel":"ACCACAA",
    "ovalen":"AGGCCTCA"
}
barva_oci = {
    "modra":"TTGTGGTGGC",
    "zelena":"GGGAGGTGGC",
    "rjava":"AAGTAGTGAC"
}
spol = {
    "moski":"TGCAGGAACTTC",
    "zenska":"TGAAGGACCTTC"
}
rasa = {
    "belec":"AAAACCTCA",
    "crnec":"CGACTACAG",
    "azijec":"CGCGGGCCG"
}

def get_hair_color(dna):
    for barva in barva_las.keys():
        if (dna.find(barva_las[barva]) != -1):
            return barva
    return "neznana"

def get_oblika_obraza(dna):
    for obraz in oblika_obraza.keys():
        if (dna.find(oblika_obraza[obraz]) != -1):
            return obraz
    return "neznana"

def get_barva_oci(dna):
    for oci in barva_oci.keys():
        if (dna.find(barva_oci[oci]) != -1):
            return oci
    return "neznana"

def get_spol(dna):
    for spol_osumljenca in spol.keys():
        if (dna.find(spol[spol_osumljenca]) != -1):
            return spol_osumljenca
    return "neznan"

def get_rasa(dna):
    for rasa_osumljenca in rasa.keys():
        if (dna.find(rasa_osumljenca[rasa]) != -1):
            return rasa_osumljenca
    return "neznana"

def get_person(hair_color, oblika_obraza, barva_oci, spol, rasa):
    if (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(
            hair_color["korencek"]) != -1 and dna.find(barva_oci["rjava"]) != -1) and dna.find(
            oblika_obraza["okrogel"]) != -1:
        print ("Bil je Ziga!")

    elif (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(
            hair_color["crna"]) != -1 and dna.find(barva_oci["modra"]) != -1 and dna.find(
            oblika_obraza["ovalen"]) != -1):
        print ("Bil je Matej!")

    elif (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(
            hair_color["rjava"]) != -1 and dna.find(barva_oci["zelena"]) != -1 and dna.find(
            oblika_obraza["kvadraten"]) != -1):
        print ("Bil je Miha!")
    else:
        print ("Krivca ni med osumljenci..")





