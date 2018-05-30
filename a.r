set.seed(123, kind=NULL)
x <- rt(100000, 10)

write.csv(x, 'x.csv')

y <- rt(100000, 100000)

write.csv(y, 'y.csv')
