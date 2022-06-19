#include <Adafruit_LiquidCrystal.h>
Adafruit_LiquidCrystal painel(0);

#define echoPin 7
#define trigPin 6

long duration;
int distancia;

//definir variáveis
int verde_1 = 10;
int amarelo_1 = 9;
int vermelho_1 = 8;
int verde_2 = 13;
int amarelo_2 = 12;
int vermelho_2 = 11;
int delay_curto = 2000;
int delay_longo = 4000;

//função setup
void setup() {
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  //primeiro semáforo
  pinMode(verde_1, OUTPUT);
  pinMode(amarelo_1, OUTPUT);
  pinMode(vermelho_1, OUTPUT);

  //segundo sinaleiro
  pinMode(verde_2, OUTPUT);
  pinMode(amarelo_2, OUTPUT);
  pinMode(vermelho_2, OUTPUT);

  //painel
  painel.begin(16, 2);
}

//abre função loop
void loop() {
  int distancia = sonarPulse();

  // 50 cm
  if (distancia <= 50) {
    digitalWrite(vermelho_1, LOW);
    digitalWrite(amarelo_1, HIGH);
    digitalWrite(verde_1, LOW);

    digitalWrite(vermelho_2, HIGH);
    digitalWrite(verde_2, LOW);
    digitalWrite(amarelo_2, LOW);
    delay(delay_curto);

    digitalWrite(vermelho_1, HIGH);
    digitalWrite(amarelo_1, LOW);

    //10 seg completar loop
    for (int seconds = 0; seconds < 10; seconds++) {
      painel.clear();
      painel.print("SIGA");

      painel.setCursor(0, 1);
      painel.print(10 - seconds);
      delay(1000); 
    }
    digitalWrite(vermelho_1, LOW);
  }
  semaforoLoop();
}

void semaforoLoop() {
  painel.clear();
  painel.print("PARE");

  digitalWrite(verde_1, HIGH);
  digitalWrite(vermelho_2, HIGH);
  delay(delay_longo);

  digitalWrite(verde_1, LOW);
  digitalWrite(vermelho_2, LOW);

  digitalWrite(amarelo_1, HIGH);
  digitalWrite(verde_2, HIGH);
  delay(delay_curto);

  digitalWrite(amarelo_1, LOW);
  digitalWrite(verde_2, LOW);

  digitalWrite(vermelho_1, HIGH);
  digitalWrite(amarelo_2, HIGH);
  delay(delay_longo);

  digitalWrite(vermelho_1, LOW);
  digitalWrite(amarelo_2, LOW);

  digitalWrite(verde_1, HIGH);
}

int sonarPulse() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2;
}
