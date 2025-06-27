library(tidyverse)
# install.packages("ggthemes")
library(palmerpenguins)
library(ggthemes)
# View(penguins)
# a <- ggplot(
#   data = penguins,
#   mapping = aes(x = flipper_length_mm, y = body_mass_g)
# ) +
#   geom_point(aes(color = species, shape = species)) +
#   geom_smooth(method = "lm") +
#   labs(
#     title = "Body mass and flipper length",
#     subtitle = "Dimensions for Adelie, Chinstrap, and Gentoo Penguins",
#     x = "Flipper length (mm)", y = "Body mass (g)",
#     color = "Species", shape = "Species"
#   ) +
#   scale_color_colorblind()

## (3)
# ggplot(
#   data = penguins,
#   mapping = aes(x = bill_length_mm , y = bill_depth_mm )
# ) +
#   geom_point(aes(color = species, shape = species)) +
#    geom_smooth(method = "lm") +
#   labs(
#     title = "Bill length and bill depth",
#     subtitle = "Dimensions for Adelie, Chinstrap, and Gentoo Penguins",
#     x = "Bill length (mm)", y = "Bill lenght (mm)",
#     color = "Species", shape = "Species"
#   ) +
#   scale_color_colorblind()
## what is the relationship???? it looks like there is no direct relationship


# ## (4)
# ggplot(
#   data = penguins,
#   mapping = aes(x =  bill_depth_mm, y = species)
# ) +
#   geom_boxplot(aes(color = species, shape = species)) +
#   labs(
#     title = "Bill depth by species",
#     subtitle = "Dimensions for Adelie, Chinstrap, and Gentoo Penguins",
#     x = "Bill depth (mm)", y = "Bill species (mm)",
#     color = "Species", shape = "Species"
#   ) +
#   scale_color_colorblind()
#   ## boxplot is the best visualization of bill depth vs species

# (5)
# ggplot(data = penguins) + 
#   geom_point()
## it gives an error since the dataset penguins has multiple columns and one must specify which column should be on the x and which should be on the y axes

#(6/7)
# ggplot(
#   data = penguins,
#   mapping = aes(x = flipper_length_mm, y = body_mass_g)
# ) +
#   geom_point(aes(color = species, shape = species), na.rm = TRUE) +
#   labs(caption = "Data come from the palmerpenguins package.")
# ## na.rm=TRUE removes data that is incomplete. I'm not getting the warning that some data is incomplete

## (8)
# ggplot(
#   data = penguins,
#   mapping = aes(x = flipper_length_mm, y = body_mass_g)
# ) +
#   geom_point(aes(color = bill_depth_mm)) +
# geom_smooth(method = NULL)

## (9)
# ggplot(
#   data = penguins,
#   mapping = aes(x = flipper_length_mm, y = body_mass_g, color = island)
# ) +
#   geom_point() +
#   geom_smooth(se = FALSE)
# ## predicted correctly the absence of confidence areas. did not expect 3 different trends to be displayed. did expect them not to be linear

## (10)
# ggplot(
#   data = penguins,
#   mapping = aes(x = flipper_length_mm, y = body_mass_g)
# ) +
#   geom_point() +
#   geom_smooth()

# ggplot() +
#   geom_point(
#     data = penguins,
#     mapping = aes(x = flipper_length_mm, y = body_mass_g)
#   ) +
#   geom_smooth(
#     data = penguins,
#     mapping = aes(x = flipper_length_mm, y = body_mass_g)
#   )

## the two graphs look the same 

## (1)
# ggplot(penguins, aes(y=species)) + geom_bar()

# ## (2)
# ggplot(penguins, aes(x = species)) +
#   geom_bar(color = "red")

# ggplot(penguins, aes(x = species)) +
#   geom_bar(fill = "red") ## better 

## (3)
# sets number of bins. inverse of binwidth

# ## (4)
# ggplot(diamonds, aes(x = carat)) + 
# geom_histogram(binwidth = 0.02)

# ## (1)
# ggplot(mpg, aes(x = displ, y = hwy, size = cyl, color = cty, shape = class)) + 
#  geom_point()

# ## (2)
# ggplot(mpg, aes(x = displ, y = hwy, linewidth = cty)) + 
#  geom_point()
#  # nothing really changes?

# ## (5)
# ggplot(penguins, aes(y = bill_length_mm , x = bill_depth_mm, color = species)) + 
#  geom_point() +
#  facet_wrap(~species)
# #  ## different species have different bill lengths and bill depths

## (6)
# ggplot(
#   data = penguins,
#   mapping = aes(
#     x = bill_length_mm, y = bill_depth_mm, 
#     color = species, shape = species
#   )
# ) +
#   geom_point() 
# #   labs(color = "Species")

# ggplot(penguins, aes(x = island, fill = species)) +
#   geom_bar(position = "fill") # frequency of penguin species per island
# ggplot(penguins, aes(x = species, fill = island)) +
#   geom_bar(position = "fill") # distribution of species per island where they can be found

