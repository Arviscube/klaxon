#pragma once
#include "Arduino.h"

#define NUMBERMUSIC 3

const int memHeader[NUMBERMUSIC*2] = {0,66,66,13,79,62};

struct MusicNote {
    uint16_t duration;
    uint8_t note;
};


const MusicNote memMusic[500]  = {


// genrated from: .\7eCompagnies3.mid
// lenght: 66
// Total Time: 15.975s
    {0,8},
    {328,0},
    {172,8},
    {375,0},
    {0,4},
    {125,0},
    {0,2},
    {414,0},
    {94,2},
    {427,0},
    {83,2},
    {732,0},
    {0,1},
    {250,0},
    {0,2},
    {1000,0},
    {0,4},
    {414,0},
    {70,4},
    {391,0},
    {0,8},
    {125,0},
    {0,16},
    {1000,0},
    {0,8},
    {451,0},
    {57,8},
    {367,0},
    {0,16},
    {125,0},
    {0,32},
    {1000,0},
    {0,8},
    {404,0},
    {83,8},
    {388,0},
    {0,4},
    {125,0},
    {0,2},
    {370,0},
    {130,2},
    {326,0},
    {174,2},
    {750,0},
    {0,1},
    {250,0},
    {0,2},
    {1000,0},
    {0,4},
    {396,0},
    {112,4},
    {367,0},
    {0,8},
    {125,0},
    {0,16},
    {500,0},
    {0,8},
    {375,0},
    {0,4},
    {125,0},
    {0,8},
    {500,0},
    {0,16},
    {487,48},
    {13,32},
    {987,0},


// genrated from: .\totallispies2.mid
// lenght: 13
// Total Time: 1.042s
    {0,8},
    {105,0},
    {12,16},
    {93,0},
    {47,16},
    {349,0},
    {12,32},
    {116,0},
    {0,16},
    {140,0},
    {23,8},
    {151,0},
    {2000,0},

// genrated from: .\gendarme1.mid
// lenght: 62
// Total Time: 10.588s
    {0,4},
    {495,0},
    {5,16},
    {370,0},
    {5,8},
    {120,0},
    {5,4},
    {120,0},
    {130,16},
    {120,0},
    {130,8},
    {120,0},
    {130,4},
    {120,0},
    {130,2},
    {448,0},
    {52,1},
    {370,0},
    {5,2},
    {120,0},
    {5,4},
    {995,0},
    {83,4},
    {417,0},
    {5,16},
    {370,0},
    {5,32},
    {109,48},
    {10,16},
    {109,0},
    {146,32},
    {120,0},
    {135,32},
    {120,0},
    {109,16},
    {120,0},
    {146,16},
    {245,0},
    {5,32},
    {495,0},
    {5,16},
    {245,0},
    {5,32},
    {995,0},
    {5,4},
    {495,0},
    {5,16},
    {370,0},
    {5,8},
    {104,0},
    {21,4},
    {99,0},
    {151,16},
    {120,0},
    {130,8},
    {120,0},
    {130,4},
    {120,0},
    {130,2},
    {495,0},
    {5,1},
    {120,0},




};
