# AlexaYoutube en español
Skill de Alexa para reproducir YouTube con dispositivos Echo
## Habilidad no oficial de YouTube para Alexa
__Last update: 05 Ago 2021 (USE Python 3.7 in Amazon AWS)__

# Si te gustó la publicación ayúdame a continuar: [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate?business=DL494DZCBC3HS&no_recurring=0&item_name=Continuar+investigaci%C3%B3n+para+publicar+nuevas+skills&currency_code=USD)

## Características
* Reproducir audio de videos de YouTube
* Reproducir video (si es compatible) en videos en vivo o si solicita solo un video específico (comando 8)
* Hace una lista de todos los videos reproducidos en la aplicación Alexa.

## Lanzamiento
* In English, say "Alexa, launch YouTube".
* In German, say "Alexa, öffne YouTube".
* In Italian, say "Alexa, avvia YouTube".
* In Spanish, say "Alexa, abrir YouTube".

## Comandos de habilidad

1.	Reproduce un video, por ejemplo, "Alexa, abre YouTube y pon Rock".
2.	Reproduce una lista de reproducción, por ejemplo, "Alexa, abre YouTube y reproduce la playlist Rock de los 80s y 90s".
3.	Reproducir un canal, por ejemplo, "Alexa, abre YouTube y reproduce el canal eSavants"
4.	Puedes reemplazar "reproducir" con "aleatorio" para obtener una versión aleatoria de los resultados de búsqueda / canal / playlist, por ejemplo, "Alexa, abre YouTube y pon en aleatorio la playlist Rock de los 80s y 90s".
5. 	Puedes agregar más comandos directamente en el archivo que colocarás más adelante en el "JSON Editor" en la parte de la creación de la skill para amazon.


## Problemas conocidos

1. Parece que esta habilidad solo funciona en productos de Amazon Echo, no en productos de terceros que admiten Alexa.
2. Los videos en vivo funcionan en dispositivos Gen 2 en adelante, no en el Gen 1 Echo original.
     
## __Instrucciones de configuración__
## Obtenga el ARN de AWS Lambda
## Parte de Google
1.	Necesitamos una clave de desarrollador de YouTube.
2.	Vaya a: https://developers.google.com/ inicie sesión o cree una nueva cuenta
3.	Vaya a: https://console.developers.google.com/project y haga click en "Crear un nuevo proyecto"
4.	Asígnele un nombre, por ejemplo, "Token de API actualizado".
5.	Haga click en "Crear"
6.	Espere unos segundos a que se cree el proyecto (puede verificar mediante una notificación en la esquina superior derecha de la pantalla)
7.	Abrir en una página nueva: https://console.developers.google.com/apis/library?project=tester-api-key
8.	Seleccione "Elegir un proyecto" y haga click en el proyecto recién creado ("Token API actualizado")
9.	En la barra de búsqueda, escriba "youtube" y seleccione "API de datos de YouTube v3".
10.	Haga click en él y seleccione "HABILITAR"
11.	Haga click en "Crear credenciales" y luego Ayúdame a elegir.
12. Establecer así:
      - “¿Qué API estás usando?”: YouTube Data API v3
      - “¿A qué datos quieres acceder?”: Datos públicos
	  -	Siguiente
13. Click en listo.
14. **COPIAR** y **GUARDAR** la clave en el bloc de notas.

## Parte Amazon AWS
###### Para las personas que no tienen una cuenta de Amazon AWS
1.	Vaya a: http://aws.amazon.com
2.	Haga click en "Abrir consola" en la esquina superior derecha
3.	Cree una nueva cuenta de AWS haciendo click en "Crear una nueva cuenta de AWS"
4. 	***Durante el registro ¡SELECCIONE EL PLAN BÁSICO GRATUITO! (Si no ve una página para elegir el plan, significa que ha seleccionado el plan básico gratuito).*** 
	***Para confirmar tu identidad Amazon te pedirá una Tarjeta de Crédito, ESTO ES NORMAL, no pagas nada pero necesitas tener al menos 1 € en la tarjeta para la preautorización. Para confirmar la activación de su cuenta, Amazon puede tardar desde algunos minutos hasta algunas horas.***
	***Verás esta página:***
	***Para acelerar el proceso, intente hacer click en "Complete su registro de AWS" y confirme su número de teléfono móvil. Si tardará más de 24 horas, intente ponerse en contacto con el soporte.***
5.	Después de la activación de la cuenta, vaya aquí: http://aws.amazon.com .
6.	Haga click en "Abrir consola".
7. 	***MUY IMPORTANTE comprobar la región en la esquina superior derecha “N. Virginia ”y seleccione la región correcta, Ejemplo:***
	***región de EE . UU. Este (Norte de Virginia) para conocimientos de inglés (EE. UU.) O inglés (CA)***
	***Región de la UE (Irlanda) para inglés (Reino Unido), inglés (IN), alemán (DE), Habilidades en español (ES) o francés (FR)***
	***Región de EE . UU. Oeste (Oregón) para habilidades en japonés e inglés (AU).***
8.	Haga click en Servicios y busque Lambda
9.	Haga click en Crear función
10.	Seleccione el plan "Crear desde cero. Proporcione un nombre de función y elija Python 3.7 para el tiempo de ejecución".
11.	Haga click en Cambiar el rol de ejecución predeterminado. Luego seleccione Creación de un nuevo rol desde la política de AWS templates y coloque "ejecucion_basica_lambda" en el nombre del rol y "Permisos básicos de Lambda@Edge (para el desencadenador de CloudFront)" en Plantillas de políticas - opcional
12.	Después de la creación, seleccione Agregar desencadenador y elija "Alexa Skills Kit".
13.	Desactivar la verificación de ID de la habilidad
14. En la pestaña de Código, dar Click en Carga desde Archivo .zip. Cargar este archivo:            https://github.com/nestorlasso/AlexaYoutubeES/blob/master/AlexaYoutubeESLambda.zip
15.	En la pestaña de configuración, click en Variables de entorno, luego en editar.
16.	Agrega las variables de entorno con DEVELOPER_KEY y el código que hemos tomado de Google (guardado antes).
17.	Agrega las variables de entorno con youtube_dl y su valor en false inicialmente, si presenta errores en en log de AWS relacionado con pytube, cambiar este valor a true para que funcione con youtube_dl.
18.	En los campos de configuración general, click en editar y configurar 512 en memoria (MB) y 20 segundos en tiempo de espera
19.	Haga click en guardar y copiar el ARN, en la esquina superior derecha de la página.


## Configuración de Alexa Skill
1. Vaya a la consola de Alexa (https://developer.amazon.com/alexa/console/ask)
2. Si no se ha registrado como desarrollador de Amazon, deberá hacerlo. Siga los pasos solicitados y listo.
3.	Una vez que haya iniciado sesión en su cuenta, ir a la pestaña Alexa y seleccionar Alexa Skills Kit o ir directamente a la url (https://developer.amazon.com/alexa/console/ask). Haga click en "Create Skill" en el lado derecho.
4.	Dale a tu habilidad cualquier nombre, por ejemplo, "Mi habilidad de YouTube".
5. **Importante** Establezca el idioma en el que esté configurado su dispositivo Echo. Si no está seguro, vaya a la aplicación Alexa, vaya a Configuración, Configuración del dispositivo, luego haga click en su dispositivo Echo y busque en Idioma. Si su Echo está configurado en español (US), entonces la habilidad debe ser español (US), ¡otros tipos de español no funcionarán!
6.	Elija "Custom" como modelo, y "Provision your own" como método, luego haga click en "Create Skill". En la página de la plantilla, elija "Start from Scratch".
7.	En el lado izquierdo, haga click en "JSON Editor" en la sección Interaction Model.
8. Elimine todo en el cuadro de texto y copie el texto de https://github.com/nestorlasso/AlexaYoutubeES/blob/master/InteractionModel/InteractionModel_es.json, (o use InteractionModel_fr.json, InteractionModel_it.json, InteractionModel_de.json, InteractionModel_en.json, InteractionModel_ja.json o InteractionModel_pt-br.json para francés, italiano, alemán, inglés, japonés o portugués de Brasil.)
9. Click "Save Model" en la parte superior.
10. Click "Interfaces" en el menú de la izquierda, y habilitar "Audio Player" y "Video App". Click en "Save Interfaces".
11. Click "Endpoint" en el menú de la izquierda, and seleccione "AWS Lambda ARN". En "Default Region", colocar la ARN (de la parte de Amazon AWS).
12. Click "Save Endpoints"
13. Click "Permissions", en la parte inferior del menú de la izquierda en tools.
14. Habilitar "Lists Read" y "Lists Write".
15. Click "Custom" en el menú de la izquierda.
16. Click "Invocations" en el menú de la izquierda.
17. Si quiere nombrar la skillde otra manera diferente a "youtube", cambiar en la opción Skill Invocation Name. Click "Save Model" y será modificado.
18. Click "Build Model". Esto tomará algunos minutos. Cuando termine dirá que el modelo se encuentra bien.
19. **Importante:** En la parte superior, click "Test". Donde dice "Skill testing is enabled in:", cambiar de "Off" a "Development".

Y eso es todo. 