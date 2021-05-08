import faker
f = faker.Faker ("ko-KR")
t=[]
for i in range(100):
	p=[f.name(),f.address(),f.ssn()]
	t.append(p)
for j in t:
    n = int(j[2][0:2])
    if n >= 80:
        print (j)
