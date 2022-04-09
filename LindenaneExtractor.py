import csv
import pandas as pd
from pyteomics import mgf
from matplotlib import pyplot as plt
from adjustText import adjust_text

'''Input mgf file and csv file generated by MZmine 2'''
file = open('input.txt', 'r')
line = file.read().splitlines()
input_mgf_file = line[0]
input_csv_file = line[1]
file.close()
input_mgf = input_mgf_file
input_csv = input_csv_file

'''Lists for recording the molecular parameters to the filtered mgf file and csv files.'''
target = []
row_ID = []
row_mass = []
row_retention_time = []
Peak_area = []
Peak_Unnamed = []

'''Lists for recording the molecular parameters for classification.'''
Classification = []    # List for recording the lindenane sesquiterpenoid classification
Monomer_Score = 0    # Classification score for monomer (Figure 1)
Dimer_Score = 0    # Classification score for dimer (Figure 1)
Trimer_Score = 0    # Classification score for trimer (Figure 1)
lindenane = 0    # Parameter for lindenane sesquiterpenoid identification
Eudesmane = 0    # Parameter for eudesmane sesquiterpenoid identification
Diagnostic_ion = []    # List for recording diagnostic ions for subclass classification
Subclass = []    # List for recording the subclass classification
plt_index = []    # List for recording the subclass classification for plotting RT-m/z plot
Identification = []
lindenane_database = [677, 694, 619, 636, 579, 596, 635, 652, 637, 654, 693, 710, 727,
                      229, 231, 245, 247, 255, 263, 277, 289, 291, 303, 305, 307, 319,
                      337, 339, 353, 381, 385, 387, 403, 409, 419, 447, 457, 459, 473,
                      475, 487, 491, 503, 505, 529, 549, 551, 553, 561, 563, 565, 567,
                      571, 577, 589, 595, 617, 663, 633, 661, 679, 759, 605, 497, 541,
                      711, 717, 733, 735, 747, 749, 751, 761, 765, 767, 777, 791, 547,
                      795, 823, 849, 246, 248, 262, 264, 272, 280, 294, 306, 308, 320,
                      322, 324, 336, 354, 356, 370, 398, 402, 404, 420, 426, 436, 464,
                      474, 476, 490, 492, 504, 508, 520, 522, 546, 566, 568, 570, 578,
                      580, 582, 584, 588, 594, 606, 612, 634, 680, 650, 477, 559, 517,
                      678, 696, 728, 734, 750, 752, 764, 766, 768, 778, 535, 365, 653,
                      782, 784, 794, 808, 812, 840, 866, 215, 273, 249, 287, 261, 265,
                      281, 323, 295, 279, 321, 293, 425, 391, 427, 441, 309, 311, 325,
                      343, 611, 597, 393, 232, 290, 266, 304, 278, 282, 298, 340, 312,
                      296, 338, 310, 442, 408, 444, 458, 326, 328, 342, 360, 628, 614,
                      410, 670, 382, 552, 534, 576, 494, 564, 558, 514, 622, 776, 744,
                      443, 461, 489, 493, 501, 519, 533, 537, 539, 545, 555, 569, 573,
                      575, 581, 593, 607, 621, 633, 649, 651, 667, 701, 709, 723, 731,
                      743, 745, 763, 781, 783, 795, 797, 807, 811, 460, 478, 506, 510,
                      518, 536, 550, 554, 556, 562, 572, 586, 590, 592, 598, 610, 624,
                      638, 650, 666, 668, 684, 718, 726, 740, 748, 760, 762, 780, 798,
                      800, 812, 814, 824, 828]   # The molecular weight of reported lindenane sesquiterpenoids


with mgf.read(input_mgf) as spectra:
    with open(input_csv) as f:
        reader = csv.reader(f)
        header_row = next(reader)[3]
    data = pd.read_csv(input_csv)
    for i, spectrum in enumerate(spectra):
        intensity_max = max(spectrum['intensity array'])  # intensity normalization
        intensity_min = min(spectrum['intensity array'])  # intensity normalization
        x = (spectrum['intensity array'] - intensity_min) / (intensity_max - intensity_min)  # intensity normalization

        if 229 <= spectrum['params']['pepmass'][0] <= 520:    # Precursor mass classification
            u = spectrum['params']['pepmass'][0]
            for y, fragment_ion in enumerate(spectrum['m/z array']):

                '''Filtering the eudesmane sesquiterpenoid'''
                if 155.0825 <= fragment_ion <= 155.0885:
                    Monomer_Score = Monomer_Score + 1
                    lindenane += x[y]
                if 157.0982 <= fragment_ion <= 157.1042:
                    Monomer_Score = Monomer_Score + 1
                    Eudesmane += x[y]

                '''The characteristic ions for lindenane sesquiterpenoid monomers.'''
                if x[y] > 0.1:
                    if 183.1138 <= fragment_ion <= 183.1198:
                        Monomer_Score = Monomer_Score + 1
                        Diagnostic_ion.append(fragment_ion)
                    if 168.0904 <= fragment_ion <= 168.0964:
                        Monomer_Score = Monomer_Score + 1
                    if 105.0669 <= fragment_ion <= 105.0729:
                        Monomer_Score = Monomer_Score + 1
                    if 156.0904 <= fragment_ion <= 156.0964:
                        Monomer_Score = Monomer_Score + 1
                    if 153.0669 <= fragment_ion <= 153.0729:
                        Monomer_Score = Monomer_Score + 1
                    if 143.0825 <= fragment_ion <= 143.0885:
                        Monomer_Score = Monomer_Score + 1
                    if 141.0669 <= fragment_ion <= 141.0729:
                        Monomer_Score = Monomer_Score + 1
                    if 142.0747 <= fragment_ion <= 142.0807:
                        Monomer_Score = Monomer_Score + 1
                    if 129.0669 <= fragment_ion <= 129.0807:
                        Monomer_Score = Monomer_Score + 1
                    if 115.0512 <= fragment_ion <= 115.0572:
                        Monomer_Score = Monomer_Score + 1
                    if 128.0591 <= fragment_ion <= 128.0651:
                        Monomer_Score = Monomer_Score + 1
                    if 199.1086 <= fragment_ion <= 199.1146:
                        Monomer_Score = Monomer_Score + 1
                        Diagnostic_ion.append(fragment_ion)
                    if 138.0645 <= fragment_ion <= 138.0703:
                        Monomer_Score = Monomer_Score + 1
                        Diagnostic_ion.append(fragment_ion)
                    if 137.0566 <= fragment_ion <= 137.0626:
                        Monomer_Score = Monomer_Score + 1
                        Diagnostic_ion.append(fragment_ion)
                    if 171.1138 <= fragment_ion <= 171.1198:
                        Monomer_Score = Monomer_Score + 1

            '''Monomer identification and subclass classification'''
            if Monomer_Score >= 6:
                target.append(i)
                Classification.append('Monomer')
                plt_index.append(0)
                if int(u) in lindenane_database:
                    Identification.append('possibly known compounds')
                else:
                    Identification.append('potentially new compound')
                if not Diagnostic_ion:
                    Subclass.append('other')
                for diagnostic_ions in Diagnostic_ion:
                    if 137 < diagnostic_ions < 139 or 183 < diagnostic_ions < 184:
                        Subclass.append('LS monomer with Δ8,9')
                        break
                    if 199 < diagnostic_ions < 200:
                        Subclass.append('LS monomer with OH-9 or 8,9-epoxy group')

                '''Filtering the eudesmane sesquiterpenoid. Eudesmane sesquiterpenoids are another predominant 
                sesquiterpenoids in Sarcandra. These compounds displayed the same fragmentation pathway with that of 
                LSMs. By comparing their fragment ions, we discovered that the ion intensity of m/z 155 was always 
                higher that of m/z 157 in LSMs, however, it was opposite in eudesmane. '''
                if Eudesmane > 0 or lindenane > 0:
                    if lindenane < Eudesmane:
                        target.pop(-1)
                        Classification.pop(-1)
                        Subclass.pop(-1)
                        plt_index.pop(-1)
                        plt_index.append(3)
                        Identification.pop(-1)
            else:
                plt_index.append(3)
            Monomer_Score = 0
            Diagnostic_ion = []
            lindenane = 0
            Eudesmane = 0

        if 520 < spectrum['params']['pepmass'][0] < 820:    # Precursor mass classification
            u = spectrum['params']['pepmass'][0]
            for y, fragment_ion in enumerate(spectrum['m/z array']):

                '''The characteristic ions for lindenane sesquiterpenoid dimers.'''
                if x[y] > 0.1:
                    if 225.0880 <= fragment_ion <= 225.0940:
                        Dimer_Score = Dimer_Score + 1
                        Diagnostic_ion.append(fragment_ion)
                    if 243.0986 <= fragment_ion <= 243.1046:
                        Dimer_Score = Dimer_Score + 1
                    if 467.1823 <= fragment_ion <= 467.1883:
                        Dimer_Score = Dimer_Score + 1

                    if 257.1142 <= fragment_ion <= 257.1202:
                        Dimer_Score = Dimer_Score + 1
                    if 275.1248 <= fragment_ion <= 275.1308:
                        Dimer_Score = Dimer_Score + 1
                    if 197.0931 <= fragment_ion <= 197.0991:
                        Dimer_Score = Dimer_Score + 1
                    if 345.1244 <= fragment_ion <= 345.1304:
                        Dimer_Score = Dimer_Score + 1
                        Diagnostic_ion.append(fragment_ion)
                    if 360.1479 <= fragment_ion <= 360.1539:
                        Dimer_Score = Dimer_Score + 1
                        Diagnostic_ion.append(fragment_ion)
                    if 350.1635 <= fragment_ion <= 350.1695:
                        Dimer_Score = Dimer_Score + 1
                        Diagnostic_ion.append(fragment_ion)
                    if 365.1929 <= fragment_ion <= 365.1989:
                        Dimer_Score = Dimer_Score + 1
                        Diagnostic_ion.append(fragment_ion)

            '''Dimer identification and subclass classification'''
            if Dimer_Score >= 2:
                target.append(i)
                Classification.append('Dimer')
                plt_index.append(1)
                if int(u) in lindenane_database:
                    Identification.append('possibly known compounds')
                else:
                    Identification.append('potentially new compound')
                if not Diagnostic_ion:
                    Subclass.append('other')
                for diagnostic_ions in Diagnostic_ion:
                    if 225 < diagnostic_ions < 226:
                        if spectrum['params']['pepmass'][0] < 733:
                            Subclass.append('Classical [4+2] cycloaddition product')
                        if spectrum['params']['pepmass'][0] >= 733:
                            Subclass.append('Classical [4+2] cycloaddition product with 18-membered macrocyclic '
                                            'ester ring')
                        break
                    if 345 < diagnostic_ions < 361:
                        Subclass.append('Aromatic product')
                        break

            else:
                plt_index.append(3)

            Dimer_Score = 0
            Diagnostic_ion = []

        if 820 < spectrum['params']['pepmass'][0]:    # Precursor mass classification
            u = spectrum['params']['pepmass'][0]
            for y, fragment_ion in enumerate(spectrum['m/z array']):

                '''The characteristic ions for lindenane sesquiterpenoid trimers.'''
                if x[y] > 0.1:
                    if 791.3396 <= fragment_ion <= 791.3456:
                        Trimer_Score = Trimer_Score + 1
                    if 225.0880 <= fragment_ion <= 225.0940:
                        Trimer_Score = Trimer_Score + 1
                    if 258.1220 <= fragment_ion <= 258.1280:
                        Trimer_Score = Trimer_Score + 1
                    if 245.1142 <= fragment_ion <= 245.1202:
                        Trimer_Score = Trimer_Score + 1
                    if 773.3290 <= fragment_ion <= 773.3350:
                        Trimer_Score = Trimer_Score + 1

            '''Trimer identification and subclass classification'''
            if Trimer_Score >= 2:
                target.append(i)
                if int(u) in lindenane_database:
                    Identification.append('possibly known compounds')
                else:
                    Identification.append('potentially new compound')
                Classification.append('Trimer')
                plt_index.append(2)
                Subclass.append('Trimer')
            else:
                plt_index.append(3)
            Trimer_Score = 0

        if 0 < spectrum['params']['pepmass'][0] < 229:    # Classification for plotting
            plt_index.append(3)


'''Writing csv file'''
for t in target:
    row_ID.append(int(data.loc[t]['row ID']))
    row_mass.append(data.loc[t]['row m/z'])
    row_retention_time.append(data.loc[t]['row retention time'])
    Peak_area.append(data.loc[t][str(header_row)])
    Peak_Unnamed.append(data.loc[t]['Unnamed: 4'])
list_total = [row_ID, row_mass, row_retention_time, Peak_area, Peak_Unnamed]
list_total2 = [Classification, Subclass, row_ID, row_mass, row_retention_time, Identification]
df = pd.DataFrame(data=list_total)
df2 = pd.DataFrame(df.values.T, columns=["row ID", "row m/z", 'row retention time', 'Peak area', 'Unnamed: 4'])
df2.to_csv('Output for FBMN.csv', encoding='gbk', index=False)
df3 = pd.DataFrame(data=list_total2)
df4 = pd.DataFrame(df3.values.T,
                   columns=["Classification", 'Subclass classification', "row ID", "row m/z", 'row retention time',
                            'Identification'])
df4.to_csv('Output for check.csv', encoding='gbk', index=False)

'''Writing mgf file'''
with mgf.read(input_mgf) as spectra:
    for title in row_ID:
        spectrum = mgf.get_spectrum(input_mgf, title=str(int(title)))
        mgf.write((spectrum,),
                  output='target.mgf')

'''Plotting Rt-m/z plot'''
Monomer_x = []
Monomer_y = []
Dimer_x = []
Dimer_y = []
Trimer_x = []
Trimer_y = []
Other_x = []
Other_y = []
for o, p in enumerate(plt_index):
    if p == 0:
        Monomer_x.append(data.loc[o]['row retention time'])
        Monomer_y.append(data.loc[o]['row m/z'])
    if p == 1:
        Dimer_x.append(data.loc[o]['row retention time'])
        Dimer_y.append(data.loc[o]['row m/z'])
    if p == 2:
        Trimer_x.append(data.loc[o]['row retention time'])
        Trimer_y.append(data.loc[o]['row m/z'])
    if p == 3:
        Other_x.append(data.loc[o]['row retention time'])
        Other_y.append(data.loc[o]['row m/z'])

plt.figure(figsize=(10, 18), dpi=600)
plt.scatter(Monomer_x, Monomer_y, marker='o', s=100)
plt.scatter(Dimer_x, Dimer_y, marker='o', s=100)
plt.scatter(Trimer_x, Trimer_y, marker='o', s=100)
plt.scatter(Other_x, Other_y, marker='o', zorder=0, color='darkgray')
plt.xlabel('Retention time  (min)', fontsize=20)
plt.ylabel('m/z', fontsize=20, style='italic')
plt.tick_params(labelsize=20)

new_texts = [plt.text(Monomer_x[p], Monomer_y[p], 'm/z'' ''%.2f' % m,
                      fontsize=8) for p, m in enumerate(Monomer_y)]
adjust_text(new_texts,
            only_move={'text': 'xy'},
            arrowprops=dict(arrowstyle='-', color='red'),
            save_steps=False)

new_texts = [plt.text(Dimer_x[p], Dimer_y[p], 'm/z'' ''%.2f' % m,
                      fontsize=8) for p, m in enumerate(Dimer_y)]
adjust_text(new_texts,
            only_move={'text': 'xy'},
            arrowprops=dict(arrowstyle='-', color='red'),
            save_steps=False)

new_texts = [plt.text(Trimer_x[p], Trimer_y[p], 'm/z'' ''%.2f' % m,
                      fontsize=8) for p, m in enumerate(Trimer_y)]
adjust_text(new_texts,
            only_move={'text': 'xy'},
            arrowprops=dict(arrowstyle='-', color='red'),
            save_steps=False)
plt.legend(labels=['Monomer', 'Dimer', 'Trimer', 'Other'])
plt.savefig('target.jpg')
