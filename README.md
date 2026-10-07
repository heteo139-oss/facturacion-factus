Módulo de Facturación Electrónica DIAN y Recaudos con Factus API (Sandbox)

Este repositorio contiene la integración desarrollada en Python para la automatización de cobros y la emisión de facturas electrónicas con validez tributaria ante la DIAN, utilizando los servicios del proveedor tecnológico Factus en su entorno Sandbox.

Integrantes del Equipo
Mateo Hernández
Dilan Zabala
Andy Rodríguez

Programa: Tecnología en Sistematización de Datos

Tecnologías y Herramientas Utilizadas
Lenguaje de Programación: Python 3.x
Librerías: requests
Cliente y Pruebas de API: Postman
Servicios de Factus:
Factus Pay Sandbox: Gestión de pasarela de pago y registro de recaudos.
Factus V2 Sandbox: API para la validación, emisión y firma de facturas electrónicas ante la DIAN.
Enlaces de Trabajo y Pruebas
Workspace en Postman: Mateo's Postman Workspace
Panel de Recaudos Factus Pay: Colección Sandbox Factus Pay
Arquitectura y Flujo de Trabajo

El proyecto conecta dos componentes principales para completar el ciclo de cobro y facturación electrónica:

Factus Pay (pay-api-sandbox.factus.com.co):

Encargado de registrar el cobro y confirmar la transacción del cliente. Se procesaron recaudos de prueba (como REC-0001 y REC-0002) confirmando el cambio de estado a "Pagado".

Factus V2 (api-sandbox.factus.com.co):

Encargado de la transmisión tributaria formal ante la DIAN. Toma los datos del recaudo confirmado, aplica el cálculo del IVA (19%), asigna el rango de numeración habilitado (389), genera el código CUFE y emite la representación gráfica en formato PDF y XML.

Instrucciones de Ejecución Local
1. Requisitos Previos

Tener instalado Python 3.x y el gestor de paquetes pip.

2. Instalación de Dependencias
pip install requests
3. Configuración del Token de Autorización

Obtener un access_token activo consumiendo el endpoint /oauth/token mediante Postman con las credenciales correspondientes, e incluirlo en la variable TOKEN_BEARER del archivo facturacion.py.

4. Ejecución del Módulo
py facturacion.py
Resultados de la Ejecución

Al ejecutar el script, la API de Factus V2 retorna una respuesta exitosa con código HTTP 201 Created, devolviendo la siguiente información clave:

cufe: Código Único de Factura Electrónica asignado por la DIAN.
qr: Enlace oficial para la consulta del estado del documento dentro del catálogo de la DIAN.
public_url: URL pública para la visualización y descarga directa de la factura electrónica en formato PDF.
