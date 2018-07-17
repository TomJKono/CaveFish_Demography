# Plot the distributions of split times (Ts+Tsc) for each pair of populations.
# We will make a 5x2 grid of plots. Also plot the Ts and Tsc distribtuions
# for the supplement.

# Read data
dat <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Full_Dadi_Summary_50Reps.txt", header=TRUE)

# Define a data frame here that will be the best models for each population
best <- data.frame(
    Pop1=c("Choy", "Choy", "Choy", "Choy", "Molino", "Molino", "Molino", "Pachon", "Pachon", "Rascon"),
    Pop2=c("Molino", "Pachon", "Rascon", "Tinaja", "Pachon", "Rascon", "Tinaja", "Rascon", "Tinaja", "Tinaja"),
    Model=c("SC2M", "SC2M", "SC2M", "SC2M", "SC2M", "IM2M", "SC2M", "IM2M", "SC2M", "SC2M")
)

# Then, define a plotting function
plot_split <- function(x) {
    p1 <- x["Pop1"]
    p2 <- x["Pop2"]
    mod <- x["Model"]
    # Get the Ts and Tsc values from the data table
    ts <- dat[dat$Pop1 == p1 & dat$Pop2 == p2 & dat$Model == "SC2M", "Ts"]
    tsc <- dat[dat$Pop1 == p1 & dat$Pop2 == p2 & dat$Model == "SC2M", "Tsc"]
    # Split time is Ts + Tsc
    split <- ts+tsc
    # make a plot
    comp <- paste(p1, p2, sep="-")
    comp <- gsub("Choy", "Río Choy", comp)
    plot(
        density(split),
        col="black",
        xlim=c(0, 4000000),
        xlab="Estimated Split Time (Millions of Generations ago)",
        ylab="Density",
        main=paste("Split Time for", comp, sep=" "),
        axes=F)
    # If IM2M is the best model, then we add the plot on top
    if(mod == "IM2M") {
        ts_im <- dat[dat$Pop1 == p1 & dat$Pop2 == p2 & dat$Model == "IM2M", "Ts"]
        lines(density(ts_im), col="blue")
        legend("topright", c("SC2M", "IM2M"), col=c("black", "blue"), lwd=1)
    }
    else {
        legend("topright", "SC2M", col="black", lwd=1)
    }
    axis(side=1, at=seq(0, 4000000, by=250000), labels=seq(0, 4, by=0.25))
    axis(side=2)
}

# Plot them all
pdf(file="Ts_Estimates.pdf", height=11, width=8.5)
# Set the grid
par(mfrow=c(5, 2))
apply(best, 1, plot_split)
dev.off()
