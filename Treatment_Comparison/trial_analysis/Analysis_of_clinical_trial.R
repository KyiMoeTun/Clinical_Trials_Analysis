#the following tutorial has been taken from the Clinical Trial Data Analysis Using R and SAS
#Demonstration purposes only
#t-test, Wilcoxon test, Welch test, F-tests are implemented in this r code



#read the data from the above folder
dat = read.csv('../creating_dataframe/DBP.csv', header=T)
#create a new column for blood pressure difference
dat$diff = dat$DBP5 - dat$DBP1
head(dat)

#Call the boxplot 
boxplot(diff~TRT, dat, xlab='Treatment', ylab='DBP changes', las=1)

#t-test
#Assuming the data is normal and equal variance
t.test(diff~TRT, dat, var.equal=T)

#Assuming the data is normal and unequal variance
#Welch t-test
t.test(diff~TRT, dat, var.equal=F)

#Checking if the variances are equal
var.test(diff~TRT, dat)

#Wilcoxon rank-sum test
#Assuming the data is not normal
wilcox.test(diff~TRT, dat)

#Assuming the data is normal
#One-sided t-test
diff.A = dat[dat$TRT=="A", ]$diff
diff.B = dat[dat$TRT=="B", ]$diff
t.test(diff.A, diff.B, alternative="less")




