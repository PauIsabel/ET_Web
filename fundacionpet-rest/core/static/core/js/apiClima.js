/**SE hacen peticiones a una API */
//Para cargue los elemntos que se solicitan de la API
window.addEventListener('load', () => {
    //Primero debemos obtener nuestra ubicacion
    //Segundo pasamos los parametros de la ubicacion
    if (navigator.geolocation) {

        //Los elementos de HTML deben ser capturados con JS (DOM) por su ID
        let temValor = document.getElementById('temperatura-valor')
        let temDescripcion = document.getElementById('temperatura-descripcion')

        let ubicacion = document.getElementById('ubicacion')
        let iconoAnimado = document.getElementById('icono-animado')

        let porcenHumedad = document.getElementById('humedad')

        //Ver datos que entrega JSON PUBLICA de la API Weather
        let longitud;
        let latitud;

        navigator.geolocation.getCurrentPosition((posicion) => {
            longitud = posicion.coords.longitude
            latitud = posicion.coords.latitude

            //Ubicacion actual
            //const url = `https://api.openweathermap.org/data/2.5/weather?lat=${latitud}&lon=${longitud}&appid=e97a95fe93f401887e4aa5f34b9f3ba5`

            //Ubicacion por ciudad
            const url = `https://api.openweathermap.org/data/2.5/weather?q=Chile&lang=es&units=metric&appid=e97a95fe93f401887e4aa5f34b9f3ba5`
                //console.log(url)

            //Realizar las peticiones hacia la API con "FETCH"
            fetch(url)
                //Obtenemos la respuesta
                .then((respuesta) => {
                    return respuesta.json()
                })
                //Mostramos la respuesta
                .then((data) => {

                    let temperatura = Math.round(data.main.temp)
                    temValor.textContent = `${temperatura} °C`

                    let descripcion = data.weather[0].description
                    temDescripcion.textContent = descripcion.toUpperCase()

                    let ciudad = data.name
                    ubicacion.textContent = ciudad.toUpperCase()

                    let humedad = data.main.humidity
                    porcenHumedad.textContent = `${humedad} %`

                    //Iconos Estaticos
                    // let iconCode = data.weather[0].icon
                    // const url_IconAPI =`https://api.openweathermap.org/image/ClimaApi//wn${iconCode}.png`
                    // console.log(url_IconAPI)

                    console.log(data)

                    /** ICONOS ANIMADOS */
                    switch (data.weather[0].main) {
                        case 'Thunderstorm':
                            iconoAnimado.src = "image/ClimaApi/thunder.svg"
                            console.log('Thunderstorm')
                            break;

                        case 'Drizzle':
                            iconoAnimado.src = "image/ClimaApi/rainy-2.svg"
                            console.log('Drizzle')
                            break;

                        case 'Rain':
                            iconoAnimado.src = "image/ClimaApi/rainy-7.svg"
                            console.log('Rain')
                            break;

                        case 'Snow':
                            iconoAnimado.src = "image/ClimaApi/snowy-6.svg"
                            console.log('Snow')
                            break;

                        case 'Clear':
                            iconoAnimado.src = "image/ClimaApi/day.svg"
                            console.log('Clear')
                            break;

                        case 'Atmosphere':
                            iconoAnimado.src = "image/ClimaApi//weather.svg"
                            console.log('Atmosphere')
                            break;

                        case 'Clouds':
                            iconoAnimado.src = "image/ClimaApi//cloudy-day-1.svg"
                            console.log('Clouds')
                            break;

                        default:
                            iconoAnimado.src = "image/ClimaApi//cloudy-day-1.svg"
                            console.log('Por defecto')
                            break;

                    }

                })
                .catch((error) => {
                    console.log(error)
                })



        })







    }
})