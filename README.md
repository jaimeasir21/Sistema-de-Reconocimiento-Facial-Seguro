Este proyecto final de curso de ASIR (Administración de Sistemas Informáticos en Red) consiste en el desarrollo de un sistema de vigilancia inteligente y seguro basado en el uso de una Raspberry Pi 4, una cámara, y un equipo Windows, todo conectado mediante una VPN segura. El objetivo principal es crear una solución de videovigilancia eficiente, con capacidades de reconocimiento facial para identificar y diferenciar entre rostros conocidos y desconocidos, ofreciendo así una medida adicional de seguridad.

Descripción del Proyecto:

Captura de Video: La cámara conectada a la Raspberry Pi 4 captura el video en tiempo real.
Transmisión de Video: La Raspberry Pi transmite el video al equipo Windows mediante el protocolo RTSP, asegurando baja latencia y alta calidad de imagen.
VPN Segura: La transmisión de video y los datos se aseguran mediante una VPN configurada con OpenVPN, utilizando cifrado AES-256 para garantizar la seguridad de la conexión.
Reconocimiento Facial: El equipo Windows ejecuta un script en Python que recibe la transmisión de video, analiza las imágenes en tiempo real y compara los rostros detectados con una base de datos de rostros conocidos. Los rostros conocidos se marcan con un recuadro verde y los desconocidos con un recuadro rojo, activando una alarma sonora en caso de detectar intrusos.
Registro de Eventos: El sistema registra todos los eventos de detección de rostros en un archivo CSV, incluyendo la fecha y hora de cada detección.
Metodología de Pruebas:

Se utilizó una metodología de prueba y error para desarrollar y ajustar cada componente del sistema, basándose en la experiencia de otros proyectos similares y adaptando soluciones específicas a los desafíos encontrados.
Resultados de las Pruebas:

Transmisión de Video: Se probó con varios protocolos de transmisión, eligiendo RTSP por su baja latencia y alta calidad. La verificación se realizó utilizando VLC en Windows.
Reconocimiento Facial: Se realizaron pruebas exhaustivas para ajustar la sensibilidad y precisión del reconocimiento facial, logrando un equilibrio adecuado entre precisión y rendimiento.
VPN: Se solucionaron problemas iniciales de configuración de OpenVPN, asegurando que cada cliente recibiera una IP única y que la comunicación entre clientes fuera posible mediante la activación del IP Forwarding en Windows.
Impacto y Beneficios:

El proyecto ofrece una solución de vigilancia de bajo costo en comparación con las soluciones comerciales, que suelen ser mucho más costosas y no siempre ofrecen capacidades de reconocimiento facial. Este sistema no solo mejora la seguridad mediante la identificación en tiempo real, sino que también proporciona una plataforma extensible para futuras mejoras y funcionalidades adicionales.
Consideraciones Éticas y Legales:

Se consideraron los aspectos éticos y legales de la privacidad de los datos y la legislación sobre videovigilancia, asegurando que el sistema cumpla con las normativas vigentes y respete los derechos de privacidad de los individuos.
En conclusión, este proyecto no solo demuestra la capacidad técnica para desarrollar una solución de vigilancia avanzada, sino que también subraya la importancia de la seguridad, la eficiencia y el cumplimiento legal en la implementación de sistemas de vigilancia en entornos empresariales y domésticos.
