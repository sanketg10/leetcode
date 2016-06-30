#power of n(putting default value as 4)
powerofn<- function(x,n=4){
  power<-function(x){
    x^1/n
  }
  test <- all.equal(power(x), as.integer(power(x)))
  if(test == TRUE) return (TRUE)
  else  return (FALSE)
}
#here log is the required function
powerofn(9,3)
powerofn(15)
