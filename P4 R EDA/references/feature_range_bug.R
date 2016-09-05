library(ggplot2)
library(plyr)
library(scales)
library(randomforest)

data(airquality)
airquality <- na.omit(airquality)
set.seed(131)
features = airquality
model <- randomForest(Ozone ~ ., features, importance=TRUE)

###############################################################################
## The following code does not work:
###############################################################################

feature_range <- function(features, model)
{
  print(head(features))
  partials <- data.frame()

  imp <- importance(model)
  impvar <- rownames(imp)[order(imp[, 1], decreasing=TRUE)]
  for (i in seq_along(impvar)) {
    partial <- partialPlot(model, features, impvar[i],
                           xlab=impvar[i], plot=FALSE)
    xt <- rescale(partial$x)
    partials <- rbind(partials, data.frame(x=partial$x,
                                           xt=xt, y=partial$y,
                                           feature=impvar[i]))
  }

  ranges <- ddply(partials, "feature", function(d) {
    r <- range(d$y)
    data.frame(feature=d$feature[1], range=r[2]-r[1])
  })

  features_to_plot <- ranges[ranges$range>0.05*max(ranges$range),"feature"]
  ggplot(partials[partials$feature %in% features_to_plot,], aes(x=xt, y=y, color=feature)) +
    geom_line(size=2) +
    theme_light(base_size=16)
}

feature_range(features, model)

###############################################################################
## The following code works:
###############################################################################
partials <- data.frame()

imp <- importance(model)
impvar <- rownames(imp)[order(imp[, 1], decreasing=TRUE)]
for (i in seq_along(impvar)) {
  partial <- partialPlot(model, features, impvar[i],
                         xlab=impvar[i], plot=FALSE)
  xt <- rescale(partial$x)
  partials <- rbind(partials, data.frame(x=partial$x,
                                         xt=xt, y=partial$y,
                                         feature=impvar[i]))
}

ranges <- ddply(partials, "feature", function(d) {
  r <- range(d$y)
  data.frame(feature=d$feature[1], range=r[2]-r[1])
})

features_to_plot <- ranges[ranges$range>0.05*max(ranges$range),"feature"]

ggplot(partials[partials$feature %in% features_to_plot,], aes(x=xt, y=y, color=feature)) +
  geom_line(size=2) +
  theme_light(base_size=16)
