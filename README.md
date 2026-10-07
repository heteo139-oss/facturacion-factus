Módulo de Facturación Electrónica DIAN y Recaudos con Factus API (Sandbox)
Este repositorio contiene la integración desarrollada en Python para la automatización de cobros y la emisión de facturas electrónicas con validez tributaria ante la DIAN, utilizando los servicios del proveedor tecnológico Factus.
👥 Integrantes del Equipo
Mateo Hernández
Dilan Zabala
Andy Rodríguez
🛠️ Tecnologías y Herramientas Utilizadas
Lenguaje de Programación: Python 3.x
Librerías: requests
Cliente de Pruebas de API: Postman
Servicios de Factus:
Factus Pay Sandbox: Gestión de pasarela de pago y recaudos.
Factus V2 Sandbox: Emisión y firma de facturas electrónicas para la DIAN.
🔗 Enlaces de Trabajo y Pruebas
Workspace en Postman: Mateo's Postman Workspace
Panel de Recaudos Factus Pay: Colección Sandbox Factus Pay
📌 Arquitectura y Flujo de Trabajo
El proyecto conecta dos componentes principales para completar el ciclo de cobro y facturación:
Factus Pay (pay-api-sandbox.factus.com.co):
Encargado de registrar el cobro y confirmar el pago monetario del cliente.
Se procesaron recaudos de prueba (ejemplo: REC-0001 y REC-0002) confirmando el cambio de estado a "Pagado".
Factus V2 (api-sandbox.factus.com.co):
Encargado de la transmisión tributaria formal ante la DIAN.
Procesa la información del pago, aplica el IVA (19%), asigna el rango de numeración habilitado (389), genera el código CUFE y emite la representación gráfica en PDF.
🚀 Instrucciones de Ejecución Local
1. Requisitos Previos
Tener instalado Python 3.x y el gestor de paquetes pip.
2. Instalación de Dependencias
pip install requests


3. Configuración del Token de Autorización
Obtener un access_token activo consumiendo el endpoint /oauth/token en Postman o mediante una petición POST, e incluirlo en la variable TOKEN_BEARER del archivo facturacion.py.
4. Ejecución del Módulo
py facturacion.py


📊 Resultados de la Ejecución
Al ejecutar el script, la API de Factus V2 retorna una respuesta con código HTTP 201 Created, incluyendo:
cufe: Código Único de Factura Electrónica emitido por la DIAN.
qr: Enlace oficial para consultar el estado del documento en el catálogo de la DIAN.
public_url: URL pública para consultar y descargar el PDF de la factura electrónica.
