library(gRain) 
yn <- c("yes","no")
a <- cptable(~asia, values=c(1,99),levels=yn)
t.a <- cptable(~tub+asia, values=c(5,95,1,99),levels=yn)
s <- cptable(~smoke, values=c(5,5), levels=yn)
l.s <- cptable(~lung+smoke, values=c(1,9,1,99), levels=yn)
b.s <- cptable(~bronc+smoke, values=c(6,4,3,7), levels=yn)
e.lt <- cptable(~either+lung+tub,values=c(1,0,1,0,1,0,0,1),levels=yn)
x.e <- cptable(~xray+either, values=c(98,2,5,95), levels=yn)
d.be <- cptable(~dysp+bronc+either, values=c(9,1,7,3,8,2,1,9), levels=yn)
cpt.list <- compileCPT(list(a, t.a, s, l.s, b.s, e.lt, x.e, d.be))

ftable(cpt.list$either, row.vars=1)
bnet <- grain(cpt.list)
bnet <- compile(bnet)
par(mfrow=c(1,2))


# plot(bnet$dag)

# plot(triangulate(moralize(bnet$dag)))
#plot(jTree(bnet$ug))




# jtree <- ug(~asia.tub:tub.lung.either:)
# plot(jtree)
# 
# 
graphicalModel = plot(dag(~asia+tub|asia+either|tub+xray|either+either|lung+dysp|either:bronc+bronc+bronc|smoke+lung|smoke))

moralizeGraph = plot(moralize(dag(~asia+tub|asia+either|tub+xray|either+either|lung+dysp|either:bronc+bronc+bronc|smoke+lung|smoke)))

triangulateGraph = plot(triangulate(moralize(dag(~asia+tub|asia+either|tub+xray|either+either|lung+dysp|either:bronc+bronc+bronc|smoke+lung|smoke))))

# 



