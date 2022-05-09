from pyteomics import mgf

input_mgf = 'C:/Users/Li/Desktop/标准品图谱/数据库/MASSBANK.mgf'  # The path of input mgf file (test fot public database)

Monomer_Standard = 0
Dimer_Standard = 0
Trimer_Standard = 0
library = 0
total = 0
lindenane = 0
Eudesmane = 0
with mgf.read(input_mgf) as spectra:
    for i, spectrum in enumerate(spectra):
        if spectrum['m/z array'].size > 0:
            library += 1
            intensity_max = max(spectrum['intensity array'])
            intensity_min = min(spectrum['intensity array'])
            x = (spectrum['intensity array'] - intensity_min) / (intensity_max - intensity_min)
            if 229 <= spectrum['params']['pepmass'][0] <= 520:
                for y, fragment_ion in enumerate(spectrum['m/z array']):
                    if 155.0825 <= fragment_ion <= 155.0885:
                        Monomer_Standard = Monomer_Standard + 1
                        lindenane += x[y]
                    if 157.0982 <= fragment_ion <= 157.1042:
                        Monomer_Standard = Monomer_Standard + 1
                        Eudesmane += x[y]
                    if x[y] > 0.1:
                        if 183.1138 <= fragment_ion <= 183.1198:
                            Monomer_Standard = Monomer_Standard + 1
                        if 168.0904 <= fragment_ion <= 168.0964:
                            Monomer_Standard = Monomer_Standard + 1
                        if 105.0669 <= fragment_ion <= 105.0729:
                            Monomer_Standard = Monomer_Standard + 1
                        if 156.0904 <= fragment_ion <= 156.0964:
                            Monomer_Standard = Monomer_Standard + 1
                        if 153.0669 <= fragment_ion <= 153.0729:
                            Monomer_Standard = Monomer_Standard + 1
                        if 143.0825 <= fragment_ion <= 143.0885:
                            Monomer_Standard = Monomer_Standard + 1
                        if 141.0669 <= fragment_ion <= 141.0729:
                            Monomer_Standard = Monomer_Standard + 1
                        if 142.0747 <= fragment_ion <= 142.0807:
                            Monomer_Standard = Monomer_Standard + 1
                        if 129.0669 <= fragment_ion <= 129.0807:
                            Monomer_Standard = Monomer_Standard + 1
                        if 115.0512 <= fragment_ion <= 115.0572:
                            Monomer_Standard = Monomer_Standard + 1
                        if 128.0591 <= fragment_ion <= 128.0651:
                            Monomer_Standard = Monomer_Standard + 1
                        if 199.1086 <= fragment_ion <= 199.1146:
                            Monomer_Standard = Monomer_Standard + 1
                        if 138.0645 <= fragment_ion <= 138.0703:
                            Monomer_Standard = Monomer_Standard + 1
                        if 137.0566 <= fragment_ion <= 137.0626:
                            Monomer_Standard = Monomer_Standard + 1
                        if 171.1138 <= fragment_ion <= 171.1198:
                            Monomer_Standard = Monomer_Standard + 1
                print(Monomer_Standard)
                if Monomer_Standard >= 6:
                    print('monoer')
                    total=total+1
                    if 229 <= spectrum['params']['pepmass'][0] <= 400:
                        if Eudesmane > 0 or lindenane > 0:
                            if lindenane < Eudesmane:
                                total = total - 1
                Monomer_Standard = 0

            if 500 < spectrum['params']['pepmass'][0] < 820:
                for y, fragment_ion in enumerate(spectrum['m/z array']):
                    if x[y] > 0.1:
                        if 225.0880 <= fragment_ion <= 225.0940:
                            Dimer_Standard = Dimer_Standard + 1
                        if 243.0986 <= fragment_ion <= 243.1046:
                            Dimer_Standard = Dimer_Standard + 1
                        if 467.1823 <= fragment_ion <= 467.1883:
                            Dimer_Standard = Dimer_Standard + 1
                        if 257.1142 <= fragment_ion <= 257.1202:
                            Dimer_Standard = Dimer_Standard + 1
                        if 275.1248 <= fragment_ion <= 275.1308:
                            Dimer_Standard = Dimer_Standard + 1
                        if 197.0931 <= fragment_ion <= 197.0991:
                            Dimer_Standard = Dimer_Standard + 1
                        if 345.1244 <= fragment_ion <= 345.1304:
                            Dimer_Standard = Dimer_Standard + 1
                        if 360.1479 <= fragment_ion <= 360.1539:
                            Dimer_Standard = Dimer_Standard + 1
                        if 350.1635 <= fragment_ion <= 350.1695:
                            Dimer_Standard = Dimer_Standard + 1
                        if 365.1929 <= fragment_ion <= 365.1989:
                            Dimer_Standard = Dimer_Standard + 1

                if Dimer_Standard >= 2:
                    print(x[y])
                    print('dimer')
                    total = total + 1
                Dimer_Standard = 0

            if 820 < spectrum['params']['pepmass'][0]:
                for y, fragment_ion in enumerate(spectrum['m/z array']):
                    if x[y] > 0.1:
                        if 791.3396 <= fragment_ion <= 791.3456:
                            Trimer_Standard = Trimer_Standard + 1
                        if 225.0880 <= fragment_ion <= 225.0940:
                            Trimer_Standard = Trimer_Standard + 1
                        if 258.1220 <= fragment_ion <= 258.1280:
                            Trimer_Standard = Trimer_Standard + 1
                        if 245.1142 <= fragment_ion <= 245.1202:
                            Trimer_Standard = Trimer_Standard + 1
                        if 773.3290 <= fragment_ion <= 773.3350:
                            Trimer_Standard = Trimer_Standard + 1
                if Trimer_Standard >= 2:
                    print(x[y])
                    print('trimer')
                    total = total + 1
                Trimer_Standard = 0
print('total=',total)
print('library total=',library)
