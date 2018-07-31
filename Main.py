from Algorithm import distance, getNeighbors, normalizer, sim, updateAbundance
from LoadData import lodData
#########################################################
# tempAbundance for balancing data
tempAbundance = [1 , 1 , 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0 , 0, 1, 0, 1, 0, 1, 0, 0, 1,
                 0 , 0 , 1 , 1 , 1, 1 , 1 , 0, 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1, 0, 0 , 1, 1 , 1, 1, 1, 1, 1 , 1, 0 , 0, 0 , 0, 0 , 0, 0, 1,
                 1 , 1 , 0 , 0, 0 , 0, 0, 0 , 0 , 0 , 0, 0 , 0, 0, 0, 0 , 0, 0 , 0 , 0, 0, 0, 0 , 1 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0, 0, 0, 0, 0 , 0,
                 0 , 1 , 1, 0 , 1 , 1 , 1, 1 , 1, 1, 1, 1 , 1 , 1, 1, 0, 0, 1, 1 , 1 , 1 , 1, 0, 0 , 0, 0, 0, 0, 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0,
                 0 , 0 , 0 , 0 , 0, 0, 0, 1, 0, 1 , 0, 0, 0 , 0 , 0, 0 , 0, 0, 0, 0 , 0 , 0 , 0 , 0 , 0 , 1, 1, 1, 1, 0, 0 , 0, 0, 0, 0, 0, 0,
                 0 , 0, 0, 1 , 1 , 0, 0, 0, 0, 0 , 0, 0, 0, 0 , 0, 0, 0 , 0 , 0 , 0 , 0, 0, 0 , 0, 0, 0 , 0 , 0, 0 , 0, 0, 0 , 0, 0, 0, 0, 0,
                 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0, 0 , 0 , 0, 0 , 0 , 0, 0 , 0 , 0, 0 , 0 , 0, 1, 0 , 0, 0, 0, 0, 0, 0, 0 , 0,
                 0 , 0 , 0, 0 , 0 , 1, 1 , 1]
#########################################################
d1 = lodData('p$dData/1-dead.xlsx', "dead", tempAbundance)
d2 = lodData('p$dData/2-dead.xlsx', "dead", tempAbundance)
d3 = lodData('p$dData/3-dead.xlsx', "dead", tempAbundance)
d4 = lodData('p$dData/4-dead.xlsx', "dead", tempAbundance)
d5 = lodData('p$dData/5-dead.xlsx', "dead", tempAbundance)
d6 = lodData('p$dData/6-dead.xlsx', "dead", tempAbundance)
d7 = lodData('p$dData/7-dead.xlsx', "dead", tempAbundance)
p1 = lodData('p$dData/1-patient.xlsx', "alive", tempAbundance)
p2 = lodData('p$dData/2-patient.xlsx', "alive", tempAbundance)
p3 = lodData('p$dData/3-patient.xlsx', "alive", tempAbundance)
p4 = lodData('p$dData/4-patient.xlsx', "alive", tempAbundance)
p5 = lodData('p$dData/5-patient.xlsx', "alive", tempAbundance)
p6 = lodData('p$dData/6-patient.xlsx', "alive", tempAbundance)
p7 = lodData('p$dData/7-patient.xlsx', "alive", tempAbundance)
p8 = lodData('p$dData/8-patient.xlsx', "alive", tempAbundance)
p9 = lodData('p$dData/9-patient.xlsx', "alive", tempAbundance)
p10 = lodData('p$dData/10-patient.xlsx', "alive", tempAbundance)
p11 = lodData('p$dData/11-patient.xlsx', "alive", tempAbundance)
p12 = lodData('p$dData/12-patient.xlsx', "alive", tempAbundance)
p13 = lodData('p$dData/13-patient.xlsx', "alive", tempAbundance)
p14 = lodData('p$dData/14-patient.xlsx', "alive", tempAbundance)
p15 = lodData('p$dData/15-patient.xlsx', "alive", tempAbundance)
p16 = lodData('p$dData/16-patient.xlsx', "alive", tempAbundance)
p17 = lodData('p$dData/17-patient.xlsx', "alive", tempAbundance)
p18 = lodData('p$dData/18-patient.xlsx', "alive", tempAbundance)
p19 = lodData('p$dData/19-patient.xlsx', "alive", tempAbundance)
p20 = lodData('p$dData/20-patient.xlsx', "alive", tempAbundance)
p21 = lodData('p$dData/21-patient.xlsx', "alive", tempAbundance)
p22 = lodData('p$dData/22-patient.xlsx', "alive", tempAbundance)
p23 = lodData('p$dData/23-patient.xlsx', "alive", tempAbundance)
p24 = lodData('p$dData/24-patient.xlsx', "alive", tempAbundance)
p25 = lodData('p$dData/25-patient.xlsx', "alive", tempAbundance)

# d1 = lodData('p$dData/1-dead.xlsx', 0)
# d2 = lodData('p$dData/2-dead.xlsx', 0)
# d3 = lodData('p$dData/3-dead.xlsx', 0)
# d4 = lodData('p$dData/4-dead.xlsx', 0)
# d5 = lodData('p$dData/5-dead.xlsx', 0)
# d6 = lodData('p$dData/6-dead.xlsx', 0)
# d7 = lodData('p$dData/7-dead.xlsx', 0)
# p1 = lodData('p$dData/1-patient.xlsx', 1)
# p2 = lodData('p$dData/2-patient.xlsx', 1)
# p3 = lodData('p$dData/3-patient.xlsx', 1)
# p4 = lodData('p$dData/4-patient.xlsx', 1)
# p5 = lodData('p$dData/5-patient.xlsx', 1)
# p6 = lodData('p$dData/6-patient.xlsx', 1)
# p7 = lodData('p$dData/7-patient.xlsx', 1)
# p8 = lodData('p$dData/8-patient.xlsx', 1)
# p9 = lodData('p$dData/9-patient.xlsx', 1)
# p10 = lodData('p$dData/10-patient.xlsx', 1)
# p11 = lodData('p$dData/11-patient.xlsx', 1)
# p12 = lodData('p$dData/12-patient.xlsx', 1)
# p13 = lodData('p$dData/13-patient.xlsx', 1)
# p14 = lodData('p$dData/14-patient.xlsx', 1)
# p15 = lodData('p$dData/15-patient.xlsx', 1)
# p16 = lodData('p$dData/16-patient.xlsx', 1)
# p17 = lodData('p$dData/17-patient.xlsx', 1)
# p18 = lodData('p$dData/18-patient.xlsx', 1)
# p19 = lodData('p$dData/19-patient.xlsx', 1)
# p20 = lodData('p$dData/20-patient.xlsx', 1)
# p21 = lodData('p$dData/21-patient.xlsx', 1)
# p22 = lodData('p$dData/22-patient.xlsx', 1)
# p23 = lodData('p$dData/23-patient.xlsx', 1)
# p24 = lodData('p$dData/24-patient.xlsx', 1)
# p25 = lodData('p$dData/25-patient.xlsx', 1)

# d1 = normalizer(d1)
# d2 = normalizer(d2)
# d3 = normalizer(d3)
# d4 = normalizer(d4)
# d5 = normalizer(d5)
# d6 = normalizer(d6)
# d7 = normalizer(d7)
# p1 = normalizer(p1)
# p2 = normalizer(p2)
# p3 = normalizer(p3)
# p4 = normalizer(p4)
# p5 = normalizer(p5)
# p6 = normalizer(p6)
# p7 = normalizer(p7)
# p8 = normalizer(p8)
# p9 = normalizer(p9)
# p10 = normalizer(p10)
# p11 = normalizer(p11)
# p12 = normalizer(p12)
# p13 = normalizer(p13)
# p14 = normalizer(p14)
# p15 = normalizer(p15)
# p16 = normalizer(p16)
# p17 = normalizer(p17)
# p18 = normalizer(p18)
# p19 = normalizer(p19)
# p20 = normalizer(p20)
# p21 = normalizer(p21)
# p22 = normalizer(p22)
# p23 = normalizer(p23)
# p24 = normalizer(p24)
# p25 = normalizer(p25)


trainSet = [d1, d2, d3, d4, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
testInstance = d6


neighbors = getNeighbors(trainSet, testInstance, 2)
print "first neighbor tag is: " + neighbors[0][-1]
print "second neighbor tag is: " + neighbors[1][-1]




