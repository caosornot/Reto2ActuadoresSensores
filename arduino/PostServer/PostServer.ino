/*
  Reto 2 - Actuadores y Sensores
  Carlos Andres Osorno Tejada
  Modificación de Ejemplo para postear al servidor
  
      Simple POST client for ArduinoHttpClient library
      Connects to server once every five seconds, sends a POST request
      and a request body
    
      created 14 Feb 2016
      by Tom Igoe
      
      this example is in the public domain
 */
#include <ArduinoHttpClient.h>
#include <WiFi101.h>

float temp;

/////// Configuración Wifi ///////
char ssid[] = "ONE E1003";
char pass[] = "caosornot";


char serverAddress[] = "165.227.197.35";  // Dirección IP del servidor
int port = 5000;    // Puerto de Flask

WiFiClient wifi;
HttpClient client = HttpClient(wifi, serverAddress, port);
int status = WL_IDLE_STATUS;
String response;
int statusCode = 0;

void setup() {
  Serial.begin(9600);

  // Proceso de conexión a red Wifi
  while ( status != WL_CONNECTED) {
    Serial.print("Attempting to connect to Network named: ");
    Serial.println(ssid);                   // print the network name (SSID);

    // Conexión a red WPA/WPA2:
    status = WiFi.begin(ssid, pass);
  }

  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);
}

void loop() {

  temp = analogRead(0) ;            // selecciona la entrada analoga 0
  temp = (3.3*temp*100.0)/1024.0; //fórmula que convierte el valor obtenido del pin análogo al que se encuentra conectado nuestro LM35 a grados Celsius
  delay(1000);                      // llama un retardo de 200 milisegundo
  Serial.print("Temperatura: ");  // muestra mensaje CONVERSOR A/D
  Serial.println(temp);           // muestra el valor numérico de la conversión

  Serial.println("making POST request");
  String contentType = "application/json";
  String postData = "{ \"temp\" : ";
  postData += temp;
  postData += " }";

  client.post("/", contentType, postData);

  // read the status code and body of the response
  statusCode = client.responseStatusCode();
  response = client.responseBody();

  Serial.print("Status code: ");
  Serial.println(statusCode);
  Serial.print("Response: ");
  Serial.println(response);

  Serial.println("Wait five seconds");
  delay(5000);
}
