# Generate Akaike weights for each model, for each replicate. The goal of this
# is to show the variation in confidence that we have that we chose the best
# model for each population comparison. Takes the path to the collated AIC
# values as an argument

# Take args
args <- commandArgs(TRUE)

# Read in the data file
aic_dat <- read.table(args[1], header=TRUE)

# Define a function that calculates the weights from a row of the data frame
akaike_weight <- function(x) {
    # Cast the row to a numeric vector
    x <- as.numeric(x)
    # Get the minimum AIC value
    min_aic <- min(x, na.rm=TRUE)
    # The "delta-AIC" is defined as the difference between the actual AIC vals
    # and the minimum one
    delta_aic <- x - min_aic
    # Take the exponent of -1/2 * deltaAIC
    exp_aic <- exp(-1/2 * delta_aic)
    # Return the the exp_aic divided by the sum of exp_aic
    return(exp_aic / sum(exp_aic))
}

# Apply the Akaike weight function over the AIC values
a_weights <- apply(aic_dat, 1, akaike_weight)
a_weights.mean <- apply(a_weights, 1, mean, na.rm=TRUE)
names(a_weights.mean) <- names(aic_dat)
print(a_weights.mean)
