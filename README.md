# Proyecto con Docker Compose - Entornos de Desarrollo y Producción

Este proyecto utiliza Docker Compose para gestionar entornos de desarrollo y producción separados. A continuación se presentan los comandos para levantar y detener los contenedores en cada entorno.

## Comandos

### Levantar los contenedores

#### Entorno de Desarrollo

Para iniciar el entorno de desarrollo, ejecuta el siguiente comando:

```bash
docker-compose -f docker-compose.dev.yml up -d --build
```

#### Entorno de Producción

Para iniciar el entorno de producción, ejecuta el siguiente comando:

```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

### Detener y eliminar los contenedores

#### Entorno de Desarrollo

Para detener y eliminar los contenedores del entorno de desarrollo, ejecuta:

```bash
docker-compose -f docker-compose.dev.yml down
```

#### Entorno de Producción

Para detener y eliminar los contenedores del entorno de producción, ejecuta:

```bash
docker-compose -f docker-compose.prod.yml down
```

## Explicación de los Comandos

- `-f <archivo.yml>`: Especifica el archivo de configuración de Docker Compose que deseas usar.
- `up -d --build`: Levanta los contenedores en modo "detached" (en segundo plano) y fuerza la reconstrucción de las imágenes para asegurar que estén actualizadas.
- `down`: Detiene y elimina los contenedores, redes y volúmenes definidos en el archivo especificado.
