#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
 lcd.begin(16, 2);
  pinMode(A0,INPUT);
    pinMode(A1,INPUT);
      pinMode(A2,INPUT);


}

void loop() {
while(true){
if(analogRead(A0) == 1023){
   lcd.setCursor(0, 0);  
   lcd.print("Container is");
   lcd.setCursor(0, 1);
   lcd.print("80% full");
  }
else if(analogRead(A1) == 1023){
   lcd.setCursor(0, 0);  
   lcd.print("Container is");
   lcd.setCursor(0, 1);
   lcd.print("50% full");
 }
else if(analogRead(A2) == 1023){
   lcd.setCursor(0, 0);  
   lcd.print("Container is");
   lcd.setCursor(0, 1);
   lcd.print("10% full");
}
 }

}
