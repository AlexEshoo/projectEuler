import eulerTools as tools

distinct = []

for a in range(2,101):
    factors = tools.getPrimeFactors(a)
    
    for b in range(2, 101):
        
        power_factors = {}
        for factor in factors:
            power_factors[factor] = factors[factor]*b
            
        if not power_factors in distinct:
            distinct.append(power_factors)

print len(distinct)