# Entrega-Comparada
Preentrega tp final coderhouse
 Realizacion de una pagina web (eCommerce) sobre zapatillas urbanas 

Requerimientos para obtener una copia del codigo completo y funcionando 
         Ver -> Requirements.txt

Correr codigo en Visual Studio Code 
        1- Clonar codigo via git
            . git init
            . git clone https://github.com/Francisco-Comparada/Entrega-Comparada.git
        2- Tener instalados en su respectiva version
            .Django       4.0.6
            .Pillow       9.2.0
        3- Correr local servidor 
            .python manage.py runserver    

urls
        admin/ 'Panel del administrador, se necesita un usuario y contraseña para ingresar. El cual lo podemos crear con "python manage.py createsuperuser", en este url podremos administrar los usuarios(AUTHENTICATION AND AUTHORIZATION),
        y los productos. Como por ejemplo agregar, eliminar o editar

        index/ url de la pagina de inicio, aca veremos una pagina de inicio en la cual tendremos la posibilidad de acceder a las demas url haciendo clik en las diferentes opciones 


        shop/ Url que hereda parte del index/, aca veremos las categorias de productos que tenemos contando con la opcion de hacer click en cualquiera de ellos y dirigirte a la categoria seleccionada 


    sneakers/ varias opciones 

        sneakers/ list_Jordans/ [name='list_Jordans'] 
        listado de todas las zapatillas Jordans agregadas con sus respectivos atributos. Se ingresa desde la pagina haciendo click. En shop donde dice jordans o su imagen, como tambien podemos ingresar desde la pagina de inicio donde dice productos destacados haciendo clik en su respectiva imagen o en el boton Go Shop, otra opcion es en el footer haciendo click en la parte de poductos en su nombre. Tambien teniendo la posibilidad de ingresar manualmente a su url "/sneakers/list_Jordans/"

        sneakers/ add_Jordans/ [name='add_Jordans'] 
        url que se encarga de agregar zapatillas Jordans, con cada campo de esta clase. Se ingresa manualmente escribiendo la url  "/sneakers/add_Jordans/"

        sneakers/ list_Air_Force/ [name='list_Air_Force']
        listado de todas las zapatillas Air_Force agregadas con sus respectivos atributo. Se ingresa desde la pagina haciendo click. En shop donde dice Air Force o su imagen, como tambien podemos ingresar desde la pagina de inicio donde dice productos destacados haciendo clik en su respectiva imagen o en el boton Go Shop, otra opcion es en el footer haciendo click en la parte de poductos en su nombre.Tambien teniendo la posibilidad de ingresar manualmente a su url "/sneakers/list_Air_Force/"

        sneakers/ add_Air_Force/ [name='add_Air_Force']
        url que se encarga de agregar zapatillas Air_Force, con cada campo de esta clase. Se ingresa manualmente escribiendo la url  "/sneakers/add_Air_Force/"

        sneakers/ list_Accessories/ [name='list_Accessories']
        listado de todos los Accessories agregadas con sus respectivos atributo. Se ingresa desde la pagina haciendo click. En shop donde dice Accesorios o su imagen, como tambien podemos ingresar desde la pagina de inicio donde dice productos destacados haciendo clik en su respectiva imagen o en el boton Go Shop, otra opcion es en el footer haciendo click en la parte de poductos en su nombre. Tambien teniendo la posibilidad de ingresar manualmente a su url "/sneakers/list_Accessories/"

        sneakers/ add_Accessories/ [name='add_Accessories']
        url que se encarga de agregar Accessories, con cada campo de esta clase. Se ingresa manualmente escribiendo la url  "/sneakers/add_Accessories/"
        
        sneakers/ search_products/ [name='search_products']
        url que se encarga de buscar un producto, escribiendo en caso de las zapatillas su modelo y en caso de los accesorios su nombre, hace una busqueda general por todos los productos que hay en el ecommerce y los muestra en un listado con alguno de sus datos. Para aceder a esta opcion debemos apretar en la lupa de la pagina web 


Para la parte visual (frontEnd) de la pagina se uso una plantilla descargada https://templatemo.com/ la cual contiene css, jv, img, webfonts y los html usados, fueron modificados a gusto para poder utiliarlos. Con esto quedando una pagina mas agradable a la vista e intuitiva para el uso. Fue modificado settings.py para el uso de estos 

Proximos cambios a realizar 
        Agregar urls para cada producto en la cual mostrar todos sus datos 
        Agregar about, contact
        Agregar la subida de prodctos con verificacion de usuario 
        Completar el footer con todos sus links 
        Agregar Carrito 
        Agregar usuarios 
        Mejorar visual del shop 






