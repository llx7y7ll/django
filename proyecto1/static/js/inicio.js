$(document).ready(function() {

    /**
     * Genera un color hexadecimal aleatorio.
     * @returns {string} Código de color hexadecimal (ej. #A3B5F2).
     */
    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }

    /**
     * Calcula el color complementario de un color hexadecimal dado.
     * @param {string} hexColor - Código de color hexadecimal (ej. #A3B5F2).
     * @returns {string} Código del color complementario.
     */
    function getComplementaryColor(hexColor) {
        // Convierte el color hexadecimal a RGB.
        const r = parseInt(hexColor.slice(1, 3), 16);
        const g = parseInt(hexColor.slice(3, 5), 16);
        const b = parseInt(hexColor.slice(5, 7), 16);

        // Calcula el color complementario invirtiendo los valores.
        const compR = (255 - r).toString(16).padStart(2, '0');
        const compG = (255 - g).toString(16).padStart(2, '0');
        const compB = (255 - b).toString(16).padStart(2, '0');

        return `#${compR}${compG}${compB}`;
    }

    console.log("Inicio.js cargado"); 
      $('.jumbotron').on('click', function() {
         // 1. Genera un color aleatorio para el fondo.
       const newBackgroundColor = getRandomColor();

        // 2. Calcula su color complementario para el texto.
        const newTextColor = getComplementaryColor(newBackgroundColor);

        // 3. Aplica los nuevos colores.
        $(this).css({
            'background-color': newBackgroundColor,
            'color': newTextColor
        });
        
    });
});