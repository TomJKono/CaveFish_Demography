# Generate the means/medians/ranges summary table for select models for
# select populations. This will be an ugly script, but it will make a nice table

# Read huge data table
dat <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Full_Dadi_Summary_50Reps.txt", header=TRUE)

# Define populations and models for building the comparisons
pop1 <- c("Choy", "Choy", "Choy", "Choy", "Choy", "Molino", "Molino", "Molino", "Molino", "Pachon", "Pachon", "Pachon", "Rascon")
pop2 <- c("Molino", "Molino", "Pachon", "Rascon", "Tinaja", "Pachon", "Rascon", "Rascon", "Tinaja", "Rascon", "Rascon", "Tinaja", "Tinaja")
models <- c("IM2M", "SC2M", "SC2M", "SC2M", "SC2M", "SC2M", "IM2M", "SC2M", "SC2M", "IM2M", "SC2M", "SC2M", "SC2M")

# Define the parameters we want to summarize
params <- c("N1", "N2", "Ts", "Tsc", "m21", "m12", "mi21", "mi12", "p")

# Then, aspply over the rows of these vectors to calculate the min, max, mean,
# and median of the parameters of interest.
summarize_params <- function(x) {
    # Define a summary function
    psum <- function(y, a ,b, mod) {
        trimmed <- dat[(dat$Pop1 == a & dat$Pop2 == b & dat$Model == mod), y]
        mean_est <- mean(trimmed)
        min_est <- min(trimmed)
        max_est <- max(trimmed)
        med_est <- median(trimmed)
        ret <- c(mean_est, med_est, min_est, max_est)
        names(ret) <- c("Mean", "Median", "Min", "Max")
        return(ret)
    }
    # Unpack the row that was sent
    p1 <- x["pop1"]
    p2 <- x["pop2"]
    m <- x["models"]
    # Apply over the parameters and summarize them
    s <- sapply(params, psum, p1, p2, m)
    return(as.vector(s))
    }

all_vals <- t(apply(cbind(pop1, pop2, models), 1, summarize_params))

# Put it into a data frame with the original data (UGLY!)
out <- data.frame(
    Pop1=pop1,
    Pop2=pop2,
    Model=models,
    MeanN1=all_vals[,1],
    MedianN1=all_vals[,2],
    MinN1=all_vals[,3],
    MaxN1=all_vals[,4],
    MeanN2=all_vals[,5],
    MedianN2=all_vals[,6],
    MinN2=all_vals[,7],
    MaxN2=all_vals[,8],
    MeanTS=all_vals[,9],
    MedianTs=all_vals[,10],
    MinTs=all_vals[,11],
    MaxTs=all_vals[,12],
    MeanTsc=all_vals[,13],
    MedianTsc=all_vals[,14],
    MinTsc=all_vals[,15],
    MaxTsc=all_vals[,16],
    MeanM21=all_vals[,17],
    MedianM21=all_vals[,18],
    MinM21=all_vals[,19],
    MaxM21=all_vals[,20],
    MeanM12=all_vals[,21],
    MedianM12=all_vals[,22],
    MinM12=all_vals[,23],
    MaxM12=all_vals[,24],
    MeanMi21=all_vals[,25],
    MedianMi21=all_vals[,26],
    MinMi21=all_vals[,27],
    MaxMi21=all_vals[,28],
    MeanMi12=all_vals[,29],
    MedianMi12=all_vals[,30],
    MinMi12=all_vals[,31],
    MaxMi12=all_vals[,32],
    MeanP=all_vals[,33],
    MedianP=all_vals[,34],
    MinP=all_vals[,35],
    MaxP=all_vals[,36],
    TotM21=all_vals[,2]*all_vals[,18],
    TotM12=all_vals[,6]*all_vals[,22],
    TotMi21=all_vals[,2]*all_vals[,26],
    TotMi12=all_vals[,6]*all_vals[,30])

# Save it as a csv
write.csv(out, file="Dadi_Best_Model_Summary.csv", quote=FALSE, row.names=FALSE)
