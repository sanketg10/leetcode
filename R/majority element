v<-c(1,1,1,4,4,3,3,3,3,3)
z<-function(x){
  m<-unique(sort(x))
  k<-table(x)
  c<-numeric()
  for (i in 1:length(m)){
    if (k[[i]]>=length(v)/2) c[i]<-m[i]
  }
  good<-complete.cases(c)
  c[good]
}
z(v)
