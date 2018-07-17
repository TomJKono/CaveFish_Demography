# Make a side-by-side boxplot of the estimated Ne from dadi modeling. Because
# each population was included in four combinations, each population has 80
# estimates of Ne.

# Read in the data
dat <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Full_Dadi_Summary_50Reps.txt", header=TRUE)

# Extract the information from the big data table. This will be ugly, but we
# only want to use the best-fitting model for each comparison
choy <- c(
    dat[dat$Pop1 == "Choy" & dat$Pop2 == "Molino" & dat$Model == "SC2M", "N1"],
    dat[dat$Pop1 == "Choy" & dat$Pop2 == "Pachon" & dat$Model == "SC2M", "N1"],
    dat[dat$Pop1 == "Choy" & dat$Pop2 == "Rascon" & dat$Model == "SC2M", "N1"],
    dat[dat$Pop1 == "Choy" & dat$Pop2 == "Tinaja" & dat$Model == "SC2M", "N1"])
molino <- c(
    dat[dat$Pop1 == "Choy" & dat$Pop2 == "Molino" & dat$Model == "SC2M", "N2"],
    dat[dat$Pop1 == "Molino" & dat$Pop2 == "Pachon" & dat$Model == "SC2M", "N1"],
    dat[dat$Pop1 == "Molino" & dat$Pop2 == "Rascon" & dat$Model == "SC2M", "N1"],
    dat[dat$Pop1 == "Molino" & dat$Pop2 == "Tinaja" & dat$Model == "SC2M", "N1"])
pachon <- c(
    dat[dat$Pop1 == "Choy" & dat$Pop2 == "Pachon" & dat$Model == "SC2M", "N2"],
    dat[dat$Pop1 == "Molino" & dat$Pop2 == "Pachon" & dat$Model == "SC2M", "N2"],
    dat[dat$Pop1 == "Pachon" & dat$Pop2 == "Rascon" & dat$Model == "SC2M", "N1"],
    dat[dat$Pop1 == "Pachon" & dat$Pop2 == "Tinaja" & dat$Model == "SC2M", "N1"])
rascon <- c(
    dat[dat$Pop1 == "Choy" & dat$Pop2 == "Rascon" & dat$Model == "SC2M", "N2"],
    dat[dat$Pop1 == "Molino" & dat$Pop2 == "Rascon" & dat$Model == "SC2M", "N2"],
    dat[dat$Pop1 == "Pachon" & dat$Pop2 == "Rascon" & dat$Model == "SC2M", "N2"],
    dat[dat$Pop1 == "Rascon" & dat$Pop2 == "Tinaja" & dat$Model == "SC2M", "N1"])
tinaja <- c(
    dat[dat$Pop1 == "Choy" & dat$Pop2 == "Tinaja" & dat$Model == "SC2M", "N2"],
    dat[dat$Pop1 == "Molino" & dat$Pop2 == "Tinaja" & dat$Model == "SC2M", "N2"],
    dat[dat$Pop1 == "Pachon" & dat$Pop2 == "Tinaja" & dat$Model == "SC2M", "N2"],
    dat[dat$Pop1 == "Rascon" & dat$Pop2 == "Tinaja" & dat$Model == "SC2M", "N2"])

# Put them into a data frame for plotting
toplot <- data.frame(
    Pop=c(
        rep("Choy", length(choy)),
        rep("Molino", length(molino)),
        rep("Pachon", length(pachon)),
        rep("Rascon", length(rascon)),
        rep("Tinaja", length(tinaja))),
    Ne=c(choy, molino, pachon, rascon, tinaja))

# And plot it
pdf(file="Ne_Estimates.pdf", height=6, width=6)
boxplot(
    toplot$Ne ~ toplot$Pop,
    xlab="Population",
    ylab="Estimated Ne (Thousands of Individuals)",
    main="Estimated Ne From SC2M Model",
    pch=19,
    axes=FALSE
    )
axis(
    side=1,
    at=c(1, 2, 3, 4, 5),
    labels=c("Río Choy", "Molino", "Pachon", "Rascon", "Tinaja")
)
axis(
    side=2,
    at=c(10000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 750000),
    labels=c("10", "100", "200", "300", "400", "500", "600", "700", "750"),
    las=2
)
dev.off()

# Make a CSV for records
dat <- data.frame(
    Pop=c("Choy", "Molino", "Pachon", "Rascon", "Tinaja"),
    MinNe=c(min(choy), min(molino), min(pachon), min(rascon), min(tinaja)),
    MeanNe=c(mean(choy), mean(molino), mean(pachon), mean(rascon), mean(tinaja)),
    MedianNe=c(median(choy), median(molino), median(pachon), median(rascon), median(tinaja)),
    MaxNe=c(max(choy), max(molino), max(pachon), max(rascon), max(tinaja)))
write.csv(dat, file="Ne_Summary.csv", row.names=FALSE, quote=FALSE)
