# Plot the migration rates as a matrix of density plots.

library(ggplot2)

# Read the appropriate data sheets.
choy_molino_M21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Molino_M21.txt", header=FALSE)$V1
choy_pachon_M21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Pachon_M21.txt", header=FALSE)$V1
choy_rascon_M21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Rascon_M21.txt", header=FALSE)$V1
choy_tinaja_M21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Tinaja_M21.txt", header=FALSE)$V1
molino_pachon_M21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Pachon_M21.txt", header=FALSE)$V1
molino_rascon_M21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Rascon_M21.txt", header=FALSE)$V1
molino_tinaja_M21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Tinaja_M21.txt", header=FALSE)$V1
pachon_rascon_M21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Pachon-Rascon_M21.txt", header=FALSE)$V1
pachon_tinaja_M21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Pachon-Tinaja_M21.txt", header=FALSE)$V1
rascon_tinaja_M21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Rascon-Tinaja_M21.txt", header=FALSE)$V1
choy_molino_M12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Molino_M12.txt", header=FALSE)$V1
choy_pachon_M12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Pachon_M12.txt", header=FALSE)$V1
choy_rascon_M12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Rascon_M12.txt", header=FALSE)$V1
choy_tinaja_M12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Tinaja_M12.txt", header=FALSE)$V1
molino_pachon_M12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Pachon_M12.txt", header=FALSE)$V1
molino_rascon_M12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Rascon_M12.txt", header=FALSE)$V1
molino_tinaja_M12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Tinaja_M12.txt", header=FALSE)$V1
pachon_rascon_M12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Pachon-Rascon_M12.txt", header=FALSE)$V1
pachon_tinaja_M12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Pachon-Tinaja_M12.txt", header=FALSE)$V1
rascon_tinaja_M12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Rascon-Tinaja_M12.txt", header=FALSE)$V1
choy_molino_Mi21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Molino_Mi21.txt", header=FALSE)$V1
choy_pachon_Mi21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Pachon_Mi21.txt", header=FALSE)$V1
choy_rascon_Mi21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Rascon_Mi21.txt", header=FALSE)$V1
choy_tinaja_Mi21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Tinaja_Mi21.txt", header=FALSE)$V1
molino_pachon_Mi21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Pachon_Mi21.txt", header=FALSE)$V1
molino_rascon_Mi21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Rascon_Mi21.txt", header=FALSE)$V1
molino_tinaja_Mi21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Tinaja_Mi21.txt", header=FALSE)$V1
pachon_rascon_Mi21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Pachon-Rascon_Mi21.txt", header=FALSE)$V1
pachon_tinaja_Mi21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Pachon-Tinaja_Mi21.txt", header=FALSE)$V1
rascon_tinaja_Mi21 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Rascon-Tinaja_Mi21.txt", header=FALSE)$V1
choy_molino_Mi12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Molino_Mi12.txt", header=FALSE)$V1
choy_pachon_Mi12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Pachon_Mi12.txt", header=FALSE)$V1
choy_rascon_Mi12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Rascon_Mi12.txt", header=FALSE)$V1
choy_tinaja_Mi12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Choy-Tinaja_Mi12.txt", header=FALSE)$V1
molino_pachon_Mi12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Pachon_Mi12.txt", header=FALSE)$V1
molino_rascon_Mi12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Rascon_Mi12.txt", header=FALSE)$V1
molino_tinaja_Mi12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Molino-Tinaja_Mi12.txt", header=FALSE)$V1
pachon_rascon_Mi12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Pachon-Rascon_Mi12.txt", header=FALSE)$V1
pachon_tinaja_Mi12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Pachon-Tinaja_Mi12.txt", header=FALSE)$V1
rascon_tinaja_Mi12 <- read.table("/Users/tomkono/Dropbox/GitHub/SEM_CaveFish/Demography/Results/Population_Parameters/Rascon-Tinaja_Mi12.txt", header=FALSE)$V1

# Then, we want to make a data frame for plotting.
toplot <- data.frame(
    Pop1=c(
        rep("Choy", length(choy_molino_M21)),
        rep("Choy", length(choy_pachon_M21)),
        rep("Choy", length(choy_rascon_M21)),
        rep("Choy", length(choy_tinaja_M21)),
        rep("Molino", length(molino_pachon_M21)),
        rep("Molino", length(molino_rascon_M21)),
        rep("Molino", length(molino_tinaja_M21)),
        rep("Pachon", length(pachon_rascon_M21)),
        rep("Pachon", length(pachon_tinaja_M21)),
        rep("Rascon", length(rascon_tinaja_M21)),
        rep("Choy", length(choy_molino_M12)),
        rep("Choy", length(choy_pachon_M12)),
        rep("Choy", length(choy_rascon_M12)),
        rep("Choy", length(choy_tinaja_M12)),
        rep("Molino", length(molino_pachon_M12)),
        rep("Molino", length(molino_rascon_M12)),
        rep("Molino", length(molino_tinaja_M12)),
        rep("Pachon", length(pachon_rascon_M12)),
        rep("Pachon", length(pachon_tinaja_M12)),
        rep("Rascon", length(rascon_tinaja_M12)),
        rep("Choy", length(choy_molino_Mi21)),
        rep("Choy", length(choy_pachon_Mi21)),
        rep("Choy", length(choy_rascon_Mi21)),
        rep("Choy", length(choy_tinaja_Mi21)),
        rep("Molino", length(molino_pachon_Mi21)),
        rep("Molino", length(molino_rascon_Mi21)),
        rep("Molino", length(molino_tinaja_Mi21)),
        rep("Pachon", length(pachon_rascon_Mi21)),
        rep("Pachon", length(pachon_tinaja_Mi21)),
        rep("Rascon", length(rascon_tinaja_Mi21)),
        rep("Choy", length(choy_molino_Mi12)),
        rep("Choy", length(choy_pachon_Mi12)),
        rep("Choy", length(choy_rascon_Mi12)),
        rep("Choy", length(choy_tinaja_Mi12)),
        rep("Molino", length(molino_pachon_Mi12)),
        rep("Molino", length(molino_rascon_Mi12)),
        rep("Molino", length(molino_tinaja_Mi12)),
        rep("Pachon", length(pachon_rascon_Mi12)),
        rep("Pachon", length(pachon_tinaja_Mi12)),
        rep("Rascon", length(rascon_tinaja_Mi12))),
    Pop2=c(
        rep("Molino", length(choy_molino_M21)),
        rep("Pachon", length(choy_pachon_M21)),
        rep("Rascon", length(choy_rascon_M21)),
        rep("Tinaja", length(choy_tinaja_M21)),
        rep("Pachon", length(molino_pachon_M21)),
        rep("Rascon", length(molino_rascon_M21)),
        rep("Tinaja", length(molino_tinaja_M21)),
        rep("Rascon", length(pachon_rascon_M21)),
        rep("Tinaja", length(pachon_tinaja_M21)),
        rep("Tinaja", length(rascon_tinaja_M21)),
        rep("Molino", length(choy_molino_M12)),
        rep("Pachon", length(choy_pachon_M12)),
        rep("Rascon", length(choy_rascon_M12)),
        rep("Tinaja", length(choy_tinaja_M12)),
        rep("Pachon", length(molino_pachon_M12)),
        rep("Rascon", length(molino_rascon_M12)),
        rep("Tinaja", length(molino_tinaja_M12)),
        rep("Rascon", length(pachon_rascon_M12)),
        rep("Tinaja", length(pachon_tinaja_M12)),
        rep("Tinaja", length(rascon_tinaja_M12)),
        rep("Molino", length(choy_molino_Mi21)),
        rep("Pachon", length(choy_pachon_Mi21)),
        rep("Rascon", length(choy_rascon_Mi21)),
        rep("Tinaja", length(choy_tinaja_Mi21)),
        rep("Pachon", length(molino_pachon_Mi21)),
        rep("Rascon", length(molino_rascon_Mi21)),
        rep("Tinaja", length(molino_tinaja_Mi21)),
        rep("Rascon", length(pachon_rascon_Mi21)),
        rep("Tinaja", length(pachon_tinaja_Mi21)),
        rep("Tinaja", length(rascon_tinaja_Mi21)),
        rep("Molino", length(choy_molino_Mi12)),
        rep("Pachon", length(choy_pachon_Mi12)),
        rep("Rascon", length(choy_rascon_Mi12)),
        rep("Tinaja", length(choy_tinaja_Mi12)),
        rep("Pachon", length(molino_pachon_Mi12)),
        rep("Rascon", length(molino_rascon_Mi12)),
        rep("Tinaja", length(molino_tinaja_Mi12)),
        rep("Rascon", length(pachon_rascon_Mi12)),
        rep("Tinaja", length(pachon_tinaja_Mi12)),
        rep("Tinaja", length(rascon_tinaja_Mi12))),
    Rate=c(
        rep("M21", length(c(choy_molino_M21, choy_pachon_M21, choy_rascon_M21,
                            choy_tinaja_M21, molino_pachon_M21, molino_rascon_M21,
                            molino_tinaja_M21, pachon_rascon_M21, pachon_tinaja_M21,
                            rascon_tinaja_M21))),
        rep("M12", length(c(choy_molino_M12, choy_pachon_M12, choy_rascon_M12,
                            choy_tinaja_M12, molino_pachon_M12, molino_rascon_M12,
                            molino_tinaja_M12, pachon_rascon_M12, pachon_tinaja_M12,
                            rascon_tinaja_M12))),
        rep("Mi21", length(c(choy_molino_Mi21, choy_pachon_Mi21, choy_rascon_Mi21,
                            choy_tinaja_Mi21, molino_pachon_Mi21, molino_rascon_Mi21,
                            molino_tinaja_Mi21, pachon_rascon_Mi21, pachon_tinaja_Mi21,
                            rascon_tinaja_Mi21))),
        rep("Mi12", length(c(choy_molino_Mi12, choy_pachon_Mi12, choy_rascon_Mi12,
                            choy_tinaja_Mi12, molino_pachon_Mi12, molino_rascon_Mi12,
                            molino_tinaja_Mi12, pachon_rascon_Mi12, pachon_tinaja_Mi12,
                            rascon_tinaja_Mi12)))),
    Value=c(
        choy_molino_M21,
        choy_pachon_M21,
        choy_rascon_M21,
        choy_tinaja_M21,
        molino_pachon_M21,
        molino_rascon_M21,
        molino_tinaja_M21,
        pachon_rascon_M21,
        pachon_tinaja_M21,
        rascon_tinaja_M21,
        choy_molino_M12,
        choy_pachon_M12,
        choy_rascon_M12,
        choy_tinaja_M12,
        molino_pachon_M12,
        molino_rascon_M12,
        molino_tinaja_M12,
        pachon_rascon_M12,
        pachon_tinaja_M12,
        rascon_tinaja_M12,
        choy_molino_Mi21,
        choy_pachon_Mi21,
        choy_rascon_Mi21,
        choy_tinaja_Mi21,
        molino_pachon_Mi21,
        molino_rascon_Mi21,
        molino_tinaja_Mi21,
        pachon_rascon_Mi21,
        pachon_tinaja_Mi21,
        rascon_tinaja_Mi21,
        choy_molino_Mi12,
        choy_pachon_Mi12,
        choy_rascon_Mi12,
        choy_tinaja_Mi12,
        molino_pachon_Mi12,
        molino_rascon_Mi12,
        molino_tinaja_Mi12,
        pachon_rascon_Mi12,
        pachon_tinaja_Mi12,
        rascon_tinaja_Mi12)
    )

# Convert the pop labels into factors for facet_grid()
toplot$Pop1 <- factor(toplot$Pop1)
toplot$Pop2 <- factor(toplot$Pop2)
pdf(file="M_Estimates.pdf", width=6, height=6)
    plt <- ggplot(toplot, aes(x=Value, color=Rate))
    plt <- plt + geom_density(position="identity", alpha=0.1, size=0.3, aes(fill=Rate))
    plt <- plt + scale_x_log10(
        name="Migrant Proportion Per Gen.",
        limits=c(1e-10, 1e-3),
        breaks=c(1e-9, 1e-6, 1e-3),
        labels=c("1e-9", "1e-6", "1e-3"))
    plt <- plt + scale_y_continuous(
        name="Density",
        limits=c(0, 8))
    plt <- plt + theme(
        panel.background=element_blank(),
        panel.grid.major=element_line(color="grey", size=0.2))
    plt <- plt + facet_grid(Pop1 ~ Pop2, labeller=label_both)
    plt
dev.off()
