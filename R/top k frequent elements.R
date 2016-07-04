v<-c(1,1,1,4,4,3)
i<-function(x,n){
  m<-unique(sort(x))
  k<-table(x)
  c<-numeric()
  for (i in 1:length(m)){
    if (k[[i]]>=n) c[i]<-m[i]
  }
  good<-complete.cases(c)
  c[good]
}
i(v,3)
