from LOGGIN.capa_datos_persona.Usuario import Usuario
from logger_base import log
from LOGGIN.capa_datos_persona.usuario_dao import UsuarioDAO

opcion = None
while opcion != 5:
    print('Opciones: ')
    print('1. Listar Usuarios')
    print('2. Agregar Usuario')
    print('3. Modificar Usuario')
    print('4. Eliminar Usuario')
    print('5. Salir')

    try:
        opcion = int(input('Digite la opcion (1-5): '))
    except ValueError as e:
        log.error(f'Error: Debes ingresar un número válido. {e}')
        continue

    if opcion == 1:
        try:
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                log.info(usuario)
        except Exception as e:
            log.error(f'Error al listar los usuarios: {e}')

    elif opcion == 2:
        try:
            username_var = input('Digite el nombre de usuario: ')
            password_var = input('Digite su contraseña: ')
            usuario = Usuario(username=username_var, password=password_var)
            usuario_insertado = UsuarioDAO.insertar(usuario)
            log.info(f'Usuario insertado: {usuario_insertado}')
        except Exception as e:
            log.error(f'Error al agregar el usuario: {e}')

    elif opcion == 3:
        try:
            id_usuario_var = int(input('Digite el id del usuario a modificar: '))
            username_var = input('Digite el nombre del usuario a modificar: ')
            password_var = input('Digite la contraseña del usuario a modificar: ')
            usuario = Usuario(id_usuario=id_usuario_var, username=username_var, password=password_var)
            usuario_actualizado = UsuarioDAO.actualizar(usuario)
            log.info(f'Usuario actualizado: {usuario_actualizado}')
        except ValueError as e:
            log.error(f'Error: Debes ingresar un número válido para el ID. {e}')
        except Exception as e:
            log.error(f'Error al modificar el usuario: {e}')

    elif opcion == 4:
        try:
            id_usuario_var = int(input('Digite el id del usuario a eliminar: '))
            usuario = Usuario(id_usuario=id_usuario_var)
            usuario_eliminado = UsuarioDAO.eliminar(usuario)
            log.info(f'Usuario eliminado: {usuario_eliminado}')
        except ValueError as e:
            log.error(f'Error: Debes ingresar un número válido para el ID. {e}')
        except Exception as e:
            log.error(f'Error al eliminar el usuario: {e}')

    elif opcion == 5:
        log.info('Salimos de la aplicación. ¡Hasta pronto!')
    else:
        log.error('Opción no válida. Por favor, elige una opción entre 1 y 5.')
