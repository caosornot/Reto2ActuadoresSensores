// Reto 2- Actuadores y Sensores
// Carlos Andres Osorno Tejada
// Codigo para lectura de Sensor LM35 con MKR1000


float   temp;                          // definir la variable valor como una variable tipo flotante para la operacion matematica de conversion
                                 
void setup() 
  {  
      Serial.begin(9600);                 // Inicio de comunicación Serial
  }

void loop()
 {               
    temp = analogRead(0) ;            // selecciona la entrada analoga 0
    temp = (3.2*temp*100.0)/1024.0; //fórmula que convierte el valor obtenido del pin análogo al que se encuentra conectado nuestro LM35 a grados Celsius
    delay(1000);                      // llama un retardo de 200 milisegundo
    Serial.print("Temperatura: ");  // muestra mensaje CONVERSOR A/D
    Serial.println(temp);           // muestra el valor numérico de la conversión                            
 }
