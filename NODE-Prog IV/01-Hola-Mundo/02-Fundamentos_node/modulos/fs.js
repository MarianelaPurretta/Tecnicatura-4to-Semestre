const fs = require('fs');


//Leemos el archivo txt
function leer(ruta, cb) {
    fs.readFile(ruta, (err, data) => {
        cb(data.toString());
    })
}

leer(`${__dirname}/archivo.txt`, console.log);

//Segundo escribimos el archivo1.txt creandolo
function escribir(ruta, contenido) {
    fs.writeFile(ruta, contenido, function (err) {
        if (err) {
            console.log('No se ha podido escribir', err);
        } else {
            console.log('Archivo creado con éxito');
        }
    })
}

//Tercero, eliminamos el archivo1.txt
function borrar(ruta, cb) {
    fs.unlink(ruta, cb);
}
borrar(`${__dirname}/archivo1.txt`, console.log);

//escribir(`${__dirname}/archivo1.txt`,'Reescribimos el archivo', console.log);
leer(`${__dirname}/archivo1.txt`, console.log);