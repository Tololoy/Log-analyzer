## **Mini proyecto** : _Analizador de Logs_
### Estructura del proyecto:
* src/
    * reader.py >  Abre archivos y produce lineas
    * parser.py > Convierte linea -> dict normalizado
    * metrics.py > agregadores y contadores
    * report.py > presentacion/ tablas/ formatos
    * cli.py > punto de entrada: menus u argparse mas adelante
* data/
    * sample.log > dataset para pruebas
* README.md
    
### Social network and website 
* Linkedin: [Contact](https://www.linkedin.com/in/eloy-colirio-carrillo/)
* My website: [elingeniebrio](https://elingeniebrio.com/)
* GitHub:  [Tololoy](https://github.com/Tololoy)

## Blockquotes

> Proyecto nivel basico/intermedio en Python para practicar contenido de la PCAP, para los logs se usara el standard __*Apache combined Log Format*__
>> **Campos**: _ip, ident, user, [timestamp], "METHOD PATH PROTO", status, size, "referrer", "user_agent"_

>> **Ejemplo:** _203.0.113.52 - - [24/Aug/2025:10:16:10 -0700] "GET /images/logo.png HTTP/1.1" 200 20480 "https://example.com/" "Mozilla/5.0"_

## extra

This excercise was developed in `python 3.13` by [Tololoy](https://github.com/Tololoy)
