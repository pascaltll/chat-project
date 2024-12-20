# chat-project

Es un chat grupal que permite enviar mensajes a una sala comund, tambien permite interacutar con un identificador de numeros de 0 a 9, le resultado se envia en el chat comun

Luego de inicar secion, puedes escribir el nombre de la sala comun, tabien puedes cambiar la foto de pefil


construir la imagen:

```cmd
docker build -t elchat_image .
```

verificar si tflow esta intalado conrrectamente

```cmd
docker run -it --rm elchat_image bash
```


inicar el servicio

```cmd

docker run -it --rm -p 8000:8000 elchat_image
```

link

http://localhost:8000
