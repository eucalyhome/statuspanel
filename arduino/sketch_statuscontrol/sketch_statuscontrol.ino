#include <M5Core2.h>

#include "EEPROM.h"
#include <Wire.h>

#include "statusimages.h"

byte touchflag = 0;
byte valuemain = 0;
byte valuesub = 0;
byte valuestatus = 0;
byte initflag = 0;
byte motorflag = 0;

void outputdata() {
  Serial.println("valuemain: " + String(valuemain));
  Serial.println("valuesub: " + String(valuesub));
  Serial.println("valuestatus: " + String(valuestatus));
}
void setup() {
  M5.begin(true, true, true, true);
  if (!EEPROM.begin(1000)) {
    delay(1000);
    ESP.restart();
  }
  valuemain = EEPROM.readInt(0);
  valuesub = EEPROM.readInt(1);
  valuestatus = EEPROM.readInt(2);

//  Serial.begin(115200);
  M5.Axp.ScreenBreath(10);
  M5.Lcd.setRotation(1);
  M5.Lcd.setSwapBytes(false);
  M5.Lcd.fillScreen(BLACK);
}

void loop() {
  TouchPoint_t pos = M5.Touch.getPressPoint();
  int changeflag = 0;
  if (pos.x > 0) {
    if (touchflag == 0) {
      if (pos.y > 209) {
        // nop
      }
      else if (pos.y > 140) {
        valuestatus++;
        if (valuestatus > 2) {
          valuestatus = 0;
        }
        changeflag = 3;
        touchflag = 1;
      }
      else if (pos.y > 70) {
        valuesub++;
        if (valuesub > 3) {
          valuesub = 0;
        }
        changeflag = 2;
        touchflag = 1;
      }
      else {
        valuemain++;
        if (valuemain > 7) {
          valuemain = 0;
        }
        changeflag = 1;
        touchflag = 1;
      }
    }
  }
  else {
    touchflag = 0;
    changeflag = 0;
  }

  if ((changeflag == 1) || (initflag == 0)) {
    M5.Lcd.fillRect(0, 0, 319, 69, BLACK);
    if (valuemain == 0) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 2, imgWidth, imgHeight, img00);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 2);
      M5.Lcd.print("MAIN: MonsterParade");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 22);
      M5.Lcd.print("Procession of monsters");
      M5.Lcd.setCursor(80, 32);
      M5.Lcd.print("CPU Temp : MonsterSpeed");
      M5.Lcd.setCursor(80, 42);
      M5.Lcd.print("CPU Load : MonsterCount");
      M5.Lcd.setCursor(80, 52);
      M5.Lcd.print("GPU Temp : BG Weather");
    }
    if (valuemain == 1) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 2, imgWidth, imgHeight, img01);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 2);
      M5.Lcd.print("MAIN: FieldView");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 22);
      M5.Lcd.print("Automatically generate fields");
      M5.Lcd.setCursor(80, 32);
      M5.Lcd.print("CPU Load : Generate Objects");
      M5.Lcd.setCursor(80, 42);
      M5.Lcd.print("CPU Temp : Field Type");
      M5.Lcd.setCursor(80, 52);
      M5.Lcd.print(" ");
    }
    if (valuemain == 2) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 2, imgWidth, imgHeight, img02);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 2);
      M5.Lcd.print("MAIN: TileMosaic");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 22);
      M5.Lcd.print("Tile-like effects");
      M5.Lcd.setCursor(80, 32);
      M5.Lcd.print("CPU Load : Generate RGB Tiles");
      M5.Lcd.setCursor(80, 42);
      M5.Lcd.print("GPU Load : Generate YMC Tiles");
      M5.Lcd.setCursor(80, 52);
      M5.Lcd.print(" ");
    }
    if (valuemain == 3) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 2, imgWidth, imgHeight, img03);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 2);
      M5.Lcd.print("MAIN: bar");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 22);
      M5.Lcd.print("Like a BeBox!");
      M5.Lcd.setCursor(80, 32);
      M5.Lcd.print("CPU Clock #1 : Left bar");
      M5.Lcd.setCursor(80, 42);
      M5.Lcd.print("CPU Clock #2 : Right bar");
      M5.Lcd.setCursor(80, 52);
      M5.Lcd.print(" ");
    }
    if (valuemain == 4) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 2, imgWidth, imgHeight, img04);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 2);
      M5.Lcd.print("MAIN: circle");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 22);
      M5.Lcd.print("analog meter style?");
      M5.Lcd.setCursor(80, 32);
      M5.Lcd.print("CPU Load : top circle");
      M5.Lcd.setCursor(80, 42);
      M5.Lcd.print("GPU Load : bottom circle");
      M5.Lcd.setCursor(80, 52);
      M5.Lcd.print(" ");
    }
    if (valuemain == 5) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 2, imgWidth, imgHeight, img05);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 2);
      M5.Lcd.print("MAIN: StatusStream");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 22);
      M5.Lcd.print("The situation is flooding");
      M5.Lcd.setCursor(80, 32);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 42);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 52);
      M5.Lcd.print(" ");
    }
    if (valuemain == 6) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 2, imgWidth, imgHeight, img06);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 2);
      M5.Lcd.print("MAIN: StatusCode");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 22);
      M5.Lcd.print("Electroharmonix");
      M5.Lcd.setCursor(80, 32);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 42);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 52);
      M5.Lcd.print(" ");
    }
     if (valuemain == 7) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 2, imgWidth, imgHeight, img07);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 2);
      M5.Lcd.print("MAIN: Logo");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 22);
      M5.Lcd.print("static NZXT");
      M5.Lcd.setCursor(80, 32);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 42);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 52);
      M5.Lcd.print(" ");
    }
    EEPROM.writeInt(0,valuemain);
    EEPROM.commit();
    outputdata();
  }
  if ((changeflag == 2) || (initflag == 0)) {
    M5.Lcd.fillRect(0, 70, 319, 69, BLACK);
    if (valuesub == 0) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 72, imgWidth, imgHeight, img05);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 72);
      M5.Lcd.print("SUB: StatusStream");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 92);
      M5.Lcd.print("The situation is flooding");
      M5.Lcd.setCursor(80, 102);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 112);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 122);
      M5.Lcd.print(" ");
    }
    if (valuesub == 1) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 72, imgWidth, imgHeight, img06);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 72);
      M5.Lcd.print("SUB: StatusCode");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 92);
      M5.Lcd.print("Electroharmonix");
      M5.Lcd.setCursor(80, 102);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 112);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 122);
      M5.Lcd.print(" ");
    }
    if (valuesub == 2) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 72, imgWidth, imgHeight, img02);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 72);
      M5.Lcd.print("SUB: TileMosaic");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 92);
      M5.Lcd.print("Tile-like effects");
      M5.Lcd.setCursor(80, 102);
      M5.Lcd.print("CPU Load : Generate RGB Tiles");
      M5.Lcd.setCursor(80, 112);
      M5.Lcd.print("GPU Load : Generate YMC Tiles");
      M5.Lcd.setCursor(80, 122);
      M5.Lcd.print(" ");
    }
    if (valuesub == 3) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 72, imgWidth, imgHeight, img08);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 72);
      M5.Lcd.print("SUB: LifeGame");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 92);
      M5.Lcd.print("Conway's Game of Life");
      M5.Lcd.setCursor(80, 102);
      M5.Lcd.print("CPU Temp : Generate Cyan Seeds");
      M5.Lcd.setCursor(80, 112);
      M5.Lcd.print("GPU Temp : Generate Green Seeds");
      M5.Lcd.setCursor(80, 122);
      M5.Lcd.print(" ");
    }
    EEPROM.writeInt(1,valuesub);
    EEPROM.commit();
    outputdata();
  }
  if ((changeflag == 3) || (initflag == 0)) {
    M5.Lcd.fillRect(0, 140, 319, 69, BLACK);
    if (valuestatus == 0) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 142, imgWidth, imgHeight, img09);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 142);
      M5.Lcd.print("STATUS: Small Size");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 162);
      M5.Lcd.print("Be reluctant");
      M5.Lcd.setCursor(80, 172);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 182);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 192);
      M5.Lcd.print(" ");
    }
    if (valuestatus == 1) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 142, imgWidth, imgHeight, img10);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 142);
      M5.Lcd.print("STATUS: Big Size");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 162);
      M5.Lcd.print("self-assertion");
      M5.Lcd.setCursor(80, 172);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 182);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 192);
      M5.Lcd.print(" ");
    }
    if (valuestatus == 2) {
      M5.Lcd.startWrite();
      M5.Lcd.pushImage(4, 142, imgWidth, imgHeight, img11);
      M5.Lcd.endWrite();
      M5.Lcd.setTextSize(2);
      M5.Lcd.setCursor(72, 142);
      M5.Lcd.print("STATUS: OFF");
      M5.Lcd.setTextSize(1);
      M5.Lcd.setCursor(80, 162);
      M5.Lcd.print("quiet nomodeset");
      M5.Lcd.setCursor(80, 172);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 182);
      M5.Lcd.print(" ");
      M5.Lcd.setCursor(80, 192);
      M5.Lcd.print(" ");
    }
    EEPROM.writeInt(2,valuestatus);
    EEPROM.commit();
    outputdata();
  }
  if (motorflag != 0) {
    motorflag++;
    if (motorflag > 10) {
      M5.Axp.SetLDOEnable(3, false);
      motorflag = 0;
    }
  }
  if (changeflag != 0) {
    M5.Axp.SetLDOEnable(3, true);
    changeflag = 0;
    motorflag = 1;
  }
  initflag = 1;

  if ( Serial.available() > 0 ) {
    String str = Serial.readStringUntil('\n');
    M5.Lcd.setTextSize(2);
    M5.Lcd.setCursor(2, 212);
    M5.Lcd.print(str);
  }


  delay(10);
}
