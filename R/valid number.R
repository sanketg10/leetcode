a<-function(x){
    !is.na(as.numeric(x))
}
a("hello")#returns false
a("22")#returns true
