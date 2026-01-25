#ifndef SIMPLEMC7_H
#define SIMPLEMC7_H

#include "Vanilla3.hpp"
#include "Parameters.hpp"
#include "MCStatistics.h"

void SimpleMonteCarlo5(const VanillaOption& TheOption,
        double Spot,
        const Parameters& Vol,
        const Parameters& r,
        unsigned long NumberOfPaths,
        StatisticsMC& gatherer);

#endif
