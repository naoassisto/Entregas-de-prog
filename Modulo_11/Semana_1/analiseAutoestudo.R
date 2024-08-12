# Load necessary libraries
library(tidyverse)
library(ggplot2)
library(lubridate)

# Define the RMarkdown content
rmd_content <- "
---
title: 'Exploratory Data Analysis Report'
author: 'Your Name'
output: 
  pdf_document: default
  html_document: default
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
library(tidyverse)
library(ggplot2)
library(lubridate)



# Load Employee Data
employee_data <- read_csv('employee_final.csv')

# Convert dates
employee_data <- employee_data %>%
  mutate(initial_date = dmy(initial_date),
         end_date = dmy(end_date),
         year = year(initial_date))

# Plot distributions
ggplot(employee_data, aes(x=status)) + 
  geom_bar(fill='steelblue') + 
  theme_minimal() + 
  ggtitle('Distribution of Employee Status')

ggplot(employee_data, aes(x=role)) + 
  geom_bar(fill='steelblue') + 
  theme_minimal() + 
  ggtitle('Distribution of Employee Roles') + 
  theme(axis.text.x = element_text(angle=45, hjust=1))

ggplot(employee_data, aes(x=year)) + 
  geom_histogram(bins=20, fill='steelblue') + 
  theme_minimal() + 
  ggtitle('Distribution of Initial Dates (Yearly)')
  
  
  
  # Calculate employment duration
employee_data <- employee_data %>%
  mutate(employment_duration = ifelse(is.na(end_date),
                                      as.numeric(Sys.Date() - initial_date),
                                      as.numeric(end_date - initial_date)))

# Plot employment duration by role
ggplot(employee_data, aes(x=role, y=employment_duration)) + 
  geom_boxplot(fill='steelblue') + 
  theme_minimal() + 
  ggtitle('Employment Duration by Role') + 
  theme(axis.text.x = element_text(angle=45, hjust=1))

