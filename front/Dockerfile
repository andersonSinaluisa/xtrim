# Usa una imagen oficial de Node.js como base
FROM node:20.9.0 as build

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copia el archivo package.json y package-lock.json a la imagen
COPY package*.json ./

# Instala las dependencias de la aplicación
RUN npm install

# Copia el resto de la aplicación al contenedor
COPY . .
ARG API_URL
ENV API_URL=$API_URL

# Compila la aplicación Angular para producción
RUN npm run build --prod


# Etapa de producción
FROM nginx:1.17.1-alpine

# Copia el archivo de configuración de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copia los archivos de la etapa de compilación a la imagen de Nginx
COPY --from=build /usr/src/app/dist/front /usr/share/nginx/html

# Expone el puerto 80
EXPOSE 80

# Inicia Nginx
CMD ["nginx", "-g", "daemon off;"]

