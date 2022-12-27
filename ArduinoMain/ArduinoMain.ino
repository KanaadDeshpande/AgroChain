#include "DHT.h"

#define DHTPIN 9

#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(9600);

    pinMode(8, OUTPUT);
    pinMode(10, OUTPUT);

    pinMode(A0, OUTPUT);
    pinMode(A1, OUTPUT);
    pinMode(A2, INPUT);
    pinMode(A3, INPUT);

    digitalWrite(8, HIGH);
    digitalWrite(10, LOW);

    digitalWrite(A0, HIGH);
    digitalWrite(A1, LOW);

    dht.begin();
}

void loop() {
    delay(2000);

    float h = dht.readHumidity();
    float t = dht.readTemperature();
    float m = analogRead(A3);

    if (isnan(h) || isnan(t)) {
        Serial.println(F("Failed to read from DHT sensor!"));
        return;
    }

    Serial.print(t);
    Serial.print(",");
    Serial.print(h);
    Serial.print(",");
    Serial.println(m);
}
