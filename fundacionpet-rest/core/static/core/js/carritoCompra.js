/** CART */
let cartIcon_Nav = document.querySelector("#cart-icon")
let cart_Nav = document.querySelector(".cart")
let closeCart_Nav = document.querySelector("#close-cart")

/** Abre Cart */
cartIcon_Nav.onclick = () => {
    cart_Nav.classList.add("active")
};

/**Cierra Cat */
closeCart_Nav.onclick = () => {
    cart_Nav.classList.remove("active")
};

/**Logica CART con JS */
if(document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready();
}

/**Crear FUNCION 'ready()' */
function ready(){
    /**Remover ITEMS desde el CART */
    let removeCartButtons = document.getElementsByClassName('cart-remove')
    
    /**Recorrer */
    console.log(removeCartButtons)
    for(let i = 0; i < removeCartButtons.length; i++){
        let button = removeCartButtons[i]
        button.addEventListener('click', removeCartItem)
    }

    /**Cambiar cantidad */
    let cantidadInputs = document.getElementsByClassName('cart-cantidad')
    for(let i = 0; i < cantidadInputs.length; i++){
        let input = cantidadInputs[i]
        input.addEventListener('change', cantidadChanged);
    }

    /**Agregar CART */
    let addCart = document.getElementsByClassName('add-cart');
    for(let i = 0; i < addCart.length; i++){
        let button = addCart[i]
        button.addEventListener('click', addCartClicked)
    }


    /**Boton comprar */
    document.getElementsByClassName('btn-buy')[0].addEventListener('click', buyButtonClicked)
}

/** Crear FUNCION buyButtonClicked()*/
function buyButtonClicked(){
    alert("Tu pedido esta hecho")

    let cartContent = document.getElementsByClassName('cart-content')[0];

    while(cartContent.hasChildNodes()){
        cartContent.removeChild(cartContent.firstChild); 
    }

    updateTotal();

}

/**Crear FUNCION 'removeCartItem()' */
function removeCartItem(event){
    let buttonCliked = event.target
    buttonCliked.parentElement.remove()

    updateTotal();
}

/**Crear FUNCION 'cantidadChanged()' */ 
function cantidadChanged(event){
    let input = event.target

    if(isNaN(input.value) || input.value <= 0 ){
        input.value = 1;
    }

    updateTotal();
}

/**Crear FUNCION 'addCartClicked()' -> Agregar al CARRO*/
function addCartClicked(event){
    let button = event.target;
    let shopProducts = button.parentElement;
    let title = shopProducts.getElementsByClassName('product-title')[0].innerText;
    let price = shopProducts.getElementsByClassName('price')[0].innerText;
    let productImg = shopProducts.getElementsByClassName('product-img')[0].src;
    
    addProductToCart(title, price, productImg);
    updateTotal();
}

/**Crear FUNCION 'addCartClicked()' */
function addProductToCart(title, price, productImg){
    let cartShopBox = document.createElement("div");
    cartShopBox.classList.add("cart-box")
    let cartItems = document.getElementsByClassName("cart-content")[0];
    let cartItemsNames = cartItems.getElementsByClassName("cart-product-title");

    for(let i = 0; i < cartItemsNames.length; i++){
        if(cartItemsNames[i].innerText == title){
            alert("Has agregado este articulo al carrito")
            return;
        }  
    }

    let cartBoxContent = `
                        <img src="${productImg}" alt="" class="cart-img">
                        <div class="detail-box">
                            <div class="cart-product-title">${title}</div>
                            <div class="cart-price">${price}</div>
                            <input type="number" value="1" class="cart-cantidad">
                        </div>
                        <!-- Remove Cart -->
                        <i class='bx bxs-trash-alt cart-remove'></i>
`
    cartShopBox.innerHTML = cartBoxContent;
    cartItems.append(cartShopBox);
    cartShopBox
        .getElementsByClassName('cart-remove')[0]
        .addEventListener('click', removeCartItem);
    cartShopBox
        .getElementsByClassName('cart-cantidad')[0]
        .addEventListener('change', cantidadChanged);

}


/**Actualizar el Toral */
function updateTotal(){
    let cartContent = document.getElementsByClassName('cart-content')[0];
    let cartBoxes = cartContent.getElementsByClassName('cart-box');
    let total = 0;

    for(let i = 0; i < cartBoxes.length; i++){
        let cartBox = cartBoxes[i]
        let priceElement = cartBox.getElementsByClassName('cart-price')[0]
        let price = parseFloat(priceElement.innerText.replace('$',""))
        let cantidadElement = cartBox.getElementsByClassName('cart-cantidad')[0]
        let cantidad = cantidadElement.value

        total = total + (price * cantidad);
    }    

    //Si el precio contiene decimas
    total = Math.round(total * 100) / 100;

    document.getElementsByClassName('total-price')[0].innerText = '$' + total;
    
}

























