#include <Arduino.h>
#include <mem.h>

#define TROMPE1 2
#define TROMPE2 3
#define TROMPE3 4
#define TROMPE4 5
#define TROMPE5 6
#define TROMPE6 7

#define BOUTON1 8
#define BOUTON2 9
#define DECLANCHEUR 10

//function declaration

unsigned long stopTime;
int numMusic = 0;
int musicPointer = 0;
int musicend =0;
bool finishedMusic = false;

// put function declarations here:
void writePin(char value);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(TROMPE1,OUTPUT);
  pinMode(TROMPE2,OUTPUT);
  pinMode(TROMPE3,OUTPUT);
  pinMode(TROMPE4,OUTPUT);
  pinMode(TROMPE5,OUTPUT);
  pinMode(TROMPE6,OUTPUT);

  pinMode(BOUTON1,INPUT_PULLUP);
  pinMode(BOUTON2,INPUT_PULLUP);
  pinMode(DECLANCHEUR,INPUT_PULLUP);

  Serial.println("Program Start");
}

void loop() {

  Serial.println("");
  Serial.println("stop");
  writePin(0);
  //delay(1000);

  while (digitalRead(DECLANCHEUR) && digitalRead(BOUTON2) && digitalRead(BOUTON1)){

    // if(!digitalRead(BOUTON1)){
    //   numMusic++;
    //   if(numMusic>=NUMBERMUSIC){
    //     numMusic = 0;
    //   }
    //   Serial.print("music selected : ");
    //   Serial.println(numMusic);
    //   delay(100);//rebound protection
    //   while (!digitalRead(BOUTON1));
    //   delay(100);//rebound protection
    // }
    
    // if(!digitalRead(BOUTON2)){
    //   numMusic--;
    //   if(numMusic<0){
    //     numMusic = NUMBERMUSIC - 1;
    //   }
    //   Serial.print("music selected : ");
    //   Serial.println(numMusic);
    //   delay(100);//rebound protection
    //   while (!digitalRead(BOUTON2)); 
    //   delay(100);//rebound protection
    // }     
  }
  if(!digitalRead(DECLANCHEUR)){numMusic=0;}
  if(!digitalRead(BOUTON2)){numMusic=1;}
  if(!digitalRead(BOUTON1)){numMusic=2;}

  Serial.println("");
  Serial.println("start");
  //delay(1000);
  musicPointer = memHeader[numMusic*2];
  musicend = memHeader[numMusic*2] + memHeader[numMusic*2 + 1] - 1;
  Serial.print("music start : ");
  Serial.println(musicPointer);
  Serial.print("music finish : ");
  Serial.println(musicend);
  stopTime = 0;
  finishedMusic = false;
  while (!digitalRead(DECLANCHEUR)||!digitalRead(BOUTON1)||!digitalRead(BOUTON2)){
    if(stopTime<millis() && !finishedMusic){
      if(musicPointer>=musicend){
        Serial.println("Finished Music, Restart");
        musicPointer = memHeader[numMusic*2];
        stopTime = millis() + memMusic[musicPointer].duration;
        writePin(0);
      }
      else{
        Serial.print("Position : ");
        Serial.print(musicPointer);
        Serial.print(" / ");
        Serial.print(musicend);
        Serial.print("   ");
        Serial.println(memMusic[musicPointer].note);
        writePin(memMusic[musicPointer].note);
        musicPointer++;
        stopTime = millis() + memMusic[musicPointer].duration;
      }      
    }    
  } 
}

void writePin(char value){
  digitalWrite(TROMPE1,value & 0b000001);
  digitalWrite(TROMPE2,value & 0b000010);
  digitalWrite(TROMPE3,value & 0b000100);
  digitalWrite(TROMPE4,value & 0b001000);
  digitalWrite(TROMPE5,value & 0b010000);
  digitalWrite(TROMPE6,value & 0b100000);
}